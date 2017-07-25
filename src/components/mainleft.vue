<template>
  <div class="mainleft">
   <div class="left-content">
      <div class="left-top">
        <div class="lefthead">
          <a href="javascript:;" class="hot-title">热门推荐</a>
          <ul>
            <li v-for="hot in hotrecommend" :class="{'li-sp':hot[1]}"><a href="/#" class="hot-subtitle">{{hot[0]}}</a></li>
          </ul>
          <span><a href="/#" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
        <ul class="hot-item">
          <li v-for="item in hotitem">
            <div class="item-wrap">
              <img :src="item.img">
              <router-link :to="'/playlist/'+item.playlistID" class="msk"></router-link>
              <div class="item-bottom">
                <span class="ico"></span>
                <span class="hot-num">{{item.playTimes}}</span>
                <a href="/#" class="hotplay"></a>
              </div>
            </div>
            <p><router-link :to="'/playlist/'+item.playlistID" class="hot-descrp">{{item.playlistTitle}}</router-link></p>
          </li>
        </ul>
      </div>
      <div class="left-ad">
        <a href="#" class="ad"></a>
        <a target="_blank" href="http://www.kaola.com/activity/detail/15809.shtml?tag=39c18428bdd72630e076b136f47c6b31&__da_4cdeb8a1_57188748ea833c82#zid_9957431215">
          <img src="../../static/ad.jpg">
        </a>
      </div>
      <div class="left-center">
        <div class="lefthead">
          <a href="javascript:;" class="hot-title">新碟上架</a>
          <span><a href="/#" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
        <div class="disk">
          <div class="disk-wrap">
            <a class="disk-tab disk-left" @click="diskSlide('left')"></a>
            <div class="disk-scroll">
              <ul class="disk-group" v-for="(group,num) in diskgroup" :style="'left:'+group+'px;'">
                <li v-for="(top,index) in disk[num%2]">
                  <div class="disk-mask0">
                    <img :src="top[0]">
                    <router-link :to="'/album/'+top[6]" :title="top[1]" class="disk-mask"></router-link>
                    <a href="/#" title="播放" class="disk-play"></a>
                  </div>
                  <p><router-link :to="'/album/'+top[6]" class="disk-des">{{top[1]}}</router-link></p>
                  <p><router-link :to="'/artist/'+top[4]" class="disk-singer">{{top[2]}}</router-link></p>
                </li>
              </ul>
            </div>
            <a class="disk-tab disk-right" @click="diskSlide('right')"></a>
          </div>
        </div>
      </div>
      <div class="left-bottom">
        <div class="lefthead">
          <a href="javascript:;" class="hot-title">榜单</a>
          <span><a href="javascript:;" class="hot-subtitle">更多</a><sub></sub></span>
        </div>
        <div class="song-list">
          <dl class="bill" v-for="(bill,num) in billborad">
            <dt class="bill-top">
              <div class="billtop-des">
                <img :src="bill.img">
                <a :title="bill.title" href="/#"></a>
              </div>
              <div class="billtop-title">
                <a :title="bill.title" href="/#" class="bill-title"><h3>{{bill.title}}</h3></a>
                <a title="播放" href="/#" class="bill-play"></a>
                <a title="收藏" href="/#" class="bill-collect"></a>
              </div>
            </dt>
            <dd>
              <ol>
                <li v-for="(song,index) in bill.songs">
                  <span class="song-num" :class="{'song-numtop':index<3}">{{index+1}}</span>
                  <router-link :to="'/song/'+song.songHref" class="song-item" :title="song.songName">
                    {{song.songName}}
                  </router-link>
                </li>
              </ol>
              <div><a href="/#" class="view-allsong">查看全部></a></div>
            </dd>
          </dl>
        </div>
      </div>
   </div>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'slides',
  props:['leftData'],
  data () {
    return {
      hotrecommend: [["华语",false],["流行",true],["摇滚",true],["民谣",true],["电子",true]],
      ulWidth: 645,//ul.width
      diskgroup: null,//645=ul.width
    }
  },
  created:function(){
    this.diskgroup = [-this.ulWidth,0,this.ulWidth,this.ulWidth*2];
  },
  methods:{
    diskSlide:function(type){//
      var current = this.diskgroup.indexOf(0),//当前显示的ul索引      
          count = 0,//setInterval执行次数
          dataParm = {};//setInteval参数

      if (type == 'left'){
        dataParm.next = current-1;
        dataParm.nextVal = this.ulWidth; 
      } else if(type == "right"){
        dataParm.next = current-3;
        dataParm.nextVal = -this.ulWidth; 
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
  computed:{
    hotitem:function(){
      return this.leftData?this.leftData.recommendList:[];
    },
    billborad:function(){
      return this.leftData?this.leftData.blk:[];
    },
    disk:function(){
      if (!this.leftData){//数据未返回
        return [];
      } else {//数据已返回
        var newAlbum = this.leftData.newAlbum;
        var outputDisk = new Array(new Array(5),new Array(5));

        for (var i=0;i<newAlbum.length;i++){
          if (i<5){       
            outputDisk[0][i] = new Array(6);
            outputDisk[0][i] = [newAlbum[i].img,newAlbum[i].title,newAlbum[i].artistName,false,newAlbum[i].artistHref,newAlbum[i].artistHref,newAlbum[i].href];
          } else {
            outputDisk[1][i-5] = new Array(6);
            outputDisk[1][i-5]=[newAlbum[i].img,newAlbum[i].title,newAlbum[i].artistName,false,newAlbum[i].artistHref,newAlbum[i].artistHref,newAlbum[i].href];
          };
        };
        return outputDisk;
      };
    }
  }
}  
</script>

<style>  
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
  position: relative;
  width: 689px;
  height: 75px;
  margin-bottom: 35px;
}
.lef-ad img{
  width: 100%;
  height: 100%;
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
.hot-descrp sub{
  position: relative;
  top:-1px;
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
.hotplay:hover{
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
.disk-mask0:hover .disk-play{
  display: block;
}
.disk-play{
  display: none;
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
a.disk-des:hover,a.hot-artist:hover,a.taba:hover{
  text-decoration: underline;
}
a.disk-left:hover{
  cursor:pointer;
  background: url(../assets/index.png) no-repeat scroll -280px -75px; 
} 
a.disk-right:hover{
  cursor:pointer;
  background: url(../assets/index.png) no-repeat scroll -320px -75px; 
}
.song-list{
  width: 100%;
  height: 472px;
  margin-top:20px;
  background: url(../assets/index_bill.png) no-repeat scroll 0 0;
}
.bill{
  float: left;
  width: 230px;
  height: 100%;
  margin: 0;
}
.bill-top{
  display: block;
  height: 100px;
  position: relative;
  padding: 20px 0 0 20px;
  text-align: left;
}
.billtop-des{
  position: relative;
  display: inline-block;
  width: 80px;
  height: 80px;
}
.billtop-des img,.billtop-des a{
  width: 100%;
  height: 100%;
  position: absolute;
  top:0;
  left:0;
}
.billtop-des a{
  background: url(../assets/coverall.png) no-repeat scroll -145px -57px; 
}
.billtop-title{
  position: absolute;
  top:20px;
  left: 100px;
  width: 114px;
  height: 51px;
  margin: 6px 0 23px 10px;
}
.billtop-title h3{
  margin: 0 0 10px 0;
  color: rgb(51,51,51);
  font-size: 14px;
}
a.bill-title:hover,a.song-item:hover,a.view-allsong:hover{
  text-decoration: underline;
}
.bill-play{
  display: inline-block;
  width: 22px;
  height: 22px;
  margin-right: 5px;
  background: url(../assets/index.png) no-repeat scroll -267px -205px; 
}
.bill-play:hover{
  background: url(../assets/index.png) no-repeat scroll -267px -235px; 
}
.bill-collect{
  display: inline-block;
  width: 22px;
  height: 22px;
  margin-right: 5px;
  background: url(../assets/index.png) no-repeat scroll -300px -205px; 
}
.bill-collect:hover{
  background: url(../assets/index.png) no-repeat scroll -300px -235px; 
}
dd{
  margin: 0;
}
dd ol{
  margin: 0 0 0 50px;
  padding: 0;
  width: auto;
  list-style:none;
}
dd li{
  height: 32px;
  font-size: 12px;
  text-align: left;

}
dd div{
  height: 32px;
  margin-right:32px;
  line-height: 32px; 
  text-align: right;
}
.song-num{
  display: inline-block;
  width: 35px;
  height: 32px;
  margin-left:-35px;
  line-height: 32px;
  font-size: 16px;
  position: relative;
  float: left;
  text-align: center;
  color: rgb(51,51,51);

}
.song-numtop{
  color: rgb(193,13,12);
}
.song-item{
  float: left;
  width: 170px;
  height: 32px;
  line-height: 32px;
  color: rgb(51,51,51);
}
.view-allsong{
  text-align: right;
  font-size: 12px;
  color: inherit;
}
</style>
