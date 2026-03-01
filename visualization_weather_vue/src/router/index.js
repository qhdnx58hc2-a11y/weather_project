/*
 * @Description:
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-27 13:40:21
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 14:19:50
 */
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export const constantRoutes = [
  // {
  //   path: '/contentList3',
  //   component: () => import('@/views/dashboard/index'),
  // },
  // {
  //   path: '/dashboard',
  //   component: () => import('@/views/dashboard/index'),
  // },
  {
    path: "/dashboard",
    component: () => import("@/views/HomeView.vue"),
  },
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/login/index.vue"),
    meta: { title: "登录", keepAlive: false },
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/register/index.vue"),
    meta: { title: "注册", keepAlive: false },
  },
  /* {
    path: "/forget",
    name: "forget",
    component: () => import("@/views/forget/index.vue"),
    meta: { title: "注册", keepAlive: false },
  }, */
  {
    path: "/home",
    name: "home",
    component: () => import("@/views/home/index.vue"),
    meta: { title: "首页", keepAlive: false },
    children: [
      {
        path: "/personal",
        name: "personal",
        meta: { title: "个人中心", keepAlive: false },
        component: () => import("@/views/home/personal/index.vue"),
      },
      {
        path: "/indexManage",
        name: "indexManage",
        meta: { title: "灾害统计", keepAlive: false },
        component: () => import("@/views/home/indexManage/index.vue"),
      },
      {
        path: "/indexManage1",
        name: "indexManage1",
        meta: { title: "灾害分布", keepAlive: false },
        component: () => import("@/views/home/indexManage1/index.vue"),
      },
      {
        path: "/contentManage",
        name: "contentManage",
        meta: { title: "灾害管理", keepAlive: false },
        component: () => import("@/views/home/contentManage/index.vue"),
      },
      {
        path: "/classificationManage",
        name: "classificationManage",
        meta: { title: "灾害分类", keepAlive: false },
        component: () => import("@/views/home/classificationManage/index.vue"),
      },
      {
        path: "/userManage",
        name: "userManage",
        meta: { title: "用户管理", keepAlive: false },
        component: () => import("@/views/home/userManage/index.vue"),
      },
    ],
  },
];

const createRouter = () =>
  new Router({
    mode: "history",
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes,
  });

const router = createRouter();

export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher;
}

export default router;

