<template>
  <div class="playlist-right">
    <div class="ad-wrap">
      <a href="#" class="ad"></a>
      <a href="#"><img src="https://haitaoad.nosdn.127.net/ad.bid.material_f73d40bef46d4b0098283ea63ca4b579?imageView&thumbnail=200x220&quality=100"></a>
    </div>
    <div class="rela-cmd u-head">
      <h3>相关推荐</h3>
      <ul>
        <li>
          <div class="rela-msk">
            <a href="#">
              <img src="http://p3.music.126.net/1L_rIf-sofhXEG1R2JQ5bQ==/1365593506719668.jpg?param=50y50">
            </a>
          </div>
          <div class="rela-info">
            <p class="rela-title p-over">
              <a href="#" title="传统世界音乐【器乐】">传统世界音乐【器乐】</a>
            </p>
            <p class="p-over">
              <span>by</span>
              <a href="#" title="紫de甘蓝">紫de甘蓝</a>
            </p>
          </div>
        </li>
        <li>
          <div class="rela-msk">
            <a href="#">
              <img src="http://p4.music.126.net/rnHLMLESV1c-PcFbDgAngg==/18775260557760255.jpg?param=50y50">
            </a>
          </div>
          <div class="rela-info">
            <p class="rela-title p-over">
              <a href="#" title="一个人的乌德琴">一个人的乌德琴</a>
            </p>
            <p class="p-over">
              <span>by</span>
              <a href="#" title="珠疯">珠疯</a>
            </p>
          </div>
        </li>
      </ul>
    </div>
    <div class="multi-dowm u-head">
      <h3>网易云音乐多端下载</h3>
      <ul class="dowm-methods">
        <li><a class="m1" href="https://itunes.apple.com/app/id590338362" target="_blank"></a></li>
        <li><a class="m2" href="http://music.163.com/api/pc/download/latest"  target="_blank"></a></li>
        <li><a class="m3" href="http://music.163.com/api/android/download/latest2" target="_blank"></a></li>
      </ul>
      <p>同步歌单，随时畅听320k好音乐</p>
    </div>
  </div> 
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'generalRight',
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
.rela-title a{
  font-size: 14px;
  color: black;
}  
.rela-info{
  margin: 0 0 0 60px;
}
.rela-info a:hover{
  text-decoration: underline;
}
.rela-info p{
  width: 140px;
  margin: 0;
  font-size: 12px;
  line-height: 24px;
}
.rela-msk{
  margin: 0 -60px 0 0;
}
.rela-msk img{
  display: block;
  width: 50px;
  height: 50px;
}
.rela-cmd ul{
  margin: 0 0 25px 0;
  padding: 0;
  list-style-type: none;
}
.rela-cmd li{
  width: 200px;
  height: 50px;
  margin: 0 0 15px 0;
  overflow: hidden;
}
.rela-cmd div{
  float: left;
}
.m1{
  width: 42px;
}
.m1:hover{
  background: url(../assets/sprite.png) no-repeat scroll 0 -472px;
}
.m2{
  width: 116px;
}
.m2:hover{
  background: url(../assets/sprite.png) no-repeat scroll -42px -472px;
}
.m3{
  width: 42px;
}
.m3:hover{
  background: url(../assets/sprite.png) no-repeat scroll -158px -472px;
}
.dowm-methods{
  height: 65px;
  margin:0 0 10px 0;
  padding: 0;
  background: url(../assets/sprite.png) no-repeat scroll 0 -392px;
  list-style-type: none;
  overflow:hidden;
}
.dowm-methods a{
  display: block;
  height: 48px;
}
.dowm-methods li{
  float: left;
}
.u-head{
  font-size: 12px;
  margin: 20px 0;
}
.u-head h3{
  height: 23px;
  margin: 0 0 20px 0;
  border-bottom: 1px solid rgb(204,204,204);
  color: rgb(51,51,51);
  font-size: inherit;
}
.u-head p{
  color: rgb(153,153,153);
}
.ad-wrap{
  position: relative;
  width: 200px;
  height: 220px;
  margin-bottom: 40px;
}
.ad-wrap img{
  width: 100%;
  height: 100%;
}
.ad{
  position: absolute;
  right: 0;
  bottom: 0;
  width: 24px;
  height: 18px;
  background: url(../assets/short.png) no-repeat scroll 0 0;
}
.playlist-right{
  display: inline-block;
  width: 200px;
  height: 100%;
  padding: 20px 40px 40px 30px;
  vertical-align:top;
}
</style>
