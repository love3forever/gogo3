<template>
  <div class="origin">
    <slides></slides>
    <div class="main">
      <mainleft></mainleft>
      <mainright></mainright>
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
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>  
</style>
