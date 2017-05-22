<template>
  <div class="topbar">
    <h1 class="logo"><a href="/#"><span class="isHide">网易云音乐</span></a></h1> 
    <ul class="inbl" id="btnlist">
      <li class="inbl" v-for="(item,index) in title" @mouseover="mouseInbtn()" @mouseout="mouseOutbtn()" :class="[btnIn ? 'btnInact' :'']">
        <a href="/#"><span>{{item}}</span></a>
      </li>
    </ul>
    <div class="wrap" id="search">
      <span class="wrap" style="margin-top:3px;"><input name="search" placeholder="单曲/歌手/专辑/歌单/MV/用户"></span>
      <div class="wrap">   
      </div>
    </div>
    <a href="/#"></a>
    <div class="wrap" id="logwrap" @mouseover="showLogmethods" @mouseout="hideLogmethods">
      <a href="">登录</a><span :class="[logHide ? 'logbtnHide' :'logbtnShow']"></span>
      <div id="logmethods" :class="[logHide ? 'isHide' :'wrap']">
        <ul>
          <li v-for="item in log">
            <a href="/#">{{item}}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'topbar',
  data () {
    return {
      btnIn:false,
      logHide:true,
      title: ['发现音乐','我的音乐','朋友','商城','音乐人','下载客户端'],
      log:['手机号登录','微信登录','QQ登录','新浪微博登录','网易邮箱账号登录']
    }
  },
  methods:{
    mouseInbtn:function(index){
      this.btnIn=true;
    },
    mouseOutbtn:function(index){
       this.btnIn=false;
    },
    showLogmethods:function(){
      this.logHide = false;
    },
    hideLogmethods:function(){
     this.logHide = true;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>  
.topbar{
  height: 100%;
  display: -webkit-flex; 
  display: flex;
  justify-content:center;
  align-items:center;
}
.btnInact{
  background-image: url(../assets/topbar.png);
  background-repeat: none;
  background-attachment:fixed;
  background-position: 0px -470px;
}
.logo{
  display: inline-block;
  width: 162px;
  height: 46px;  
  margin: 0;
  background: url(../assets/topbar.png) no-repeat scroll 0 0;
}
.logo a{
  display:inline-block;
  width:100%;
  height:90%;
}
.isHide{
  display: none;
}
.inbl {
  display: inline-block;
  margin: 0;
  height: 100%;
}
.inbl a{
  display: inline-block;
  height: 100%;
}
.inbl span{
  display: inline-block;
  margin-top: 26.3px;
}
.wrap{
  display: inline-block;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 0 15px;
  text-align: left;
}
a {
  text-decoration:none;
  font-size: 13px;
  color: rgb(221,220,220);
}
input {
  width: 150px;
  height: 10px;
  border: 0;
  font-size: 11px;
  line-height: 5px;
  background: none;
  outline:none;
}

#logwrap{
  position: relative;
  padding-right: 20px;
}
.logbtnHide{
  position: absolute;
  right: 0;
  top: 30%;
  width: 12px;
  height: 7px;
  background-image: url(../assets/topbar.png);
  background-repeat: no-repeat;
  background-attachment:scroll;
  background-position:-228px -380px;
}
.logbtnShow{
  position: absolute;
  right: 0;
  top: 30%;
  width: 12px;
  height: 7px;
  background-image: url(../assets/topbar.png);
  background-repeat: no-repeat;
  background-attachment:scroll;
  background-position:-228px -418px;
}
#logmethods{
  width: 150px;
  position: absolute;
  top: 10px;
  left: -50px;
}
#search{
  width: 210px;
  height: 31px;
  margin-left: 80px;
  margin-right: 20px;
  background-image: url(../assets/topbar.png);
  background-repeat: no-repeat;
  background-attachment:scroll;
  background-position: 0 -550px; 
}
</style>
