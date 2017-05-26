#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 22:57:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

song_blueprint = Blueprint(__name__, 'song_blueprint')
songAPI = Api(song_blueprint)


@songAPI.resource('/api/v1/song/detail/<string:songId>')
class SongDetail(Resource):
    """get song detail by song id"""

    def get(self, songId):
        if songId:
            data = data_poster.get_song_detail(songId)
            if data:
                return output(jsonify(data))
            else:
                abort(404, message='no song detail for {}'.format(songId))
        else:
            abort(
                404, message='do request with a right songId, current id:{}'.format(songId))


@songAPI.resource('/api/v1/song/comments/<string:songId>')
class SongComments(Resource):
    """docstring for SongComments"""

    def get(self, songId):
        if songId:
            data = data_poster.get_song_comments(songId)
            if data:
                return output(jsonify(data))
            else:
                abort(404, message='no song comments for {}'.format(songId))
        else:
            abort(
                404, message='do request with a right songId, current id:{}'.format(songId))
