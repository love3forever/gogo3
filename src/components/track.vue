<template>
  <div class="playlist main">
    <div  v-if="hasResult">
      <div class="playlist-left">
        <div class="playlist-head">
          <div id="a-cover" class="playlist-cover">
            <img id="a-pic":src="hasResult.picUrl">
            <span id="a-song"></span>
          </div>
          <div class="playlist-content">
            <div class="content-title">
              <i id="trackIcon"></i>
              <h2>
                {{hasResult.name}}
                <a class="plyMv" href="javascript:;">
                  <i></i>
                </a>    
              </h2> 
            </div>
            <div class="content-author">
              <p class="a-author">
                <span>歌手:
                  <router-link :to="'/artist/'+hasResult.singer_id" class="author-link">
                    {{hasResult.singer}}
                  </router-link>
                </span>
              </p>
              <p class="a-author">
                <span >发行时间:     
                  {{hasResult.publish_time}}
                </span>
              </p>
            </div>
            <div class="content-opreation">
              <a href="#" class="btn-play">
                <i><em class="ply"></em>播放</i>
              </a>
              <a href="#" class="add-to"></a>
              <a href="#" class="btn-fav">
                <i>收藏</i>
              </a>
              <a href="#" class="btn-share">
                <i>分享</i>
              </a>
              <a href="#" class="btn-dl">
                <i>下载</i>
              </a>
              <a href="#" class="btn-cm">
                <i>评论</i>
              </a>
              <div class="clear"></div>
            </div>
          </div>
        </div>
        <div class="track-info">
          <h3>专辑介绍：</h3>
<!--           <p>无论是谁都有一个成长的过程，同时也要感谢那些想尽办法要将你置于死地的人，如果不是他们步步紧逼，也不会有今天的我们。</p> -->
            <pre v-show="!des.isShowMore">{{des.descDot}}<b class="u-desc" v-show="des.descMore">...</b></pre>
            <pre v-show="des.isShowMore">{{des.descMore}}</pre>
            <div class="show-more" v-if="des.descMore">
              <a href="javascript:;" class="fr" @click="tabShowMore">{{des.isShowMore?"收起":"展开"}}</a>
              <i class="u-ico" :class="{'u-icoActive':des.isShowMore}"></i>
            </div>
        </div>
        <div class="playlist-tracks">
          <div class="u-title">
            <h3>包含歌曲列表</h3>
            <span class="u-lft">{{`${hasResult.songs.length}首歌`}}</span>
            <div class="u-rgt">
              <i></i>
              <a href="">生成外链播放器</a>
            </div>
          </div>
          <div class="u-content">
            <table class="tracks-table">
              <thead>
                <tr>
                  <th class="w1"><div class="u-wrap"></div></th>
                  <th><div class="u-wrap">歌曲标题</div></th>
                  <th class="w5"><div class="u-wrap">时长</div></th>
                  <th class="w6"><div class="u-wrap">歌手</div></th>
                </tr>
              </thead>
              <tbody @click="plySong">
                <tr v-for="(track,index) in songs" :class="{'track-fill':index%2==0}">
                  <td>
                    <div class="w-ply">
                      <em>{{index+1}}</em>
                      <span :class="[track.click?'tracks-cli':'tracks-ply']" :data-tag="index"></span>
                    </div>
                  </td>
                  <td class="p-over">
                    <router-link :to="'/song/'+track.id" :title="track.name">
                      {{track.name}}
                    </router-link>
                  </td>
                  <td>{{track.duration}}</td>
                  <td class="p-over">
                    <router-link :to="'/artist/'+track.artists[0].id" :title="track.artists[0].name">
                      {{track.artists[0].name}}
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <comment :url="cmtUrl"></comment>
      </div>
      <playlistRight></playlistRight> 
    </div>
    <div class="loading" v-show="!hasResult">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import playlistRight from './generalRight'
import comment from './generalComment'
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'track',
  components:{
    playlistRight,comment
  },
  data () {
    return {
      hasResult:false,//是否返回歌单数据
      songs:null,
      des:{
        isShowMore:false,
        descDot:null,
        descMore:null,
      },
      listUrl:`http://123.206.211.77:33333/api/v1/album/${this.$route.params.id}/detail`,
      cmtUrl:`http://123.206.211.77:33333/api/v1/album/${this.$route.params.id}/comments/`,
    }
  },
  methods:{
    //歌单介绍-展开/收起按钮点击事件
    tabShowMore:function(){
      this.des.isShowMore = !this.des.isShowMore;
    },
    //歌单播放按钮点击事件
    plyClick:function(index){
      var clickList = this.songs.map(function(item){
        return item.click;
      });

      var current = clickList.indexOf(true);
      if (current>-1){
        mouseBtnEv.setNewVal(this.songs[current], 'click', false);
      }
      mouseBtnEv.setNewVal(this.songs[index], 'click', true);
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
    //请求歌单数据
    this.$http.get(this.listUrl)
      .then(response => {
        this.hasResult = response.data;//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
  },
  watch:{
    //歌单数据返回后，提取、格式化需要的数据
    hasResult:function(result){
      //解构result.tracks
      var list = new Array();
      
      for ( let item of result.songs ){ 
        let { duration, mvid, name, id, artists} = item;

        duration = mouseBtnEv.changeTime(duration);
        list.push({ duration, mvid, name, id, artists, click:false});
      }

      this.songs = list;
      this.des = {
        isShowMore:false,
        descDot:result.desc.substr(0,99),
        descMore:result.desc.length>99?result.desc:null,
      };
    },
  }
}
</script>

<style scoped>
.track-info pre{
  padding:0 24px;
  line-height: 24px;
}
.w5{
  width: 91px;
}
.w6{
  width: 127px;
}
#trackIcon{
  background-position: 0 -186px;
}
.track-info{
  margin-top:20px;
  font-size: 12px;
}
.track-info h3{
  margin:0;
  font-size: 12px;
}
.track-info p{
  color: rgb(102,102,102);
  text-indent: 2em;
  line-height: 24px;
  margin-top: 4px;
}
#rel-time{
  color: inherit;
}
#a-cover{
  width: 177px;
  height: 177px;
  border: 0;
  margin-right: 20px;
}
.upload-lrc{
  margin-top: 48px;
  text-align: right;
}
.upload-lrc a{
  margin-left: 5px;
  text-decoration: underline;
  color: rgb(153,153,153);
}
#a-song{
  width: 209px;
  height: 177px;
  left: 0;
  top: 0;
  background:  url(../assets/coverall.png) no-repeat scroll 0 -986px;
}
#a-pic{
  width: 177px;
  height: 177px;
  margin: 0;
}
</style>

