<template>
  <div class="topbar">
    <h1 class="logo"><a href="/#"><span class="isHide">网易云音乐</span></a></h1> 
    <ul class="inbl" id="btnlist">
      <li class="inbl" v-for="(item,index) in title" track-by="$index" @mouseover="mouseInbtn(index)" @mouseout="mouseOutbtn(index)" @click="mouseClick(index)" :class="{ 'btnInact': item[1], 'btnCliact': item[2]}">
        <a href="/#"><span>{{item[0]}}</span><sub :class="{'subHide': !item[2]}"></sub></a>
      </li>
    </ul>
    <div class="wrap" id="search">
      <span class="wrap" style="margin:2% 0;"><input name="search" placeholder="单曲/歌手/专辑/歌单/MV/用户"></span>
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
      logHide:true,
      title: [['发现音乐',false,true],['我的音乐',false,false],['朋友',false,false],['商城',false,false],['音乐人',false,false],['下载客户端',false,false]],
      log:['手机号登录','微信登录','QQ登录','新浪微博登录','网易邮箱账号登录']
    }
  },
  methods:{
    mouseInbtn:function(index){
      this.$set(this.title[index], 1, true);
      this.title[index].splice(1, 1, true);
    },
    mouseOutbtn:function(index){
      this.$set(this.title[index], 1, false);
      this.title[index].splice(1, 1, false);
    },
    mouseClick:function(index){
      for (var i=0;i<this.title.length;i++){
        if (this.title[i][2]===true){
          this.$set(this.title[i], 2, false);
          this.title[i].splice(2, 1, false);
        }
      }
      this.$set(this.title[index], 2, true);
      this.title[index].splice(2, 1, true);
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
  background: url(../assets/topbar.png) no-repeat scroll 0px -470px;
  background-size: 96px 622px;
}
.btnCliact{
  background: url(../assets/topbar.png) no-repeat scroll  0px -155px;
  background-size: 96px 622px;
  
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
  margin: 0;
}
a {
  text-decoration:none;
  font-size: 14px;
  color: rgb(221,220,220);
}
input {
  width: 155px;
  height: 12px;
  border: 0;
  font-size: 11px;
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
  background: url(../assets/topbar.png) no-repeat scroll -228px -380px;
}
.logbtnShow{
  position: absolute;
  right: 0;
  top: 30%;
  width: 12px;
  height: 7px;
  background: url(../assets/topbar.png) no-repeat scroll -228px -418px;
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
  background: url(../assets/topbar.png)  no-repeat scroll 0 -550px;
}
#btnlist li{
  width: 96px;
}
#btnlist a{
  width: 100%;
}
#btnlist span{
  display: inline-block;
  width: 100%;
  background: url(../assets/topbar.png) no-repeat scroll  -143.8px -328px;
}
#btnlist sub{
  display: inline-block;
  width: 14px;
  height: 9px;
  margin-bottom: -12px;
  background: url(../assets/topbar.png) no-repeat scroll  -226px 0;
}
.subHide{
  visibility: hidden;
}
</style>
