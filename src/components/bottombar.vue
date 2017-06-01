<template>
  <div class="bottombar" v-if="isshow">
    <ul class="inbl">
      <li class="inbl" v-for="(item,index) in subtitle">
        <a href="/#" track-by="$index" @mouseover="mouseInbtn(index)" @mouseout="mouseOutbtn(index)" @click="mouseClick(index)" :class="{ 'btnInact': item[1]||item[2]}">{{item[0]}}</a>
      </li>
    </ul>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'bottombar',
  props:['isshow'],
  data () {
    return {
      subtitle: [//按钮:[名称,是否mouseover,是否click,]
        ['推荐',false,true],['排行榜',false,false],['歌单',false,false],['主播电台',false,false],['歌手',false,false],['新碟上架',false,false]
      ],
    }
  },
  methods:{
    mouseInbtn:function(index){
      mouseBtnEv.setNewVal(this.subtitle[index], 1, true);
    },
    mouseOutbtn:function(index){
      mouseBtnEv.setNewVal(this.subtitle[index], 1, false);
    },
    mouseClick:function(index){//获取之前被激活的按钮->取消激活->激活当前按钮
      var current = this.subtitle.map(function(item){
        return item[2];
      }).indexOf(true);
      
      mouseBtnEv.setNewVal(this.subtitle[current], 2, false);
      mouseBtnEv.setNewVal(this.subtitle[index], 2, true);
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>  
.bottombar{
  height: 35px;
  background: url(../assets/topbar.png) repeat-x scroll 0px -230px;
}
ul{
  display: inline-block;
  margin: 0 0 0 -230px;
  padding: 0;
  height: 100%;
  list-style-type: none;
}
li{
  display: inline-block;
  margin: 0 17px;
  width: 52px;
  height: 100%;
  line-height: 35px;
}
a{
  text-decoration:none;
  font-size: 10px;
  color: rgb(221,220,220);
  display: inline-block;
  width: 100%;
}
.btnInact{
  background-image: url(../assets/redclick.png);
}
</style>
