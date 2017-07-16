<template>
  <div>
    <div class="uh-content" v-if="playlistCreate">
  <!--     <div class="uh-vid">
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
      </div> -->
      <div class="uh-crt">
        <div class="u-title">
          <h3>{{`创建的歌单${playlistCreateCount}`}}</h3>
        </div>
          <ul id="uh-listwrap" class="hot-item">
            <li v-for="item in playlistCreate" class="uh-list">
              <div class="item-wrap">
                <img :src="item.img" class="creat-wrap">
                <router-link :to="'/playlist/'+item.id" class="msk"></router-link>
                <div class="item-bottom">
                  <span class="ico"></span>
                  <span class="hot-num">{{item.playTimes}}</span>
                  <a href="/#" class="hotplay"></a>
                </div>
              </div>
              <p class="p-over uh-listdes"><router-link :to="'/playlist/'+item.id" class="hot-descrp">{{item.playlistTitle}}</router-link></p>
            </li>
          </ul>
      </div>
  <!--     <div class="uh-fav">
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
      </div> -->
    </div>
    <div class="loading" v-if="!playlistCreate">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'user',
  data () {
    return {
      playlistCreate:[],
      playlistCreateCount:0,
    }
  },
  beforeCreate:function(){
    //请求歌单数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/user/${this.$route.params.id}/playlist`)
      .then(response => {
         var result= response.data.playlist;//初始化全部歌单数据
         this.playlistCreateCount = result.length;

         for (var item of result){
          console.log(item)
          this.playlistCreate.push({
            id:item.id,
            img:item.coverImgUrl,
            playTimes:item.playCount,
            playlistTitle:item.name,
          });
         }

      })
      .catch(response => {
        console.log(response)
    });
  },

}
</script>

<style>
.creat-wrap{
  width: 140px;
  height: 140px;
}
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

