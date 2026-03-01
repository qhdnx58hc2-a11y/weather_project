<script>
import IndustryProportion from "@/components/IndustryProportion.vue";
import ECharts from "@/components/ECharts.vue";
import ChinaMapVue from "@/components/ChinaMap.vue";
import DisasterLevelList from "@/components/DisasterLevelList.vue";
// import NoticeList from "@/components/NoticeList.vue";
import CorrectionInfo from "@/components/CorrectionInfo.vue";
import EmissionSituation from "@/components/EmissionSituation.vue";
import PersonnelRelations from "@/components/PersonnelRelations.vue";

export default {
  name: "ModuleMain",
  components: {
    IndustryProportion,
    ECharts,
    ChinaMapVue,
    DisasterLevelList,
    // NoticeList,
    CorrectionInfo,
    EmissionSituation,
    PersonnelRelations,
  },
  data() {
    return {
      // 水位图
      waterConfig: {
        data: [66, 45],
        shape: "roundRect",
      },
      // 进度池
      percentConfig: {
        value: 66,
        borderWidth: 0,
        borderRadius: 10,
        borderGap: 5,
      },
    };
  },
};
</script>
<template>
  <div style="height: 100%">
    <div class="grid-container">
      <div class="item item1">
        <dv-border-box-12 style="width: 100%; height: 100%">
          <IndustryProportion />
        </dv-border-box-12>
      </div>
      <div class="item item2">
        <dv-border-box-12 style="width: 100%; height: 100%">
          <ECharts />
        </dv-border-box-12>
      </div>
      <div class="item item3">
        <dv-border-box-12 style="width: 100%; height: 100%">
          <EmissionSituation />
        </dv-border-box-12>
      </div>
      <div class="item item4">
        <ChinaMapVue />
      </div>
      <div class="item item5">
        <CorrectionInfo />
      </div>
      <div class="item item6"><DisasterLevelList /></div>
      <!-- <div class="item item7"><NoticeList /></div> -->
      <div class="item item8">
        <dv-border-box-12 style="width: 100%; height: 100%">
          <PersonnelRelations />
        </dv-border-box-12>
      </div>
    </div>
  </div>
</template>
<style>
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: repeat(4, 1fr);
  gap: 10px;
  height: 100%;
}
.item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.item1 {
  grid-column: 1 / 2;
  grid-row: 1 / 2;
}

.item2 {
  grid-column: 1 / 2;
  grid-row: 2 / 3;
}

.item3 {
  grid-column: 1 / 2;
  grid-row: 3 / 4;
}

.item4 {
  grid-column: 2 / 3;
  grid-row: 1 / 3; /* 这里让中间一列的首元素与第二个元素合并，占据两行 */
}

.item5 {
  grid-column: 2 / 3;
  grid-row: 3 / 4;
}

.item6 {
  grid-column: 3 / 4;
  grid-row: 1 / 3;
}

.item7 {
  grid-column: 3 / 4;
  grid-row: 2 / 3;
}

.item8 {
  grid-column: 3 / 4;
  grid-row: 3 / 4;
}

.item9 {
  grid-column: 2 / 3;
  grid-row: 2 / 3;
}
</style>
