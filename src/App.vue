<template>
  <div id="app">
    <topbar></topbar>
    <div class="content">
      <router-view></router-view>
    </div>
    <foot></foot>
    <a href="/#" id="back2top" class="back2top" title="回到顶部" v-if="scrollLength!==0" @click="goToTop">回到顶部</a>
  </div>
</template>

<script>
import topbar from './components/topbar'
import origin from './components/origin'
import foot from './components/foot'

export default {
  name: 'app',
  components: {
    topbar,origin,foot
  },
  data () {
    return {
      scrollLength:0,//垂直滚动条距顶部距离
    }
  },
  methods:{
    //返回顶部按钮点击事件
    goToTop:function(){
      let backlength = document.documentElement.scrollTop || document.body.scrollTop; 
      backlength = 0;
    }
  },
  mounted:function(){
    //模板挂载完成后开始监听window.onscroll事件
    this.$nextTick(function(){  
      window.addEventListener('scroll', ()=>{//箭头函数修正this指针
        this.scrollLength = document.documentElement.scrollTop || document.body.scrollTop; 
      });  
    });  
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(102,102,102);
  background: rgb(245,245,245);
}
.main{
  position: relative;
  width: 980px;
  margin: 0 auto;
  border-left: 1px solid rgb(204,204,204);
  background: white;
}
a{
  text-decoration: none;
  color: rgb(102,102,102);
  font-size: 12px;
}
.back2top{
  position: fixed;
  left: 50%;
  bottom: 160px;
  width: 49px;
  height: 44px;
  margin-left: 500px;
  text-indent: -9999px;
  background: url(./assets/sprite.png) no-repeat scroll -265px -47px;
}
.back2top:hover{
  background: url(./assets/sprite.png) no-repeat scroll -325px -47px;
}
</style>
