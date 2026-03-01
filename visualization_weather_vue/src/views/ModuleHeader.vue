<template>
  <!-- 中间三行三列 -->
  <div class="module-box">
    <!--  左侧胶囊图-->
    <div style="flex: 0 1 50%">
      <dv-border-box-6 style="height: 150px">
        <!-- 将胶囊图封装为组件 -->
        <CapsuleChart :capsuleColors="capsuleColors" />
      </dv-border-box-6>
    </div>
    <!-- 右侧进度条 -->
    <div style="flex: 0 1 50%">
      1231
      <div style="color: #FFF;">123</div>
    </div>
  </div>
</template>

<script>
// 导入封装的 胶囊柱图
import CapsuleChart from '@/components/CapsuleChart.vue'

export default {
  name: 'ModuleHeader',
  components: {
    CapsuleChart
  },
  data() {
    return {
      // 胶囊图颜色
      capsuleColors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
      // 胶囊图数据
      capsuleData: [
        { name: '春季', value: 102 },
        { name: '夏季', value: 200 },
        { name: '秋季', value: 134 },
        { name: '冬季', value: 189 }
      ],
      // 进度条数据
      percentConfig: {
        value: 59,
        borderWidth: 0 // 边框宽度
      }
    }
  }
}
</script>

<style></style>
