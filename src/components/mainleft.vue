<template>
  <div class="mainleft">
   <div class="left-content">
      <div class="left-top">
        <div class="lefthead">
          <a href="/#" class="hot-title">热门推荐</a>
          <ul>
            <li v-for="hot in hotrecommend" :class="{'li-sp':hot[1]}"><a href="/#" class="hot-subtitle">{{hot[0]}}</a></li>
          </ul>
          <span><a href="/#" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
        <ul class="hot-item">
          <li v-for="(item,index) in hotitem">
            <div class="item-wrap">
              <img :src="item[0]">
              <a href="/#" class="msk"></a>
              <div class="item-bottom">
                <span class="ico"></span>
                <span class="hot-num">{{item[1]}}</span>
                <a href="/#" class="hotplay" :class="{'hotplay-Active':item[4]}" @mouseover="btnIn(index)" @mouseout="btnOut(index)"></a>
              </div>
            </div>
            <p><a href="/#" class="hot-descrp"><sub v-if="item[3]"></sub>{{item[2]}}</a></p>
          </li>
        </ul>
      </div>
      <div class="left-ad">
        <a target="_blank" href="http://www.kaola.com/activity/detail/15809.shtml?tag=39c18428bdd72630e076b136f47c6b31&__da_4cdeb8a1_57188748ea833c82#zid_9957431215">
          <img src="../../static/ad.jpg">
        </a>
      </div>
      <div class="left-center">
        <div class="lefthead">
          <a href="/#" class="hot-title">新碟上架</a>
          <span><a href="/#" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
        <div class="disk">
          <div class="disk-wrap">
            <a :class="['disk-tab','disk-left',{'diskleft-Active':disktab.left}]" @click="diskSlide('left')" @mouseover="disktabIn('left')" @mouseout="disktabOut('left')"></a>
            <div class="disk-scroll">
              <ul class="disk-group" v-for="(group,num) in diskgroup" :style="'left:'+group+'px;'">
                <li v-for="(top,index) in disk[num%2]">
                  <div>
                    <img :src="top[0]">
                    <a href="/#" :title="top[1]" class="disk-mask" @mouseover="diskIn(num%2,index)" @mouseout="diskOut(num%2,index)"></a>
                    <a href="/#" title="播放" class="disk-play" v-if="top[3]"></a>
                  </div>
                  <p><a href="/#" class="disk-des">{{top[1]}}</a></p>
                  <p><a href="/#" class="disk-singer">{{top[2]}}</a></p>
                </li>
              </ul>
            </div>
            <a :class="['disk-tab','disk-right',{'diskright-Active':disktab.right}]" @click="diskSlide('right')" @mouseover="disktabIn('right')" @mouseout="disktabOut('right')"></a>
          </div>
        </div>
      </div>
      <div class="left-bottom">
        <div class="lefthead">
          <a href="/#" class="hot-title">榜单</a>
          <span><a href="/#" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
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
      hotrecommend:[["华语",false],["流行",true],["摇滚",true],["民谣",true],["电子",true]],
      hotitem:[
          ["./static/hot01.jpg","220万","2017年五月最热新歌TOP50",false,false],
          ["./static/hot02.jpg","25万","『福音之旅』聆听清风絮语，静沐斜阳暖心",false,false],
          ["./static/hot03.jpg","48万","『电音故事』从生命的起源说起",true,false],
          ["./static/hot04.jpg","18230","『哲学公开课』切实的幸福",false,false],
          ["./static/hot05.jpg","220万","『锐韧Trap』风骚霸道，黑暗的迷人性格",false,false],
          ["./static/hot06.jpg","220万","健身小白应该注意些啥？",true,false],
          ["./static/hot07.jpg","220万","Deep House深窈之道",false,false],
          ["./static/hot08.jpg","220万","刘瑜：色",true,false],
      ],
      diskgroup:[-645,0,645,645*2],//645=ul.width
      disktab:{left:false,right:false},
      disk:[
        [
          ["./static/10top01.jpg","PRODUCE 101 - 35 Boys 5 Concepts","PRODUCE 101",false],
          ["./static/10top02.jpg","我想和你唱 第二季 第6期","群星",false],
          ["./static/10top03.jpg","Wonder Woman: Original Motion Picture Soundtrack","Rupert Gregson-Williams",false],
          ["./static/10top04.jpg","2017跨界歌王 第八期","群星",false],
          ["./static/10top05.jpg","LONELY","Sistar",false],
        ],
        [
          ["./static/5top01.jpg","放&披风","陈奕迅",false],
          ["./static/5top02.jpg","欢乐颂2 电视原声带","群星",false],
          ["./static/5top03.jpg","군주 - 가면의 주인 OST","V.A.",false],
          ["./static/5top04.jpg","hopeless fountain kingdom (Deluxe)","Halsey",false],
          ["./static/5top05.jpg","There For You","Martin Garrix / Troye Sivan",false],
        ]
      ]
    }
  },
  methods:{
    btnIn: function(index){
      mouseBtnEv.setNewVal(this.hotitem[index], 4, true);
    },
    btnOut:function(index){
      mouseBtnEv.setNewVal(this.hotitem[index], 4, false);
    },
    diskIn:function(num,index){
      mouseBtnEv.setNewVal(this.disk[num][index], 3, true);
    },
    diskOut:function(num,index){
      mouseBtnEv.setNewVal(this.disk[num][index], 3, false);
    },
    disktabIn:function(type){
      mouseBtnEv.setNewVal(this.disktab, type, true);
    },
    disktabOut:function(type){
      mouseBtnEv.setNewVal(this.disktab, type, false);
    },
    diskSlide:function(type){//
      var current = this.diskgroup.indexOf(0);//当前显示的ul索引      
      var count = 0;//setInterval执行次数
      var dataParm = {};//setInteval参数
      var ulWidth = null;//ul.width
      //初始化ulWidth
      if (current !== 0){
        ulWidth = Math.abs(this.diskgroup[current-1]);
      } else {
        ulWidth = Math.abs(this.diskgroup[current+1]);
      };
      //根据切换方向的不同，初始化dataParm
      if (type == 'left'){
        dataParm.next = current-1;
        dataParm.nextVal = ulWidth; 
      } else if(type == "right"){
        dataParm.next = current-3;
        dataParm.nextVal = -ulWidth; 
      };

      var chageLeft = setInterval(()=>{
        count++;//计次
        var addVal = count*dataParm.nextVal/50;//切换时元素left增加的值,=当前次数*ul.width/总次数
        //每20ms改变一次current、next ul的left值
        mouseBtnEv.setNewVal(this.diskgroup, dataParm.next, addVal-dataParm.nextVal);
        mouseBtnEv.setNewVal(this.diskgroup, current, addVal);
        //执行50次后(共1s)停止，并改变备用ul的left值
        if (count == 50){//总计1000ms=50次*20ms/次
          mouseBtnEv.setNewVal(this.diskgroup, current-2, -dataParm.nextVal);
          clearInterval(chageLeft);
        };
      },20);
    },
  },
}  
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>  
.mainleft{
  width: 730px;
  height: 100%;
  margin-right: 250px;
  color: rgb(51,51,51);
}
.left-content{
  width: 690px;
  padding: 20px 20px 40px 20px;
}
.lefthead{
  height: 33px;
  padding: 0 10px 0 34px;
  border-bottom: 2px solid rgb(193,13,12);
  background: url(../assets/index.png) no-repeat scroll -225px -156px;
  background-clip: border-box;
  overflow: hidden;
}
.hot-title{
  text-decoration: none;
  font-size: 20px;
  line-height: 28px;
  float: left;
  color: inherit;
}
.lefthead ul{
  display: inline-block;
  padding: 0;
  margin: 7px 0 0 10px;
  float: left;
}
.lefthead li{
  display: inline-block;
  padding: 0 10px;
  margin: 0;
  font-size: 12px;
}
.li-sp{
  border-left: 1px solid rgb(204,204,204);
}
a{
  text-decoration: none;
  color: rgb(102,102,102);
}
a.hot-subtitle:hover,a.hot-descrp:hover{
  text-decoration: underline;
}
.lefthead span{
  display: inline-block;
  font-size: 12px;
  margin-top: 9px;
  float: right;
}
.lefthead sub{
  display: inline-block;
  width: 12px;
  height: 12px;
  margin-left: 4px;
  background: url(../assets/index.png) no-repeat scroll 0 -240px;
}
.left-ad{
  margin-bottom: 35px;
}
.item-wrap{
  position: relative;
  height: 140px;
}
.msk{
  position: absolute;
  top: 0;
  left: 0;
  width: 140px;
  height: 140px;
  background: url(../assets/coverall.png) no-repeat scroll 0 0;
}
.item-bottom{
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 27px;
  background: url(../assets/coverall.png) no-repeat scroll 0 -537px;
  text-align: left;
}
.ico{
  float: left;
  width: 14px;
  height: 11px;
  margin: 9px 5px 9px 10px;
  background: url(../assets/iconall.png) no-repeat scroll 0 -24px;
}
.hot-num{
  float: left;
  margin: 6px 0;
}
.hotplay{
  float: right;
  width: 16px;
  height: 16px;
  margin: 6px;
  background: url(../assets/iconall.png) no-repeat scroll 0 0;
}
.hotplay-Active{
  background: url(../assets/iconall.png) no-repeat scroll 0 -60px;
}
.hot-item{
  display: inline-block;
  margin: 20px 0 0 -42px;
  padding: 0;
  font-size: 12px;
  color: rgb(220,220,220);
}
.hot-item li{
  display: inline-block;
  height: 204px;
  padding: 0 0 30px 42px;
  margin: 0;
  vertical-align: top;
}
.hot-item p{
  width: 140px;
  font-size: 14px;
  text-align: left;
}
.hot-item sub{
  display: inline-block;
  width: 35px;
  height: 15px;
  margin-right: 3px;
  background: url(../assets/icon.png) no-repeat scroll -31px -658px;
}
.disk{
  height: 184px;
  margin: 20px 0 37px 0;
  border: 1px solid rgb(211,211,211);
}
.disk-wrap{
  position: relative;
  height: 182px;
  padding-left: 16px;
  border: 1px solid white;
  background: rgb(245,245,245);
}
.disk-tab{
  text-decoration: none;
  display: inline-block;
  width: 17px;
  height: 17px;
  position: absolute;
  top:71px;
}
.disk-left{
  left: 4px;
  background: url(../assets/index.png) no-repeat scroll -260px -75px; 
}
.disk-right{
  right: 4px;
  background: url(../assets/index.png) no-repeat scroll -300px -75px; 
}
.disk-scroll{
  width: 645px;
  height: 180px;
  position: relative;
  overflow: hidden;
}
.disk-group{
  text-decoration: none;
  width: 100%;
  height: 150px;
  margin: 28px 0 0 0;
  padding: 0;
  position: absolute;
}
.disk-group li{
  display: inline-block;
  width: 118px;
  height: 100%;
  margin-left: 11px;
  vertical-align: top;
}
.disk-group div{
  position: relative;
  width: 100px;
  height: 100px;
  margin-bottom: 7px;
}
.disk-mask{
  position: absolute;
  top:0;
  left: 0;
  width: 118px;
  height: 100%;
  background-clip: border-box;
  background: url(../assets/coverall.png) no-repeat scroll 0 -570px;
}
.disk-play{
  position: absolute;
  right: 5px;
  bottom: 5px;
  width: 22px;
  height: 22px;
  background: url(../assets/iconall.png) no-repeat scroll 0 -85px;
}
.disk-group p{
  width: 90%;
  height: 18px;
  line-height: 18px;
  font-size: 12px;
  margin: 0;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.disk-des{
  color: black;
}
a.disk-des:hover{
  text-decoration: underline;
}
.diskleft-Active{
  cursor:pointer;
  background: url(../assets/index.png) no-repeat scroll -280px -75px; 
} 
.diskright-Active{
  cursor:pointer;
  background: url(../assets/index.png) no-repeat scroll -320px -75px; 
}
</style>
