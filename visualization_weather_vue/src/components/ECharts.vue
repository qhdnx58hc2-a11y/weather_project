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
      灾害统计
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
      labels: ["台风", "洪涝", "干旱", "寒潮", "梅雨", "龙卷风", "泥石流"],
      items: [143, 134, 108, 199, 149, 147, 123], // 存储后端返回的动态数据
    };
  },
  mounted() {
    // this.initWebsocket()
    // this.initChart();
    this.list();
  },
  methods: {
    // 初始化图表
    initChart() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(this.$refs.charts);
      // 指定图表的配置项和数据
      var option = {
        color: "#fbc321",
        xAxis: {
          data: this.labels,
          axisLine: {
            lineStyle: {
              color: "#fff",
            },
          },
          axisLabel: {
            interval: 0,
          },
        },
        yAxis: {
          axisLine: {
            lineStyle: {
              color: "#fff",
            },
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dotted",
              color: "rgba(255, 255, 255,0.3)",
            },
          },
        },
        grid: {
          top: 65,
          right: 40,
          bottom: 40,
          left: 40,
        },
        series: [
          {
            type: "bar",
            data: this.items,
            barWidth: "20%",
            label: {
              show: true,
              position: "outside",
            },
            itemStyle: {
              borderRadius: [10, 10, 0, 0],
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "#38D458" },
                { offset: 1, color: "#22AB42" },
              ]),
            },
          },
        ],
        // // 配置图标在容器中的位置
        // grid: {
        //   top: '10%',
        //   left: '5%',
        //   right: '5%',
        //   bottom: '5%',
        //   containLabel: true // 此属性设置为 true 才会有效果
        // }
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
      const list = result.data.returnData;
      this.labels = list.map((item) => {
        return item.name;
      });
      this.items = list.map((item) => {
        return item.value;
      });
      this.initChart();
    },
    // // websocket获取实时数据
    // initWebsocket() {
    //   const ws = new WebSocket('ws://127.0.0.1:8090')
    //   // 接收消息触发
    //   ws.onmessage = (data) => {
    //     // 注意1：data.data里面的存储的数据是 字符串 形式的，需要转化为对象
    //     let msg = JSON.parse(data.data)
    //     this.items = msg.message
    //     // 注意2：此时的初始化方法就不要放在生命周期里面了，异步会使得先初始化数据，在发送websocket请求
    //     // this.initChart()
    //   }
    // }
    // items = [1343, 934, 908, 799, 649, 647]
  },
};
</script>
