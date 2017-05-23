<template>
  <div id="app">
    <topbar></topbar>
    <bottombar></bottombar>
  </div>
</template>

<script>
import topbar from './components/topbar'
import bottombar from './components/bottombar'

export default {
  name: 'app',
  components: {
    topbar,bottombar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: url(assets/topbar.png) repeat-x fixed 0px -80px;
  height: 70px;
}
</style>
