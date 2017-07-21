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
                <i>{{cmtNumber}}</i>
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
        <div class="playlist-cmt">
          <div class="u-title">
            <h3>评论</h3>
            <span class="u-lft">{{`共${cmtNumber}条评论`}}</span>
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
            <h3 >最新评论</h3>
            <div class="cmt1" v-for="cmt in cmts">
              <div class="cmt-head">
                <router-link :to="'/user/'+cmt.user.userId"><img :src="cmt.user.avatarUrl"></router-link>
              </div>
              <div class="cmt-wrap">
                <div class="cmt-rel">
                  <router-link :to="'/user/'+cmt.user.userId">{{cmt.user.nickname}}</router-link>：{{cmt.content}}
                </div>
                <div class="isRpl" v-if="cmt.beReplied.length">
                  <span>
                    <i class="bd">◆</i>
                    <i class="db">◆</i>
                  </span>
                  <router-link :to="'/user/'+cmt.beReplied[0].user.userId">{{cmt.beReplied[0].user.nickname}}</router-link>：{{cmt.beReplied[0].content}}
                </div>
                <div class="cmt-desc">
                  <span>{{cmt.time}}</span>
                  <a href="/#" class="rpl">回复</a>
                  <a href="/#" class="rpl-ct"><i class="nofav"></i>{{`(${cmt.likedCount})`}}</a>
                </div>
              </div>
            </div>
          </div>
          <div class="loading" v-show="!cmts">
            <i></i>
            加载中...
          </div> 
          <div class="cmt-tab" v-if="cmtLength>1"> 
              <a href="javascript:;" class="frt" :class="{'disa-frt':cmtIndex.first[0].isclick}" @click="cmtClick(-1)">上一页</a>
              <a href="javascript:;" :class="[cmtIndex.first[0].isclick?'page-cli':'page']" @click="cmtClick(null,0)">{{cmtIndex.first[0].num}}</a>
              <span v-show="cmtFrontMore">...</span>
              <a href="javascript:;" :class="[val.isclick?'page-cli':'page']" v-for="(val,index) in cmtIndex.others" @click="cmtClick(null,index+1)">{{val.num}}</a>
              <span v-show="cmtNextMore">...</span>
              <a href="javascript:;" :class="[cmtIndex.last[0].isclick?'page-cli':'page']" @click="cmtClick(null,cmtIndex.others.length+1)">{{cmtIndex.last[0].num}}</a>
              <a href="javascript:;" class="nxt" :class="{'disa-nxt':cmtIndex.last[0].isclick}" @click="cmtClick(1)">下一页</a>
           </div>
        </div>
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
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'comment',
  components:{
    playlistRight
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
      hasCmt:null,//是否返回评论数据
      maxlength:140,//允许输入的最多字数
      cmtContent:"",//评论内容
      cmtNumber:null,//评论总数
      cmtIndex:{//评论页码
        first: [{ num: 1, isclick: true}],//第一页
        others: [],//中间页
        last: [{ num: null, isclick: false}],//最后一页
      },
      cmts:null,
    }
  },
  methods:{
    //点击@按钮，评论内容中自动加入@字符
    addAT:function(){
      if (this.cmtContent.length < this.maxlength){
        this.cmtContent += "@";
      }  
    },
    //歌单介绍-展开/收起按钮点击事件
    tabShowMore:function(){
      this.lyc.isFlod = !this.lyc.isFlod;
    },
    //评论翻页按钮，改变不同类型按钮的isclick值
    cmtClearTrue:function(cmt,index,len,val){
      if (index===0){//第一页
        cmt.first[0].isclick = val;
      } else if (index===len-1){//最后一页
        cmt.last[0].isclick = val;
      } else {//其它
        cmt.others[index-1].isclick = val;
      };
    },
    //确定评论翻页后，列表显示的页数（cmtIndex.others）
    cmtNum:function(cmt,type,diff){
      if(type){
        cmt.others.forEach(function(val,ind){
          val.num = ind+diff;
        });
      } else {
        cmt.others.forEach(function(val){
          val.num += diff;
        });
      };
    },
    //确定按下切换评论的按钮之前，已经被按下的按钮索引
    cmtCalcuCurrent:function(cmt){
      var clickList = new Array();

      for (let page in cmt){
        clickList.push(...cmt[page].map(function(val){
            return val.isclick
          })
        );
      }

      var len = clickList.length;
      var current = clickList.findIndex(function(val){
        return val===true;
      });
      return { cmt,len,current }
    },
    //按钮列表页数改变后，确定应被按下的按钮
    cmtSetTrue:function(cmt, len, current, index,cmtLength){
      var diff = null;
      //再次按中同一个按钮不会触发click事件，因此此处无需加current!==index
      if (cmtLength<11){ //总页数少于11页时，无需省略页数  
        this.cmtClearTrue(cmt,index,len,true);
      } else {
        if (index===0){
          diff=2;//2=len-cmt.others.length,指的是第一页+最后一页
          this.cmtNum(cmt,true,diff);
          this.cmtClearTrue(cmt,index,len,true);
        } else if(index===len-1){
          diff = cmtLength-len+2;//40
          this.cmtNum(cmt,true,diff);
          this.cmtClearTrue(cmt,index,len,true);
        } else {
          var targetNum = cmt.others[index-1].num;
          switch (true)
          {
            case targetNum<6:
              diff=2;
              this.cmtNum(cmt,true,diff);
              this.cmtClearTrue(cmt,targetNum-1,len,true);
              break;
            case targetNum>cmtLength-5:
              diff = cmtLength-len+2;
              this.cmtNum(cmt,true,diff);
              this.cmtClearTrue(cmt,targetNum-diff+1,len,true);
              break;
            default:
              diff = targetNum-cmt.others[3].num;
              this.cmtNum(cmt,false,diff);
              cmt.others[3].isclick = true;
              break;
          }
        };
      };
    },
    //切换评论按钮点击事件
    cmtClick:function(add,index){
      this.cmts = null;//新一页评论数据返回之前隐藏当前评论
      var { cmt, len, current} = this.cmtCalcuCurrent(this.cmtIndex);
      if (add!==null){//上一页、下一页
        var index = current+add;
      }

      var pageIndex = null;
      if (index===0){
        pageIndex = cmt.first[0].num;
      } else if (index===len-1) {
        pageIndex = cmt.last[0].num;
      } else {
        pageIndex = cmt.others[index-1].num;
      };

      this.$http.get(`http://123.206.211.77:33333/api/v1/song/comments/${this.$route.params.id}/page/${pageIndex}`)
        .then(response => {
          this.cmts = response.data.comments;
          this.cmtNumber = response.data.total;
        })
        .catch(response => {
          console.log(response)
      });
      
      this.cmtClearTrue(cmt,current,len,false);
      this.cmtSetTrue(cmt, len, current, index,this.cmtLength);
    },
  },
  beforeCreate:function(){
    //请求歌单数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/song/detail/${this.$route.params.id}`)
      .then(response => {
        this.hasResult = response.data.songs[0];//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
    //请求歌词数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/song/lyrics/${this.$route.params.id}`)
      .then(response => {
        this.wholeLyc = response.data;//初始化歌词数据
      })
      .catch(response => {
        console.log(response)
    });
    //请求评论数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/song/comments/${this.$route.params.id}/page/1`)
      .then(response => {
        this.cmts = response.data.comments;//初始化全部评论数据
        this.cmtNumber = response.data.total;//初始化评论总数
      })
      .catch(response => {
        console.log(response)
    });
  },
  computed:{
    //当前还允许继续输入的字数
    cmtCount:function(){
      var content = this.cmtContent;
      return typeof content==="undefined"?this.maxlength:this.maxlength-content.length;
    },
    //评论页数（每页20条评论）
    cmtLength:function(){
      return this.cmtNumber===null?null:Math.ceil(this.cmtNumber/20);
    },
    //第一页之后是否显示...
    cmtFrontMore:function(){
      return this.cmtLength>10&&this.cmtIndex.others[0].num>2;
    },
    //最后一页之前是否显示...
    cmtNextMore:function(){
      var numb = this.cmtIndex.others;
      return this.cmtLength>10&&numb[numb.length-1].num<this.cmtLength-1;
    },
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
    //评论数据返回后，提取、格式化需要的数据
    cmts:function(result){
      if (result!==null){
        for (let cmt of result){
          cmt.time = mouseBtnEv.setCommentTime(cmt.time)
        }
      }
    },
    //确定当前评论页数
    cmtLength:function(newVal,oldVal){
      if (oldVal===null){//页面打开时初始化
        var othersLen = newVal<11?newVal-2:7; 
        for (let i =0;i<othersLen;i++){
            this.cmtIndex.others.push({num:2+i,isclick: false});
          }
      } 
      this.cmtIndex.last[0].num = newVal;
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

