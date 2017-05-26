<template>
  <div class="mainright">
    <div class="right-top">
      <p>登录网易云音乐，可以享受无限收藏的乐趣，并无限同步到手机</p>
      <a href="/#" class="login" @mouseover="logBtnIn" @mouseout="logBtnOut" :class="{'log-Active':logActive}">用户登录</a>
    </div>
    <div class="right-center">
      <h3>
        <span>入驻歌手</span>
        <a href="">查看全部></a>
      </h3>
      <ul>
        <li>data</li>
      </ul>
    </div>
    <div class="right-bottom"></div>
  </div>
</template>

<script>
export default {
  name: 'slides',
  data () {
    return {
      logActive:false,
    }
  },
  methods:{
   logBtnIn: function(){
    this.logActive = true;
   },
   logBtnOut:function(){
    this.logActive = false;
   },
  },
}  
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>  
.mainright{
  position: absolute;
  top: 0;
  right: 0;
  width: 250px;
  height: 100%;
  border: 1px solid rgb(204,204,204);
}
.right-top{
  height: 126px;
  background: url(../assets/index.png) no-repeat scroll 0 0;
}
.right-top p{
  color: rgb(102,102,102);
  font-size: 13.33px;
  text-align:left;
  width: 205px;
  margin: 0 auto;
  padding: 16px 0 ;
}
.login{
  display: inline-block;
  width: 100px;
  height: 31px;
  margin: 0 auto;
  text-decoration:none;
  line-height: 31px;
  font-size: 13px;
  color: rgb(221,220,220);
  background: url(../assets/index.png) no-repeat scroll 0 -195px;
}
.log-Active{
  background: url(../assets/index.png) no-repeat scroll -110px -195px;
}
.right-center{
  margin-top: 15px;
  text-align:left;
}
.right-center h3{
  position: relative;
  width: 210px;
  height: 24px;
  margin: 0 auto;
  border-bottom: 1px solid rgb(204,204,204);
  font-size: 13px;
}
.right-center a{
  color: rgb(102,102,102);
  font-size: 12px;
  text-decoration:none;
  text-align:right;
  position: absolute;
  right: 0;
}
.right-center ul{
  margin: 6px 0 14px 20px;
  padding: 0;
}
.right-center li{
  list-style-type:none;
  width: 210px;
  height: 62px;
  margin-top: 14px;
  padding: 0;
}
</style>
