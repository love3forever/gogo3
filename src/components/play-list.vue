<template>
  <div class="playlist main">
    <div  v-show="hasResult">
      <div class="playlist-left">
        <div class="playlist-head">
          <div class="playlist-cover">
            <img :src="songs.coverImgUrl">
            <span></span>
          </div>
          <div class="playlist-content">
            <div class="content-title">
              <i></i>
              <h2>{{songs.name}}</h2>
            </div>
            <div class="content-author">
              <a href="'/user/'+songs.creator.id"><img :src="songs.creator.avatarUrl"></a>
              <span><router-link :to="'/user/'+songs.creator.userId" class="author-link">{{songs.creator.nickname}}</router-link></span>
              <sup></sup>
              <span>{{songs.createtime}}&nbsp创建</span>
            </div>
            <div class="content-opreation">
              <a href="#" class="btn-play">
                <i><em class="ply"></em>播放</i>
              </a>
              <a href="#" class="add-to"></a>
              <a href="#" class="btn-fav">
                <i>{{`(${songs.subscribedCount})`}}</i>
              </a>
              <a href="#" class="btn-share">
                <i>{{`(${songs.shareCount})`}}</i>
              </a>
              <a href="#" class="btn-dl">
                <i>下载</i>
              </a>
              <a href="#" class="btn-cm">
                <i>{{`(${songs.commentCount})`}}</i>
              </a>
              <div class="clear"></div>
            </div>
            <div class="content-tag">
              <b>标签：</b>
              <a href="#" class="u-tag" v-for="tag in songs.tags">
                <i>{{tag}}</i>
              </a>
              <div class="clear"></div>
            </div>
            <pre v-show="!songs.isShowMore"><b class="u-desc">介绍：</b>{{songs.descDot}}<b class="u-desc" v-show="songs.descMore">...</b></pre>
            <pre v-show="songs.isShowMore"><b class="u-desc">介绍：</b>{{songs.descMore}}</pre>
            <div class="show-more" v-if="songs.descMore">
              <a href="javascript:;" class="fr" @click="tabShowMore">{{songs.isShowMore?"收起":"展开"}}</a>
              <i class="u-ico" :class="{'u-icoActive':songs.isShowMore}"></i>
            </div>
          </div>
        </div>
        <div class="playlist-tracks">
          <div class="u-title">
            <h3>歌曲列表</h3>
            <span class="u-lft">{{`${songs.trackCount}首歌`}}</span>
            <span class="u-rgt">播放：<strong>{{songs.playCount}}</strong>次</span>
            <div class="u-rgt">
              <i></i>
              <a href="">生成外链播放器</a>
            </div>
          </div>
          <div class="u-content">
            <table class="tracks-table">
              <thead>
                <tr>
                  <th class="w1"><div class="u-wrap"></div></th>
                  <th><div class="u-wrap">歌曲标题</div></th>
                  <th class="w2"><div class="u-wrap">时长</div></th>
                  <th class="w3"><div class="u-wrap">歌手</div></th>
                  <th class="w4"><div class="u-wrap">专辑</div></th>
                </tr>
              </thead>
              <tbody @click="plySong">
                <tr v-for="(track,index) in songs.tracks" :class="{'track-fill':index%2==0}">
                  <td>
                    <div class="w-ply">
                      <em>{{index+1}}</em>
                      <span :class="[track.click?'tracks-cli':'tracks-ply']" :data-tag="index"></span>
                    </div>
                  </td>
                 <td class="p-over">
                   <router-link :to="'/song/'+track.id" :title="track.songName">
                    {{track.songName}}
                   </router-link>
                 </td>
                  <td>{{track.duration}}</td>
                  <td class="p-over">
                    <router-link :to="'/artist/'+track.artId" :title="track.artName">
                      {{track.artName}}
                    </router-link>
                  </td>
                  <td class="p-over">
                    <router-link :to="'/album/'+track.albId" :title="track.albName">
                      {{track.albName}}
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <comment :url="cmtUrl"></comment>
      </div>
      <playlistRight></playlistRight>
    </div>
    <div class="loading" v-show="!hasResult">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import playlistRight from './generalRight'
import comment from './generalComment'
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'playlist',
  components:{
    playlistRight,comment
  },
  data () {
    return {
      hasResult:false,//是否返回歌单数据
      songs:{//歌单
        coverImgUrl:null,
        name:null,
        subscribedCount:null,
        shareCount:null,
        commentCount:null,
        tags:null,
        trackCount:null,
        playCount:null,
        tracks:null,     //歌曲
        creator:{},    //歌单创建者
        createtime:null, //歌单创建时间
        descDot:null,    //歌单介绍part1
        descMore:null,   //歌单介绍part2
        isShowMore:false,//歌单介绍是否展开
      },
      listUrl:`http://123.206.211.77:33333/api/v1/playlist/detail/${this.$route.params.id}`,
      cmtUrl:`http://123.206.211.77:33333/api/v1/playlist/comments/${this.$route.params.id}/page/`,
    }
  },
  methods:{
    //歌单介绍-展开/收起按钮点击事件
    tabShowMore:function(){
      this.songs.isShowMore = !this.songs.isShowMore;
    },
    //歌单播放按钮点击事件
    plyClick:function(index){
      var clickList = this.songs.tracks.map(function(item){
        return item.click;
      });

      var current = clickList.indexOf(true);
      if (current>-1){
        mouseBtnEv.setNewVal(this.songs.tracks[current], 'click', false);
      }
      mouseBtnEv.setNewVal(this.songs.tracks[index], 'click', true);
    },
    //歌单播放按钮点击事件代理
    plySong:function(ev){
      var ev = ev||window.event;
      var target = ev.target||ev.srcElement;

      if (target.nodeName.toLowerCase() == "span"){
        var index = parseInt(target.dataset.tag);
        this.plyClick(index);             
      }
    },
  },
  created:function(){
    //请求歌单数据
    this.$http.get(this.listUrl)
      .then(response => {
        this.hasResult = response.data.result;//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
  },
  watch:{
    //歌单数据返回后，提取、格式化需要的数据
    hasResult:function(result){
      //解构result.tracks
      var originTracks = result.tracks,
          list = new Array();
      for ( let item of originTracks ){ 
        let { id,duration, name:songName, album:{name:albName}, album:{id:albId}, album:{artists:[{name:artName}]}, album:{artists:[{id:artId}]}} = item;
        duration = mouseBtnEv.changeTime(duration);
        list.push({ id, duration, songName, albName, albId, artName, artId, click:false});
      }
      //初始化songs
      this.songs = {
        coverImgUrl:result.coverImgUrl,
        name:result.name,
        subscribedCount:result.subscribedCount,
        shareCount:result.shareCount,
        commentCount:result.commentCount,
        tags:result.tags,
        trackCount:result.trackCount,
        playCount:result.playCount,
        tracks:list,
        creator:result.creator,
        createtime:new Date(result.createTime).toLocaleDateString().replace(/\//g,"-"),
        descDot:result.description.substr(0,99),
        descMore: result.description.length>99?result.description:null,
        isShowMore:false,   
      };
    },
  }
}
</script>

<style>
.loading{
  height: 1000px;
  line-height: 1000px;
  font-size:12px;
  text-align: center;
}
.loading i{
  width: 16px;
  height: 16px;
  vertical-align: middle;
  background: url(../assets/loading.gif) no-repeat scroll 0 0;
}
.playlist-left{
  display: inline-block;
  width: 640px;
  height: 100%;
  padding: 47px 30px 40px 39px;
  border-right: 1px solid rgb(204,204,204);
  vertical-align:top;
}
.playlist{
  font-size: 0;
  -webkit-text-size-adjust:none;
  border-right: 1px solid rgb(204,204,204);
  text-align: left;
}
.playlist-head{
  vertical-align: top;
}
.playlist-cover{
  position: relative;
  display: inline-block;
  width: 200px;
  height: 200px;
  vertical-align:top;
}
.playlist-cover img{
  width: 100%;
  height: 100%;
}
.playlist-cover span{
  position: absolute;
  left: -4px;
  top:-4px;
  width: 208px;
  height: 208px;
  background: url(../assets/coverall.png) no-repeat scroll 0 -1285px;
}
.playlist-content{
  display: inline-block;
  width: 410px;
  margin-left: 30px;
  vertical-align:top;
}
.content-title{
  vertical-align: top;
  margin-bottom: 12px;
  margin-left: 64px;
}
.content-title i{
  display: inline-block;
  width: 54px;
  height: 24px;
  margin: 0 10px 0 -64px;
  vertical-align: top;
  background: url(../assets/icon.png) no-repeat scroll 0 -243px;
}
.content-title h2{
  display: inline-block;
  margin: 0;
  font-size: 20px;
  line-height: 24px;
  font-weight: normal;
  color: rgb(51,51,51);
  vertical-align: top;
}
.content-author{
  height: 35px;
  margin-bottom: 20px;
  vertical-align: middle;
  font-size: 12px;
  color: rgb(153,153,153);
}
.content-author img{
  vertical-align: middle;
  width: 35px;
  height: 35px;
}
.content-author sup{
  display: inline-block;
  width:12px; 
  height:13px;
  margin: -4px 15px 0 0;
  vertical-align: middle;
  background: url(../assets/icon.png) no-repeat scroll -65px -840px;
}
.author-link{
  color: #0c73c2;
  margin-left: 10px;
}
.author-link:hover,.show-more a:hover{
  text-decoration: underline;
}
.content-opreation a{
  float: left;
  height: 31px;
  line-height: 31px;
  overflow: hidden;
}
i{
   display: inline-block;
   height: 100%;
   font-style: normal;
   overflow: hidden;
}
.ply{
  float: left;
  width: 20px;
  height: 18px;
  margin: 6px 2px 2px 0;
  background: url(../assets/button2.png) no-repeat scroll 0 -1622px;
  overflow: hidden;
}
.ply:hover{
    background: url(../assets/button2.png) no-repeat scroll -28px -1622px;
}
.btn-play{
  padding-right: 5px;
  background: url(../assets/button2.png) no-repeat scroll 100% -428px;
}
.btn-play:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -510px;
}
.btn-play i{
  color: white;
  padding: 0 7px 0 8px;
  background: url(../assets/button2.png) no-repeat scroll 0 -387px;
}
.btn-play i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -469px;
}
.add-to{
  width: 31px;
  margin: 0 5px 0 -3px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1588px;
}
.add-to:hover{
  background: url(../assets/button2.png) no-repeat scroll -40px -1588px;
}
.btn-fav,.btn-share,.btn-dl,.btn-cm{
  padding-right: 5px;
  margin-right: 6px;
  background: url(../assets/button2.png) no-repeat scroll 100% -1020px;
}
.btn-fav:hover,.btn-share:hover,.btn-dl:hover,.btn-cm:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -1106px;
}
.btn-fav i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -977px;
}
.btn-fav i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1063px;
}
.btn-share i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1225px;
}
.btn-share i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1268px;
}
.btn-dl i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -2761px;
}
.btn-dl i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -2805px;
}
.btn-cm i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1465px;
}
.btn-cm i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1508px;
}
.content-tag{

  margin: 25px 0 5px 0;
}
.clear{
  clear: both;
}
.content-tag b{
  float: left;
  font-size: 12px;
  font-weight: normal;
  height: 22px;
  line-height: 22px;
}
.u-tag{
  float: left;
  height: 22px;
  line-height: 22px;
  padding-right: 10px;
  margin: 0 10px 3px 0;
  background: url(../assets/button2.png) no-repeat scroll 100% -27px;
}
.u-tag:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -1430px;
}
.u-tag i{
  padding: 0 3px 0 13px;
  background: url(../assets/button2.png) no-repeat scroll 0 0;
}
.u-tag i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1400px;
}
.playlist p{
  margin: 0;
  font-size: 12px;
}
.show-more{
  text-align: right;
}
.fr{
  color: #0c73c2; 
}
.u-ico{
  display: inline-block;
  width: 11px;
  height: 8px;
  background: url(../assets/icon.png) no-repeat scroll -65px -520px;
}
.u-icoActive{
  background: url(../assets/icon.png) no-repeat scroll -45px -520px;
}
.u-desc{
  font-weight: normal;
}
pre{
  font-size: 12px;
  font-family: inherit;
  white-space: pre-wrap;       
  white-space: -moz-pre-wrap;  
  white-space: -pre-wrap;      
  white-space: -o-pre-wrap;    
  word-wrap: break-word;  
}
.playlist-tracks{
  margin-top: 27px;
}
.u-title{
  height: 33px;
  border-bottom: 2px solid #c20c0c;
  font-size: 12px;
  color: rgb(51,51,51);
}
.u-title h3{
  float: left;
  height: 26px;
  margin: 0;
  font-size: 20px;
  font-weight: normal;
}
.u-title span{
  height: 16px;
  line-height: 16px;
  color: rgb(102,102,102);
  margin: 9px 0 0 20px;
}
.u-title strong{
  color: #c20c0c;
}
.u-lft{
  float: left;
}
.u-rgt{
  float: right;
}
div.u-rgt{
  margin-top: 8px;
  vertical-align: bottom;
}
div.u-rgt i{
  display: inline-block;
  width: 16px;
  height: 16px;
  background: url(../assets/icon.png) no-repeat scroll -34px -863px;
  vertical-align: bottom;
}
div.u-rgt a{
  color: #4996d1;
  text-decoration: underline;
}
.tracks-table{
  width: 100%;
  border: 1px solid rgb(217,217,217);
  border-collapse: collapse;
  table-layout: fixed;
  font-size: 12px;
}
.tracks-table thead{
  width: 100%;
}
.tracks-table th{
  height: 38px;
  padding: 0;
  margin: 0;
  background: url(../assets/table.png) repeat-x scroll 0 0;
}
.w1{
  width: 74px;
}
.w2{
  width: 111px;
}
.w3{
  width: 89px;
}
.w4{
  width: 127px;
}
.u-wrap{
  font-weight: normal;
  height: 18px;
  padding: 8px 10px;
  background: url(../assets/table.png) no-repeat scroll 0 -56px;
}
.w1 div{
  background: none;
}
.tracks-table td{
  padding:6px 10px;
}
.tracks-ply{
  float: right;
  width: 17px;
  height: 17px;
  background: url(../assets/table.png) no-repeat scroll 0 -103px;
}
.tracks-ply:hover{
  background: url(../assets/table.png) no-repeat scroll 0 -128px;
}
.tracks-cli{
  float: right;
  width: 17px;
  height: 17px;
  background: url(../assets/table.png) no-repeat scroll -20px -128px;
}
.w-ply{
  height: 18px;
  line-height: 18px;
}
.w-ply em{
  font-style: normal;
}
td a{
  color: rgb(51,51,51);
}
td a:hover{
  text-decoration: underline;
}
.track-fill{
  background: rgb(247,247,247);
}
</style>
