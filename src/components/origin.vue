<template>
  <div class="origin">
    <slides></slides>
    <div class="main" v-if="leftData&&rightData">
      <mainleft :leftData="leftData"></mainleft>
      <mainright :rightData="rightData"></mainright>
    </div>
  </div>
</template>

<script>
import slides from './slides'
import mainleft from './mainleft'
import mainright from './mainright'

export default {
  name: 'foot',
  data () {
    return {
      leftData:null,
      rightData:null,
    }
  },
  components:{
    slides,mainleft,mainright
  },
  beforeCreate:function(){
      this.$http.get('http://123.206.211.77:33333/api/v1/index/direct')
      .then(response => {
        console.log('数据get');
        let { blk, hotdj,newAlbum,newSinger,recommendList } = response.data;
        this.rightData = {newSinger,hotdj};
        this.leftData = {blk,newAlbum,recommendList};
      })
      .catch(response => {
        console.log(response)
      });
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
</style>
