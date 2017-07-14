<template>
  <div class="fansfav-mode">
    <ul class="uh-fans">
      <li>
        <a href="" class="fans-pic"><img src="http://p1.music.126.net/bvAv9YNFMemNAiZlbGDOfA==/3401888987155718.jpg?param=60y60"></a>
        <div class="fans-info">
          <a href="" class="fans-name">瞧那谁</a><i class="female"></i>
          <p class="fans-conect">
            <a href="">动态<span>0</span></a><span class="line">|</span>
            <a href="">关注<span>0</span></a><span class="line">|</span>
            <a href="">粉丝<span>0</span></a>
          </p>
        </div>
        <div class="fans-fav">
          <a href="javascript:;" class="follow"><i>关&nbsp&nbsp注&nbsp</i></a>
        </div>
      </li>
      <li></li>
    </ul>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'fansfavmode',

}
</script>

<style>
.fans-conect a span{
  color:  #0c73c2;
}
.line{
  margin: 0 8px;
  color: rgb(153,153,153);
}
.fans-conect{
  margin: 0;
  margin-top: 25px;
  font-size: 12px;
  text-align: left;
}
.fans-info i{
  width: 14px;
  height: 15px;
  margin: 2px 0 0 4px;
  background: url(../assets/icon.png) no-repeat scroll -70px -20px;
}
.fans-name{
  float: left;
  color: #0c73c2;
  font-size: 14px;
}
.fans-name{
  float: left;
  color: #0c73c2;
  font-size: 14px;
}
.fans-info a:hover{
  text-decoration: underline;
}
.fans-fav{
  float: left;
}
.fans-info{
  float: left;
  width: 250px;
  height: 53px;
  margin-left: 10px;

}
.uh-fans{
  list-style-type: none;
  padding: 0;
  margin: 0;
  border-left: 1px solid rgb(213,213,213);
  overflow: hidden;
}
.uh-fans li{
  float: left;
  width: 408px;
  height: 80px;
  padding: 20px;
  padding-bottom: 0;
  border-right: 1px solid rgb(213,213,213);
}
.fans-pic{
  float: left;
  width: 60px;
  height: 60px;
}
.uh-fans li img{
  width: 100%;
  height: 100%;
}
</style>

