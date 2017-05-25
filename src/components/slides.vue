<template>
  <div class="slides" :style="'background:'+imgData[colorchange][3]">
    <div class="flagwrap">
      <div style="width:100%;height:100%;">
        <a href="/#" style="display:inline-block;width:100%;height:100%;"> 
          <img id="flag" @webkitAnimationIteration="itertation(index)" class="fade" :class="{'slidepause':mouseInimg}" @mouseover="imgon" @mouseout="imgout" v-for="(item,index) in imgData" :src="item[0]" v-if="item[2]">
        </a>  
        <a class="tabflag tabl" id="tabl" @mouseover="tabflagon('tabl')" @mouseout="tabflagout('tabl')" @click="slide('tabl')" :class="{'tabl-active':tabflagbtn.tabl}" href="/#"></a>
        <a class="tabflag tabr" id="tabr" @mouseover="tabflagon('tabr')" @mouseout="tabflagout('tabr')" @click="slide('tabr')" :class="{'tabr-active':tabflagbtn.tabr}" href="/#"></a>
        <div id="tabb">
          <a href="/#" class="tabbbtn" v-for="(item,index) in imgData" @mouseover="tabbon(index)" @mouseout="tabbout(index)" @click="tabbClick(index)" :class="{'tabb-active':item[1],'tabb-cli':item[2]}"></a>
        </div>
      </div>
      <div id="downloadwarp">
        <a href="/#" :class="{'down-Active':mouseIndown}" @mouseover="downIn" @mouseout="downOut"></a>
        <p>PC 安卓 iPhone WP iPad Mac 六大客户端</p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'slides',
  data () {
    return {
      colorchange:0,
      mouseInimg:false,
      mouseIndown:false,
      tabflagbtn:{
        tabl:false,
        tabr:false,
      },
      imgData:[
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
    imgon:function(e){
      this.mouseInimg=true;
    },
    imgout:function(){
      this.mouseInimg=false;
    },
    tabflagon:function(key){
      this.tabflagbtn[key] = true;
    },
    tabflagout:function(key){
      this.tabflagbtn[key] = false;
    },
    tabbon:function(index){
      this.$set(this.imgData[index], 1, true);
      this.imgData[index].splice(1, 1, true);
    },
    tabbout:function(index){
      this.$set(this.imgData[index], 1, false);
      this.imgData[index].splice(1, 1, false);
    },
    tabbClick:function(index){
      for (var i=0;i<this.imgData.length;i++){
        if (this.imgData[i][2]===true){
          this.$set(this.imgData[i], 2, false);
          this.imgData[i].splice(2, 1, false);
        }
      }
      this.$set(this.imgData[index], 2, true);
      this.imgData[index].splice(2, 1, true);
      this.colorchange=index;
    },
    slide:function(side){
      var current =null;
      this.imgData.forEach(function(value,index){
        if(value[2]===true){
          return current=index;
        }
      });

      if (side=='tabr') {
        this.itertation(current);
      } else {
        this.$set(this.imgData[current], 2, false);
        this.imgData[current].splice(2, 1, false);

        var front = this.imgData.length-1;
        if (current!==0){
          front=current-1;
        }; 
        this.tabbClick(front);
        this.colorchange=front;
      };
    },
    itertation:function(index){
      this.$set(this.imgData[index], 2, false);
      this.imgData[index].splice(2, 1, false);
      var nextIndex=0;
      if (index!==this.imgData.length-1){
        nextIndex=index+1;
      }; 
      this.tabbClick(nextIndex);
      this.colorchange=nextIndex;
    },
    downIn:function(){
      this.mouseIndown=true;
    },
    downOut:function(){
      this.mouseIndown=false;
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
  animation: fade-in 6s infinite;
  -webkit-animation:fade-in 6s infinite;
}
@keyframes fade-in {
    0% {opacity: 0;}/*初始状态 透明度为0*/
    10% {opacity: 1;}/*结束状态 透明度为1*/
    90% {opacity: 1;}/*过渡状态 透明度为1*/
    100% {opacity: 0;}/*结束状态 透明度为1*/
}
@-webkit-keyframes fade-in {/*针对webkit内核*/
    0% {opacity: 0;}/*初始状态 透明度为0*/
    10% {opacity: 1;}/*结束状态 透明度为1*/
    90% {opacity: 1;}/*过渡状态 透明度为1*/
    100% {opacity: 0;}/*结束状态 透明度为1*/
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
