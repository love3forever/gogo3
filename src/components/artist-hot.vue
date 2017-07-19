<template>
  <div>
    <div v-if="top50">
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
      <table class="tracks-table" id="artist-topsongs">
        <tbody>
          <tr v-for="(track,index) in top50" :class="{'track-fill':index%2==0}">
            <td class="td1">
              <div class="w-ply artist-play">
                <em>{{index+1}}</em>
                <span :class="[track.click?'tracks-cli':'tracks-ply']" :data-tag="index"></span>
              </div>
            </td>
           <td class=" td2 p-over"> 
           <div class="song-link p-over">
             <router-link :to="'/song/'+track.songId" :title="track.songName" class="p-over">
                {{track.songName}}
              </router-link>
              <span v-if="track.alias[0]" class="song-alias p-over">{{`- &nbsp${track.alias[0]}`}}</span>
              <span class="artist-mv" v-if="track.mvid"></span>
           </div>

           </td>
            <td>{{track.duration}}</td>
            <td class="p-over"><a href="#" :title="track.albumName"> {{track.albumName}}</a></td>
            <td class="p-over"><a href="#" :title="track.albName">{{track.albumId}}</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="loading" v-if="!top50">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'track',
  props:['top50'],
  data () {
    return {
      artistTitle:[
        { title:"热门50单曲",isclick:true },
        { title:"所有专辑",isclick:false },
        { title:"相关MV",isclick:false },
        { title:"歌手介绍",isclick:false },
      ],
      result:null,
    }
  },
  methods:{
/*    //歌单播放按钮点击事件
    plyClick:function(index){
      var clickList = this.songs.tracks.map(function(item){
        return item.click;
      });

      var current = clickList.indexOf(true);
      if (current>-1){
        mouseBtnEv.setNewVal(this.songs.tracks[current], 'click', false);
      }
      mouseBtnEv.setNewVal(this.songs.tracks[index], 'click', true);
    },
    //歌单播放按钮点击事件代理
    plySong:function(ev){
      var ev = ev||window.event;
      var target = ev.target||ev.srcElement;

      if (target.nodeName.toLowerCase() == "span"){
        var index = parseInt(target.dataset.tag);
        this.plyClick(index);             
      }
    },*/
  },


}
</script>

<style>
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

