<template>
  <div class="main userhome">
    <div class="uh-head">
      <img src="http://p1.music.126.net/31NA7TgzLACMHO1Om1LQVw==/18636722092805728.jpg?param=180y180">
      <div class="uh-des">
        <div>
        <h2><span>一只林轩</span></h2>
        </div>
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
.uh-des{
  padding-left: 228px;
}
.uh-des h2{
  float: left;
  margin: 0;
  font-size: 22px;
  font-weight: normal;
  color: black;
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

