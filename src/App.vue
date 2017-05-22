<template>
  <div id="app">
    <topbar></topbar>
  </div>
</template>

<script>
import topbar from './components/topbar'

export default {
  name: 'app',
  components: {
    topbar
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
  background-image: url(assets/topbar.png);
  background-repeat: none;
  background-attachment:fixed;
  background-position: 0px -80px;
  height: 70px;
}
</style>
