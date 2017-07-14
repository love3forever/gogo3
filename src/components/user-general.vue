<template>
  <div class="uh-content">
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
            <p class="p-over uh-listdes"><router-link :to="'/use/playlist/'+'233333'" class="hot-descrp">{{item.playlistTitle}}</router-link></p>
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
            <p class="p-over uh-listdes"><router-link :to="'/use/playlist/'+'233333'" class="hot-descrp">{{item.playlistTitle}}</router-link></p>
          </li>
        </ul>
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
</style>

