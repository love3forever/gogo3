#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-21 14:22:57
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

album_blueprint = Blueprint(__name__, "album_blueprint")
albumAPI = Api(album_blueprint, prefix='/api/v1/album')


@albumAPI.resource('/<string:albumId>/detail')
class AlbumDetail(Resource):
    """docstring for AlbumDetail"""

    def get(self, albumId):
        data = data_poster.get_album_detail(albumId)
        if data:
            return output(jsonify(data))
        else:
            abort(404)


@albumAPI.resource('/<string:albumId>/comments/<int:page>')
class AlbumComments(Resource):
    """docstring for AlbumComments"""

    def get(self, albumId, page):
        data = data_poster.get_album_comments_withoffset(albumId, page)
        if data:
            return output(jsonify(data))
        else:
            abort(404)
