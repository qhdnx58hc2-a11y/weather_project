<template>
  <div style="width: 100%; height: 100%; position: relative">
    <div
      style="
        position: absolute;
        top: 18px;
        width: 100%;
        padding: 0 20px;
        box-sizing: border-box;
        z-index: 1000;
      "
    >
      <div style="font-weight: 700; font-size: 18px">灾害统计</div>
    </div>
    <div
      style="
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        height: 100%;
        padding: 0 20px;
      "
    >
      <div ref="barOne" style="width: 100%; height: 75%; margin-top: 34%"></div>
      <div ref="barTwo" style="width: 100%; height: 75%; margin-top: 34%"></div>
      <div
        ref="barThree"
        style="width: 100%; height: 75%; margin-top: 34%"
      ></div>
    </div>
  </div>
</template>

<script>
// 导入 ECharts
import * as echarts from "echarts";

export default {
  name: "ECharts",
  data() {
    return {
      items: [],
      activeType: 1,
      color: [
        { name: "红色", color: "#ff0000" },
        { name: "橙色", color: "#ffa11c" },
        { name: "黄色", color: "#ffd26f" },
        { name: "蓝色", color: "#73C0DE" },
      ],
      chartT1: {
        dom: null,
        data: [
          { value: 15, name: "台风" },
          { value: 26, name: "洪涝" },
          { value: 12, name: "干旱" },
          { value: 9, name: "梅雨" },
        ],
      },
      chartT2: {
        dom: null,
        data: [
          { value: 18, name: "红色" },
          { value: 12, name: "黄色" },
          { value: 28, name: "橙色" },
          { value: 19, name: "蓝色" },
        ],
      },
      chartT3: {
        dom: null,
        data: [
          { value: 26, name: "龙卷风" },
          { value: 18, name: "冰雹" },
          { value: 8, name: "强降雨" },
          { value: 3, name: "雷暴" },
        ],
      },
    };
  },
  mounted() {
    this.list1();
    this.list2();
    this.list3();
  },
  methods: {
    initChartT1() {
      // 基于准备好的dom，初始化echarts实例
      this.chartT1.dom = echarts.init(this.$refs.barOne);
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: "灾害占比",
          left: "center",
          textStyle: {
            color: "#FFF",
            fontSize: "15px",
          },
        },
        legend: {
          orient: "horizontal",
          bottom: "0%",
          left: "8%",
          icon: "diamond",
          itemWidth: 12,
          itemHeight: 12,
          itemGap: 10,
          width: "150rem",
          align: "left",
          textStyle: {
            color: "#fff",
            rich: {
              a: {
                width: 20,
                height: 38,
                padding: [10, 40, 0, 0],
              },
            },
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "灾害占比",
            type: "pie",
            radius: ["30%", "70%"],
            center: ["50%", "42%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: this.chartT1.data,
          },
        ],
      };
      this.chartT1.dom.setOption(option);
    },
    initChartT2() {
      // 基于准备好的dom，初始化echarts实例
      this.chartT2.dom = echarts.init(this.$refs.barTwo);
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: "预警占比",
          left: "center",
          textStyle: {
            color: "#FFF",
            fontSize: "15px",
          },
        },
        legend: {
          orient: "horizontal",
          bottom: "0%",
          left: "0%",
          icon: "diamond",
          itemWidth: 12,
          itemHeight: 12,
          itemGap: 10,
          width: "150rem",
          align: "left",
          textStyle: {
            color: "#fff",
            rich: {
              a: {
                width: 20,
                height: 38,
                padding: [10, 40, 0, 0],
              },
            },
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "预警占比",
            type: "pie",
            radius: ["40%", "70%"],
            center: ["50%", "42%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: this.chartT2.data,
          },
        ],
      };
      this.chartT2.dom.setOption(option);
    },
    initChartT3() {
      // 基于准备好的dom，初始化echarts实例
      this.chartT3.dom = echarts.init(this.$refs.barThree);
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: "异常统计",
          left: "center",
          textStyle: {
            color: "#FFF",
            fontSize: "15px",
          },
        },
        legend: {
          orient: "horizontal",
          bottom: "0%",
          left: "8%",
          icon: "diamond",
          itemWidth: 12,
          itemHeight: 12,
          itemGap: 10,
          width: "150rem",
          align: "left",
          textStyle: {
            color: "#fff",
            rich: {
              a: {
                width: 30,
                height: 38,
                padding: [10, 40, 0, 0],
              },
            },
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "异常统计",
            type: "pie",
            radius: ["40%", "70%"],
            center: ["50%", "42%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: this.chartT3.data,
          },
        ],
      };
      this.chartT3.dom.setOption(option);
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
      this.chartT1.data = result.data.returnData;
      this.initChartT1();
    },
    async list2() {
      let param = {
        type: "chart",
        field: "alarm",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.chartT2.data = result.data.returnData.map((item) => {
        return {
          value: item.value,
          name: item.name,
          itemStyle: {
            color: this.color.find((n) => item.name.includes(n.name)).color,
          },
        };
      });
      console.log(this.chartT2.data);
      this.initChartT2();
    },

    async list3() {
      let param = {
        type: "chart",
        field: "classification",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.chartT3.data = result.data.returnData;
      this.initChartT3();
    },
  },
};
</script>
<style></style>
