<template>
  <div class="playlist main" v-show="hasResult">
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
            <a href="/#"><img :src="songs.creator.avatarUrl"></a>
            <span><a href="/#" class="author-link">{{songs.creator.nickname}}</a></span>
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
            <a href="#" class="fr" @click="tabShowMore">{{songs.isShowMore?"收起":"展开"}}</a>
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
                <td class="p-over"><a href="#" :title="track.songName">{{track.songName}}</a></td>
                <td>{{track.duration}}</td>
                <td class="p-over"><a href="#" :title="track.artName">{{track.artName}}</a></td>
                <td class="p-over"><a href="#" :title="track.albName">{{track.albName}}</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="playlist-cmt">
        <div class="u-title">
          <h3>评论</h3>
          <span class="u-lft">{{`共${songs.trackCount}条评论`}}</span>
        </div>
        <div class="iptarea">
          <img src="http://s4.music.126.net/style/web2/img/default/default_avatar.jpg?param=50y50">
          <div class="area">
            <!-- onchange、onkeydown、onkeyup为了兼容IE9及以下:onchange="this.value=this.value.substring(0, 140)" onkeydown="this.value=this.value.substring(0, 140)" onkeyup="this.value=this.value.substring(0, 140)"-->
            <textarea placeholder="评论" v-model="cmtContent" :maxlength="maxlength"></textarea>
            <div class="btn-wrap">
              <i class="emj"></i>
              <i class="at" @click="addAT"></i>
              <a href="javascript:;">评论</a>
              <span>{{cmtCount}}</span>
            </div>
            <div class="corr">
              <em>◆</em>
              <span>◆</span>
            </div>
          </div>
        </div>
        <div class="u-cmt" v-show="cmts">
          <h3>最新评论</h3>
          <div class="cmt1" v-for="cmt in cmts">
            <div class="cmt-head">
              <a href="/#"><img :src="cmt.user.avatarUrl"></a>
            </div>
            <div class="cmt-wrap">
              <div class="cmt-rel">
                <a href="">{{cmt.user.nickname}}</a>：{{cmt.content}}
              </div>
              <div class="isRpl" v-if="cmt.beReplied.length">
                <span>
                  <i class="bd">◆</i>
                  <i class="db">◆</i>
                </span>
                <a href="/#">{{cmt.beReplied[0].user.nickname}}</a>：{{cmt.beReplied[0].content}}
              </div>
              <div class="cmt-desc">
                <span>15分钟前</span>
                <a href="/#" class="rpl">回复</a>
                <a href="/#" class="rpl-ct"><i class="nofav"></i>{{`(${cmt.likedCount})`}}</a>
              </div>
            </div>
          </div>
          <div class="cmt-tab" v-if="cmtLength>1"> 
            <a href="#" class="frt">上一页</a>
            <a href="#" class="page">1</a>
            <span v-show="cmtFrontMore">...</span>
            <a href="#" :class="[val.isclick?'page-cli':'page']" v-for="val in cmtIndex">{{val.num}}</a>
            <span v-show="cmtNextMore">...</span>
            <a href="#" class="page">{{cmtLength}}</a>
            <a href="#" class="nxt">下一页</a>
         </div>
        </div>
      </div>
    </div>
    <div class="playlist-right">
      <div class="ad-wrap">
        <a href="#" class="ad"></a>
        <a href="#"><img src="https://haitaoad.nosdn.127.net/ad.bid.material_f73d40bef46d4b0098283ea63ca4b579?imageView&thumbnail=200x220&quality=100"></a>
      </div>
      <div class="rela-cmd u-head">
        <h3>相关推荐</h3>
        <ul>
          <li>
            <div class="rela-msk">
              <a href="#">
                <img src="http://p3.music.126.net/1L_rIf-sofhXEG1R2JQ5bQ==/1365593506719668.jpg?param=50y50">
              </a>
            </div>
            <div class="rela-info">
              <p class="rela-title p-over">
                <a href="#" title="传统世界音乐【器乐】">传统世界音乐【器乐】</a>
              </p>
              <p class="p-over">
                <span>by</span>
                <a href="#" title="紫de甘蓝">紫de甘蓝</a>
              </p>
            </div>
          </li>
          <li>
            <div class="rela-msk">
              <a href="#">
                <img src="http://p4.music.126.net/rnHLMLESV1c-PcFbDgAngg==/18775260557760255.jpg?param=50y50">
              </a>
            </div>
            <div class="rela-info">
              <p class="rela-title p-over">
                <a href="#" title="一个人的乌德琴">一个人的乌德琴</a>
              </p>
              <p class="p-over">
                <span>by</span>
                <a href="#" title="珠疯">珠疯</a>
              </p>
            </div>
          </li>
        </ul>
      </div>
      <div class="multi-dowm u-head">
        <h3>网易云音乐多端下载</h3>
        <ul class="dowm-methods">
          <li><a class="m1" href="https://itunes.apple.com/app/id590338362" target="_blank"></a></li>
          <li><a class="m2" href="http://music.163.com/api/pc/download/latest"  target="_blank"></a></li>
          <li><a class="m3" href="http://music.163.com/api/android/download/latest2" target="_blank"></a></li>
        </ul>
        <p>同步歌单，随时畅听320k好音乐</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'playlist',
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
      hasCmt:null,//是否返回评论数据
      maxlength:140,//允许输入的最多字数
      cmtContent:"",//评论内容
      cmtLength: Math.ceil(140/3),
      cmtIndex:[
        { num: 2, isclick: true},
        { num: 3, isclick: false},
        { num: 4, isclick: false},
        { num: 5, isclick: false},
        { num: 6, isclick: false},
        { num: 7, isclick: false},
        { num: 8, isclick: false},
      ],
      cmts:null,
    }
  },
  methods:{
    initData:function(result){
      //解构result.tracks
      var originTracks = result.tracks,
          list = new Array();
      for ( let item of originTracks ){ 
        let { duration, name:songName, album:{name:albName}, album:{artists:[{name:artName}]}} = item;
        duration = mouseBtnEv.changeTime(duration);
        list.push({ duration, songName, albName, artName, click:false});
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
      return true;
    },
    addAT:function(){
      if (this.cmtContent.length < this.maxlength){
        this.cmtContent += "@";
      }  
    },
    tabShowMore:function(){
      this.songs.isShowMore = !this.songs.isShowMore;
    },
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
    plySong:function(ev){
      var ev = ev||window.event;
      var target = ev.target||ev.srcElement;

      if (target.nodeName.toLowerCase() == "span"){
        var index = parseInt(target.dataset.tag);
        this.plyClick(index);             
      }
    }
  },
  beforeCreate:function(){
    this.$http.get('http://123.206.211.77:33333/api/v1/playlist/detail/static')
      .then(response => {
        console.log('歌单数据get');
        var result = response.data.result;
        this.hasResult = this.initData(result);
      })
      .catch(response => {
        console.log(response)
    });

    this.$http.get('http://123.206.211.77:33333/api/v1/playlist/comments/static')
      .then(response => {
        console.log('评论数据get');
        this.cmts = response.data.comments;
      })
      .catch(response => {
        console.log(response)
    });

  },
  computed:{
    cmtCount:function(){
      var content = this.cmtContent;
      return typeof content==="undefined"?this.maxlength:this.maxlength-content.length;
    },
    cmtFrontMore:function(){
      return this.cmtIndex[0]>2;
    },
    cmtNextMore:function(){
      return this.cmtLength>10&&this.cmtIndex[this.cmtIndex.length-1]<this.cmtLength-4;
    },
  },
}
</script>

<style>
.page-cli{
  margin: 0 1px 0 2px;
  padding: 0 8px;
  cursor: default;
  pointer-events: none;
  border: 1px solid rgb(162, 22, 27);
  color: white;
  background: url(../assets/button.png) no-repeat scroll 0 -650px;
}
.page{
  margin: 0 1px 0 2px;
  padding: 0 8px;
}
.page:hover{
  border: 1px solid rgb(51,51,51);
}
.cmt-tab{
  color: rgb(51,51,51);
}
.cmt-tab a{
  display: inline-block;
  height: 22px;
  border: 1px solid rgb(204,204,204);
  border-radius: 2px;
  line-height: 24px;
}
.frt{
  width: 54px;
  padding-left:12px;
  background:  url(../assets/button.png) no-repeat scroll 0 -560px;
}
.frt:hover{
   background-position: 0 -590px;
}
.nxt{
  width: 54px;
  padding-right:12px;
  background:  url(../assets/button.png) no-repeat scroll -75px -560px;
}
.nxt:hover{
  background-position: -75px -590px;
}
.cmt-tab{
  margin: 20px 0;
  text-align: center;
}
.cmt1{
  overflow: hidden;
}
.isRpl{
  position: relative;
  margin-top:10px;
  padding: 8px 19px;
  border: 1px solid rgb(222,222,222);
  background-color: rgb(244,244,244);
}
.isRpl span{
  position: absolute;
  top:-7px;
  left: 20px;
  font-size: 12px;
  line-height: 14px;
}
.bd{
  display: block;
  color: rgb(222,222,222);
}
.db{
  display: block;
  color:  rgb(244,244,244);
  margin-top:-13px;
}
.nofav{
  width: 15px;
  height: 14px;
  margin-right: 3px;
  background:  url(../assets/icon2.png) no-repeat scroll -150px 0;
}
.rpl{
  padding-left: 8px;
  border-left: 1px solid rgb(205,204,204);
}
.rpl-ct{
  margin-right: 8px;
}
.cmt-desc{
  margin-top: 15px;
}
.cmt-desc a{
  float: right;
  vertical-align: middle;
}
.cmt-rel{
  width: 580px;
  color: rgb(51,51,51);
}
.cmt-rel a,.isRpl a{
  color: #0c73c2;
}
.cmt-rel a:hover,.cmt-desc a:hover,.isRpl a:hover{
  text-decoration: underline;
}
.cmt-wrap{
  float: left;
  margin-left: 60px;
}
.cmt-head{
  float: left;
  margin-right: -50px;
}
.cmt-head img{
  display: block;
  width: 50px;
  height: 50px;
}
.cmt1{

  padding: 15px 0;
  border-top: 1px dotted rgb(204,204,204);
}
.u-cmt h3{
  font-size: 12px;
  height: 20px;
  margin: 0 0 -1px 0;
  border-bottom: 1px solid rgb(207,207,207);
}
.emj{
  width: 18px;
  height: 18px;
  margin: 3px 10px 0 0;
  cursor: pointer;
  background:  url(../assets/icon.png) no-repeat scroll -40px -490px;
}
.at{
  width: 18px;
  height: 18px;
  margin-top: 3px;
  cursor: pointer;
  background:  url(../assets/icon.png) no-repeat scroll -60px -490px;
}
.btn-wrap{
  padding-top: 10px;
  vertical-align: middle;
  overflow: hidden;
}
.btn-wrap span{
  float: right;
  height: 25px;
  margin-right: 10px;
  line-height: 25px;
  color: rgb(153,153,153);
}
.btn-wrap a{
  float: right;
  width: 46px;
  height: 25px;
  line-height: 25px;
  text-align: center;
  color: white;
  background:  url(../assets/button.png) no-repeat scroll -84px -64px;
}
.corr{
  position: absolute;
  left: -7px;
  top: 12px;
  width: 13px;
  height: 14px;
  font-size: 15px;
  font-family: SimSun;

}
.corr em{
  display: block;
  font-style: normal;
  color: rgb(205,205,205);
  height: 10px;
}
.corr span{
  color: white;
  display: block;
  margin: -10px 0 0 1px;
  height: 10px;
}
.iptarea{
  margin: 20px 0;
  vertical-align: top;
  overflow: hidden;
}
.iptarea img{
  float: left;
  width: 50px;
  height: 50px;
  margin-right: -50px;
  vertical-align: top;
}
.area{
  float: left;
  position: relative;
  margin-left: 62px;
  vertical-align: top;
}
.area textarea{
  width: 564px;
  height: 50px;
  padding: 5px 6px 6px 6px;
  border-color: rgb(205,205,205);
  border-radius: 2px;
  font-size: 12px;
  font-family:Arial, Helvetica, sans-serif;
  resize: none;
}
.playlist-cmt{
  margin-top: 40px;
  font-size: 12px;
}
.rela-title a{
  font-size: 14px;
  color: black;
}  
.rela-info{
  margin: 0 0 0 60px;
}
.rela-info a:hover{
  text-decoration: underline;
}
.rela-info p{
  width: 140px;
  margin: 0;
  font-size: 12px;
  line-height: 24px;
}
.rela-msk{
  margin: 0 -60px 0 0;
}
.rela-msk img{
  display: block;
  width: 50px;
  height: 50px;
}
.rela-cmd ul{
  margin: 0 0 25px 0;
  padding: 0;
  list-style-type: none;
}
.rela-cmd li{
  width: 200px;
  height: 50px;
  margin: 0 0 15px 0;
  overflow: hidden;
}
.rela-cmd div{
  float: left;
}
.m1{
  width: 42px;
}
.m1:hover{
  background: url(../assets/sprite.png) no-repeat scroll 0 -472px;
}
.m2{
  width: 116px;
}
.m2:hover{
  background: url(../assets/sprite.png) no-repeat scroll -42px -472px;
}
.m3{
  width: 42px;
}
.m3:hover{
  background: url(../assets/sprite.png) no-repeat scroll -158px -472px;
}
.dowm-methods{
  height: 65px;
  margin:0 0 10px 0;
  padding: 0;
  background: url(../assets/sprite.png) no-repeat scroll 0 -392px;
  list-style-type: none;
  overflow:hidden;
}
.dowm-methods a{
  display: block;
  height: 48px;
}
.dowm-methods li{
  float: left;
}
.u-head{
  font-size: 12px;
  margin: 20px 0;
}
.u-head h3{
  height: 23px;
  margin: 0 0 20px 0;
  border-bottom: 1px solid rgb(204,204,204);
  color: rgb(51,51,51);
  font-size: inherit;
}
.u-head p{
  color: rgb(153,153,153);
}
.ad-wrap{
  position: relative;
  width: 200px;
  height: 220px;
  margin-bottom: 40px;
}
.ad-wrap img{
  width: 100%;
  height: 100%;
}
.ad{
  position: absolute;
  right: 0;
  bottom: 0;
  width: 24px;
  height: 18px;
  background: url(../assets/short.png) no-repeat scroll 0 0;
}
.playlist{
  font-size: 0;
  -webkit-text-size-adjust:none;
  border-right: 1px solid rgb(204,204,204);
  text-align: left;
}
.playlist-left{
  display: inline-block;
  width: 640px;
  height: 100%;
  padding: 47px 30px 40px 39px;
  border-right: 1px solid rgb(204,204,204);
  vertical-align:top;

}
.playlist-right{
  display: inline-block;
  width: 200px;
  height: 100%;
  padding: 20px 40px 40px 30px;
  vertical-align:top;
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
}
.content-title i{
  display: inline-block;
  width: 54px;
  height: 24px;
  margin-right: 10px;
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
