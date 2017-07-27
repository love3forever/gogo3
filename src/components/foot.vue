<template>
  <footer>
    <div class="foot-msk">
      <div class="foot-content">
        <div class="copyright">
          <p>
            <a class="about" :href="item[1]" target="_blank" :class="{'about-first':item[2]}" v-for="item in about">{{item[0]}}</a>
          </p>
          <p>
            <span class="copy">网易公司版权所有©1997-2017</span>
            杭州乐读科技有限公司运营：
            <a href="http://p1.music.126.net/-DB9zs1FAJq8vg7HOb-yOQ==/3250156395654666.jpg" target="_blank" class="permission">浙网文[2015] 0415-135号</a>
          </p>
        </div>
        <ul class="enter">
          <li v-for="item in enter">
            <a :href="item[1]" target="_blank" :style="item[2]">{{item[0]}}</a>
          </li>
        </ul>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'foot',
  data () {
    return {
      about:[
        ["关于网易","http://music.163.com/about",true],
        ["客户服务","http://help.mail.163.com/service.html",false],
        ["服务条款","http://music.163.com/html/web2/service.html",false],
        ["网站导航","http://sitemap.163.com/",false],
        ["意见反馈",,false],
      ],
      enter:[
        ["独立音乐人","http://music.163.com/nmusician/web/index","background-position:-60px -80px;"],
        ["音乐专栏","http://music.163.com/topic/recruit","background-position:0px -80px;"],
        ["自媒体","http://music.163.com/topic/selfmedia","background-position: 0 0;"],
        ["赞赏","http://music.163.com/web/reward","background-position:-60px 0;"],
      ]
    }
  },
}
</script>

<style>  
footer{
  width: 100%;
  height: 140px;
  border-top: 1px solid rgb(204,204,204);
}
.foot-msk{
  width: 980px;
  margin: 0 auto;
}
.copyright{
  float: left;
  width: 490px;
  padding-top:35px;
  line-height: 24px;
  font-size: 12px;
}
.copyright p{
  margin: 0;
  text-align: left;
}
.copy{
  margin-right:12px;
}
.copyright a:hover{
  text-decoration: underline;
}
.about{
  padding: 0 9px;
  border-left:1px solid rgb(194,194,194);
  color: rgb(153,153,153);
}
.about-first{
  padding-left:0;
  border: 0;
}
.foot-content{
  overflow: hidden;
}
.enter{
  float: right;
  width: 330px;
  padding: 0;
  margin: 21px 0 0 0;
  list-style: none;
}
.enter a{
  float: left;
  width: 60px;
  height: 70px;
  margin-left: 22px;
  text-indent: -9999px;
  background: url(../assets/foot_enter.png) no-repeat scroll;
}
</style>
