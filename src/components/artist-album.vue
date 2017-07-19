<template>
  <div>
    <div v-if="albums">

    </div>
    <div class="loading" v-if="!albums">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>
import { mouseBtnEv } from '../js/generalChangeVal.js'

export default {
  name: 'artistAlbum',
  data () {
    return {
      albums:null
    }
  },
  methods:{

  },
  beforeCreate:function(){
    //请求歌手数据
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

</style>

