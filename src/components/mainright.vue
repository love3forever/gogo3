<template>
  <div class="mainright">
    <div class="right-top">
      <p>登录网易云音乐，可以享受无限收藏的乐趣，并无限同步到手机</p>
      <a href="/#" class="login">用户登录</a>
    </div>
    <div class="right-center">
      <h3>
        <span>入驻歌手</span>
        <a class="viewall" href="">查看全部></a>
      </h3>
      <ul>
        <li class="singer-wrap" v-for="(singer,index) in singerData">
          <a class="singer" href="/#">
            <div class="head">
              <img :src="singer.img">
            </div>
            <div class="info">
              <h4><span>{{singer.name}}</span></h4>
              <p class="p-over">{{singer.desc}}</p>
            </div>
          </a>
        </li>
      </ul>
      <a href="/#" class="singer-apply">申请成为音乐人</a>
    </div>
    <div class="right-bottom">
      <h3><span>热门DJ</span></h3>
      <ul>
        <li class="dj-wrap" v-for="dj in djData">
          <a href="/#" class="dj"><img :src="dj.img"></a>
          <div class="info dj-info">
            <p><a href="/#" class='dj-Name'>{{dj.name}}</a><sub class="dj-v"></sub></p>
            <p class="p-over">{{dj.desc}}</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'slides',
  props:['rightData'],
  computed:{
    singerData:function(){
      return this.rightData?this.rightData.newSinger:[];
    },
    djData:function(){
      return this.rightData?this.rightData.hotdj:[];
    },
  }
}  
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
a{
  text-decoration:none;
}
.mainright{
  position: absolute;
  top: 0;
  right: 0;
  width: 250px;
  height: 100%;
  border-left: 1px solid rgb(204,204,204);
  border-right: 1px solid rgb(204,204,204);
}
.right-top{
  height: 126px;
  background: url(../assets/index.png) no-repeat scroll 0 0;
}
.right-top p{
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
a.login:hover{
  background: url(../assets/index.png) no-repeat scroll -110px -195px;
}
.right-center{
  margin-top: 15px;
  text-align:left;
}
.right-center h3,.right-bottom h3{
  position: relative;
  width: 210px;
  height: 24px;
  margin: 0 auto;
  border-bottom: 1px solid rgb(204,204,204);
  font-size: 13px;
}
.right-center a{
  color: inherit;
  font-size: 12px;
  text-decoration:none;
}
.viewall{
  text-align:right;
  position: absolute;
  right: 0;
}
.right-center ul,.right-bottom ul{
  margin: 6px 0 14px 20px;
  padding: 0;
}
.singer-wrap{
  list-style-type:none;
  width: 210px;
  height: 62px;
  margin-top: 14px;
  padding: 0;
  border: 0.1px solid rgb(233,233,233);
  background-color: rgb(250,250,250);
}
a.singer-apply:hover,li.singer-wrap:hover{
  background-color: rgb(244,244,244);
}
.head{
  display: inline-block;
  width: 62px;
  height: 100%;
}
.mainright img{
  width: 100%;
  height: 100%;
}
.info{
  display: inline-block;
  width: 130px;
  height: 100%;
  padding-left: 12px;
  overflow:hidden;

}
.singer{
  display: inline-block;
  width: 100%;
  height: 100%;
}
.mainright h4{
  margin: 0.8em 0;
  padding: 0;
}
.info p{
  margin: 0;

}
.singer-apply{
  display: inline-block;
  width: 210px;
  height: 31px;
  margin-left: 20px;
  border: 1px solid rgb(204,204,204);
  border-radius: 3px;
  text-align:center;
  line-height: 31px;
  background: rgb(250,250,250);
}
.apply-Active{
  background: none;
}
.right-bottom{
  margin-top: 30px;
  font-size: 12px;
  text-align: left;
}
.dj-wrap{
  list-style-type:none;
  width: 210px;
  height: 40px;
  margin-top: 14px;
  padding: 0;
}
.dj-info{
  padding-left: 7px;
  width: 158px;
}
.dj-info p{
  margin-bottom: 4px;
}
.dj{
  display: inline-block;
  width: 40px;
  height: 40px;
}
.dj-v{
  display: inline-block;
  width: 12px;
  height: 12px;
  background: url(../assets/icon.png) repeat-x scroll 0 0;
}
.dj-Name{
  color: black;
}
a.dj-Name:hover,a.viewall:hover{
  text-decoration: underline;
}
.p-over{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
