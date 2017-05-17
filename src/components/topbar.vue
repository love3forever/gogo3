<template>
  <div class="topbar">
    <h1 class="inbl"><a href="/#">网易云音乐</a></h1>
    <ul class="inbl">
      <li class="inbl" v-for="item in title"><a href="/#">{{item}}</a></li>
    </ul>
    <div class="wrap">
      <input name="search" placeholder="单曲/歌手/专辑/歌单/MV/用户">
      <div class="wrap">
        
      </div>
    </div>
    <a href="/#"></a>
    <div class="wrap" id="logwrap" @mouseover="showLogmethods" @mouseout="hideLogmethods">
      <a href="">登录</a>
      <div class="wrap" id="logmethods" style="display:none">
        <ul>
          <li v-for="item in log"><a href="/#">{{item}}</a></li>
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
      title: ['发现音乐','我的音乐','朋友','商城','音乐人','下载客户端'],
      log:['手机号登录','微信登录','QQ登录','新浪微博登录','网易邮箱账号登录']
    }
  },
  methods:{
    showLogmethods:function(){
      document.getElementById('logmethods').style.display='';
    },
    hideLogmethods:function(){
      document.getElementById('logmethods').style.display='none';
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inbl {
  display: inline-block;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 0 10px;
  text-align: left;
}

a {
  text-decoration:none
}

input {
  width: 210px;
  border-radius: 10px;
}

.wrap{
  display: inline-block;  
}
#logwrap{
  position: relative;
}
#logmethods{
  width: 150px;
  position: absolute;
  top: 10px;
  left: -50px;
}
</style>
