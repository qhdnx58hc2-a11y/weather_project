<template>
  <div class="content bg">
    <dv-full-screen-container>
      <el-button
        class="back_btn"
        icon="el-icon-arrow-left"
        @click="$router.push({ path: '/home' })"
        >返回</el-button
      >
      <ModuleTitle />
      <ModuleMain />
      <!-- <ModuleHeader /> -->
    </dv-full-screen-container>
  </div>
</template>

<script>
import ModuleTitle from "./ModuleTitle.vue";
import ModuleHeader from "./ModuleHeader.vue";
import ModuleMain from "./ModuleMain.vue";

export default {
  name: "HomeView",
  components: {
    ModuleTitle,
    ModuleHeader,
    ModuleMain,
  },
};
</script>

<style>
/* 主体 */
.content {
  color: #fff;
  background: #000;
  width: 100%;
  height: 100vh;
}
.bg {
  background: url("../assets/img/pageBg.png") no-repeat center center;
  background-size: cover;
}
.back_btn {
  position: absolute;
  top: 36px;
  left: 20px;
  z-index: 9999;
  color: #fff;
  background-color: transparent;
  border: none;
}
</style>
