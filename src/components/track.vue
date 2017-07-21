<template>
  <div class="playlist main">
    <div  v-if="hasResult">
      <div class="playlist-left">
        <div class="playlist-head">
          <div id="a-cover" class="playlist-cover">
            <img id="a-pic":src="hasResult.picUrl">
            <span id="a-song"></span>
          </div>
          <div class="playlist-content">
            <div class="content-title">
              <i id="trackIcon"></i>
              <h2>
                {{hasResult.name}}
                <a class="plyMv" href="javascript:;">
                  <i></i>
                </a>    
              </h2> 
            </div>
            <div class="content-author">
              <p class="a-author">
                <span>歌手:
                  <router-link :to="'/artist/'+hasResult.singer_id" class="author-link">
                    {{hasResult.singer}}
                  </router-link>
                </span>
              </p>
              <p class="a-author">
                <span >发行时间:     
                  {{hasResult.publish_time}}
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
          </div>
        </div>
        <div class="track-info">
          <h3>专辑介绍：</h3>
<!--           <p>无论是谁都有一个成长的过程，同时也要感谢那些想尽办法要将你置于死地的人，如果不是他们步步紧逼，也不会有今天的我们。</p> -->
            <pre v-show="!des.isShowMore">{{des.descDot}}<b class="u-desc" v-show="des.descMore">...</b></pre>
            <pre v-show="des.isShowMore">{{des.descMore}}</pre>
            <div class="show-more" v-if="des.descMore">
              <a href="javascript:;" class="fr" @click="tabShowMore">{{des.isShowMore?"收起":"展开"}}</a>
              <i class="u-ico" :class="{'u-icoActive':des.isShowMore}"></i>
            </div>
        </div>
        <div class="playlist-tracks">
          <div class="u-title">
            <h3>包含歌曲列表</h3>
            <span class="u-lft">{{`${hasResult.songs.length}首歌`}}</span>
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
                  <th class="w5"><div class="u-wrap">时长</div></th>
                  <th class="w6"><div class="u-wrap">歌手</div></th>
                </tr>
              </thead>
              <tbody @click="plySong">
                <tr v-for="(track,index) in songs" :class="{'track-fill':index%2==0}">
                  <td>
                    <div class="w-ply">
                      <em>{{index+1}}</em>
                      <span :class="[track.click?'tracks-cli':'tracks-ply']" :data-tag="index"></span>
                    </div>
                  </td>
                  <td class="p-over">
                    <router-link :to="'/song/'+track.id" :title="track.name">
                      {{track.name}}
                    </router-link>
                  </td>
                  <td>{{track.duration}}</td>
                  <td class="p-over">
                    <router-link :to="'/artist/'+track.artists[0].id" :title="track.artists[0].name">
                      {{track.artists[0].name}}
                    </router-link>
                  </td>
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
  name: 'track',
  components:{
    playlistRight
  },
  data () {
    return {
      hasResult:false,//是否返回歌单数据
      songs:null,
      des:{
        isShowMore:false,
        descDot:null,
        descMore:null,
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
      this.des.isShowMore = !this.des.isShowMore;
    },
    //歌单播放按钮点击事件
    plyClick:function(index){
      var clickList = this.songs.map(function(item){
        return item.click;
      });

      var current = clickList.indexOf(true);
      if (current>-1){
        mouseBtnEv.setNewVal(this.songs[current], 'click', false);
      }
      mouseBtnEv.setNewVal(this.songs[index], 'click', true);
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

      this.$http.get(`http://123.206.211.77:33333/api/v1/album/${this.$route.params.id}/comments/${pageIndex}`)
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
    this.$http.get(`http://123.206.211.77:33333/api/v1/album/${this.$route.params.id}/detail`)
      .then(response => {
        this.hasResult = response.data;//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
    //请求评论数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/album/${this.$route.params.id}/comments/1`)
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
      var list = new Array();
      for ( let item of result.songs ){ 
        let { duration, mvid, name, id, artists} = item;

        duration = mouseBtnEv.changeTime(duration);
        list.push({ duration, mvid, name, id, artists, click:false});
      }
      this.songs = list;
      this.des = {
        isShowMore:false,
        descDot:result.desc.substr(0,99),
        descMore:result.desc.length>99?result.desc:null,
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

<style scoped>
.track-info pre{
  padding:0 24px;
  line-height: 24px;
}
.w5{
  width: 91px;
}
.w6{
  width: 127px;
}
#trackIcon{
  background-position: 0 -186px;
}
.track-info{
  margin-top:20px;
  font-size: 12px;
}
.track-info h3{
  margin:0;
  font-size: 12px;
}
.track-info p{
  color: rgb(102,102,102);
  text-indent: 2em;
  line-height: 24px;
  margin-top: 4px;
}
#rel-time{
  color: inherit;
}
#a-cover{
  width: 177px;
  height: 177px;
  border: 0;
  margin-right: 20px;
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
#a-song{
  width: 209px;
  height: 177px;
  left: 0;
  top: 0;
  background:  url(../assets/coverall.png) no-repeat scroll 0 -986px;
}
#a-pic{
  width: 177px;
  height: 177px;
  margin: 0;
}
</style>

