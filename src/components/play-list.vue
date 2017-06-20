<template>
  <div class="playlist main">
    <div class="playlist-left">
      <div class="playlist-head">
        <div class="playlist-cover">
          <img src="http://p1.music.126.net/i3uyC0I4mcUnKgXFCnGUOg==/109951162945982389.jpg">
          <span></span>
        </div>
        <div class="playlist-content">
          <div class="content-title">
            <i></i>
            <h2>|华语励志| 用最初的心走最远的路</h2>
          </div>
          <div class="content-author">
            <a href="/#"><img src="http://p1.music.126.net/Rjpe1fUw8cJsW-NSGKpF6w==/109951162864851765.jpg"></a>
            <span><a href="/#" class="author-link">-武姜儿-</a></span>
            <sup></sup>
            <span>2017-05-27&nbsp创建</span>
          </div>
        </div>
      </div>
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
  text-align: left;
}
.playlist-left{
  display: inline-block;
  width: 640px;
  height: 100%;
  padding: 47px 30px 40px 20px;
  border-right: 1px solid rgb(204,204,204);
  vertical-align:top;

}
.playlist-right{
  display: inline-block;
  width: 200px;
  height: 100%;
  padding: 20px 40px 40px 30px;
  vertical-align:top;
}
.playlist-head{
  vertical-align: top;
}
.playlist-cover{
  position: relative;
  display: inline-block;
  width: 200px;
  height: 200px;
  vertical-align:top;
}
.playlist-cover img{
  width: 100%;
  height: 100%;
}
.playlist-cover span{
  position: absolute;
  left: -4px;
  top:-4px;
  width: 208px;
  height: 208px;
  background: url(../assets/coverall.png) no-repeat scroll 0 -1285px;
}
.playlist-content{
  display: inline-block;
  width: 410px;
  height:100px;
  margin-left: 30px;
  vertical-align:top;
}
.content-title{
  vertical-align: top;
  margin-bottom: 12px;
}
.content-title i{
  display: inline-block;
  width: 54px;
  height: 24px;
  margin-right: 10px;
  vertical-align: top;
  background: url(../assets/icon.png) no-repeat scroll 0 -243px;
}
.content-title h2{
  display: inline-block;
  margin: 0;
  font-size: 20px;
  line-height: 24px;
  font-weight: normal;
  color: rgb(51,51,51);
  vertical-align: top;
}
.content-author{
  height: 35px;
  margin-bottom: 20px;
  vertical-align: middle;
  font-size: 12px;
  color: rgb(153,153,153);
}
.content-author img{
  vertical-align: middle;
  width: 35px;
  height: 35px;
}
.content-author sup{
  display: inline-block;
  width:12px; 
  height:13px;
  margin: -4px 15px 0 0;
  vertical-align: middle;
  background: url(../assets/icon.png) no-repeat scroll -65px -840px;
}
.author-link{
  color: #0c73c2;
  margin-left: 10px;
}
.author-link:hover{
  text-decoration: underline;
}
</style>
