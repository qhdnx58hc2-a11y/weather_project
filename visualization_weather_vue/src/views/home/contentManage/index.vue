<template>
  <div>
    <br />
    <div>
      <el-row>
        <el-col>
          <div>
            <el-form ref="form" :model="form" label-width="120px">
              <el-row>
                <el-col :span="6">
                  <el-form-item label="名称：">
                    <el-input v-model="search.name"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="6">
                  <el-form-item label="分类：">
                    <el-select
                      v-model="search.classification"
                      placeholder="请选择分类"
                    >
                      <el-option
                        v-for="item in classificationList"
                        :key="item.name"
                        :label="item.name"
                        :value="item.name"
                      >
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :span="6">
                  <el-form-item prop="alarm" label="预警：">
                    <el-select v-model="search.alarm" placeholder="请选择预警">
                      <el-option
                        v-for="item in alarmList"
                        :key="item.name"
                        :label="item.name"
                        :value="item.name"
                      >
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
              </el-row>
              <br />
              <el-row style="text-align: center">
                <el-button type="primary" @click="handleSearch">查询</el-button>
                <el-button @click="clearSearch">清空</el-button>

                <div style="text-align: left; margin-right: 20px">
                  <el-button type="warning" size="small" @click="addClick"
                    >新增</el-button
                  >
                  <el-button type="primary" size="small" @click="generateClick"
                    >采集数据</el-button
                  >
                </div>
              </el-row>
            </el-form>
          </div>
          <br />
          <el-table :data="tableData" border style="width: 100%">
            <el-table-column
              prop="id"
              label="编号"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="time"
              label="时间"
              width="200"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="address"
              label="地址"
              width="200"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="name"
              label="灾害"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="classification"
              label="分类"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column
              prop="alarm"
              label="预警"
              header-align="center"
              align="center"
            ></el-table-column>
            <el-table-column label="操作" width="200">
              <template slot-scope="scope">
                <el-button
                  @click="modifyClick(scope.row)"
                  type="primary"
                  size="small"
                  >修改</el-button
                >
                <el-popconfirm
                  title="删除不可恢复,确定删除吗？"
                  @confirm="deleteClick(scope.row)"
                >
                  <el-button type="danger" size="small" slot="reference"
                    >删除</el-button
                  >
                </el-popconfirm>
              </template>
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
    </div>
    <br />
    <div style="text-align: center">
      <el-pagination
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="page.currentPage"
        :page-sizes="[]"
        :page-size="page.pageSize"
        layout="total, prev, pager, next, slot, jumper"
        :total="page.total"
      >
      </el-pagination>
    </div>
    <!-- 修改 -->
    <el-dialog title="编辑" :visible.sync="modifyVisible">
      <el-form :model="form" :rules="rules" ref="modifyForm">
        <el-form-item prop="time" label="时间：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-date-picker
              v-model="form.time"
              type="datetime"
              placeholder="选择日期时间"
              format="yyyy-MM-dd HH:mm"
              value-format="yyyy-MM-dd HH:mm"
            >
            </el-date-picker>
          </div>
        </el-form-item>
        <el-form-item prop="name" label="灾害：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="classification"
          label="分类："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-select v-model="form.classification" placeholder="请选择分类">
              <el-option
                v-for="item in classificationList"
                :key="item.name"
                :label="item.name"
                :value="item.name"
              >
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item prop="alarm" label="预警：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-select v-model="form.alarm" placeholder="请选择预警">
              <el-option
                v-for="item in alarmList"
                :key="item.name"
                :label="item.name"
                :value="item.name"
              >
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item
          prop="address"
          label="地址："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-cascader
              v-model="form.address"
              placeholder="请选择地址"
              :options="cityList"
              filterable
            ></el-cascader>
          </div>
        </el-form-item>
        <el-form-item label="图片：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <img
              v-if="form.image"
              :src="form.image"
              width="120px;"
              height="120px;"
              class="head_pic"
            />
            <i v-else class="el-icon-plus head_pic_icon"></i>
            <el-upload
              class="upload-demo"
              action=""
              :on-success="handleSuccess"
              :before-upload="beforeUploadFile"
              single
            >
              <el-button size="small">点击上传</el-button>
            </el-upload>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="modifyVaccinum">确 定</el-button>
        <el-button @click="modifyVisible = false">取 消</el-button>
      </div>
    </el-dialog>
    <!-- 新增 -->
    <el-dialog title="新增" :visible.sync="addVisible">
      <el-form :model="form" :rules="rules" ref="addForm">
        <el-form-item prop="time" label="时间：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-date-picker
              v-model="form.time"
              type="datetime"
              placeholder="选择日期时间"
              format="yyyy-MM-dd HH:mm"
              value-format="yyyy-MM-dd HH:mm"
            >
            </el-date-picker>
          </div>
        </el-form-item>
        <el-form-item prop="name" label="灾害：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="classification"
          label="分类："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-select v-model="form.classification" placeholder="请选择分类">
              <el-option
                v-for="item in classificationList"
                :key="item.name"
                :label="item.name"
                :value="item.name"
              >
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item prop="alarm" label="预警：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-select v-model="form.alarm" placeholder="请选择预警">
              <el-option
                v-for="item in alarmList"
                :key="item.name"
                :label="item.name"
                :value="item.name"
              >
              </el-option>
            </el-select>
          </div>
        </el-form-item>
        <el-form-item
          prop="address"
          label="地址："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-cascader
              v-model="form.address"
              placeholder="请选择地址"
              :options="cityList"
              filterable
            ></el-cascader>
          </div>
        </el-form-item>
        <el-form-item label="图片：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <img
              v-if="form.image"
              :src="form.image"
              width="120px;"
              height="120px;"
              class="head_pic"
            />
            <i v-else class="el-icon-plus head_pic_icon"></i>
            <el-upload
              class="upload-demo"
              action=""
              :on-success="handleSuccess"
              :before-upload="beforeUploadFile"
              single
            >
              <el-button size="small">点击上传</el-button>
            </el-upload>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="addVaccinum">确 定</el-button>
        <el-button @click="addVisible = false">取 消</el-button>
      </div>
    </el-dialog>
    <!-- 删除提示 -->
    <!-- <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <span>您已选中{{ form.username }}，请确认您的选择，此动作不能撤销</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteVaccinum">确 定</el-button>
      </span>
    </el-dialog> -->
    <!-- <el-dialog title="选择分类" :visible.sync="classificationVisible">
      <el-form :model="form">
        <el-form-item
          label="一级分类："
          :label-width="formLabelWidth"
          style="text-align: left"
        >
          <el-select
            v-model="form.first"
            @change="firstChange"
            placeholder="请选择"
          >
            <el-option
              v-for="item in firstList"
              :key="item.id"
              :label="item.name"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="二级分类："
          :label-width="formLabelWidth"
          style="text-align: left"
        >
          <el-select
            v-model="form.second"
            @change="secondChange"
            placeholder="请选择"
          >
            <el-option
              v-for="item in secondList"
              :key="item.id"
              :label="item.label"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="三级分类："
          :label-width="formLabelWidth"
          style="text-align: left"
        >
          <el-select v-model="form.classification" placeholder="请选择">
            <el-option
              v-for="item in thirdList"
              :key="item.id"
              :label="item.label"
              :value="item.id"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="classificationVaccinum"
          >确 定</el-button
        >
        <el-button @click="classificationVisible = false">取 消</el-button>
      </div>
    </el-dialog> -->
    <!-- 新增部门 -->
    <!-- <el-dialog title="添加分类" :visible.sync="departVisible">
      <el-form :model="form">
        <el-form-item label="分类名称：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="departVaccinum">确 定</el-button>
        <el-button @click="departVisible = false">取 消</el-button>
      </div>
    </el-dialog>
    <el-dialog title="修改架构" :visible.sync="departModifyVisible">
      <el-form :model="form">
        <el-form-item label="架构名称：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="departModifyVaccinum"
          >确 定</el-button
        >
        <el-button @click="departModifyVisible = false">取 消</el-button>
      </div>
    </el-dialog> -->
  </div>
</template>

<script>
import { exportTempletes } from "../../../services/templete";
import { jiangsu } from "@/utils/citys";

export default {
  data() {
    return {
      departModifyVisible: false,
      classificationVisible: false,
      departVisible: false,
      dialogVisible: false,
      modifyVisible: false,
      addVisible: false,
      page: {
        currentPage: 1,
        pageSize: 10,
        total: 7634,
      },
      search: {
        name: "",
        classification: "",
        alarm: "",
      },
      form: {
        id: "",
        uid: "",
        name: "",
        image: "",
        classification: "",
        address: "",
        time: "",
        alarm: "",
      },
      rules: {
        name: [{ required: true, message: "请输入灾害", trigger: "blur" }],
        time: [{ required: true, message: "请输入时间", trigger: "blur" }],
        classification: [
          { required: true, message: "请输入分类", trigger: "blur" },
        ],
        alarm: [{ required: true, message: "请输入预警", trigger: "blur" }],
        address: [{ required: true, message: "请输入地址", trigger: "blur" }],
      },
      dialogFormVisible: false,
      formLabelWidth: "120px",
      data: [],
      firstList: [],
      secondList: [],
      thirdList: [],
      classificationList: [],
      alarmList: [
        { id: "1", name: "红色预警" },
        { id: "2", name: "橙色预警" },
        { id: "3", name: "黄色预警" },
        { id: "4", name: "蓝色预警" },
      ],
      cityList: [],
      statusList: [],
      tableData: [],
    };
  },
  created() {
    this.list();
    this.cityList = Object.keys(jiangsu).map((item) => {
      return {
        value: item,
        label: item,
        children: jiangsu[item].map((n) => {
          return { value: n, label: n };
        }),
      };
    });
  },
  methods: {
    /* classificationClick() {
      this.classificationVisible = true;
    },
    async getClassificationList() {
      let param = {
        parent: "",
      };
      const result = await this.$http.post("/rest/classification/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.classificationList = result.data.returnData.list;
      this.firstList = result.data.returnData.firstList;
      this.data = result.data.returnData.list;
    },
    async departVaccinum() {
      let param = {
        parent: this.form.parent,
        name: this.form.name,
      };
      const result = await this.$http.post("/rest/classification/add", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.$message.success("操作成功");
      this.departVisible = false;
      this.getClassificationList();
    },
    classificationVaccinum() {
      console.log("classification " + this.form.classification);
      if (
        this.form.classification === "" ||
        this.form.classification === undefined ||
        this.form.classification === null
      ) {
        this.$message.error("请选择分类");
        return;
      }
      let _this = this;
      _this.thirdList.forEach(function (item) {
        if (item.id === _this.form.classification) {
          _this.form.classificationName = item.label;
        }
      });
      console.log("classificationName " + this.form.classificationName);
      this.classificationVisible = false;
    },
    async departModifyVaccinum() {
      let param = {
        id: this.form.id,
        name: this.form.name,
      };
      const result = await this.$http.post(
        "/rest/classification/modify",
        param
      );
      if (result.data.returnCode !== "200") {
        this.departModifyVisible = false;
        this.$message.error(result.data.message);
        return;
      }
      this.departModifyVisible = false;
      this.getClassificationList();
    }, */
    /* firstChange() {
      console.log("first " + this.form.first);
      let _this = this;
      _this.classificationList.forEach(function (item) {
        if (item.id === _this.form.first) {
          _this.secondList = item.children;
        }
      });
    },
    secondChange() {
      console.log("second " + this.form.second);
      let _this = this;
      _this.secondList.forEach(function (item) {
        if (item.id === _this.form.second) {
          _this.thirdList = item.children;
        }
      });
    },
    async deleteVaccinum() {
      let param = {
        uid: this.form.uid,
      };
      const result = await this.$http.post(
        "/rest/classification/delete",
        param
      );
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        this.dialogVisible = false;
        return;
      }
      this.$message.success("删除成功");
      this.dialogVisible = false;
      this.list();
    },
    renderContent(h, { node, data }) {
      return (
        <span class="custom-tree-node">
          <span style="margin-right:10px;">{node.label}</span>
          <span>
            <span on-click={() => this.append(data)}>
              <i class="el-icon-circle-plus-outline"></i>
            </span>
            <span on-click={() => this.remove(node, data)}>
              <i class="el-icon-remove-outline"></i>
            </span>
            <span on-click={() => this.modify(node, data)}>
              <i class="el-icon-edit"></i>
            </span>
          </span>
        </span>
      );
    },
    addDepart() {
      this.form.parent = "";
      this.departVisible = true;
    },
    currentChecked(nodeObj, SelectedObj) {
      this.search.classification = SelectedObj.checkedKeys.join(",");
      this.list();
    },
    async remove(node, data) {
      let param = {
        id: data.id,
      };
      const result = await this.$http.post(
        "/rest/classification/delete",
        param
      );
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.getClassificationList();
    },
    append(data) {
      console.log("[data] " + data.id);
      this.form.parent = data.id;
      this.departVisible = true;
    },
    async modify(node, data) {
      this.form.name = data.label;
      this.form.id = data.id;
      this.departModifyVisible = true;
    },
    handleClick(row) {
      this.form = row;
      this.dialogFormVisible = true;
    }, */
    addClick() {
      this.form = {
        id: "",
        uid: "",
        name: "",
        image: "",
        classification: "",
        address: "",
        time: "",
        alarm: "",
      };
      this.secondList = [];
      this.addVisible = true;
    },
    modifyClick(row) {
      console.log("[modifyClick]row " + JSON.stringify(row));
      this.form = JSON.parse(JSON.stringify(row));
      this.form.address = row.address.includes(",")
        ? row.address.split(",")
        : row.address;
      this.modifyVisible = true;
    },
    detailClick(row) {
      console.log("[detailClick]row " + JSON.stringify(row));
      this.form = row;
      this.detailVisible = true;
    },
    async modifyVaccinum() {
      this.$refs["modifyForm"].validate(async (valid) => {
        if (valid) {
          let param = {
            name: this.form.name,
            image: this.form.image,
            classification: this.form.classification,
            address: this.form.address.join(),
            time: this.form.time,
            alarm: this.form.alarm,
            uid: this.form.uid,
            id: this.form.id,
          };
          const result = await this.$http.post("/rest/content/modify", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$message.success("保存成功！");
          this.modifyVisible = false;
          this.list();
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    async addVaccinum() {
      this.$refs["addForm"].validate(async (valid) => {
        if (valid) {
          let param = {
            name: this.form.name,
            image: this.form.image,
            classification: this.form.classification,
            address: this.form.address.join(),
            time: this.form.time,
            alarm: this.form.alarm,
          };
          const result = await this.$http.post("/rest/content/add", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$message.success("保存成功！");
          this.addVisible = false;
          this.list();
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    async deleteClick(row) {
      this.form = row;
      let param = {
        uid: row.uid,
        id: row.id,
      };
      const result = await this.$http.post("/rest/content/delete", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.$message.success("删除成功");
      // 删除逻辑中增加页码判断,删除最后一页的最后一条数据后页面显示为空
      if (this.tableData.length === 1 && this.page.currentPage > 1) {
        this.page.currentPage--;
      }
      this.list();
    },
    async generateClick() {
      this.$prompt("请输入采集数据数量", "是否采集数据？", {
        inputValue: 10,
        inputPattern: /^(100|[1-9][0-9]?)$/,
        inputErrorMessage: "请输入1-100之间的数字",
        inputPlaceholder: "请输入采集数据数量",
      })
        .then(async ({ value }) => {
          console.log("[generateClick]value " + value);

          let param = { dataSize: parseInt(value) || 10 };
          const result = await this.$http.post("/rest/content/generate", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$message.success("操作成功");
          this.list();
        })
        .catch(() => {});
    },
    async list() {
      let param = {
        classification: this.search.classification,
        name: this.search.name,
        alarm: this.search.alarm,
        currentPage: this.page.currentPage,
        pageSize: this.page.pageSize,
      };
      const result = await this.$http.post("/rest/content/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.tableData = result.data.returnData.list;
      this.classificationList = result.data.returnData.classificationList;
      this.page = result.data.returnData.page;
    },
    handleSearch() {
      this.list();
    },
    clearSearch() {
      this.search.name = "";
      this.search.classification = "";
      this.search.alarm = "";
      this.list();
    },
    selectChange() {
      this.list();
    },
    handleCurrentChange(currentPage) {
      this.page.currentPage = currentPage;
      this.list();
    },
    handleClose() {
      this.dialogVisible = false;
    },
    /**
     * 设置分页的size
     */
    handleSizeChange(val) {
      this.page.pageSize = val;
      this.page.currentPage = 0;
      this.list();
    },
    beforeUploadFile(file) {
      let extension = file.name.substring(file.name.lastIndexOf(".") + 1);
      let size = file.size / 1024 / 1024;
      if (extension !== "png" && extension !== "jpg" && extension !== "bmp") {
        this.$notify.warning({
          title: "警告",
          message: `只能上传后缀是png/jpg/bmp的图片`,
        });
      }
      if (size > 2) {
        this.$notify.warning({
          title: "警告",
          message: `文件大小不得超过2M`,
        });
      }
      this.uploadFile(file);
    },
    async uploadFile(file) {
      let param = new FormData();
      param.append("file", file);
      param.append("uid", this.form.uid);
      console.log("[uploadFile]uid " + this.form.uid);
      await this.$http
        .post("/rest/image/upload", param, {
          timeout: 10000,
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          if (res.data.returnCode !== "200") {
            this.$message.error(res.data.message);
            return;
          }
          this.form.image = res.data.returnData.image;
          console.log("[uploadFile]image " + this.form.image);
        });
    },
    handleSuccess(file) {
      console.log("handleSuccess");
      console.log(file.name);
      this.$notify.success({
        title: "成功",
        message: `文件上传成功`,
      });
    },
    async exportClick() {
      let param = new URLSearchParams();
      await exportTempletes("/rest/user/export", param, "用户模板.xlsx");
    },
  },
};
</script>
<style scoped>
/* 解决 上传下载按钮 不能再一行显示 */
.inline-block {
  display: inline-block;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
