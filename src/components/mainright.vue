<template>
  <div class="mainright">
    <div class="right-top">
      <p>登录网易云音乐，可以享受无限收藏的乐趣，并无限同步到手机</p>
      <a href="/#" class="login" @mouseover="btnIn('logActive')" @mouseout="btnOut('logActive')" :class="{'log-Active':logActive}">用户登录</a>
    </div>
    <div class="right-center">
      <h3>
        <span>入驻歌手</span>
        <a class="viewall" href="">查看全部></a>
      </h3>
      <ul>
        <li class="singer-wrap" :class="{'singer-Active':item[1]}" v-for="(item,index) in singerData" @mouseover="singerIn(index)" @mouseout="singerOut(index)">
          <a class="singer" href="/#">
            <div class="head">
              <img :src="item[0]">
            </div>
            <div class="info">
              <h4><span>{{item[3]}}</span></h4>
              <p>{{item[4]}}</p>
            </div>
          </a>
        </li>
      </ul>
      <a href="/#" class="singer-apply" :class="{'apply-Active':applyActive}"  @mouseover="btnIn('applyActive')" @mouseout="btnOut('applyActive')" >申请成为音乐人</a>
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
      applyActive:false,
      singerData:[//入驻歌手:[图片,是否mouseover,是否click,姓名,描述]
        ['./static/singer01.jpg',false,false,'张惠妹aMEI','台湾歌手张惠妹'],
        ['./static/singer02.jpg',false,false,'尚雯婕','原创电子唱作人'],
        ['./static/singer03.jpg',false,false,'羽泉组合','国内知名演唱组合 羽泉'],
        ['./static/singer04.jpg',false,false,'李志','个体音乐人李志'],
        ['./static/singer05.jpg',false,false,'马頔麻油叶','民谣音乐人'],
      ],
    }
  },
  methods:{
   btnIn: function(key){//后续写成全局复用
    this[key] = true;
   },
   btnOut:function(key){
    this[key] = false;
   },
   singerIn:function(index){
    this.singerData[index].splice(1, 1, true);
   },
   singerOut:function(index){
    this.singerData[index].splice(1, 1, false);
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
}
.viewall{
  text-align:right;
  position: absolute;
  right: 0;
}
.right-center ul{
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
.singer-Active{
  background-color: rgb(244,244,244);
}
.head{
  display: inline-block;
  width: 62px;
  height: 100%;
}
img{
  width: 100%;
  height: 100%;
}
.info{
  display: inline-block;
  width: 133px;
  height: 100%;
  padding-left: 12px;
  overflow:hidden;

}
.singer{
  display: inline-block;
  width: 100%;
  height: 100%;
}
h4{
  margin: 1em 0;
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
</style>
