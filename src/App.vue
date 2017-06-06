<template>
  <div id="app">
    <topbar></topbar>
    <slides></slides>
    <div class="main">
      <mainleft></mainleft>
      <mainright></mainright>
    </div>
  </div>
</template>

<script>
import topbar from './components/topbar'
import slides from './components/slides'
import mainleft from './components/mainleft'
import mainright from './components/mainright'

export default {
  name: 'app',
  components: {
    topbar,slides,mainleft,mainright
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  //color: #2c3e50;
  color: rgb(102,102,102);
  background: rgb(245,245,245);
}
.main{
  position: relative;
  width: 980px;
  height: 1000px;
  margin: 0 auto;
  border-left: 1px solid rgb(204,204,204);
  background: white;
}
</style>
