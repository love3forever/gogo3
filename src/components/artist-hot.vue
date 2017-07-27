<template>
  <div>
    <div v-if="top">
      <div class="artist-addbtn">
        <div class="content-opreation">
          <a href="#" class="btn-play">
            <i><em class="ply"></em>播放</i>
          </a>
          <a href="#" class="add-to"></a>
          <a href="#" class="btn-fav">
            <i>收藏热门50</i>
          </a>
          <div class="clear"></div>
        </div>
      </div>
      <table class="tracks-table" id="artist-topsongs" @click="plySong">
        <tbody>
          <tr v-for="(track,index) in top50" :class="{'track-fill':index%2==0}">
            <td class="td1">
              <div class="w-ply artist-play">
                <em>{{index+1}}</em>
                <span :class="[track.click?'tracks-cli':'tracks-ply']" :data-tag="index"></span>
              </div>
            </td>
           <td class="td2 p-over"> 
             <div class="song-link p-over">
               <router-link :to="'/song/'+track.songId" :title="track.songName" class="p-over">
                  {{track.songName}}
                </router-link>
                <span v-if="track.alias[0]" class="song-alias p-over">{{`- &nbsp${track.alias[0]}`}}</span>
                <span class="artist-mv" v-if="track.mvid"></span>
             </div>
           </td>
            <td class="td3">{{track.duration}}</td>
            <td class="p-over"><router-link :to="'/album/'+track.albumId">{{track.albumName}}</router-link></td>
            <td class="p-over">
              <span class="score-wrap">
                <i class="score" :style="'width:'+track.score*92/100+'%'">
                  <i class="score-fill"></i>
                </i>
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="loading" v-if="!top">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'artist',
  props:['top'],
  data () {
    return {
      result:null,
      top50:null,
    }
  },
  methods:{
    //歌单播放按钮点击事件
    plyClick:function(index){
      var current = this.top50.map(function(item){
        return item.click;
      }).indexOf(true);

      if (current>-1){
        mouseBtnEv.setNewVal(this.top50[current], 'click', false);
      }
      mouseBtnEv.setNewVal(this.top50[index], 'click', true);
    },
    //歌单播放按钮点击事件代理
    plySong:function(ev){
      var ev = ev||window.event;
      var target = ev.target||ev.srcElement;

      if (target.nodeName.toLowerCase() == "span"){
        var index = parseInt(target.dataset.tag);
        this.plyClick(index);             
      }
    },
  },
  created:function(){
    this.top50 = this.top.list;
  },
}
</script>

<style>
.score{
  display: block;
  height: 100%;
  padding: 0 4px;
  background:  url(../assets/table2.png) no-repeat scroll 100% -318px;
}
.score-wrap{
  display: block;
  width: 100px;
  height: 8px;
  line-height: normal;
  background:  url(../assets/table2.png) no-repeat scroll 0 -240px;
}
.score-fill{
  display: block;
  height: 100%;
  padding-left: 4px;
  margin-left: -4px;
  background:  url(../assets/table2.png) no-repeat scroll 0 -304px;
}
.artist-addbtn{
  margin: 20px 0 10px 0;
}
#artist-topsongs{
  border: 0;
}
.td1{
  width: 74px;
}
.td2{
  width: 169px;
}
.td3{
  width: 69px;
}
.song-alias{
  position: relative;
  
  color: rgb(174,174,174);
}
.song-link{
  position: relative;
  max-width: 90%;
  display: inline-block;
  padding-right: 25px;
  margin-right: -25px;
}
.artist-mv{
  position: absolute;
  right: 0;
  width: 23px;
  height: 17px;
  background:  url(../assets/table2.png) no-repeat scroll -30px -151px;  
}
</style>

