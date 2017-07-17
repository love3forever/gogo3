<template>
  <div>
     <div v-if="fav">
      <div class="u-title">
        <h3>关注（{{fav.length}}）</h3>
      </div>
      <mode :list="fav"></mode>
    </div>
    <div class="loading" v-if="!fav">
      <i></i>
      加载中...
    </div>  
  </div>
</template>

<script>
import mode from './user-fansfavmode'

export default {
  name: 'fav',
  data () {
    return {
      fav:null,  
    }
  },
  components: {
    mode
  },
  beforeCreate:function(){
    //请求歌单数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/user/${this.$route.params.id}/follows`)
      .then(response => {
         this.fav = response.data.follows;//初始化全部歌单数据
         console.log(this.fav)
      })
      .catch(response => {
        console.log(response)
    });
  },
}
</script>

<style>

</style>
