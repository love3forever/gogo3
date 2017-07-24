<template>
  <div class="playlist-cmt">
    <div class="u-title">
      <h3>评论</h3>
      <span class="u-lft" v-if="cmtNumber">{{`共${cmtNumber}条评论`}}</span>
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
            <router-link :to="'/user/'+cmt.beReplied[0].user.userId">
              {{cmt.beReplied[0].user.nickname}}
            </router-link>
            ：{{cmt.beReplied[0].content}}
          </div>
          <div class="cmt-desc">
            <span>{{cmt.time}}</span>
            <a href="/#" class="rpl">回复</a>
            <a href="/#" class="rpl-ct">
              <i class="nofav"></i>
              {{`(${cmt.likedCount})`}}
            </a>
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
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'generalComment',
  props:['url'],
  data () {
    return {
      maxlength:140,//允许输入的最多字数
      cmtContent:"",//评论内容
      cmtNumber:null,//评论总数
      cmtIndex:{//评论页码
        first: [{ num: 1, isclick: true}],//第一页
        others: [],//中间页
        last: [{ num: null, isclick: false}],//最后一页
      },
      cmts:null
    }
  },
  methods:{
    //点击@按钮，评论内容中自动加入@字符
    addAT:function(){
      if (this.cmtContent.length < this.maxlength){
        this.cmtContent += "@";
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

      this.$http.get(`${this.url}${pageIndex}`)
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
    //评论数据返回后，提取、格式化需要的数据
    cmts:function(result){
      if (result!==null){
        for (let cmt of result){
          cmt.time = mouseBtnEv.setCommentTime(cmt.time)
        }

        this.cmts = result;
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
  },
  created:function(){
    //请求评论数据
    this.$http.get(`${this.url}1`)
      .then(response => {
        this.cmts = response.data.comments;//初始化全部评论数据
        this.cmtNumber = response.data.total;//初始化评论总数
      })
      .catch(response => {
        console.log(response)
    });
  }
}
</script>

<style>
.disa-nxt{
  pointer-events: none;
  color: rgb(202,202,202);
  background-position: -75px -620px; 
}
.disa-frt{
  pointer-events: none;
  color: rgb(202,202,202);
  background-position: 0 -620px; 
}
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
  border: 1px solid rgb(204,204,204);
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

  border-radius: 2px;
  line-height: 24px;
}
.frt{
  width: 54px;
  padding-left:12px;
  border: 1px solid rgb(204,204,204);
  background:  url(../assets/button.png) no-repeat scroll 0 -560px;
}
.frt:hover{
   background-position: 0 -590px;
}
.nxt{
  width: 54px;
  padding-right:12px;
  border: 1px solid rgb(204,204,204);
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
  line-height: 20px;
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
  line-height: 20px;
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
</style>

