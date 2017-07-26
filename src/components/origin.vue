<template>
  <div class="origin">
    <slides></slides>
    <div class="main">
      <div v-show="leftData&&rightData">
        <mainleft :leftData="leftData"></mainleft>
        <mainright :rightData="rightData"></mainright>
      </div>
      <div class="loading" v-show="!(leftData&&rightData)">
        <i></i>
        加载中...
      </div> 
    </div>
  </div>
</template>

<script>
import slides from './slides'
import mainleft from './mainleft'
import mainright from './mainright'

export default {
  name: 'foot',
  components:{
    slides,mainleft,mainright
  },
  data () {
    return {
      result:null
    }
  },
  methods:{
    substractId:function(obj,attr){
      for (let value of obj){
        let index = value[attr].lastIndexOf('=');
        if (index!== -1){
          value[attr] =  value[attr].substring(index+1);
        } else {
          value[attr] = null;
        };
      }
    }
  },
  beforeCreate:function(){
    document.title = `网易云音乐`;
    
    this.$http.get('http://123.206.211.77:33333/api/v1/index/detail')
      .then(response => {
        this.result = response.data;
      })
      .catch(response => {
        console.log(response)
    });
  },
  computed:{
    leftData:function(){
      if (this.result){
        let { blk, newAlbum, recommendList } = this.result;
        //数据(id)格式化
        for (let item of blk){
          this.substractId(item.songs,'songHref');
        }
        this.substractId(newAlbum,'artistHref');
        this.substractId(newAlbum,'href');

        return {blk, newAlbum, recommendList};
      } else {
        return null
      };
    },
    rightData:function(){
      if (this.result){
        let { hotdj, newSinger} = this.result;
        //数据(id)格式化
        this.substractId(newSinger,'href');
        this.substractId(hotdj,'href');
        
        return { hotdj, newSinger };
      } else {
        return null
      };
    }
  }
}
</script>

<style>  
</style>
