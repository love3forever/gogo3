<template>
  <div id="app">
    <topbar></topbar>
    <slides></slides>
    <div class="main">
      <mainleft></mainleft>
      <mainright></mainright>
    </div>
    <foot></foot>
  </div>
</template>

<script>
import topbar from './components/topbar'
import slides from './components/slides'
import mainleft from './components/mainleft'
import mainright from './components/mainright'
import foot from './components/foot'
export default {
  name: 'app',
  components: {
    topbar,slides,mainleft,mainright,foot
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(102,102,102);
  background: rgb(245,245,245);
}
.main{
  position: relative;
  width: 980px;
  margin: 0 auto;
  border-left: 1px solid rgb(204,204,204);
  background: white;
}
a{
  text-decoration: none;
  color: rgb(102,102,102);
  font-size: 12px;
}
</style>
