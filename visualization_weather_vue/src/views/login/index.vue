<template>
  <div class="login-container">
    <el-form
      :model="ruleForm2"
      :rules="rules2"
      status-icon
      ref="ruleForm2"
      label-position="left"
      label-width="0px"
      class="demo-ruleForm login-page"
    >
      <h3 class="title" style="text-align: center; font-size: 18px">
        气象灾害分析与可视化
      </h3>
      <el-form-item prop="username">
        <el-input
          type="text"
          v-model="ruleForm2.username"
          auto-complete="off"
          placeholder="用户名"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          v-model="ruleForm2.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button
          type="danger"
          style="width: 100%"
          @click="handleSubmit"
          :loading="logining"
          >登录</el-button
        >
      </el-form-item>
      <div style="display: flex; justify-content: space-between">
        <el-button style="margin-right: 80px" @click="clearClick"
          >清空</el-button
        >
        <el-button style="margin-left: 80px" @click="toRegister"
          >注册</el-button
        >
      </div>
    </el-form>
  </div>
</template>

<script>
import cryptoJs from "crypto-js";
export default {
  data() {
    return {
      from: "",
      key: "rest@126.com",
      logining: false,
      ruleForm2: {
        username: "manager",
        password: "123456",
        captcha: "",
        uuid: "",
      },
      captchaPath: "",
      rules2: {
        username: [
          {
            required: true,
            message: "请输入您的用户名",
            trigger: "blur",
          },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
      checked: false,
    };
  },
  created() {
    // this.getCaptcha();
    // this.from = this.$route.query.from;
    // sessionStorage.setItem("from", this.from);
  },
  methods: {
    async handleSubmit() {
      this.$refs["ruleForm2"].validate(async (valid) => {
        if (valid) {
          sessionStorage.setItem("username", this.ruleForm2.username);
          let param = {
            uuid: this.ruleForm2.uuid,
            username: this.ruleForm2.username.trim(),
            password: this.ruleForm2.password.trim(),
            captcha: this.ruleForm2.captcha,
          };
          const result = await this.$http.post("/rest/user/validate", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          // let from = this.$route.query.from;
          // let uid = this.$route.query.uid;
          let logintoken = result.data.returnData.logintoken;
          let user = result.data.returnData.user;
          let navList = result.data.returnData.navList;
          sessionStorage.setItem("logintoken", logintoken);
          sessionStorage.setItem("user", JSON.stringify(user));
          sessionStorage.setItem("role", user.role);
          sessionStorage.setItem("navList", JSON.stringify(navList));
          sessionStorage.setItem("uid", user.uid);
          if (user.role === "1") {
            this.$router.push({ path: "/dashboard" });
          } else {
            this.$router.push({ path: "/dashboard" });
            // this.$router.push({ path: "/home" });
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    toRegister() {
      this.$router.push({ path: "/register", query: { from: this.from } });
    },
    /* toForget() {
      this.$router.push({ path: "/forget", query: { from: this.from } });
    }, */
    encryptDes(message) {
      const keyHex = cryptoJs.enc.Utf8.parse(this.key);
      const option = { mode: cryptoJs.mode.ECB, padding: cryptoJs.pad.Pkcs7 };
      const encrypted = cryptoJs.DES.encrypt(message, keyHex, option);
      return encrypted.toString();
    },
    clearClick() {
      this.ruleForm2 = {};
    },
    getUUID() {
      return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
        return (
          c === "x" ? (Math.random() * 16) | 0 : "r&0x3" | "0x8"
        ).toString(16);
      });
    },
    // 获取验证码
    getCaptcha() {
      this.ruleForm2.uuid = this.getUUID();
      this.captchaPath =
        "http://127.0.0.1:8084/captcha?uuid=" + this.ruleForm2.uuid;
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
