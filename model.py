#!/usr/bin/env python
# coding=utf-8

import datetime

from pony import orm

db = orm.Database()


class GameDetails(db.Entity):
    g_score1 = orm.Required(int)
    g_score2 = orm.Required(int)
    g_team1 = orm.Required(str)
    g_team2 = orm.Required(str)
    g_group = orm.Required(str)
    g_date = orm.Required(datetime.datetime)
    g_integral1 = orm.Required(int)
    g_integral2 = orm.Required(int)
    g_goal_difference1 = orm.Required(int)
    g_goal_difference2 = orm.Required(int)


class TeamDetails(db.Entity):
    t_team = orm.Required(str)
    t_group = orm.Required(str)
    t_goal_difference = orm.Required(int)
    t_integral = orm.Required(int)


db.bind(provider="sqlite", filename="database.sqlite", create_db=False)
db.generate_mapping(create_tables=False)
