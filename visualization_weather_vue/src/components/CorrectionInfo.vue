<script>
// import * as echarts from 'echarts'
export default {
  name: "ECharts",
  data() {
    return {
      page: {
        currentPage: 1,
        pageSize: 10,
        total: 7634,
      },
      active: 0,
      typeTable: [
        {
          name: "气象灾害",
          header: ["时间", "地点", "灾害", "分类", "预警"],
          data: [],
        },
        /* {
          name: "异常天气",
          header: ["时间", "地点", "灾害", "受灾", "详情"],
          data: [],
        }, */
      ],
      // 排名轮播表
      scrollBoardConfig: {
        header: ["时间", "地点", "灾害", "分类", "预警"],
        data: [],
        index: false,
        columnWidth: [160, 90, 200, 120, 120],
        align: ["left", "left"],
        headerBGC: "#3490BA", //表头背景色
      },
    };
  },
  mounted() {
    this.initChart();
  },
  methods: {
    async initChart() {
      let param = {
        currentPage: this.page.currentPage,
        pageSize: this.page.pageSize,
      };
      // 气象灾害
      let result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      // console.log(result.data.returnData.data1);
      this.typeTable[0].data = result.data.returnData.data1;

      // 异常天气
      /* result = await this.$http.post("/rest/content/list", {
        currentPage: 2,
        pageSize: this.page.pageSize,
      });
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.typeTable[1].data = result.data.returnData.data1; */

      this.setConfig();
    },
    activeChange(key) {
      this.active = key;
      this.setConfig();
    },
    setConfig() {
      this.scrollBoardConfig = {
        header: this.typeTable[this.active].header,
        data: this.typeTable[this.active].data,
        /* data: [
          [
            "2024-07-05 19:30",
            "丰县",
            "冰雹（直径4cm）砸毁果园",
            "强对流天气",
            "橙色预警  ",
          ],
          [
            "2024-08-14 02:50",
            "沛县",
            "雷暴大风（阵风13级）掀翻工厂顶棚",
            "强对流天气",
            "红色预警  ",
          ],
          [
            "2024-06-28 15:40",
            "新沂市",
            "EF2级龙卷风致民房倒塌",
            "强对流天气",
            "红色预警  ",
          ],
          [
            "2024-07-21 22:45",
            "邳州市",
            "暴雨（24小时210mm）引发山洪",
            "暴雨洪涝",
            "红色预警  ",
          ],
          [
            "2024-08-07 05:20",
            "睢宁县",
            "短时强降水（1小时150mm）淹没村庄",
            "暴雨洪涝",
            "红色预警",
          ],
        ], */
        index: false,
        columnWidth: [150, 140, 200, 120, 120],
        align: ["left", "left"],
        headerBGC: "#3490BA", //表头背景色
      };
    },
  },
};
</script>
<template>
  <dv-border-box-11 style="width: 100%; height: 100%">
    <div style="width: 100%; height: 100%; position: relative">
      <div
        style="
          position: absolute;
          top: 18px;
          left: 50%;
          font-weight: 700;
          font-size: 18px;
          transform: translateX(-50%);
        "
      >
        灾害信息
      </div>
      <div style="padding: 40px 0 0 24px; display: flex; font-size: 15px">
        <div
          v-for="(item, index) in typeTable"
          :key="index"
          :class="{ active: active === index }"
          style="margin-right: 15px; cursor: pointer"
          @click="activeChange(index)"
        >
          {{ item.name }}
        </div>
      </div>
      <dv-scroll-board
        :config="scrollBoardConfig"
        style="
          width: 95%;
          height: 65%;
          position: absolute;
          top: 70px;
          left: 50%;
          transform: translateX(-50%);
        "
      />
    </div>
  </dv-border-box-11>
</template>
<style scoped>
.active {
  border-bottom: 2px solid #3490ba;
}
</style>
