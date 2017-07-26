<template>
  <div class="slides" :style="'background:'+imgData[colorchange][2]">
    <div class="flagwrap">
      <div style="width:100%;height:100%;">
        <a href="javascript:;" class="wrp-a"> 
          <img id="flag" @webkitAnimationIteration="itertation(index)" class="fade" v-for="(item,index) in imgData" :src="item[0]" v-if="item[1]">
        </a>  
        <a class="tabflag tabl" id="tabl" @click="slide('tabl')" href="/#"></a>
        <a class="tabflag tabr" id="tabr" @click="slide('tabr')" href="/#"></a>
        <div id="tabb">
          <a href="/#" class="tabbbtn" v-for="(item,index) in imgData" @click="tabbClick(index)" :class="{'tabb-cli':item[1]}"></a>
        </div>
      </div>
      <div id="downloadwarp">
        <a href="/#" ></a>
        <p>PC 安卓 iPhone WP iPad Mac 六大客户端</p>
      </div>
    </div>

  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'slides',
  data () {
    return {
      colorchange:0,//div(.slides)的背景色为imgData[colorchange][2]
      imgData:[//轮播图片:[图片url,底部切换按钮是否click,对应背景色]
        ['./static/01.jpg',true,'rgb(0,0,0)'],
        ['./static/02.jpg',false,'rgb(255,214,228)'],
        ['./static/03.jpg',false,'rgb(226,198,194)'],
        ['./static/04.jpg',false,'rgb(252,248,237)'],
        ['./static/05.jpg',false,'rgb(235,246,248)'],
        ['./static/06.jpg',false,'rgb(186,19,3)'],
        ['./static/07.jpg',false,'rgb(0,0,0)'],
        ['./static/08.jpg',false,'rgb(244,245,247)'],
      ],
    }
  },
  methods:{
    //通用切换按钮click事件：获取之前被激活的图片->取消激活->激活当前图片->设置对应背景色
    tabbClick:function(index){
      var current = this.imgData.map(function(item){
        return item[1];
      }).indexOf(true);

      mouseBtnEv.setNewVal(this.imgData[current], 1, false);
      mouseBtnEv.setNewVal(this.imgData[index], 1, true);
      mouseBtnEv.setNewVal(this,'colorchange', index);
    },
    //两侧切换按钮click事件：获取之前被激活的图片->确定下一个被激活的图片->激活当前图片->设置对应背景色
    slide:function(side){
      var current = this.imgData.map(function(item){
        return item[1];
      }).indexOf(true);

      if (side =='tabr') {//向右切换
        this.itertation(current);
      } else {//向左切换
        var front = this.imgData.length-1;
        if (current!==0){
          front = current-1;
        }; 
        this.tabbClick(front);
        mouseBtnEv.setNewVal(this,'colorchange', front);
      };
    },
    //一张图播放完成时的结束事件：确定下一个被激活的图片->激活当前图片->设置对应背景色
    itertation:function(index){
      var nextIndex = 0;
      if (index!==this.imgData.length-1){
        nextIndex = index+1;
      }; 

      this.tabbClick(nextIndex);
      mouseBtnEv.setNewVal(this,'colorchange', nextIndex);
    },
  },
}  
</script>

<style>  
.slides{
  height: 336px;
  background-color: rgb(255,214,228);
}
.flagwrap{
  position:relative;
  width: 982px;
  height: 100%;
  margin: 0 auto;
}
.wrp-a{
  display:inline-block;
  width:100%;
  height:100%;
}
#flag{
  position: absolute;
  left: 0;
}
#downloadwarp{
  position: absolute;
  top: 0;
  right: 0;
  width: 254px;
  height: 100%;
  background: url(../assets/download.png) no-repeat scroll 0 0;
}
#downloadwarp a{
  display: inline-block;
  margin: 212px 19px 0 19px;
  width: 215px;
  height: 56px;
}
#downloadwarp a:hover{
  background: url(../assets/download.png) no-repeat scroll 0 -340px;
}

.tabflag{
  position: absolute;
  top: 136.5px;
  width: 37px;
  height: 63px;
}
.tabl{
  left: -60px;
  background: url(../assets/banner.png) no-repeat scroll 0 -360px;
}
.tabr{
  right: -60px;
  background: url(../assets/banner.png) no-repeat scroll 0 -508px;
}
a.tabl:hover{
  background: url(../assets/banner.png) no-repeat scroll 0 -430px;
}
a.tabr:hover{
  background: url(../assets/banner.png) no-repeat scroll 0 -578px;
}
#tabb{
  position: absolute;
  left: 0;
  bottom: 5px;
  width: 730px;
  height: 20px;
}
.tabbbtn{
  display: inline-block;
  width: 20px;
  height: 20px;
  background: url(../assets/banner.png) no-repeat scroll 0px -343px;
}
a.tabbbtn:hover{
  background: url(../assets/banner.png) no-repeat scroll -19px -343px;
}
.tabb-cli{
  background: url(../assets/banner.png) no-repeat scroll -19px -343px;
}
.fade{
  animation: fade-in 6s infinite;
  -webkit-animation:fade-in 6s infinite;
}
@keyframes fade-in {
    0% {opacity:0;}/*初始状态 透明度为0*/
    5% {opacity: 1;}
    80% {opacity: 1;}
    100% {opacity: 0;}
}
@-webkit-keyframes fade-in {/*针对webkit内核*/
    0% {opacity: 0;}
    5% {opacity: 1;}
    80% {opacity: 1;}
    100% {opacity: 0;}
}
#flag:hover, .paused{
  animation-play-state:paused;
  -webkit-animation-play-state:paused;
}
.slides p{
  font-size: 13px;
  color: rgb(221,220,220);  
}
</style>
