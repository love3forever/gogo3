<template>
  <div class="main">
    <div class="userhome">
      <div class="uh-head">
        <img src="http://p1.music.126.net/31NA7TgzLACMHO1Om1LQVw==/18636722092805728.jpg?param=180y180">
        <div class="uh-des">
          <div class="uhd-head">
            <h2>
              <span>一只林轩</span>
              <span class="userLv">
                <em>6</em>
                <i></i>
              </span>
              <i class="female"></i>
              <a href="javascript:;" class="sendMsg"><i>发私信</i></a>
              <a href="javascript:;" class="follow"><i>关&nbsp&nbsp注&nbsp</i></a>
            </h2>
          </div>
          <ul class="uhd-conect">
            <li id="li-frt">
              <a href="javascript:;"><strong>31</strong></br>动态</a>
            </li>
            <li>
              <a href="javascript:;"><strong>20</strong></br>关注</a>
            </li>
            <li>
              <a href="javascript:;"><strong>249</strong></br>粉丝</a>
            </li>
          </ul>
          <p class="self-intro">个人介绍：学生党，暂离。每月末回来，有事请留言或者加群Mamamoo部落粉丝群，群号码：493739853 ！ 私信已关闭，歌单:留言板(置顶) 做个歌单怎么这么难呢！ 笔芯～</p>
          <p class="uh-loca"><span>所在地区：吉林省 - 延边朝鲜族自治州</span><span>年龄：95后</span></p>
          <p class="uh-social">社交网络：<a href="" title="新浪微博" class="weibo"></a></p>
        </div>
      </div>
      <div class="uh-vid">
        <div class="u-title">
          <h3>一只林轩创建的专栏</h3>
        </div>
        <ul class="uh-vidio">
          <li>
            <a href="" class="vid-pic"><img src="http://p1.music.126.net/DHYfWefTsKDcR5pyzXS9Og==/1408474409807840.jpg?param=50y50"></a>
            <div class="vid-name"><a href="">只有音乐是我解药</a></div>
            <div class="vid-read">阅读总量：100000+</div>
            <div class="vid-update">最近更新2016-08-27</div>
            <div class="vid-circ">2期</div>
          </li>
        </ul>
      </div>
      <div class="uh-vid">
        <div class="u-title">
          <h3>一只林轩创建的电台</h3>
        </div>
        <ul class="uh-vidio">
          <li>
            <a href="" class="vid-pic"><img src="http://p1.music.126.net/Gdh7VcGd22emCGjHiNMgtw==/3439272373022999.jpg?param=50y50"></a>
            <div class="vid-rec"><a href="">晓苏电台</a></div>
            <div class="vid-update">订阅398749次</div>
            <div class="vid-circ">551期</div>
          </li>
        </ul>
      </div>
      <div class="uh-crt">
        <div class="u-title">
          <h3>一只林轩创建的歌单（70）</h3>
        </div>
          <ul id="uh-listwrap" class="hot-item">
            <li v-for="item in hotitem" class="uh-list">
              <div class="item-wrap">
                <img :src="item.img">
                <router-link :to="'/use/playlist/'+'510911448'" class="msk"></router-link>
                <div class="item-bottom">
                  <span class="ico"></span>
                  <span class="hot-num">{{item.playTimes}}</span>
                  <a href="/#" class="hotplay"></a>
                </div>
              </div>
              <p class="p-over uh-listdes"><router-link :to="'/use/playlist/'+'233333'" class="hot-descrp">{{item.playlistTitle}}</router-link><!--<sub v-if="item[3]"></sub>--></p>
            </li>
          </ul>
      </div>
      <div class="uh-fav">
        <div class="u-title">
          <h3>一只林轩收藏的歌单（270）</h3>
        </div>
          <ul id="uh-listwrap" class="hot-item">
            <li v-for="item in hotitem" class="uh-list">
              <div class="item-wrap">
                <img :src="item.img">
                <router-link :to="'/use/playlist/'+'510911448'" class="msk"></router-link>
                <div class="item-bottom">
                  <span class="ico"></span>
                  <span class="hot-num">{{item.playTimes}}</span>
                  <a href="/#" class="hotplay"></a>
                </div>
              </div>
              <p class="p-over uh-listdes"><router-link :to="'/use/playlist/'+'233333'" class="hot-descrp">{{item.playlistTitle}}</router-link><!--<sub v-if="item[3]"></sub>--></p>
            </li>
          </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'user',
  data () {
    return {
       hotitem:[
          {img:"/static/hot01.jpg",playTimes:"220万",playlistTitle:"2017年五月最热新歌TOP50",art:"王萌"},
          {img:"/static/hot02.jpg",playTimes:"25万",playlistTitle:"『福音之旅』聆听清风絮语，静沐斜阳暖心",art:"王萌"},
          {img:"/static/hot03.jpg",playTimes:"48万",playlistTitle:"『电音故事』从生命的起源说起",art:"王萌"},
          {img:"/static/hot04.jpg",playTimes:"18230",playlistTitle:"『哲学公开课』切实的幸福",art:"王萌"},
          {img:"/static/hot05.jpg",playTimes:"220万",playlistTitle:"『锐韧Trap』风骚霸道，黑暗的迷人性格",art:"王萌"},
          {img:"/static/hot06.jpg",playTimes:"220万",playlistTitle:"健身小白应该注意些啥？",art:"王萌"},
          {img:"/static/hot07.jpg",playTimes:"220万",playlistTitle:"Deep House深窈之道",art:"王萌"},
          {img:"/static/hot08.jpg",playTimes:"220万",playlistTitle:"刘瑜：色",art:"王萌"},
      ],
    }
  },
}
</script>

<style>
.uh-vid h3{
  color: rgb(102,102,102);
}
.uh-vidio div{
  float: left;
  height: 50px;
  margin-left: 10px;
  font-size: 12px;
  line-height: 50px;
  text-align: left;
  vertical-align: middle;
}
div.vid-circ{
  width: 50px;
  text-align: right;
}
.vid-read{
  width: 160px;
}
.vid-update{
  width: 190px;
}
.vid-rec{
  width: 500px;
  padding-right: 38px;
}
.vid-rec a,.vid-name a{
  color: rgb(0,0,0);
}
.vid-rec:hover,.vid-name:hover{
  text-decoration: underline;
}
.uh-vidio{
  list-style-type: none;
  padding: 0;
  border: 1px solid rgb(229,229,229);
  border-top: 0;
  margin: 0 0 24px 0;
}
.uh-vidio li{
  height: 50px;
  padding: 10px 0;
}
.vid-name{
  width: 331px;
  padding-right: 38px;
}
.vid-pic{
  float: left;
  width: 50px;
  height: 50px;
  margin-left: 20px;
}
.vid-pic img{
  width: 100%;
  height: 100%;
}
.uh-listdes{
  margin: 8px 0 3px 0;
}
.uh-listdes a{
  color: rgb(0,0,0);
  font-size: 14px;
}
#uh-listwrap{
  margin-left: -50px;
}
li.uh-list{
  height: 165px;
  padding-left: 50px;
  float: left;
}
.weibo{
  background: url(../assets/logo.png) no-repeat scroll 0 0;
}
.uh-social a{
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-right: 20px;
  vertical-align: middle;
}
.uh-loca{
    overflow: hidden;
}
.uh-loca span{
  margin-right: 20px;
}
.uhd-conect{
  list-style-type: none;
  padding: 0;
  overflow: hidden;
}
.uhd-conect li{
  float: left;
  padding:0 40px 0 20px;
  border-left: 1px solid rgb(221,221,221);
  text-align: center;
}
.uhd-conect strong{
  font-size: 24px;
  font-weight: normal;
}
.uhd-conect a:hover{
  color: #4996d1;
}
#li-frt{
  border:0;
}
.uhd-head{
  overflow: hidden;
  padding-bottom: 10px;
  border-bottom: 1px solid rgb(221,221,221);
}
.follow{
  float: left;
  width: 40px;
  height: 31px;
  margin: 4px 0 0 15px;
  padding-left: 30px;
  background: url(../assets/button.png) no-repeat scroll 0 -720px;
  line-height: 31px;
  color: white;
}
.sendMsg{
  float: left;
  width: 75px;
  height: 31px;
  margin: 4px 0 0 15px;
  background: url(../assets/button.png) no-repeat scroll 0 -810px;
  line-height: 31px;
}
.sendMsg i,.follow i{
  float: right;
  margin-right: 8px;
}
.female{
  float: left;
  width: 20px;
  height: 20px;
  margin: 8px 0 0 9px;
  background: url(../assets/icon.png) no-repeat scroll -41px -27px;
}
.userLv{
  height: 19px;
  padding-left: 29px;
  margin: 8px 0 0 10px;
  background: url(../assets/icon2.png) no-repeat scroll -135px -190px;
  color: rgb(224,58,36);
  font-size: 14px;
  line-height: 21px;
  font-weight: bold;
  vertical-align: middle;
}
.userLv em{
  float: left;
}
.userLv i{
  float: right;
  width: 9px;
  height: 19px;
  background: url(../assets/icon2.png) no-repeat scroll -191px -190px;
}
.uh-des{
  padding-left: 228px;
}
.uh-des p{
  font-size: 12px;
  line-height: 21px;
  margin: 0 0 5px 0;
}
.uh-des h2{
  float: left;
  margin: 0;
  font-size: 22px;
  font-weight: normal;
  color: black;
}
.uh-des span{
  float: left;
}
.uh-head{
  position: relative;
  margin-bottom: 43px;
  text-align: left;
}
.uh-head img{
  position: absolute;
  top:0;
  width: 188px;
  height: 188px;
  padding: 3px;
  border: 1px solid rgb(213,213,213);
}
.userhome{
  padding: 40px;
}
</style>

