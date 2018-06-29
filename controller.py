#!/usr/bin/env python
# coding=utf-8

import json

import moment
from pony import orm

from model import GameDetails, TeamDetails, db

JSON_DATA = "world_cup.json"
GROUPS = ["A", "B", "C", "D", "E", "F", "G", "H"]


@orm.db_session
def add_game_details_data():
    """
    更新 GameDetails 数据
    """
    with open(JSON_DATA, "r", encoding="utf8") as f:
        games = json.load(f)
        for game in games:
            score1 = int(game["Score1"])
            score2 = int(game["Score2"])

            if score1 > score2:
                integral1, integral2 = 3, 0
            elif score1 == score2:
                integral1, integral2 = 0, 0
            else:
                integral1, integral2 = 0, 3

            goal_difference1 = score1 - score2
            goal_difference2 = score2 - score1

            GameDetails(
                g_score1=score1,
                g_score2=score2,
                g_team1=game["Team1"],
                g_team2=game["Team2"],
                g_group=game["group"],
                g_date=moment.date("{} {}".format(game["date"], game["time"])).datetime,
                g_integral1=integral1,
                g_integral2=integral2,
                g_goal_difference1=goal_difference1,
                g_goal_difference2=goal_difference2,
            )
            orm.commit()


@orm.db_session
def add_team_details_data():
    """
    更新 TeamDetails 数据
    """
    teams = orm.distinct(
        orm.select((game.g_team1, game.g_group) for game in GameDetails)
    )

    def init_team_details():
        """
        初始化表数据
        """
        for team in teams:
            TeamDetails(
                t_team=team[0], t_group=team[1], t_goal_difference=0, t_integral=0
            )
            orm.commit()

    def update_team_details(team_name):
        """
        根据球队名称完善表数据

        :param team_name: 球队名称
        """
        _team = orm.select(t for t in TeamDetails if t.t_team == team_name).first()

        # 更新积分
        _team.t_integral = int(
            orm.select(
                sum(game.g_integral1)
                for game in GameDetails
                if game.g_team1 == "{}".format(team_name)
            ).first()
        ) + int(
            orm.select(
                sum(game.g_integral2)
                for game in GameDetails
                if game.g_team2 == "{}".format(team_name)
            ).first()
        )

        # 更新净胜球
        _team.t_t_goal_difference = orm.select(
            sum(team.g_goal_difference1)
            for team in GameDetails
            if team.g_team1 == "{}".format(team_name)
        ).first() + orm.select(
            sum(team.g_goal_difference2)
            for team in GameDetails
            if team.g_team2 == "{}".format(team_name)
        ).first()

        # 更新数据库
        orm.commit()

    init_team_details()
    for team in teams:
        update_team_details(team[0])


@orm.db_session
def most_goal_difference():
    """
    各小组净胜球最多的球队
    """
    _data = []
    for g in GROUPS:
        res = orm.select(x for x in TeamDetails if x.t_group == g).order_by(
            orm.desc(TeamDetails.t_goal_difference)
        )
        lst = [(r.t_team, r.t_goal_difference) for i, r in enumerate(res) if i < 1]
        _data.append({g: lst[0]})
    return _data


@orm.db_session
def most_integral():
    """
    各小组晋级的前两名，排名优先级：积分、净胜球、球队名)
    """
    _data = []
    for g in GROUPS:
        res = orm.select(x for x in TeamDetails if x.t_group == g).order_by(
            orm.desc(TeamDetails.t_integral),
            orm.desc(TeamDetails.t_goal_difference),
            orm.desc(TeamDetails.t_team),
        )
        lst = [(r.t_team, r.t_integral) for i, r in enumerate(res) if i < 2]
        _data.append({g: lst})
    return _data


@orm.db_session
def worst_games():
    """
    分差最大的三场比赛，按照比赛日期逆序排序
    """
    res = db.execute(
        "select (g_team1 || ':' ||  g_team2) as team, "
        "g_score1, g_score2, "
        "abs(g_score1 - g_score2) as score "
        "from GameDetails "
        "order by score desc, g_date"
    )
    return [(r[0], "{}:{}".format(r[1], r[2])) for i, r in enumerate(res) if i < 3]


@orm.db_session
def get_teams(page=1, per_page=32):
    """
    返回 32 强球队名称，使用分页

    :param page: 页数
    :param per_page: 每页数据数量
    """
    teams = orm.select(x for x in TeamDetails).page(page, pagesize=per_page)
    return [t.t_team for t in teams]


if __name__ == "__main__":
    add_game_details_data()
    add_team_details_data()
