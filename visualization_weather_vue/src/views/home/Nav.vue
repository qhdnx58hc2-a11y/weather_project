<template>
  <div>
    <el-aside class="aside" width="300px;">
      <el-menu
        default-active="$route.path"
        exact
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        router
      >
        <el-menu-item v-for="(v, i) in items" :key="i" :index="v.url">
          <i :class="v.icon"></i>
          <span slot="title">{{ v.name }}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCollapse: false,
      role: "",
      items: [
        { name: "可视化", url: "/dashboard", icon: "el-icon-house" },
        { name: "用户管理", url: "/userManage", icon: "el-icon-user" },
        { name: "灾害管理", url: "/contentManage", icon: "el-icon-news" },
        // { name: "灾害统计", url: "/indexManage", icon: "el-icon-news" },
        { name: "灾害分布", url: "/indexManage1", icon: "el-icon-news" },
      ],
    };
  },
  created() {
    this.role = sessionStorage.getItem("role");
    if (this.role === "0") {
      this.items = [
        { name: "可视化", url: "/dashboard", icon: "el-icon-house" },
        { name: "用户管理", url: "/userManage", icon: "el-icon-user" },
        { name: "灾害管理", url: "/contentManage", icon: "el-icon-news" },
        {
          name: "灾害分类",
          url: "/classificationManage",
          icon: "el-icon-news",
        },
        // { name: "灾害统计", url: "/indexManage", icon: "el-icon-news" },
        { name: "灾害分布", url: "/indexManage1", icon: "el-icon-news" },
      ];
    }
    if (this.role === "1") {
      this.items = [
        { name: "可视化", url: "/dashboard", icon: "el-icon-house" },
        { name: "个人中心", url: "/personal", icon: "el-icon-user" },
        // { name: "灾害管理", url: "/contentManage", icon: "el-icon-news" },
        // {
        //   name: "灾害分类",
        //   url: "/classificationManage",
        //   icon: "el-icon-news",
        // },
        // { name: "灾害统计", url: "/indexManage", icon: "el-icon-news" },
        // { name: "灾害分布", url: "/indexManage1", icon: "el-icon-news" },
      ];
    }
  },
  mounted() {},
  methods: {},
};
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 700px;
}

.el-aside {
  color: #333;
  text-align: left;
}
</style>
