<template>
  <div style="width: 100%; height: 100%; position: relative">
    <div
      style="
        display: flex;
        justify-content: space-between;
        position: absolute;
        top: 18px;
        width: 100%;
        padding: 0 20px;
        box-sizing: border-box;
        z-index: 1000;
      "
    >
      <div style="font-weight: 700; font-size: 18px">气象预警</div>
      <div style="display: flex">
        <div
          v-for="(item, index) in type"
          :key="index"
          class="type_btn"
          :class="{
            'mr-8': index < 3,
            activeType: activeType == index,
          }"
          @click="typeChange(index)"
        >
          {{ item.name }}
        </div>
      </div>
    </div>
    <div ref="charts" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
// 导入 ECharts
import * as echarts from "echarts";

export default {
  name: "ECharts",
  data() {
    return {
      activeType: 0,
      myChart: null,
      data: [],
      labels: ["暴雨", "台风", "暴雪", "寒潮", "大风"],
      items: [7892, 9985, 10080, 8624, 9936],
      type: [
        { name: "红色", color: ["#DB737F", "#ff0000"] },
        { name: "橙色", color: ["#e16e26", "#ffa11c"] },
        { name: "黄色", color: ["#d3a94c", "#ffd26f"] },
        { name: "蓝色", color: ["#4E68B9", "#73C0DE"] },
      ],
    };
  },
  mounted() {
    this.list();
  },
  methods: {
    typeChange(type) {
      this.activeType = type;
      if (this.data.length) {
        const list = this.data.filter((item) => {
          return item.alarm.includes(this.type[type].name);
        });

        this.labels = list.map((item) => {
          return item.name;
        });
        this.items = list.map((item) => {
          return item.value;
        });
        console.log(list);
      }
      console.log(this.data);
      console.log(this.labels);
      console.log(this.items);
      this.setChartOption();
    },
    // 初始化图表
    initChart() {
      // 基于准备好的dom，初始化echarts实例
      this.myChart = echarts.init(this.$refs.charts);
      // 指定图表的配置项和数据

      this.typeChange(this.activeType);
    },
    setChartOption() {
      this.myChart &&
        this.myChart.setOption({
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "shadow",
            },
          },
          grid: {
            top: 65,
            right: 40,
            bottom: 40,
            left: 90,
          },
          xAxis: {
            type: "value",
            boundaryGap: [0, 0.01],
            splitLine: {
              show: true,
              lineStyle: {
                type: "dotted",
                color: "rgba(255, 255, 255,0.3)",
              },
            },
          },
          yAxis: {
            type: "category",
            data: this.labels,
            axisLabel: {
              textStyle: {
                color: "rgba(219,225,255,1)",
                margin: 15,
              },
            },
            splitNumber: 5,
          },
          series: [
            {
              name: "2011",
              type: "bar",
              data: this.items,
              barWidth: "30%",
              label: {
                show: true,
                position: "outside",
              },
              itemStyle: {
                borderRadius: [0, 10, 10, 0],
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: this.type[this.activeType].color[0] },
                  { offset: 1, color: this.type[this.activeType].color[1] },
                ]),
              },
            },
          ],
        });
    },
    async list() {
      let param = {
        type: "chartAlarm",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.data = result.data.returnData;
      this.initChart();
    },
  },
};
</script>
<style>
.mr-8 {
  margin-right: 8px;
}
.type_btn {
  padding: 3px 8px;
  background-color: #a2a2a2;
  color: #dcdcdc;
  border-radius: 3px;
  cursor: pointer;
}
.activeType {
  background-color: azure;
  color: #333;
}
</style>
