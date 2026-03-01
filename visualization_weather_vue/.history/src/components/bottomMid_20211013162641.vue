<!--
 * @Description: 
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-17 09:52:45
 * @LastEditors: LMJ
 * @LastEditTime: 2021-10-13 16:26:41
-->
<template>
  <div id="mains">
    <div class="grid" v-for="(item, index) in datas" :key="index">
      <dv-border-box-13 :reverse="true">
        <span>{{ item.title }}</span>
        <span>
          <count-to
            :start-val="0"
            :end-val="item.data"
            :duration="5000"
            class="fontG" /></span
      ></dv-border-box-13>
    </div>
  </div>
</template>

<script>
import CountTo from "vue-count-to";
export default {
  components: { CountTo },
  data() {
    return {
      datas: [
        { title: "抖音数据", data: 11211 },
        { title: "暂无数据", data: 120 },
        { title: "暂无数据", data: 520 },
        { title: "暂无数据", data: 142 },
      ],
    };
  },
  created() {},
  mounted() {},
  methods: {},
};
</script>

<style scoped lang="scss">
#mains {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  .grid {
    width: 95%;
    height: 25%;
    text-align: center;
    color: #06f1ef;
    ::v-deep.border-box-content {
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-evenly !important;
    }
  }
}
</style>
