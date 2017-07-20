<template>
  <div class="playlist main">
    <div v-if="result">
      <div class="playlist-left">
        <div class="artist-wrap">
          <h2>{{artistName}}</h2>
          <h3 v-if="artistAlias">{{artistAlias}}</h3>
          <img :src="artistImg">
          <div class="artist-btn">
            <a href="" class="artist-home"></a>
            <a href="" class="artist-fav"></a>
          </div>
        </div>
        <ul class="artist-title">
          <li v-for="(title,index) in artistTitle" @click="titleClick(index)">
            <router-link :to="title.path" :class="{'titlecli-a':title.isclick}">
              <em class="nor" :class="{'titlecli-em':title.isclick}">{{title.title}}</em>
            </router-link>
          </li>
        </ul>
        <router-view :top="top50"></router-view>
      </div>
      <div class="playlist-right">
        <div class="ad-wrap">
          <a href="#" class="ad"></a>
          <a href="#"><img src="https://haitaoad.nosdn.127.net/ad.bid.material_f73d40bef46d4b0098283ea63ca4b579?imageView&thumbnail=200x220&quality=100"></a>
        </div>
        <div class="rela-cmd u-head">
          <h3>相关推荐</h3>
          <ul>
            <li>
              <div class="rela-msk">
                <a href="#">
                  <img src="http://p3.music.126.net/1L_rIf-sofhXEG1R2JQ5bQ==/1365593506719668.jpg?param=50y50">
                </a>
              </div>
              <div class="rela-info">
                <p class="rela-title p-over">
                  <a href="#" title="传统世界音乐【器乐】">传统世界音乐【器乐】</a>
                </p>
                <p class="p-over">
                  <span>by</span>
                  <a href="#" title="紫de甘蓝">紫de甘蓝</a>
                </p>
              </div>
            </li>
            <li>
              <div class="rela-msk">
                <a href="#">
                  <img src="http://p4.music.126.net/rnHLMLESV1c-PcFbDgAngg==/18775260557760255.jpg?param=50y50">
                </a>
              </div>
              <div class="rela-info">
                <p class="rela-title p-over">
                  <a href="#" title="一个人的乌德琴">一个人的乌德琴</a>
                </p>
                <p class="p-over">
                  <span>by</span>
                  <a href="#" title="珠疯">珠疯</a>
                </p>
              </div>
            </li>
          </ul>
        </div>
        <div class="multi-dowm u-head">
          <h3>网易云音乐多端下载</h3>
          <ul class="dowm-methods">
            <li><a class="m1" href="https://itunes.apple.com/app/id590338362" target="_blank"></a></li>
            <li><a class="m2" href="http://music.163.com/api/pc/download/latest"  target="_blank"></a></li>
            <li><a class="m3" href="http://music.163.com/api/android/download/latest2" target="_blank"></a></li>
          </ul>
          <p>同步歌单，随时畅听320k好音乐</p>
        </div>
      </div> 
    </div>
    <div class="loading" v-if="!result">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'track',
  data () {
    return {
      artistTitle:[
        { title:"热门50单曲",isclick:true ,path:"/artist/"+this.$route.params.id+"/hot"},
        { title:"所有专辑",isclick:false ,path:"/artist/"+this.$route.params.id+"/album"},
/*        { title:"相关MV",isclick:false ,path:"/artist/"+this.$route.params.id+"/album"},
        { title:"歌手介绍",isclick:false ,path:"/artist/"+this.$route.params.id+"/album"},*/
      ],
      result:null,
    }
  },
  methods:{
    titleClick:function(index){
      var title = this.artistTitle.map(function(item){
        return item.isclick;
      });

      var current = title.findIndex(function(value){
        return value === true;
      });
      mouseBtnEv.setNewVal(this.artistTitle[current], 'isclick', false);
      mouseBtnEv.setNewVal(this.artistTitle[index], 'isclick', true);
    }
  },
  beforeCreate:function(){
    //请求歌手数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/artist/${this.$route.params.id}/index`)
      .then(response => {
        this.result = response.data;
        console.log(this.result)
      })
      .catch(response => {
        console.log(response)
    });
  },
  computed:{
    artistName:function(){
      return this.result.artist_name?this.result.artist_name:null;
    },
    artistAlias:function(){
      return this.result.artist_alias?this.result.artist_alias:null;
    },
    artistImg:function(){
      return this.result.img?this.result.img:null;
    },
    top50:function(){
      var topsongs = this.result.top50,
          list = new Array();

      if (topsongs){
        for ( let song of topsongs){
          let { duration, id:songId, name:songName, alias, mvid, album:{id:albumId}, album:{name:albumName}, score} = song;

          duration = mouseBtnEv.changeTime(duration);
          list.push({ duration, songId, songName, alias, mvid, albumId, albumName, score, click:false});
        }
        return {list};
      } else {
        return null;
      };
    },
  }

}
</script>

<style>
.artist-title{
  height: 39px;
  margin: 0;
  padding: 0;
  border: 1px solid rgb(204,204,204);
  border-top:0;
  border-bottom: 0;
  list-style-type: none;
  background:  url(../assets/tab.png) scroll 0 0;
}
.artist-title li{
  float: left;
  width: 138px;
  height: 39px;
  position: relative;
  left: -1px;
  right: 1px;
  font-size: 14px;
  text-align: center;
  line-height: 39px;
}
.artist-title li a{
  display: block;
  padding-left:2px;
  height: 100%;
  font-size: inherit;
}
.artist-title li:hover{
  background:  url(../assets/tab.png) scroll 100% -45px;
}
.nor{
  display: block;
  height: 37px;
  font-style: normal;
  padding: 2px 2px 0 0;
  
}
.titlecli-a{
  background:  url(../assets/tab.png) scroll 0 -90px;
}
.titlecli-em{
  background:  url(../assets/tab.png) scroll 100% -90px;
}
.artist-btn{
  position: absolute;
  right: 18px;
  bottom: 18px;
  width: 200px;
  height: 32px;
  overflow: hidden;
}
.artist-home{
  float: left;
  width: 96px;
  height: 100%;
  background:  url(../assets/iconall.png) no-repeat scroll 0 -1156px; 
}
.artist-home:hover{
  background-position: 0 -1196px; 
}
.artist-fav{
  float: right;
  width: 76px;
  height: 100%;
  background:  url(../assets/iconall.png) no-repeat scroll 0 -500px; 
}
.artist-fav:hover{
  background-position: 0 -540px; 
}
.artist-wrap{
  position: relative;
  height: 333px;
  font-size: 12px;
  margin-top: -20px;
}
.artist-wrap h2{
  float: left;
  height: 35px;
  margin: 0px;
  font-size: 24px;
  font-weight: normal;
  line-height: 24px;
  color: rgb(51,51,51);
}
.artist-wrap h3{
  float: left;
  margin: 0px;
  padding: 10px 0 0 10px;
  font-size: 14px;
  font-weight: normal;

  
  color: rgb(153,153,153);
}
.artist-wrap img{
  width: 640px;
  height: 300px;
}
</style>

