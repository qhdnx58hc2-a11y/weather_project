<template>
  <div>
    <div>
      <el-form ref="form" :model="form" label-width="120px">
        <el-row>
          <el-col :span="6">
            <el-form-item label="名称：">
              <el-input v-model="search.name"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <br />
        <el-row style="text-align: center">
          <el-button type="primary" @click="handleSearch">查询</el-button>
          <el-button @click="clearSearch">清空</el-button>
          <div style="text-align: left; margin-right: 20px">
            <el-button @click="addClick" size="small" type="warning"
              >新增</el-button
            >
          </div>
        </el-row>
      </el-form>
    </div>
    <br />
    <div>
      <el-table :data="tableData" stripe border style="width: 100%">
        <el-table-column prop="id" label="编号"></el-table-column>
        <el-table-column prop="name" label="分类"></el-table-column>
        <el-table-column prop="createDate" label="创建时间"></el-table-column>
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
    <el-dialog title="修改" :visible.sync="modifyVisible">
      <el-form :model="form" :rules="rules" ref="modifyForm">
        <el-form-item prop="name" label="名称：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item label="描述：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.description"></el-input>
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
        <el-form-item prop="name" label="名称：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item label="描述：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.description"></el-input>
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
  </div>
</template>

<script>
import { exportTempletes } from "../../../services/templete";
export default {
  data() {
    return {
      addVisible: false,
      modifyVisible: false,
      detailVisible: false,
      page: {
        currentPage: 1,
        pageSize: 10,
        total: 5,
      },
      search: {
        name: "",
      },
      form: {
        uid: "",
        number: "",
        name: "",
        store: "",
        content: "",
        image: "",
      },
      rules: {
        name: [{ required: true, message: "请输入分类", trigger: "blur" }],
      },
      dialogFormVisible: false,
      formLabelWidth: "120px",
      tableData: [],
      contentList: [],
    };
  },
  created() {
    this.list();
  },
  methods: {
    handleClick(row) {
      this.form = row;
      this.dialogFormVisible = true;
    },
    addClick() {
      this.form = {
        uid: "",
        number: "",
        name: "",
        store: "",
        content: "",
        image: "",
      };
      this.addVisible = true;
    },
    modifyClick(row) {
      console.log("[modifyClick]row " + JSON.stringify(row));
      this.form = row;
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
            description: this.form.description,
            content: this.form.content,
            image: this.form.image,
            uid: this.form.uid,
          };
          const result = await this.$http.post(
            "/rest/classification/modify",
            param
          );
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
            description: this.form.description,
            content: this.form.content,
            image: this.form.image,
          };
          const result = await this.$http.post(
            "/rest/classification/add",
            param
          );
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
      };
      const result = await this.$http.post(
        "/rest/classification/delete",
        param
      );
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
    async list() {
      let param = {
        name: this.search.name,
        currentPage: this.page.currentPage,
        pageSize: this.page.pageSize,
      };
      const result = await this.$http.post("/rest/classification/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.tableData = result.data.returnData.list;
      this.page = result.data.returnData.page;
    },
    handleSearch() {
      this.list();
    },
    clearSearch() {
      this.search.name = "";
      this.list();
    },
    selectChange() {
      this.list();
    },
    handleCurrentChange(currentPage) {
      this.page.currentPage = currentPage;
      this.list();
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
