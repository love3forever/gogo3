<template>
  <div class="playlist main">
    <div  v-show="hasResult">
      <div class="playlist-left">
        <div class="playlist-head">
          <div class="playlist-cover">
            <img id="a-pic":src="desInfo.songPic">
            <span id="a-song"></span>
            <div id="a-rgtply" class="u-rgt">
              <i></i>
              <a href="">生成外链播放器</a>
            </div>
          </div>
          <div class="playlist-content">
            <div class="content-title">
              <i id="songIcon"></i>
              <h2>
                {{desInfo.songName}}
                <a class="plyMv" href="javascript:;" v-if="desInfo.mvid">
                  <i></i>
                </a>    
              </h2> 
            </div>
            <div class="content-author">
              <p class="a-author">
                <span>歌手:
                  <router-link :to="'/artist/'+desInfo.singer.id" class="author-link">
                    {{desInfo.singer.name}}
                  </router-link>
                </span>
              </p>
              <p class="a-author">
                <span>所属专辑:
                  <router-link :to="'/album/'+desInfo.track.id" class="author-link">
                    {{desInfo.track.name}}
                  </router-link>
                </span>
              </p>
            </div>
            <div class="content-opreation">
              <a href="#" class="btn-play">
                <i><em class="ply"></em>播放</i>
              </a>
              <a href="#" class="add-to"></a>
              <a href="#" class="btn-fav">
                <i>收藏</i>
              </a>
              <a href="#" class="btn-share">
                <i>分享</i>
              </a>
              <a href="#" class="btn-dl">
                <i>下载</i>
              </a>
              <a href="#" class="btn-cm">
                <i>评论</i>
              </a>
              <div class="clear"></div>
            </div>
            <pre class="lyricshow"><b class="u-desc"></b>{{lyc.part1}}</pre>
            <pre class="lyricshowMore" v-show="lyc.isFlod"><b class="u-desc"></b>{{lyc.part2}}</pre>
            <div id="a-showmore" class="show-more" v-if="lyc.part2">
              <a href="javascript:;" class="fr" @click="tabShowMore">{{lyc.isFlod?"收起":"展开"}}</a>
              <i class="u-ico" :class="{'u-icoActive':lyc.isFlod}"></i>
            </div>
            <div class="upload-lrc">
              <a href="javascript:;" v-if="wholeLyc&&wholeLyc.sgc">上传歌词</a>
              <a href="javascript:;" v-if="wholeLyc&&wholeLyc.sfy">翻译歌词</a>
              <a href="javascript:;">报错</a> 
              <p class="transLyc">
                <span v-if="wholeLyc&&wholeLyc.lyricUser">
                  贡献歌词：
                  <a>{{wholeLyc.lyricUser.nickname}}</a>
                </span>
                <span v-if="wholeLyc&&wholeLyc.transUser">
                  贡献翻译：
                  <a>{{wholeLyc.transUser.nickname}}</a>
                </span> 
                <span v-if="wholeLyc&&wholeLyc.qfy">
                  暂时没有翻译，
                  <a id="qfy">求翻译</a>
                </span>
              </p>             
            </div>
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

export default {
  name: 'song',
  components:{
    playlistRight,comment
  },
  data () {
    return {
      hasResult:false,//是否返回歌单数据
      desInfo:{
        songName:null,
        songPic:null,
        mvid:0,
        singer: {name:null,id:null},
        track: {name:null,id:null},
      },
      wholeLyc:null,
      lyc:{
        part1:null,
        part2:null,
        isFlod:false,
      },
      listUrl:`http://123.206.211.77:33333/api/v1/song/detail/${this.$route.params.id}`,
      lycUrl:`http://123.206.211.77:33333/api/v1/song/lyrics/${this.$route.params.id}`,
      cmtUrl:`http://123.206.211.77:33333/api/v1/song/comments/${this.$route.params.id}/page/`,
    }
  },
  methods:{
    //歌单介绍-展开/收起按钮点击事件
    tabShowMore:function(){
      this.lyc.isFlod = !this.lyc.isFlod;
    },
  },
  created:function(){
    //请求歌单数据
    this.$http.get(this.listUrl)
      .then(response => {
        this.hasResult = response.data.songs[0];//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
    //请求歌词数据
    this.$http.get(this.lycUrl)
      .then(response => {
        this.wholeLyc = response.data;//初始化歌词数据
      })
      .catch(response => {
        console.log(response)
    });
  },
  watch:{
    //歌单数据返回后，提取、格式化需要的数据
    hasResult:function(result){
      //解构result.tracks
      var album = result.album,
          artists = result.artists[0];
      this.desInfo = {
        songName:result.name,
        songPic:album.picUrl,
        mvid:result.mvid,
        singer: {name:artists.name,id:artists.id},
        track: {name:album.name,id:album.id},
      };
    },
    wholeLyc:function(wholeLyc){
      var tlyric = null,
          lyc = null,
          finaLyc = [];

      if (wholeLyc.tlyric&&wholeLyc.tlyric.lyric){
        tlyric = wholeLyc.tlyric.lyric.split('\n');
        lyc = wholeLyc.lrc.lyric.split('\n');
        
        for (let i = 0;i<lyc.length;i++){
          finaLyc.push(lyc[i],tlyric[i])
        };       
      } else if (wholeLyc.lrc&&wholeLyc.lrc.lyric){
        finaLyc = wholeLyc.lrc.lyric.split('\n');
      }

      this.lyc.part1 =  finaLyc.slice(0,14).join('\n');
      this.lyc.part2 =  finaLyc.slice(14).join('\n');
    }
  }
}
</script>

<style>
.lyricshow{
  height: 327px;
  margin: 13px 0 0 0;
  line-height: 23px;
}
.lyricshowMore{
  margin: 0;
  line-height: 23px;
}
#qfy{
  color: rgb(153,153,153);
}
.transLyc{
  padding-top: 10px;
  vertical-align: middle;
}
.transLyc span{
  margin-left: 10px;
}
p.transLyc a{
  color: #0c73c2;
}
.upload-lrc{
  margin-top: 48px;
  text-align: right;
}
.upload-lrc a{
  margin-left: 5px;
  text-decoration: underline;
  color: rgb(153,153,153);
}
p.a-author{
  margin:10px 0;
}
#songIcon{
  background-position: 0 -463px;
}
.plyMv {
  display: inline-block;
}
.plyMv i{
  display: block;
  width: 21px;
  height: 18px;
  margin: 0;
  background:  url(../assets/icon.png) no-repeat scroll 0 -18px;
}
#a-song{
 background:  url(../assets/coverall.png) no-repeat scroll -140px -580px;
}
#a-pic{
  width: 130px;
  height: 130px;
  margin: 34px;
}
#a-rgtply{
  float: none;
  margin-top: 16px;
  text-align: center;
}
#a-showmore{
  text-align: left;
}
</style>

