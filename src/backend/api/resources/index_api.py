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


index_json = {
    "blk": [
        {
            "href": "/discover/toplist?id=19723756",
            "img": "http://p4.music.126.net/DrRIg6CrgDfVLEph9SNh7w==/18696095720518497.jpg?param=100y100",
            "more": "/discover/toplist?id=19723756",
            "songs": [
                {
                    "songHref": "/song?id=483671599",
                    "songName": "追光者"
                },
                {
                    "songHref": "/song?id=482988471",
                    "songName": "2U"
                },
                {
                    "songHref": "/song?id=482386132",
                    "songName": "Now Or Never (R3hab Remix)"
                },
                {
                    "songHref": "/song?id=484058255",
                    "songName": "浓情淡如你"
                },
                {
                    "songHref": "/song?id=460409848",
                    "songName": "All On Me"
                },
                {
                    "songHref": "/song?id=465833911",
                    "songName": "Tell 'Em Why"
                },
                {
                    "songHref": "/song?id=483690425",
                    "songName": "死在江南烟雨中"
                },
                {
                    "songHref": "/song?id=482386220",
                    "songName": "微光"
                },
                {
                    "songHref": "/song?id=484056987",
                    "songName": "一瞬间"
                },
                {
                    "songHref": "/song?id=484058973",
                    "songName": "我们"
                }
            ],
            "title": "云音乐飙升榜"
        },
        {
            "href": "/discover/toplist?id=3779629",
            "img": "http://p4.music.126.net/N2HO5xfYEqyQ8q6oxCw8IQ==/18713687906568048.jpg?param=100y100",
            "more": "/discover/toplist?id=3779629",
            "songs": [
                {
                    "songHref": "/song?id=483671599",
                    "songName": "追光者"
                },
                {
                    "songHref": "/song?id=482988471",
                    "songName": "2U"
                },
                {
                    "songHref": "/song?id=480426313",
                    "songName": "There For You"
                },
                {
                    "songHref": "/song?id=482988834",
                    "songName": "男孩"
                },
                {
                    "songHref": "/song?id=476987525",
                    "songName": "咖喱咖喱"
                },
                {
                    "songHref": "/song?id=479422013",
                    "songName": "阿婆说"
                },
                {
                    "songHref": "/song?id=479408220",
                    "songName": "凉凉"
                },
                {
                    "songHref": "/song?id=482386133",
                    "songName": "那个男孩"
                },
                {
                    "songHref": "/song?id=479979440",
                    "songName": "最初的记忆"
                },
                {
                    "songHref": "/song?id=479028095",
                    "songName": "天已黑"
                }
            ],
            "title": "云音乐新歌榜"
        },
        {
            "href": "/discover/toplist?id=2884035",
            "img": "http://p3.music.126.net/sBzD11nforcuh1jdLSgX7g==/18740076185638788.jpg?param=100y100",
            "more": "/discover/toplist?id=2884035",
            "songs": [
                {
                    "songHref": "/song?id=482633543",
                    "songName": "战"
                },
                {
                    "songHref": "/song?id=482999745",
                    "songName": "你说"
                },
                {
                    "songHref": "/song?id=481537120",
                    "songName": "答案"
                },
                {
                    "songHref": "/song?id=479219330",
                    "songName": "我一定会爱上你"
                },
                {
                    "songHref": "/song?id=483378714",
                    "songName": "Candy Girl"
                },
                {
                    "songHref": "/song?id=483380284",
                    "songName": "成长学"
                },
                {
                    "songHref": "/song?id=482724567",
                    "songName": "Big Things Start Small"
                },
                {
                    "songHref": "/song?id=482044211",
                    "songName": "给你"
                },
                {
                    "songHref": "/song?id=481535136",
                    "songName": "念念不忘"
                },
                {
                    "songHref": "/song?id=482809168",
                    "songName": "夏日的最后一天"
                }
            ],
            "title": "网易原创歌曲榜"
        }
    ],
    "hotdj": [
        {
            "desc": "美食家陈立教授",
            "href": "/user/home?id=278438485",
            "img": "http://s4.music.126.net/style/web2/img/default/default_avatar_40.jpg",
            "name": "陈立"
        },
        {
            "desc": "著名音乐节目主持人",
            "href": "/user/home?id=91239965",
            "img": "http://s4.music.126.net/style/web2/img/default/default_avatar_40.jpg",
            "name": "DJ艳秋"
        },
        {
            "desc": "国家大剧院古典音乐官方",
            "href": "/user/home?id=324314596",
            "img": "http://s4.music.126.net/style/web2/img/default/default_avatar_40.jpg",
            "name": "国家大剧院古典音乐频道"
        },
        {
            "desc": "南京电台主持人王馨",
            "href": "/user/home?id=1611157",
            "img": "http://s4.music.126.net/style/web2/img/default/default_avatar_40.jpg",
            "name": "谢谢收听"
        },
        {
            "desc": "独立DJ，CRI环球旅游广播特邀DJ",
            "href": "/user/home?id=2313954",
            "img": "http://s4.music.126.net/style/web2/img/default/default_avatar_40.jpg",
            "name": "DJ晓苏"
        }
    ],
    "newAlbum": [
        {
            "artistHref": "/artist?id=1150195",
            "artistName": "Alien: Covenant (Original Motion Picture Soundtrack)",
            "href": "/album?id=35454135",
            "img": "http://p3.music.126.net/PxM5uQhsi0eFyVz2Wyau6A==/17792297161094069.jpg?param=100y100",
            "title": "Alien: Covenant (Original Motion Picture Soundtrack)"
        },
        {
            "artistHref": "/artist?id=1144046",
            "artistName": "疑問疑答",
            "href": "/album?id=35622056",
            "img": "http://p3.music.126.net/1dr3ocTbXETt-kbo-MfK0g==/18897306346769222.jpg?param=100y100",
            "title": "疑問疑答"
        },
        {
            "artistHref": "/artist?id=187462",
            "artistName": "现在口红",
            "href": "/album?id=35623145",
            "img": "http://p3.music.126.net/HPE5G78Eba1GSXwjUPLqEg==/18957779486268471.jpg?param=100y100",
            "title": "现在口红"
        },
        {
            "artistHref": "/artist?id=784001",
            "artistName": "Melodrama",
            "href": "/album?id=35196822",
            "img": "http://p3.music.126.net/MHIvytC5RXh5Lp2J_3tpaQ==/19017153114022258.jpg?param=100y100",
            "title": "Melodrama"
        },
        {
            "artistHref": "/artist?id=896139",
            "artistName": "Harder",
            "href": "/album?id=35448085",
            "img": "http://p3.music.126.net/3NBWin48FvpUj78qrQHLng==/18158434533531204.jpg?param=100y100",
            "title": "Harder"
        },
        {
            "artistHref": "/artist?id=127815",
            "artistName": "What's my name?",
            "href": "/album?id=35623239",
            "img": "http://p4.music.126.net/S9FIZSfEeMJtfqGsHtS8uw==/18755469348547338.jpg?param=100y100",
            "title": "What's my name?"
        },
        {
            "artistHref": "/artist?id=31211",
            "artistName": "2U",
            "href": "/album?id=35589530",
            "img": "http://p4.music.126.net/JupZKGWHlaXcpuX8UQBvkw==/19001759951394104.jpg?param=100y100",
            "title": "2U"
        },
        {
            "artistHref": "/artist?id=126737",
            "artistName": "OVER 10 YEARS",
            "href": "/album?id=35590079",
            "img": "http://p4.music.126.net/D35HY2PGv1uA7PU6s8di9g==/19076526742085503.jpg?param=100y100",
            "title": "OVER 10 YEARS"
        },
        {
            "artistHref": "/artist?id=21138",
            "artistName": "군주 - 가면의 주인 OST",
            "href": "/album?id=35471013",
            "img": "http://p3.music.126.net/oFjH859GalfHpgOilvcAlQ==/18756568860175990.jpg?param=100y100",
            "title": "군주 - 가면의 주인 OST"
        },
        {
            "artistHref": "/artist?id=122455",
            "artistName": "欢乐颂2 电视原声带",
            "href": "/album?id=35456292",
            "img": "http://p3.music.126.net/Wl7T1LBRhZFg0O26nnR2iQ==/19217264230385030.jpg?param=100y100",
            "title": "欢乐颂2 电视原声带"
        }
    ],
    "newSinger": [
        {
            "desc": "台湾歌手张惠妹",
            "href": "/user/home?id=29879272",
            "img": "http://p3.music.126.net/p9U80ex1B1ciPFa125xV5A==/5931865232210340.jpg?param=62y62",
            "name": "张惠妹aMEI"
        },
        {
            "desc": "原创电子唱作人",
            "href": "/user/home?id=188304",
            "img": "http://p3.music.126.net/BvFxS88342IznhCjp6jJKg==/5783431162155757.jpg?param=62y62",
            "name": "尚雯婕"
        },
        {
            "desc": "国内知名演唱组合 羽泉",
            "href": "/user/home?id=200645",
            "img": "http://p3.music.126.net/VIxIhQPW2wTREM_DfToHUA==/2107763790458943.jpg?param=62y62",
            "name": "羽泉组合"
        },
        {
            "desc": "个体音乐人李志",
            "href": "/user/home?id=9753203",
            "img": "http://p3.music.126.net/nS7TH_KYtj5lJr8OxDKgWw==/3263350517410958.jpg?param=62y62",
            "name": "李志"
        },
        {
            "desc": "民谣音乐人",
            "href": "/user/home?id=1742138",
            "img": "http://p4.music.126.net/2iIlyuUKcyee0x1v4TzXTg==/1375489058855837.jpg?param=62y62",
            "name": "马頔麻油叶"
        }
    ],
    "recommendList": [
        {
            "img": "http://p1.music.126.net/tPyQJY1xWTIsWnj7ZrCKeA==/18915998044418188.jpg?param=140y140",
            "playTimes": "36万",
            "playlistID": "746818250",
            "playlistTitle": "【avex 精选】不能错过的日语情歌50首",
            "playlistURL": "https://music.163.com//playlist?id=746818250"
        },
        {
            "img": "http://p1.music.126.net/jDJsNKjSxrqCw07n4VQvOA==/18512477277807530.jpg?param=140y140",
            "playTimes": "31万",
            "playlistID": "435591496",
            "playlistTitle": "艺术之花 诗遇上歌",
            "playlistURL": "https://music.163.com//playlist?id=435591496"
        },
        {
            "img": "http://p1.music.126.net/TmqvlaaHkIJTY5yh6aHhFA==/109951162914219071.jpg?param=140y140",
            "playTimes": "49万",
            "playlistID": "708628804",
            "playlistTitle": "『电音故事』 从生命的起源说起",
            "playlistURL": "https://music.163.com//playlist?id=708628804"
        },
        {
            "img": "http://p1.music.126.net/wuHe-dgRfrGVHK5Ly3xN-g==/18884112207233426.jpg?param=140y140",
            "playTimes": "5034",
            "playlistID": "906818951",
            "playlistTitle": "宇宙自然生命简史：08给地球称重",
            "playlistURL": "https://music.163.com//dj?id=906818951"
        },
        {
            "img": "http://p1.music.126.net/NqpT4F90b3TBCIJCDK79-w==/18953381439724341.jpg?param=140y140",
            "playTimes": "47万",
            "playlistID": "639952963",
            "playlistTitle": "Deep House 深窈之道",
            "playlistURL": "https://music.163.com//playlist?id=639952963"
        },
        {
            "img": "http://p1.music.126.net/xkJ-ho7eF9yTtN2bC6fThg==/19062233090864456.jpg?param=140y140",
            "playTimes": "159",
            "playlistID": "906916922",
            "playlistTitle": "【科学育儿】最好的学区房，是家里的书房",
            "playlistURL": "https://music.163.com//dj?id=906916922"
        },
        {
            "img": "http://p1.music.126.net/PazOqyr94vElWADRfTaFKQ==/18897306346737746.jpg?param=140y140",
            "playTimes": "62万",
            "playlistID": "738685644",
            "playlistTitle": "Tropical House丨侧耳倾听，入耳的美妙旋律",
            "playlistURL": "https://music.163.com//playlist?id=738685644"
        },
        {
            "img": "http://p1.music.126.net/oPe0vzDJzs5oAnFFiaGTIQ==/18932490718858937.jpg?param=140y140",
            "playTimes": "17万",
            "playlistID": "906892796",
            "playlistTitle": "“你是我唯一的美梦，也是我唯一的烦恼”",
            "playlistURL": "https://music.163.com//dj?id=906892796"
        }
    ]
}
