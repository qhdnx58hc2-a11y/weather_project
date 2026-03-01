<template>
  <dv-capsule-chart :config="config" style="width: 100%; height: 100%" />
</template>

<script>
export default {
  name: 'CapsuleChart',
  props: {
    // 数据
    capsuleData: {
      type: Array,
      default: () => [
        {
          name: '南阳',
          value: 167
        },
        {
          name: '周口',
          value: 123
        },
        {
          name: '漯河',
          value: 98
        },
        {
          name: '郑州',
          value: 75
        },
        {
          name: '西峡',
          value: 66
        }
      ]
    },
    // 颜色
    capsuleColors: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      config: {
        data: this.capsuleData,
        colors: this.capsuleColors,
        unit: '单位',
        showValue: true
      }
    }
  }
}
</script>

<style></style>
