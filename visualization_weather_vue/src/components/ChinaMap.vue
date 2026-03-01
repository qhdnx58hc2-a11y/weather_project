<template>
  <dv-border-box-8 :reverse="true" style="width: 100%; height: 100%">
    <!-- 初始化ECharts容器，ref属性用于获取标签 -->
    <div ref="charts" style="width: 100%; height: 100%"></div>
  </dv-border-box-8>
</template>

<script>
// 导入 ECharts
import * as echarts from "echarts";
// 导入中国地图的 json 数据
import zhejiangJson from "@/assets/json/jiangsu.json";

export default {
  name: "ECharts",
  data() {
    return {
      items: [],
      color: [
        { name: "红色", color: "#ff0000" },
        { name: "橙色", color: "#ffa11c" },
        { name: "黄色", color: "#ffd26f" },
        { name: "蓝色", color: "#73C0DE" },
      ],
    };
  },
  mounted() {
    this.list();
  },
  methods: {
    initChart() {
      echarts.registerMap("zhejiang", zhejiangJson);
      const myChart = echarts.init(this.$refs.charts);
      const option = {
        // 提示浮窗样式
        tooltip: {
          show: true,
          trigger: "item",
          alwaysShowContent: false,
          backgroundColor: "#0C121C",
          borderColor: "rgba(255, 255, 255, 0.16);",
          hideDelay: 100,
          triggerOn: "mousemove",
          enterable: true,
          textStyle: {
            color: "#DADADA",
          },
          showDelay: 100,
          formatter: (params) => {
            // console.log(params);
            const obj = params.data.item;
            let s = params.name + "<br>";
            this.color.forEach((n) => {
              s +=
                '<span style="color:' +
                n.color +
                ';">' +
                n.name +
                ": " +
                obj[n.name] +
                "</span><br>";
            });
            return s;
          },
        },

        geo: {
          map: "zhejiang",
          label: {
            show: true, // 显示省份标签
            color: "#FFF", // 标签字体颜色
            fontSize: 12, // 标签字体大小
            formatter: (params) => {
              return params.name;
            },
          },
          roam: true,
          itemStyle: {},
        },
        itemStyle: {
          // areaColor: "red",
          borderWidth: 0.5,
        },
        // 设置鼠标移上去高亮的样式
        emphasis: {
          itemStyle: {
            borderColor: "#34AEAE",
            areaColor: "#CCEBEB",
            borderType: "solid",
            color: "#fff",
          },
        },
        series: [
          {
            type: "effectScatter",
            coordinateSystem: "geo",
            // 涟漪特效相关配置
            rippleEffect: {
              number: 3,
              period: 4,
              brushType: "stroke",
              scale: 5,
              color: "#FFF",
            },
            data: this.items,
          },
          {
            type: "map",
            map: "zhejiang",
            roam: true,
            label: {
              show: true, // 显示省份标签
              color: "#FFF", // 标签字体颜色
            },
            data: this.items,
          },
        ],
      };
      myChart.setOption(option);
    },
    async list() {
      let param = {
        type: "chartAddress",
        field: "address",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      const data = result.data.returnData;
      console.log(JSON.stringify(data));

      this.items = data.map((item) => {
        const center = zhejiangJson.features.find(
          (feature) => feature.properties.name === item.city
        ).properties.center;

        return {
          name: item.city,
          itemStyle: {
            areaColor: this.color.find((n) => item[n.name] > 0).color,
          },
          item: item,
          value: [...center],
        };
      });
      this.initChart();
    },
  },
};
</script>
