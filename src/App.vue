<template>
  <div id="app">
    <topbar></topbar>
    <slides></slides>
  </div>
</template>

<script>
import topbar from './components/topbar'
import slides from './components/slides'

export default {
  name: 'app',
  components: {
    topbar,slides
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
}
</style>
