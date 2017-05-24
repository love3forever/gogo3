#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-22 21:00:45
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import unittest
from dataCollector.data_poster import indexURL, get_data_from_web,\
    parse_index_data, get_playlist_data, get_user_follows, get_user_fans


class Test_Data_Poster(unittest.TestCase):
    """docstring for Data_Poster"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_data_from_web(self):
        assert get_data_from_web(indexURL) is not None

    def test_parse_index_data(self):
        assert len(parse_index_data()) == 8

    def test_get_playlist_data(self):
        playlist = parse_index_data()[0]['playlistID']
        assert get_playlist_data(playlist) is not None


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


if __name__ == '__main__':
    unittest.main()
