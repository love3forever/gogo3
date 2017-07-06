<template>
  <div class="playlist main">
    <div  v-show="hasResult">
      <div class="playlist-left">
        <div class="playlist-head">
          <div class="playlist-cover">
            <img id="a-pic":src="songs.coverImgUrl">
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
                {{songs.name}}
                <a class="plyMv" href="javascript:;">
                  <i></i>
                </a>    
              </h2> 
            </div>
            <div class="content-author">
              <p class="a-author">
                <span>歌手:<a href="/#" class="author-link">{{songs.creator.nickname}}</a></span>
              </p>
              <p class="a-author">
                <span>所属专辑:<a href="/#" class="author-link">{{songs.creator.nickname}}</a></span>
              </p>
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
            <pre v-show="!songs.isShowMore"><b class="u-desc">介绍：</b>{{songs.descDot}}<b class="u-desc" v-show="songs.descMore">...</b></pre>
            <pre v-show="songs.isShowMore"><b class="u-desc">介绍：</b>{{songs.descMore}}</pre>
            <div id="a-showmore" class="show-more" v-if="songs.descMore">
              <a href="javascript:;" class="fr" @click="tabShowMore">{{songs.isShowMore?"收起":"展开"}}</a>
              <i class="u-ico" :class="{'u-icoActive':songs.isShowMore}"></i>
            </div>
          </div>
        </div>
        <div class="playlist-tracks">
          <div class="u-title">
            <h3>歌曲列表</h3>
            <span class="u-lft">{{`${songs.trackCount}首歌`}}</span>
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
    <div class="loading" v-show="!hasResult">
      <i></i>
      加载中...
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

      this.$http.get(`http://123.206.211.77:33333/api/v1/playlist/comments/551088906/page/${pageIndex}`)
        .then(response => {
          this.cmts = response.data.comments;
          this.cmtNumber = response.data.total;
        })
        .catch(response => {
          console.log(response)
      });
      
      this.cmtClearTrue(cmt,current,len,false);
      this.cmtSetTrue(cmt, len, current, index,this.cmtLength);
    } 
  },
  beforeCreate:function(){
    //请求歌单数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/playlist/detail/551088906`)
      .then(response => {
        this.hasResult = response.data.result;//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
    //请求评论数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/playlist/comments/551088906/page/1`)
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
      return this.cmtIndex.others[0].num>2;
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
    }
  }
}
</script>

<style>
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

