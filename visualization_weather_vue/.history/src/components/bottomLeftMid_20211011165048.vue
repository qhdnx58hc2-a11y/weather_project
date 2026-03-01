<!--
 * @Description: 
 * @Description: 
 * @Version: 2.0
 * @Autor: LMJ
 * @Date: 2021-09-10 11:04:58
 * @LastEditors: LMJ
 * @LastEditTime: 2021-09-27 14:56:28
-->
<template>
  <div id="mains">
    <div class="title">
      <dv-decoration-3 :reverse="true" style="width: 100px; height: 30px" />短视频传播趋势<dv-decoration-3
        style="width: 100px; height: 30px" />
    </div>
    <div class="content">
      <div class="grid" v-for="(item, index) in datas" :key="index">
        <dv-border-box-8>
          <span>{{ item.title }}</span>
          <span>
            <count-to :start-val="0" :end-val="item.data" :duration="2000" class="fontG" /></span>
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
      page: {
        currentPage: 1,
        pageSize: 10,
        total: 5,
      },
      datas: [
        { title: "暂无数据", data: 108 },
        { title: "暂无数据", data: 410 },
        { title: "暂无数据", data: 143 },
        { title: "暂无数据", data: 2300 },
        { title: "暂无数据", data: 200 },
        { title: "暂无数据", data: 1340 },
        { title: "暂无数据", data: 240 },
        { title: "暂无数据", data: 0 },
        { title: "暂无数据", data: 0 },
      ],
    };
  },
  created() { },
  mounted() {
    this.list();
  },
  methods: {
    async list() {
      let param = {
        currentPage: this.page.currentPage,
        pageSize: 9,
      };
      const result = await this.$http.post("/rest/douyin/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.datas = result.data.returnData.dataList;
    },
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
