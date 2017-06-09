<template>
  <div class="origin-list main">
      <div class="list-head">
        <h3>全部</h3><a href="javascript:;" class="list-select"><i>选择分类&nbsp∨</i></a>
        <div class="tab-hotnew" :class="{'new-show':!isHot}">
          <a href="javascript:;" class="taba" @click="tabclick(true)" :class="{'tab-show':isHot}">热门</a>
          <a href="javascript:;" class="taba" @click="tabclick(false)" :class="{'tab-show':!isHot}">最新</a>
        </div>
      </div>  
      <ul class="list-content">
        <li v-for="(item,index) in hotitem">
          <div class="item-wrap">
              <img :src="item[0]">
              <a href="/#" class="msk"></a>
              <div class="item-bottom">
                <span class="ico"></span>
                <span class="hot-num list-num">{{item[1]}}</span>
                <a href="/#" class="hotplay"></a>
              </div>
            </div>
            <p class="p-over list-des"><a href="/#" class="hot-descrp" style="color:black;font-size:14px;">{{item[2]}}</a></p>
            <p class="p-over list-artist">by&nbsp<a href="/#" class="hot-artist">{{item[3]}}</a></p>
        </li>
      </ul>  
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'foot',
  data () {
    return {
      isHot:true,
      hotitem:[
          ["./static/hot01.jpg","220万","2017年五月最热新歌TOP50","王萌"],
          ["./static/hot02.jpg","25万","『福音之旅』聆听清风絮语，静沐斜阳暖心","王萌"],
          ["./static/hot03.jpg","48万","『电音故事』从生命的起源说起","王萌"],
          ["./static/hot04.jpg","18230","『哲学公开课』切实的幸福","王萌"],
          ["./static/hot05.jpg","220万","『锐韧Trap』风骚霸道，黑暗的迷人性格","王萌"],
          ["./static/hot06.jpg","220万","健身小白应该注意些啥？","王萌"],
          ["./static/hot07.jpg","220万","Deep House深窈之道","王萌"],
          ["./static/hot08.jpg","220万","刘瑜：色","王萌"],
      ],
    }
  },
  methods:{
    tabclick:function(mode){
      this.isHot = mode;
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
.origin-list{
  width: 900px;
  padding: 40px;
  text-align: left;
  color: rgb(51,51,51);
}
.list-head{
  height: 40px;
  line-height: 40px;
  border-bottom: 2px solid rgb(193,13,12);
}
.list-head h3{
  float: left;
  margin: 0;
  font-size: 24px;
  font-weight: normal;
}
.list-select{
  display: inline-block;
  height: 31px;
  margin-left:10px;
  padding-right: 5px;
  line-height: 31px;
  color: #0c73c2;
  background: url(../assets/button2.png) no-repeat scroll 100% -100px;
}
.list-select i{
  display: inline-block;
  height: 31px;
  padding: 0 10px 0 15px;
  font-style: normal;
  background: url(../assets/button2.png) no-repeat scroll 0 -59px;
}
.tab-hotnew{
  float: right;
  width: 93px;
  height: 29px;
  line-height: 29px;
  vertical-align: top;
  color: white;
  background: url(../assets/button.png) no-repeat scroll 0 0;
}
.taba{
  display: inline-block;
  width: 44px;
  height: 29px;
  text-align: center;
  line-height: 29px;
}
.new-show{
  background: url(../assets/button.png) no-repeat scroll 0 -32px;
}
.tab-show{
  color: white;
}
.list-content{
  margin: 30px 0 0 -50px;
  padding: 0;
  list-style: none;
}
.list-content li{
  display: inline-block;
  width: 140px;
  height: 188px;
  padding: 0 0 30px 50px;
}
.list-num{
  font-size: 12px;
  color: rgb(204,204,204);
}
.list-des{
  margin: 8px 0 3px 0;
}
.list-artist{
  margin: 0;
  font-size: 12px;
}
</style>
