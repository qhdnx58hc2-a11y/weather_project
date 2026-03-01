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
        [3.275154, 2.957587],
        [-3.344465, 2.603513],
        [0.355083, -3.376585],
        [1.852435, 3.547351],
        [-2.078973, 2.552013],
        [-0.993756, -0.884433],
        [2.682252, 4.007573],
        [-3.087776, 2.878713],
        [-1.565978, -1.256985],
        [2.441611, 0.444826],
        [-0.659487, 3.111284],
        [-0.459601, -2.618005],
        [2.17768, 2.387793],
        [-2.920969, 2.917485],
        [-0.028814, -4.168078],
        [3.625746, 2.119041],
        [-3.912363, 1.325108],
        [-0.551694, -2.814223],
      ],
    };
  },
  created() {
    this.list();
  },
  mounted() {
    this.list();
    //基于准备好的dom，初始化echarts实例
    console.log("[mounted week] " + this.week);

    //https://echarts.apache.org/examples/en/editor.html?c=bar-label-rotation
  },
  methods: {
    initChart1() {
      console.log("[initChart1]" + this.scenicText);
      const dom = this.$refs.chart;
      console.log("dom " + dom);
      if (!dom) {
        return;
      }
      var myChart1 = echarts.init(dom);
      echarts.registerTransform(ecStat.transform.clustering);
      const data = this.data;
      var CLUSTER_COUNT = 6;
      var DIENSIION_CLUSTER_INDEX = 2;
      var COLOR_ALL = [
        "#37A2DA",
        "#e06343",
        "#37a354",
        "#b55dba",
        "#b5bd48",
        "#8378EA",
        "#96BFFF",
      ];
      var pieces = [];
      for (var i = 0; i < CLUSTER_COUNT; i++) {
        pieces.push({
          value: i,
          label: "灾害 " + i,
          color: COLOR_ALL[i],
        });
      }
      myChart1.setOption({
        dataset: [
          {
            source: data,
          },
          {
            transform: {
              type: "ecStat:clustering",
              // print: true,
              config: {
                clusterCount: CLUSTER_COUNT,
                outputType: "single",
                outputClusterIndexDimension: DIENSIION_CLUSTER_INDEX,
              },
            },
          },
        ],
        tooltip: {
          position: "top",
        },
        visualMap: {
          type: "piecewise",
          top: "middle",
          min: 0,
          max: CLUSTER_COUNT,
          left: 10,
          splitNumber: CLUSTER_COUNT,
          dimension: DIENSIION_CLUSTER_INDEX,
          pieces: pieces,
        },
        grid: {
          left: 120,
        },
        xAxis: {},
        yAxis: {},
        series: {
          type: "scatter",
          encode: { tooltip: [0, 1] },
          symbolSize: 15,
          itemStyle: {
            borderColor: "#555",
          },
          datasetIndex: 1,
        },
      });
    },
    async list() {
      this.initChart1();
    },
    async list1() {
      console.log("[statistic]borrow " + this.borrow);
      let param = {};
      const result = await this.$http.post("/rest/statistic/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.content = result.data.returnData.content;
      this.cart = result.data.returnData.cart;
      this.user = result.data.returnData.user;
      this.coach = result.data.returnData.coach;
      this.contentText = result.data.returnData.contentText;
      this.userText = result.data.returnData.userText;
      this.contentData = result.data.returnData.contentData;
      this.scenicText = result.data.returnData.scenicText;
      this.scenicData = result.data.returnData.scenicData;
      this.userData = result.data.returnData.userData;
      this.rateList = result.data.returnData.rateList;
      this.contentText1 = result.data.returnData.contentText1;
      this.contentData1 = result.data.returnData.contentData1;
      this.data = result.data.returnData.data;
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