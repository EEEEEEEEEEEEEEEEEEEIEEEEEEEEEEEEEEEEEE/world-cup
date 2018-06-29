#!/usr/bin/env python
# coding=utf-8

import datetime

from pony import orm

db = orm.Database()


class GameDetails(db.Entity):
    """
    比赛详细情况实体模型
    """
    # 德国：韩国 0:2，德国为 `1`（左边队伍）, 韩国为 `2`（右边队伍）
    # 左边队伍进球数
    g_score1 = orm.Required(int)
    # 右边队伍进球数
    g_score2 = orm.Required(int)
    # 左边队伍名称
    g_team1 = orm.Required(str)
    # 右边队伍名称
    g_team2 = orm.Required(str)
    # 两队的分组
    g_group = orm.Required(str)
    # 比赛日期
    g_date = orm.Required(datetime.datetime)
    # 左边队伍积分
    g_integral1 = orm.Required(int)
    # 右边队伍积分
    g_integral2 = orm.Required(int)
    # 左边队伍净胜球
    g_goal_difference1 = orm.Required(int)
    # 右边队伍净胜球
    g_goal_difference2 = orm.Required(int)


class TeamDetails(db.Entity):
    """
    球队详细情况实体模型
    """
    # 球队名称
    t_team = orm.Required(str)
    # 球队分组
    t_group = orm.Required(str)
    # 球队净胜球
    t_goal_difference = orm.Required(int)
    # 球队积分
    t_integral = orm.Required(int)


# 数据库绑定以及映射
db.bind(provider="sqlite", filename="database.sqlite", create_db=False)
db.generate_mapping(create_tables=False)
