<template>
  <div>
    <div v-if="fans">
      <div class="u-title" >
        <h3>粉丝（{{fans.length}}）</h3>
      </div>
      <mode :list="fans"></mode>
    </div>
    <div class="loading" v-if="!fans">
        <i></i>
        加载中...
    </div>  
  </div>
</template>

<script>
import mode from './user-fansfavmode'

export default {
  name: 'fans',
  data () {
    return {
      fans:null,  
    }
  },
  components: {
    mode
  },
  beforeCreate:function(){
    //请求歌单数据
    this.$http.get(`http://123.206.211.77:33333/api/v1/user/${this.$route.params.id}/fans`)
      .then(response => {
         this.fans = response.data.fans;//初始化全部歌单数据
      })
      .catch(response => {
        console.log(response)
    });
  },
}
</script>

<style>

</style>

