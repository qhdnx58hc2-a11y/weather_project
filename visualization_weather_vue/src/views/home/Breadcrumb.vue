<template>
  <div id="breadcrumb">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item v-for="(list, i) in lists" :key="i">
        <span>{{ list.meta.title }}</span>
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lists: [],
    };
  },
  created() {
    this.lists = this.$route.matched;
  },
  watch: {
    $route(to, from) {
      // console.log("from:", from);
      this.lists = to.matched;
    },
  },
  methods: {},
};
</script>
