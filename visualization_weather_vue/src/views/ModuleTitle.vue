<template>
  <!-- 顶部标题 -->
  <div class="module-box">
    <!-- 左侧细线 -->
    <div style="flex: 0 1 30%;position: relative;">
      <dv-decoration-10 style="height: 5px" />
    </div>
    <!-- 中间标题 -->
    <div style="flex: 0 1 40%">
      <div class="d-flex">
        <dv-decoration-8 style="height: 20px; flex: 1" />
        <div style="flex: 1">
          <dv-decoration-11 style="width: 100%; height: 60px;font-size: 22px;line-height: 60px;text-align: center"
            >气象灾害分析与可视化</dv-decoration-11
          >
        </div>
        <dv-decoration-8 :reverse="true" style="height: 20px; flex: 1" />
      </div>
    </div>
    <!-- 右侧细线 -->
    <div style="flex: 0 1 30%;position: relative;">
      <!-- <dv-decoration-10 style="height: 5px; transform: rotateY(180deg)" /> -->
      <!-- <div style="font-size: 22px;width: 100%;text-align: center;line-height: 55px;">
        2024年11月20日 21:48:23
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModuleTitle'
}
</script>

<style></style>
