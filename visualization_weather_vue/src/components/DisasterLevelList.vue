<script>
// import * as echarts from 'echarts'
export default {
  name: "ECharts",
  data() {
    return {
      color: [
        { name: "红色", color: "#ff0000" },
        { name: "橙色", color: "#ffa11c" },
        { name: "黄色", color: "#ffd26f" },
        { name: "蓝色", color: "#73C0DE" },
      ],
      // 排名轮播表
      scrollBoardConfig: {
        header: [
          "区域",
          '<span style="color:#ff0000;">红色</span>',
          '<span style="color:#ffa11c;">橙色</span>',
          '<span style="color:#ffd26f;">黄色</span>',
          '<span style="color:#73C0DE;">蓝色</span>',
        ],
        /* data: [
          [
            "徐州市",
            '<span style="color:#ff0000;">1232</span>',
            '<span style="color:#ffa11c;">5555</span>',
            '<span style="color:#ffd26f;">3555</span>',
            '<span style="color:#73C0DE;">2555</span>',
          ],
          [
            "连云港市",
            '<span style="color:#ff0000;">8</span>',
            '<span style="color:#ffa11c;">4</span>',
            '<span style="color:#ffd26f;">2</span>',
            '<span style="color:#73C0DE;">1</span>',
          ],
          [
            "淮安市",
            '<span style="color:#ff0000;">6</span>',
            '<span style="color:#ffa11c;">3</span>',
            '<span style="color:#ffd26f;">1</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
          [
            "盐城市",
            '<span style="color:#ff0000;">5</span>',
            '<span style="color:#ffa11c;">2</span>',
            '<span style="color:#ffd26f;">1</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
          [
            "扬州市",
            '<span style="color:#ff0000;">4</span>',
            '<span style="color:#ffa11c;">2</span>',
            '<span style="color:#ffd26f;">1</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
          [
            "南通市",
            '<span style="color:#ff0000;">3</span>',
            '<span style="color:#ffa11c;">1</span>',
            '<span style="color:#ffd26f;">0</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
          [
            "宿迁市",
            '<span style="color:#ff0000;">2</span>',
            '<span style="color:#ffa11c;">1</span>',
            '<span style="color:#ffd26f;">0</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
          [
            "泰州市",
            '<span style="color:#ff0000;">1</span>',
            '<span style="color:#ffa11c;">1110</span>',
            '<span style="color:#ffd26f;">0</span>',
            '<span style="color:#73C0DE;">0</span>',
          ],
        ], */
        data: [],
        index: false,
        columnWidth: [90],
        align: ["center", "center", "center", "center", "center"],
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
        type: "chartAddress",
        field: "address",
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      const data = result.data.returnData;
      console.log(data);
      const items = data.map((item) => {
        const nums = this.color.map(
          (n) =>
            '<span style="color:' + n.color + ';">' + item[n.name] + "</span>"
        );
        return [item.city, ...nums];
      });
      this.setConfig(items);
    },
    setConfig(data) {
      this.scrollBoardConfig = {
        header: [
          "区域",
          '<span style="color:#ff0000;">红色</span>',
          '<span style="color:#ffa11c;">橙色</span>',
          '<span style="color:#ffd26f;">黄色</span>',
          '<span style="color:#73C0DE;">蓝色</span>',
        ],
        data: data,
        /* [
          ["徐州市", 12, 5, 3, 2],
          ["连云港市", 8, 4, 2, 1],
        ], */
        index: false,
        columnWidth: [90],
        rowNum: 8,
        align: ["center", "center", "center", "center", "center"],
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
        行政区划灾害等级统计
      </div>
      <dv-scroll-board
        :config="scrollBoardConfig"
        style="
          width: 90%;
          height: 84%;
          position: absolute;
          top: 50px;
          left: 50%;
          transform: translateX(-50%);
        "
      />
    </div>
  </dv-border-box-12>
</template>
