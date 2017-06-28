#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 10:32:33
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output
from static_data import index_json

index_blueprint = Blueprint(__name__, "index_blueprint")
indexAPI = Api(index_blueprint, prefix='/api/v1/index')


@indexAPI.resource('/detail')
class Recommand(Resource):
    """docstring for Recommand"""

    def get(self):
        index_data = data_poster.parse_index_data()
        if index_data:
            return output(jsonify(index_data))
        else:
            return abort(404, 'no data avaliable')


@indexAPI.resource('/direct')
class DirectData(Resource):
    """docstring for DirectData"""

    def get(self):
        index_data = index_json
        if index_data:
            return output(jsonify(index_data))
        else:
            return abort(404, 'no data avaliable')


