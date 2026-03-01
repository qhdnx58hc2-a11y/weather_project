<template>
  <div>
    <br />
    <el-row>
      <el-col :span="12">
        <el-form ref="form" :model="form" :rules="rules2" label-width="160px">
          <el-form-item prop="name" label="姓名：">
            <div style="text-align: left">
              <el-input v-model="form.name"></el-input>
            </div>
          </el-form-item>
          <el-form-item label="头像：">
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
          <el-form-item prop="username" label="账号：">
            <div style="text-align: left">
              <el-input v-model="form.username"></el-input>
            </div>
          </el-form-item>
          <el-form-item label="性别：" style="text-align: left">
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
          <el-form-item prop="mobile" label="手机：">
            <div style="text-align: left">
              <el-input v-model="form.mobile"></el-input>
            </div>
          </el-form-item>
          <el-form-item prop="email" label="邮箱：">
            <div style="text-align: left">
              <el-input v-model="form.email"></el-input>
            </div>
          </el-form-item>
        </el-form>
        <div style="text-align: center">
          <el-button type="danger" @click="modifyVaccinum">保 存</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { validatePhone } from "@/utils/validate";
export default {
  data() {
    return {
      form: {
        uid: "",
        name: "",
        mobile: "",
        gender: "",
        username: "",
        image: "",
        age: "",
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
      },
      formLabelWidth: "120px",
      genderList: [
        {
          value: "male",
          label: "男",
        },
        {
          value: "female",
          label: "女",
        },
      ],
      dialogVisible: false,
    };
  },
  created() {
    this.initDetail();
  },
  methods: {
    async initDetail() {
      this.form.uid = sessionStorage.getItem("uid");
      let param = {
        uid: this.form.uid,
      };
      const result = await this.$http.post("/rest/user/currentUser", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.form = result.data.returnData;
    },
    async modifyVaccinum() {
      this.$refs["form"].validate(async (valid) => {
        if (valid) {
          let param = {
            name: this.form.name,
            username: this.form.username,
            gender: this.form.gender,
            mobile: this.form.mobile,
            email: this.form.email,
            image: this.form.image,
            age: this.form.age,
            uid: this.form.uid,
          };
          const result = await this.$http.post("/rest/user/modify", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$message.success("保存成功！");
        } else {
          console.log("error submit!!");
          return false;
        }
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
  },
};
</script>
