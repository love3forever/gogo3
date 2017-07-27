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
      <playlistRight></playlistRight>
    </div>
    <div class="loading" v-if="!result">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import playlistRight from './generalRight'
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'artist',
  components:{
    playlistRight
  },
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
        //更改页面title
        document.title = `${this.artistName}${this.artistAlias}-网易云音乐`;
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
        return { list };
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

