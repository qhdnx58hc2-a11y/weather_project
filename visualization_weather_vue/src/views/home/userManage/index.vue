<template>
  <div>
    <div>
      <el-form ref="form" :model="form" label-width="120px">
        <el-row>
          <el-col :span="6">
            <el-form-item label="姓名：">
              <el-input v-model="search.name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="手机：">
              <el-input v-model="search.mobile"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="性别：">
              <el-select
                v-model="search.gender"
                placeholder="请选择"
                @change="selectChange"
              >
                <el-option
                  v-for="item in genderList"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
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
        <el-table-column prop="name" label="姓名"></el-table-column>
        <el-table-column prop="username" label="账号"></el-table-column>
        <el-table-column prop="genderName" label="性别"></el-table-column>
        <el-table-column prop="email" label="邮箱"></el-table-column>
        <el-table-column label="图片">
          <template slot-scope="scope">
            <img
              :src="scope.row.image"
              width="100px;"
              height="60px;"
              class="head_pic"
            />
          </template>
        </el-table-column>
        <el-table-column prop="mobile" label="手机"></el-table-column>
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
    <el-dialog title="用户修改" :visible.sync="modifyVisible">
      <el-form :model="form" :rules="rules2" ref="modifyForm">
        <el-form-item label="编号：" :label-width="formLabelWidth">
          <div style="text-align: left">{{ form.id }}</div>
        </el-form-item>
        <el-form-item prop="name" label="姓名：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="username"
          label="账号："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input v-model="form.username"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="password"
          label="密码："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input type="password" v-model="form.password"></el-input>
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
        <el-form-item
          label="性别："
          :label-width="formLabelWidth"
          style="text-align: left"
        >
          <el-select v-model="form.gender" placeholder="请选择">
            <el-option
              v-for="item in genderList"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="email" label="邮箱：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.email"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="mobile"
          label="手机："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input v-model="form.mobile"></el-input>
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
      <el-form :model="form" :rules="rules2" ref="addForm">
        <el-form-item prop="name" label="姓名：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.name"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="username"
          label="账号："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input v-model="form.username"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="password"
          label="密码："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input v-model="form.password"></el-input>
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
        <el-form-item
          label="性别："
          :label-width="formLabelWidth"
          style="text-align: left"
        >
          <el-select v-model="form.gender" placeholder="请选择">
            <el-option
              v-for="item in genderList"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="email" label="邮箱：" :label-width="formLabelWidth">
          <div style="text-align: left">
            <el-input v-model="form.email"></el-input>
          </div>
        </el-form-item>
        <el-form-item
          prop="mobile"
          label="手机："
          :label-width="formLabelWidth"
        >
          <div style="text-align: left">
            <el-input v-model="form.mobile"></el-input>
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
import { validatePhone } from "@/utils/validate";
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
      numberVisible: true,
      numberDisabled: false,
      search: {
        mobile: "",
        name: "",
        gender: "",
      },
      form: {
        uid: "",
        number: "",
        name: "",
        image: "",
        gender: "",
        role: "",
        age: "",
        email: "",
        mobile: "",
        username: "",
        password: "",
      },
      rules2: {
        email: [
          {
            required: true,
            message: "请输入邮箱地址",
            trigger: "blur",
          },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["blur", "change"],
          },
        ],
        mobile: [
          { required: true, message: "请输入手机号码", trigger: "blur" },
          { validator: validatePhone, trigger: ["blur", "change"] },
        ],
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
        username: [
          { required: true, message: "请输入账号名", trigger: "blur" },
          {
            min: 4,
            max: 20,
            message: "长度在 4 到 20 个字符",
            trigger: "blur",
          },
          {
            pattern: /^[a-zA-Z0-9_]+$/,
            message: "账号名只能包含字母、数字和下划线",
            trigger: "blur",
          },
          {
            validator: (rule, value, callback) => {
              if (value === "admin" || value === "manager") {
                callback(new Error("该账号名不可用"));
              } else {
                callback();
              }
            },
            trigger: "blur",
          },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 6, message: "密码长度不低于 6 个字符", trigger: "blur" },
        ],
        /* role: [
          { required: true, message: "select your role", trigger: "blur" },
        ], */
      },
      dialogFormVisible: false,
      formLabelWidth: "120px",
      names: [],
      genderList: [],
      roleList: [],
      tableData: [],
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
        image: "",
        gender: "",
        role: "",
        age: "",
        email: "",
        mobile: "",
        username: "",
        password: "",
      };
      this.rules2.password[0].required = true;
      this.addVisible = true;
    },
    modifyClick(row) {
      console.log("[modifyClick]row " + JSON.stringify(row));
      this.form = row;
      // this.form.image = "";
      this.form.password = "";
      this.rules2.password[0].required = false;
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
            username: this.form.username,
            gender: this.form.gender,
            age: this.form.age,
            email: this.form.email,
            mobile: this.form.mobile,
            password: this.form.password,
            image: this.form.image,
            role: "1",
            uid: this.form.uid,
          };
          const result = await this.$http.post("/rest/user/modify", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            // this.modifyVisible = false;
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
            username: this.form.username,
            gender: this.form.gender,
            age: this.form.age,
            email: this.form.email,
            mobile: this.form.mobile,
            password: this.form.password,
            image: this.form.image,
            role: "1",
          };
          const result = await this.$http.post("/rest/user/add", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            // this.addVisible = false;
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
      const result = await this.$http.post("/rest/user/delete", param);
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
        mobile: this.search.mobile,
        gender: this.search.gender,
        role: "1",
        currentPage: this.page.currentPage,
        pageSize: this.page.pageSize,
      };
      const result = await this.$http.post("/rest/user/list", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.tableData = result.data.returnData.list;
      this.genderList = result.data.returnData.genderList;
      this.roleList = result.data.returnData.roleList;
      this.page = result.data.returnData.page;
    },
    handleSearch() {
      this.list();
    },
    clearSearch() {
      this.search.name = "";
      this.search.mobile = "";
      this.search.gender = "";
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
    beforeUploadUser(file) {
      let extension = file.name.substring(file.name.lastIndexOf(".") + 1);
      let size = file.size / 1024 / 1024;
      if (extension !== "xlsx") {
        this.$notify.warning({
          title: "警告",
          message: `只能上传后缀是xlsx的文件`,
        });
      }
      if (size > 10) {
        this.$notify.warning({
          title: "警告",
          message: `文件大小不得超过10M`,
        });
      }
      this.uploadUserFile(file);
    },
    async uploadUserFile(file) {
      let param = new FormData();
      param.append("file", file);
      console.log("[uploadFile]uid " + this.form.uid);
      await this.$http
        .post("/rest/user/upload", param, {
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
          console.log("[uploadUserFile] " + res.data.message);
          this.list();
        });
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
      await exportTempletes("/rest/user/export", param, "劳务人员花名册.xlsx");
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
