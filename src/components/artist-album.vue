<template>
  <div>
    <div v-if="albums">
      <ul class="artist-album">
        <li v-for="album in albums">
          <div class="aa-transp">
            <img :src="album.img">
            <router-link :to="'/album/'+album.id" class="aa-msk"></router-link>
            <a href="javascript:;" class="aa-ply"></a>
          </div>
          <p class="aa-name p-over">
            <router-link :to="'/album/'+album.id" :title="album.name">{{album.name}}</router-link>
          </p>
          <p>{{album.time}}</p>
        </li>
      </ul>
    </div>
    <div class="loading" v-if="!albums">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
export default {
  name: 'artistAlbum',
  data () {
    return {
      albums:null
    }
  },
  created:function(){
    //请求歌手所有专辑数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/artist/${this.$route.params.id}/albums`)
      .then(response => {
        this.albums = response.data.albums;
      })
      .catch(response => {
        console.log(response)
    });
  },
}
</script>

<style>
.artist-album{
  margin: 20px 0 0 -18px;
  padding: 0;
  list-style-type: none;
  font-size: 12px;
  overflow: hidden;
}
.artist-album li{
  float: left;
  width: 145px;
  height: 175px;
  padding: 0 0 30px 18px;
}
.aa-transp{
  position: relative;
}
.aa-msk{
  position: absolute;
  top:0;
  left: 0;
  width: 100%;
  height: 120px;
  background:  url(../assets/coverall.png) no-repeat scroll -170px -850px;
}
.aa-transpimg{
  display: block;
  width: 120px;
  height: 120px;
}
.aa-ply{
  position: absolute;
  right: 35px;
  bottom: 10px;
  width: 28px;
  height: 28px;
  background:  url(../assets/iconall.png) no-repeat scroll 0 -140px;
  display: none;
}
.aa-ply:hover{
  background-position: 0 -170px;
}
.aa-transp:hover .aa-ply{
  display: block;
}
p.aa-name{
  margin: 8px 0 4px 0;
  font-size: 14px;
}
p.aa-name a{
  font-size: inherit;
  color: rgb(0,0,0);
}
p.aa-name a:hover{
  text-decoration: underline;
}
</style>

