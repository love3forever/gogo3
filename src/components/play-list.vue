<template>
  <div class="playlist main">
    <div class="playlist-left">
      <div class="playlist-head">
        <div class="playlist-cover">
          <img src="http://p1.music.126.net/i3uyC0I4mcUnKgXFCnGUOg==/109951162945982389.jpg">
          <span></span>
        </div>
        <div class="playlist-content">
          <div class="content-title">
            <i></i>
            <h2>|华语励志| 用最初的心走最远的路</h2>
          </div>
          <div class="content-author">
            <a href="/#"><img src="http://p1.music.126.net/Rjpe1fUw8cJsW-NSGKpF6w==/109951162864851765.jpg"></a>
            <span><a href="/#" class="author-link">-武姜儿-</a></span>
            <sup></sup>
            <span>2017-05-27&nbsp创建</span>
          </div>
          <div class="content-opreation">
            <a href="#" class="btn-play">
              <i><em class="ply"></em>播放</i>
            </a>
            <a href="#" class="add-to"></a>
            <a href="#" class="btn-fav">
              <i>(12784)</i>
            </a>
            <a href="#" class="btn-share">
              <i>(72)</i>
            </a>
            <a href="#" class="btn-dl">
              <i>下载</i>
            </a>
            <a href="#" class="btn-cm">
              <i>(133)</i>
            </a>
            <div class="clear"></div>
          </div>
          <div class="content-tag">
            <b>标签：</b>
            <a href="#" class="u-tag">
              <i>欧美</i>
            </a>
            <a href="#" class="u-tag">
              <i>流行</i>
            </a>
            <div class="clear"></div>
          </div>
          <pre v-show="!isShowMore"><b class="u-desc">介绍：</b>{{descDot}}<b class="u-desc" v-show="descMore">...</b></pre>
          <pre v-show="isShowMore"><b class="u-desc">介绍：</b>{{descMore}}</pre>
          <div class="show-more" v-if="descMore">
            <a href="#" class="fr" @click="tabShowMore">{{isShowMore?"收起":"展开"}}</a>
            <i class="u-ico" :class="{'u-icoActive':isShowMore}"></i>
          </div>
        </div>
      </div>
    </div>
    <div class="playlist-right">
      
    </div>
  </div>
</template>

<script>

export default {
  name: 'playlist',
  data () {
    return {
      descDot:null,
      descMore:null,
      isShowMore:false,
    }
  },
  methods:{
    tabShowMore:function(){
      this.isShowMore = !this.isShowMore;
    }
  },
  created:function(){
    var description="我要做远方的忠诚的儿子\n和物质的短暂情人\n和所有以梦为马的诗人一样\n我不得不和烈士和小丑走在同一道路上\n万人都要将火熄灭 我一人独将此火高高举起\n此火为大 开花落英于神圣的祖国\n和所有以梦为马的诗人一样\n我藉此火得度一生的茫茫黑夜\n此火为大 祖国的语言和乱石投筑的梁山城寨\n以梦为上的敦煌——那七月也会寒冷的骨骼\n如雪白的柴和坚硬的条条白雪 横放在众神之山\n和所有以梦为马的诗人一样\n我投入此火 这三者是囚禁我的灯盏 吐出光辉\n万人都要从我刀口走过 去建筑祖国的语言\n我甘愿一切从头开始\n和所有以梦为马的诗人一样\n我也愿将牢底坐穿\n众神创造物中只有我最易朽 带着不可抗拒的 死亡的速度\n只有粮食是我珍爱\n我将她紧紧抱住 抱住她 在故乡生儿育女\n和所有以梦为马的诗人一样\n我也愿将自己埋葬在四周高高的山上 守望平静的家园\n面对大河我无限惭愧\n我年华虚度 空有一身疲倦\n和所有以梦为马的诗人一样\n岁月易逝 一滴不剩 水滴中有一匹马儿 一命归天\n千年后如若我再生于祖国的河岸\n千年后我再次拥有中国的稻田 和周天子的雪山\n天马踢踏\n和所有以梦为马的诗人一样\n我选择永恒的事业\n我的事业 就是要成为太阳的一生\n他从古至今——“日”——他无比辉煌无比光明\n和所有以梦为马的诗人一样\n最后我被黄昏的众神抬入不朽的太阳\n太阳是我的名字\n太阳是我的一生";

    if (description.length<100){
      this.descDot = description;
    } else {
      this.descDot = description.substr(0,99);
      this.descMore = description;
    };
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
.playlist{
  font-size: 0;
  -webkit-text-size-adjust:none;
  border-right: 1px solid rgb(204,204,204);
  text-align: left;
}
.playlist-left{
  display: inline-block;
  width: 640px;
  height: 100%;
  padding: 47px 30px 40px 39px;
  border-right: 1px solid rgb(204,204,204);
  vertical-align:top;

}
.playlist-right{
  display: inline-block;
  width: 200px;
  height: 100%;
  padding: 20px 40px 40px 30px;
  vertical-align:top;
}
.playlist-head{
  vertical-align: top;
}
.playlist-cover{
  position: relative;
  display: inline-block;
  width: 200px;
  height: 200px;
  vertical-align:top;
}
.playlist-cover img{
  width: 100%;
  height: 100%;
}
.playlist-cover span{
  position: absolute;
  left: -4px;
  top:-4px;
  width: 208px;
  height: 208px;
  background: url(../assets/coverall.png) no-repeat scroll 0 -1285px;
}
.playlist-content{
  display: inline-block;
  width: 410px;
  margin-left: 30px;
  vertical-align:top;
}
.content-title{
  vertical-align: top;
  margin-bottom: 12px;
}
.content-title i{
  display: inline-block;
  width: 54px;
  height: 24px;
  margin-right: 10px;
  vertical-align: top;
  background: url(../assets/icon.png) no-repeat scroll 0 -243px;
}
.content-title h2{
  display: inline-block;
  margin: 0;
  font-size: 20px;
  line-height: 24px;
  font-weight: normal;
  color: rgb(51,51,51);
  vertical-align: top;
}
.content-author{
  height: 35px;
  margin-bottom: 20px;
  vertical-align: middle;
  font-size: 12px;
  color: rgb(153,153,153);
}
.content-author img{
  vertical-align: middle;
  width: 35px;
  height: 35px;
}
.content-author sup{
  display: inline-block;
  width:12px; 
  height:13px;
  margin: -4px 15px 0 0;
  vertical-align: middle;
  background: url(../assets/icon.png) no-repeat scroll -65px -840px;
}
.author-link{
  color: #0c73c2;
  margin-left: 10px;
}
.author-link:hover,.show-more a:hover{
  text-decoration: underline;
}
.content-opreation a{
  float: left;
  height: 31px;
  line-height: 31px;
  overflow: hidden;
}
i{
   display: inline-block;
   height: 100%;
   font-style: normal;
   overflow: hidden;
}
.ply{
  float: left;
  width: 20px;
  height: 18px;
  margin: 6px 2px 2px 0;
  background: url(../assets/button2.png) no-repeat scroll 0 -1622px;
  overflow: hidden;
}
.ply:hover{
    background: url(../assets/button2.png) no-repeat scroll -28px -1622px;
}
.btn-play{
  padding-right: 5px;
  background: url(../assets/button2.png) no-repeat scroll 100% -428px;
}
.btn-play:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -510px;
}
.btn-play i{
  color: white;
  padding: 0 7px 0 8px;
  background: url(../assets/button2.png) no-repeat scroll 0 -387px;
}
.btn-play i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -469px;
}
.add-to{
  width: 31px;
  margin: 0 5px 0 -3px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1588px;
}
.add-to:hover{
  background: url(../assets/button2.png) no-repeat scroll -40px -1588px;
}
.btn-fav,.btn-share,.btn-dl,.btn-cm{
  padding-right: 5px;
  margin-right: 6px;
  background: url(../assets/button2.png) no-repeat scroll 100% -1020px;
}
.btn-fav:hover,.btn-share:hover,.btn-dl:hover,.btn-cm:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -1106px;
}
.btn-fav i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -977px;
}
.btn-fav i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1063px;
}
.btn-share i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1225px;
}
.btn-share i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1268px;
}
.btn-dl i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -2761px;
}
.btn-dl i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -2805px;
}
.btn-cm i{ 
  padding: 0 2px 0 28px;
  background: url(../assets/button2.png) no-repeat scroll 0 -1465px;
}
.btn-cm i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1508px;
}
.content-tag{

  margin: 25px 0 5px 0;
}
.clear{
  clear: both;
}
.content-tag b{
  float: left;
  font-size: 12px;
  font-weight: normal;
  height: 22px;
  line-height: 22px;
}
.u-tag{
  float: left;
  height: 22px;
  line-height: 22px;
  padding-right: 10px;
  margin: 0 10px 3px 0;
  background: url(../assets/button2.png) no-repeat scroll 100% -27px;
}
.u-tag:hover{
  background: url(../assets/button2.png) no-repeat scroll 100% -1430px;
}
.u-tag i{
  padding: 0 3px 0 13px;
  background: url(../assets/button2.png) no-repeat scroll 0 0;
}
.u-tag i:hover{
  background: url(../assets/button2.png) no-repeat scroll 0 -1400px;
}
.playlist p{
  margin: 0;
  font-size: 12px;
}
.show-more{
  text-align: right;
}
.fr{
  color: #0c73c2; 
}
.u-ico{
  display: inline-block;
  width: 11px;
  height: 8px;
  background: url(../assets/icon.png) no-repeat scroll -65px -520px;
}
.u-icoActive{
  background: url(../assets/icon.png) no-repeat scroll -45px -520px;
}
.u-desc{
  font-weight: normal;
}
pre{
  font-size: 12px;
  font-family: inherit;
}
</style>
