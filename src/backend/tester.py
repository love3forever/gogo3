#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-22 21:00:45
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import unittest
from api.resources.dataCollector.data_poster import indexURL,\
    get_data_from_web, parse_index_data, get_playlist_data,\
    get_user_follows, get_user_fans, get_playlist_comments, \
    get_song_detail, get_song_comments, get_playlist_comments_withoffset

from api.server import app


class Test_Data_Poster(unittest.TestCase):
    """docstring for Data_Poster"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_data_from_web(self):
        assert get_data_from_web(indexURL) is not None

    def test_parse_index_data(self):
        assert parse_index_data() is not None


class Test_User_Poster(unittest.TestCase):
    """docstring for Test_User_Poster"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_user_follows(self):
        assert get_user_follows('77159064') is not None

    def test_get_user_fans(self):
        assert get_user_fans('77159064') is not None

    def test_get_playlist_comments(self):
        assert get_playlist_comments('625086991') is not None

    def test_get_song_comments(self):
        assert get_song_comments('18374880') is not None

    def test_get_song_detail(self):
        assert get_song_detail('18374880') is not None


class Test_Playlist_Api(unittest.TestCase):
    """docstring for Test_Playlist_Api"""

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_playlist_detail(self):
        rv = self.app.get('/api/v1/playlist/detail/62508699')
        assert rv.status_code == 200

    def test_playlist_comments(self):
        rv = self.app.get('/api/v1/playlist/comments/625086991')
        assert rv.status_code == 200

    def test_get_playlist_comments_withoffset(self):
        rv = self.app.get('/api/v1/playlist/comments/625086991/page/1')
        assert rv.status_code == 200

    def test_song_detail(self):
        rv = self.app.get('/api/v1/song/detail/18374880')
        assert rv.status_code == 200

    def test_song_comments(self):
        rv = self.app.get('/api/v1/song/comments/490006672')
        assert rv.status_code == 200

    def test_song_comments_withoffset(self):
        rv = self.app.get('/api/v1/song/comments/490006672/page/1')
        assert rv.status_code == 200

    def test_user_follows(self):
        rv = self.app.get('/api/v1/user/77159064/follows')
        assert rv.status_code == 200

    def test_user_fans(self):
        rv = self.app.get('/api/v1/user/77159064/fans')
        assert rv.status_code == 200

    def test_song_lyric(self):
        rv = self.app.get('/api/v1/song/lyrics/405343230')
        assert rv.status_code == 200

    def test_user_playlist(self):
        rv = self.app.get('/api/v1/user/77159064/playlist')
        assert rv.status_code == 200

    def test_artist_index_data(self):
        rv = self.app.get('/api/v1/artist/5346/index')
        assert rv.status_code == 200

    def test_artist_albums(self):
        rv = self.app.get('/api/v1/artist/5346/albums')
        assert rv.status_code == 200

    def test_user_detail(self):
        rv = self.app.get('/api/v1/user/98038167/detail')
        assert rv.status_code == 200

    def test_index_apis(self):
        rv = self.app.get('/api/v1/index/info')
        assert rv.status_code == 200


class Test_Index_Api(unittest.TestCase):
    """docstring for ClassName"""

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_index_detail(self):
        rv = self.app.get('/api/v1/index/detail')
        assert rv.status_code == 200


if __name__ == '__main__':
    unittest.main()
