#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-11 14:51:53
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

djradio_blueprint = Blueprint(__name__, "djradio_blueprint")
djradioAPI = Api(djradio_blueprint, prefix='/api/v1/djradio')


@djradioAPI.resource('/comments/<string:djId>/page/<int:page>')
class DjRadioComments(Resource):
    """docstring for DjRadioComments"""

    def get(self, djId, page):
        data = data_poster.get_djradio_comments_withoffset(djId, page)
        if data:
            return output(jsonify(data))
        else:
            abort(404)


@djradioAPI.resource('/detail/<string:djId>')
class DjDetail(Resource):
    """docstring for DjDetail"""

    def get(self, djId):
        data = data_poster.get_djradio_detail(djId)
        if data:
            return output(jsonify(data))
        else:
            abort(404)
