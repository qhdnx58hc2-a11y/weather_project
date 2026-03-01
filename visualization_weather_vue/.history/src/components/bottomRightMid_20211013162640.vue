<!--
 * @Description: 
 * @Description: 
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-10 11:04:58
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 14:56:48
-->
<template>
  <div id="mains">
    <div class="title">
      <dv-decoration-3
        :reverse="true"
        style="width: 100px; height: 30px"
      />每日事件上报统计<dv-decoration-3 style="width: 100px; height: 30px" />
    </div>
    <div class="content">
      <div class="grid" v-for="(item, index) in datas" :key="index">
        <dv-border-box-8>
          <span>{{ item.title }}</span>
          <span>
            <count-to
              :start-val="0"
              :end-val="item.data"
              :duration="5000"
              class="fontG"
          /></span>
        </dv-border-box-8>
      </div>
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
        { title: "抖音数据", data: 320 },
        { title: "暂无数据", data: 230 },
        { title: "暂无数据", data: 540 },
        { title: "暂无数据", data: 130 },
        { title: "0-500", data: 102 },
        { title: "500-1000", data: 234 },
        { title: "1000-2000", data: 1340 },
        { title: "2000-3000", data: 534 },
        { title: ">3000", data: 34 },
      ],
    };
  },
  created() {},
  mounted() {
    this.init();
  },
  methods: {
    init() {},
  },
};
</script>

<style scoped lang="scss">
#mains {
  width: 100%;
  height: 100%;
  .title {
    color: #06f1ef;
    font-weight: bold;
    text-align: center;
    line-height: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 100%;
    white-space: nowrap;
  }
  .content {
    height: 90%;
    width: 100%;
    display: grid;
    grid-template-columns: 32.3% 32.3% 32.3%;
    grid-template-rows: 32% 32% 32%;
    margin: auto;
    grid-gap: 5px;
    .grid {
      text-align: center;
      color: #06f1ef;
      ::v-deep.border-box-content {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-evenly !important;
      }
    }
  }
}
</style>
