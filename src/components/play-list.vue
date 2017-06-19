<template>
  <div class="playlist main">
    <div class="playlist-left">
    </div>
    <div class="playlist-right">
      
    </div>
  </div>
</template>

<script>

export default {
  name: 'playlist',
  data () {
    return {

    }
  },
/*  beforeCreate:function(){
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
  },*/
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
.playlist{
  font-size: 0;
  -webkit-text-size-adjust:none;
  border-right: 1px solid rgb(204,204,204);
}
.playlist-left{
  display: inline-block;
  width: 640px;
  height: 100%;
  padding: 47px 30px 40px 38px;
  border-right: 1px solid rgb(204,204,204);
  vertical-align:top;

}
.playlist-right{
  display: inline-block;
  width: 200px;
  height: 100%;
  padding: 20px 40px 40px 30px;
  vertical-align:top
}
</style>
