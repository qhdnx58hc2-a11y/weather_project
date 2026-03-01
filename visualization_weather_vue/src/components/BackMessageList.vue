<script>
export default {
  name: "ECharts",
  data() {
    return {
      page: {
        currentPage: 1,
        pageSize: 10,
        total: 7634,
      },
      // 排名轮播表
      scrollBoardConfig: {
        header: ["发生时间", "异常天气", "发生地点"],
        data: [],
        index: false,
        columnWidth: [100, 140],
        align: ["center"],
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
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      // console.log(result.data.returnData.data);
      this.setConfig(result.data.returnData.data);
    },
    setConfig(data) {
      this.scrollBoardConfig = {
        header: ["发生时间", "异常天气", "发生地点"],
        data: data,
        /* [
          ["2024-07-05 19:30", "冰雹（直径4cm）砸毁果园", "丰县"],
          ["2024-08-14 02:50", "雷暴大风（阵风13级）掀翻工厂顶棚", "沛县"],
          ["2024-06-28 15:40", "EF2级龙卷风致民房倒塌", "新沂市"],
          ["2024-07-21 22:45", "暴雨（24小时210mm）引发山洪", "邳州市"],
          ["2024-08-07 05:20", "短时强降水（1小时150mm）淹没村庄", "睢宁县"],
          ["2024-09-11 16:10", '台风"梅花"登陆伴16级风', "赣榆区"],
          ["2024-07-18 11:30", "龙卷风EF1级致电线杆断裂", "东海县"],
          ["2024-08-27 02:00", "暴雨引发海堤决口", "灌云县"],
          ["2024-06-25 20:30", "雷暴大风（阵风12级）掀翻渔船", "灌南县"],
          ["2024-07-17 17:50", "冰雹（直径3cm）砸坏车辆", "沭阳县"],
        ], */
        index: false,
        columnWidth: [100, 140],
        align: ["center"],
        headerBGC: "#3490BA", //表头背景色
      };
    },
  },
};
</script>
<template>
  <dv-border-box-12 style="width: 100%; height: 100%">
    <div style="width: 100%; height: 100%; position: relative">
      <div
        style="
          position: absolute;
          top: 20px;
          left: 20px;
          font-weight: 700;
          font-size: 18px;
        "
      >
        异常天气
      </div>
      <dv-scroll-board
        :config="scrollBoardConfig"
        style="
          width: 90%;
          height: 74%;
          position: absolute;
          top: 50px;
          left: 50%;
          transform: translateX(-50%);
        "
      />
      <!-- <dv-scroll-ranking-board :config="scrollConfig"
                style=" width: 88%; height: 75%;position: absolute; top: 50px; left: 50%;transform: translateX(-50%);" /> -->
    </div>
  </dv-border-box-12>
</template>
