<script>
import * as echarts from "echarts";
export default {
  name: "ECharts",
  data() {
    return {
      items: [
        { value: 142, name: "台风" },
        { value: 135, name: "洪涝" },
        { value: 146, name: "干旱" },
        { value: 234, name: "寒潮" },
        { value: 235, name: "梅雨" },
        { value: 246, name: "龙卷风" },
        { value: 123, name: "泥石流" },
      ],
    };
  },
  mounted() {
    this.list();
  },
  methods: {
    initChart() {
      var myChart = echarts.init(this.$refs.IndustryProportionRef);
      var option = {
        legend: {
          top: "center",
          right: "right",
          padding: [0, 60, 0, 10],
          textStyle: {
            color: "#FFF",
          },
        },
        series: [
          {
            label: {
              show: true,
              position: "center",
            },
            labelLine: {
              show: true,
            },
            type: "pie",
            radius: [30, 90],
            center: ["38%", "55%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: this.items,
          },
        ],
      };
      myChart.setOption(option);
    },
    async list() {
      let param = {
        type: "chart",
        field: "classification",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.items = result.data.returnData;
      this.initChart();
    },
  },
};
</script>
<template>
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
      灾害分类
    </div>
    <div ref="IndustryProportionRef" style="width: 100%; height: 100%"></div>
  </div>
</template>
