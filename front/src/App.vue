<template>
  <div class="container">
    <search />
  </div>
</template>

<script>
import Search from "./components/Search.vue";

export default {
  name: "App",
  components: {
    Search,
  },
};
</script>

<style>
*,
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

html,
body {
  margin: 0px;
  padding: 0px;
}

#app {
  background-color: #3d5209;
  height: 100vh;
}

.button.is-primary {
  background-color: #3a5101;
}

.button.is-primary:hover {
  background-color: #968408;
}
</style>
