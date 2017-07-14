#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-15 01:14:32
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api, abort
from flask import jsonify
from dataCollector import data_poster
from common_funcs import output

artist_blueprint = Blueprint(__name__, "artist_blueprint")
artistAPI = Api(artist_blueprint, prefix='/api/v1/artist')


@artistAPI.resource('/<string:artistId>/index')
class ArtistIndex(Resource):
    """docstring for ArtistIndex"""

    def get(self, artistId):
        if artistId:
            index_data = data_poster.get_artist_index_page(artistId)
            if index_data:
                return output(jsonify(index_data))
            else:
                abort('no data for artist with id:{}'.format(artistId))
        else:
            abort(
                'please request with correct artist id, \current id is:{}'.format(artistId))
