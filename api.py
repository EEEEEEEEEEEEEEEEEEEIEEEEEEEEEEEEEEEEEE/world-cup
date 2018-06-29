#!/usr/bin/env python
# coding=utf-8

from flask import Flask, jsonify, request
from controller import get_teams, most_integral, most_goal_difference, worst_games

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/all_teams")
def all_teams():
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 32))
        return jsonify(get_teams(page, per_page))
    except:
        return jsonify({"error": "请输入正确格式的 page/per_page 参数"})


@app.route("/most_gd")
def api_most_gd():
    return jsonify(most_goal_difference())


@app.route("/most_integral")
def api_most_integral():
    return jsonify(most_integral())


@app.route("/worst_games")
def api_worst_games():
    return jsonify(worst_games())


if __name__ == "__main__":
    app.run(debug=True)
