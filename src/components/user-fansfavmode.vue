<template>
  <div class="fansfav-mode" v-if="list">
    <ul class="uh-fans">
      <li v-for="(user,index) in list" :class="{'colorGrey':colored(index)}">
        <a href="" class="fans-pic">
          <img :src="user.avatarUrl">
        </a>
        <div class="fans-info">
          <router-link :to="'/user/'+user.userId" class="fans-name">{{user.nickname}}</router-link>
          <i class="female"></i>
          <p class="fans-conect">
            <a href="javascript:;">动态<span>{{user.eventCount}}</span></a><span class="line">|</span>
            <router-link :to="'/user/'+user.userId+'/fav'">关注<span>{{user.followeds}}</span></router-link><span class="line">|</span>
            <router-link :to="'/user/'+user.userId+'/fans'">粉丝<span>{{user.follows}}</span></router-link>
          </p>
        </div>
        <div class="fans-fav">
          <a href="javascript:;" class="follow"><i>关&nbsp&nbsp注&nbsp</i></a>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'fansfavmode',
  props:['list'],
  methods:{
    colored:function(index){
      if (index%4===2||index%4===3){
        return true;
      } else {
        return false;
      };        
    }
  }
}
</script>

<style>
.colorGrey{
  background-color: rgb(250,250,250);
}
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

