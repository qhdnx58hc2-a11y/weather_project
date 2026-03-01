<template>
  <div>
    <br />
    <el-row>
      <el-col :span="24">
        <div ref="chart" style="height: 600px"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import * as echarts from "echarts";
import * as ecStat from "echarts-stat";
export default {
  data() {
    return {
      content: 567,
      cart: 345,
      coach: 987,
      user: 634,
      contentText: [],
      contentData: [],
      scenicText: [],
      scenicData: [],
      contentText1: [],
      contentData1: [],
      userText: [],
      userCountData: [],
      rateList: [],
      data: [
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
    this.list1();
    //基于准备好的dom，初始化echarts实例
    // console.log("[mounted week] ", this.week);

    //https://echarts.apache.org/examples/en/editor.html?c=bar-label-rotation
  },
  methods: {
    initChart1() {
      // console.log("[initChart1]", this.scenicText);
      const dom = this.$refs.chart;
      // console.log("dom ", dom);
      if (!dom) {
        return;
      }
      var myChart1 = echarts.init(dom);
      myChart1.setOption({
        legend: {
          top: "bottom",
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        series: [
          {
            name: "Nightingale Chart",
            type: "pie",
            radius: [50, 250],
            center: ["50%", "50%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: this.data,
          },
        ],
      });
    },
    async list() {
      this.initChart1();
    },
    async list1() {
      let param = {
        type: "chart",
        field: "classification",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.data = result.data.returnData;
      this.initChart1();
    },
  },
};
</script>
<style>
.data-view {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
</style>
