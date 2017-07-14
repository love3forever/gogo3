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
songAPI = Api(song_blueprint, prefix='/api/v1/song')


@songAPI.resource('/detail/<string:songId>')
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
                404, message='do request with a right songId, \
                current id:{}'.format(songId))


@songAPI.resource('/comments/<string:songId>')
class SongComments(Resource):
    """docstring for SongComments"""

    def get(self, songId):
        if songId:
            data = data_poster.get_song_comments(songId)
            if data:
                result = {
                    "songid": songId,
                    "comments": data,
                    "code": 200
                }
                return output(jsonify(result))
            else:
                abort(404, message='no song comments for {}'.format(songId))
        else:
            abort(
                404, message='do request with a right songId, \
                current id:{}'.format(songId))


@songAPI.resource('/comments/<string:songId>/page/<int:page>')
class SongCommentsWithPage(Resource):
    """docstring for SongCommentsWithPage"""

    def get(self, songId, page):
        if songId:
            data = data_poster.get_song_comments_withoffset(songId, page)
            if data:
                return output(jsonify(data))
            else:
                abort(404, message='no song comments for {} on page {}'.format(
                    songId, page))
        else:
            abort(
                404, message='do request with a right songId and\
                 page number, current id:{} and current page:{}\
                 '.format(songId, page))


@songAPI.resource('/lyrics/<string:songId>')
class LyricsOfSong(Resource):
    """docstring for LyricsOfSong"""

    def get(self, songId):
        if songId:
            data = data_poster.get_lyric(songId)
            if data:
                return output(jsonify(data))
            else:
                abort(404, message='no lyrics for song:{}'.format(songId))
        else:
            abort(
                404, message='do request with a right songId, \
                current id:{}'.format(songId))
