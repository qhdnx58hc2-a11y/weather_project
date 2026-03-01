<template>
  <div class="login-container">
    <el-form
      :model="ruleForm2"
      :rules="rules2"
      status-icon
      ref="ruleForm2"
      label-position="left"
      label-width="80px"
      class="demo-ruleForm login-page"
    >
      <h3 class="title">注册</h3>
      <el-form-item prop="name" label="姓名">
        <el-input
          type="text"
          v-model="ruleForm2.name"
          auto-complete="off"
          placeholder="姓名"
        ></el-input>
      </el-form-item>
      <el-form-item prop="username" label="账号">
        <el-input
          type="text"
          v-model="ruleForm2.username"
          auto-complete="off"
          placeholder="账号"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password" label="密码">
        <el-input
          type="password"
          v-model="ruleForm2.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item prop="mobile" label="手机">
        <el-input
          type="text"
          v-model="ruleForm2.mobile"
          auto-complete="off"
          placeholder="手机"
        ></el-input>
      </el-form-item>
      <el-form-item prop="email" label="邮箱">
        <el-input
          type="text"
          v-model="ruleForm2.email"
          auto-complete="off"
          placeholder="邮箱"
        ></el-input>
      </el-form-item>
      <div>
        <el-button
          type="danger"
          style="width: 100%"
          @click="handleSubmit"
          :loading="logining"
          >提交</el-button
        >
      </div>
      <br />
      <div style="display: flex; justify-content: space-between">
        <el-button style="margin-right: 80px" @click="clearClick"
          >清空</el-button
        >
        <el-button style="margin-left: 80px" @click="toLogin">登录</el-button>
      </div>
    </el-form>
  </div>
</template>

<script>
import cryptoJs from "crypto-js";
import { validatePhone } from "@/utils/validate";
export default {
  data() {
    return {
      from: "",
      key: "rest@126.com",
      logining: false,
      ruleForm2: {
        name: "",
        username: "",
        password: "",
        email: "",
        mobile: "",
        role: "",
      },
      roleList: [
        {
          value: "1",
          label: "用户",
        },
        {
          value: "2",
          label: "商家",
        },
      ],
      rules2: {
        email: [
          {
            required: true,
            message: "请输入您的邮箱地址",
            trigger: "blur",
          },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["blur", "change"],
          },
        ],
        mobile: [
          { required: true, message: "请输入您的手机号码", trigger: "blur" },
          { validator: validatePhone, trigger: ["blur", "change"] },
        ],
        name: [{ required: true, message: "请输入您的姓名", trigger: "blur" }],
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
          { required: true, message: "请输入您的密码", trigger: "blur" },
          { min: 6, message: "密码长度不低于 6 个字符", trigger: "blur" },
        ],
        /* role: [
          { required: true, message: "select your role", trigger: "blur" },
        ], */
      },
      checked: false,
    };
  },
  created() {
    this.from = this.$route.query.from;
  },
  methods: {
    async handleSubmit() {
      this.$refs["ruleForm2"].validate(async (valid) => {
        if (valid) {
          let param = {
            username: this.ruleForm2.username,
            name: this.ruleForm2.name,
            password: this.ruleForm2.password,
            email: this.ruleForm2.email,
            mobile: this.ruleForm2.mobile,
            role: "1",
          };
          const result = await this.$http.post("/rest/user/register", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$router.push({ path: "/login", query: { from: this.from } });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    toLogin() {
      this.$router.push({ path: "/login", query: { from: this.from } });
    },
    encryptDes(message) {
      const keyHex = cryptoJs.enc.Utf8.parse(this.key);
      const option = { mode: cryptoJs.mode.ECB, padding: cryptoJs.pad.Pkcs7 };
      const encrypted = cryptoJs.DES.encrypt(message, keyHex, option);
      return encrypted.toString();
    },
    clearClick() {
      this.ruleForm2 = {};
    },
  },
};
</script>

<style scoped>
.login-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  min-width: auto;
  z-index: 0;
  zoom: 1;
  background-color: #fff;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url(../../assets/opera/2157389cf1f191021630fc1dcb555206.jpg);
  -webkit-background-size: cover;
  -o-background-size: cover;
  background-position: center 0;
}

.login-page {
  margin: 100px auto 0;
  border-radius: 5px;
  width: 450px;
  padding: 35px 35px 15px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}

label.el-checkbox.rememberme {
  margin: 0px 0px 15px;
  text-align: left;
}
</style>
