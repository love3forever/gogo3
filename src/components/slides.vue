<template>
  <div class="slides" :style="'background:'+imgData[colorchange][3]">
    <div class="flagwrap">
      <div style="width:100%;height:100%;">
        <a href="/#" style="display:inline-block;width:100%;height:100%;"> 
          <img id="flag" @webkitAnimationEnd="itertation(index)" class="fade" :class="{'slidepause':mouseInimg}" @mouseover="btnIn('mouseInimg')" @mouseout="btnOut('mouseInimg')" v-for="(item,index) in imgData" :src="item[0]" v-if="item[2]">
        </a>  
        <a class="tabflag tabl" id="tabl" @mouseover="tabflagon('tabl')" @mouseout="tabflagout('tabl')" @click="slide('tabl')" :class="{'tabl-active':tabflagbtn.tabl}" href="/#"></a>
        <a class="tabflag tabr" id="tabr" @mouseover="tabflagon('tabr')" @mouseout="tabflagout('tabr')" @click="slide('tabr')" :class="{'tabr-active':tabflagbtn.tabr}" href="/#"></a>
        <div id="tabb">
          <a href="/#" class="tabbbtn" v-for="(item,index) in imgData" @mouseover="tabbon(index)" @mouseout="tabbout(index)" @click="tabbClick(index)" :class="{'tabb-active':item[1],'tabb-cli':item[2]}"></a>
        </div>
      </div>
      <div id="downloadwarp">
        <a href="/#" :class="{'down-Active':mouseIndown}" @mouseover="btnIn('mouseIndown')" @mouseout="btnOut('mouseIndown')"></a>
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
      colorchange:0,//div(.slides)的背景色为imgData[colorchange][3]
      mouseInimg:false,//鼠标是否在图片范围内.在则暂停轮播.
      mouseIndown:false,//鼠标是否在‘下载客户端’按钮范围内
      tabflagbtn:{ tabl:false, tabr:false },//两侧切换按钮是否click
      imgData:[//轮播图片:[图片url,底部切换按钮是否mouseover,底部切换按钮是否click,对应背景色]
        ['./static/01.jpg',false,true,'rgb(0,0,0)'],
        ['./static/02.jpg',false,false,'rgb(255,214,228)'],
        ['./static/03.jpg',false,false,'rgb(226,198,194)'],
        ['./static/04.jpg',false,false,'rgb(252,248,237)'],
        ['./static/05.jpg',false,false,'rgb(235,246,248)'],
        ['./static/06.jpg',false,false,'rgb(186,19,3)'],
        ['./static/07.jpg',false,false,'rgb(0,0,0)'],
        ['./static/08.jpg',false,false,'rgb(244,245,247)'],
      ],
    }
  },
  methods:{
    btnIn: function(key){
      this[key] = true;
    },
    btnOut:function(key){
      this[key] = false;
    },
    tabflagon:function(key){
      mouseBtnEv.setNewVal(this.tabflagbtn, key, true);
    },
    tabflagout:function(key){
      mouseBtnEv.setNewVal(this.tabflagbtn, key, false);
    },
    tabbon:function(index){
      mouseBtnEv.setNewVal(this.imgData[index], 1, true);
    },
    tabbout:function(index){
      mouseBtnEv.setNewVal(this.imgData[index], 1, false);
    },
    //通用切换按钮click事件：获取之前被激活的图片->取消激活->激活当前图片->设置对应背景色
    tabbClick:function(index){
      var current = this.imgData.map(function(item){
        return item[2];
      }).indexOf(true);

      mouseBtnEv.setNewVal(this.imgData[current], 2, false);
      mouseBtnEv.setNewVal(this.imgData[index], 2, true);
      mouseBtnEv.setNewVal(this,'colorchange', index);
    },
    //两侧切换按钮click事件：获取之前被激活的图片->确定下一个被激活的图片->激活当前图片->设置对应背景色
    slide:function(side){
      var current = this.imgData.map(function(item){
        return item[2];
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
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>  
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
.down-Active{
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
.tabl-active{
  background: url(../assets/banner.png) no-repeat scroll 0 -430px;
}
.tabr-active{
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
.tabb-active{
  background: url(../assets/banner.png) no-repeat scroll -19px -343px;
}
.tabb-cli{
  background: url(../assets/banner.png) no-repeat scroll -19px -343px;
}
.fade{
  animation: fade-in 6s;
  -webkit-animation:fade-in 6s;
}
@keyframes fade-in {
    0% {opacity: 0.8;}/*初始状态 透明度为0*/
    5% {opacity: 1;}
    80% {opacity: 1;}
    100% {opacity: 0;}
}
@-webkit-keyframes fade-in {/*针对webkit内核*/
    0% {opacity: 0.8;}
    5% {opacity: 1;}
    80% {opacity: 1;}
    100% {opacity: 0;}
}
.slidepause{
  animation-play-state:paused;
  -webkit-animation-play-state:paused;
}
p{
  font-size: 13px;
  color: rgb(221,220,220);  
}
</style>
