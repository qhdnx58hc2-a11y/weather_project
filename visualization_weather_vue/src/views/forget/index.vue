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
      <h3 class="title">忘记密码</h3>
      <el-form-item
        prop="email"
        label="邮箱"
      >
        <el-input
          type="text"
          v-model="ruleForm2.email"
          auto-complete="off"
          placeholder="邮箱"
        ></el-input>
      </el-form-item>
      <el-form-item
        prop="contact"
        label="电话"
      >
        <el-input
          type="text"
          v-model="ruleForm2.contact"
          auto-complete="off"
          placeholder="电话"
        ></el-input>
      </el-form-item>
      <el-form-item
        prop="password"
        label="密码"
      >
        <el-input
          type="password"
          v-model="ruleForm2.password"
          auto-complete="off"
          placeholder="密码"
        ></el-input>
      </el-form-item>
      <el-form-item
        prop="comfirmPassword"
        label="确认密码"
      >
        <el-input
          type="text"
          v-model="ruleForm2.comfirmPassword"
          auto-complete="off"
          placeholder="确认密码"
        ></el-input>
      </el-form-item>
      <!-- <el-checkbox 
                v-model="checked"
                class="rememberme"
            >记住密码</el-checkbox> -->
      <div>
        <el-button
          type="primary"
          style="width:100%;"
          @click="handleSubmit"
          :loading="logining"
        >提交</el-button>
      </div>
      <br />
      <el-button
        style="margin-right:80px;"
        @click="toLogin"
      >登录</el-button>
      <el-button
        style="margin-left:80px;"
        @click="toRegister"
      >注册</el-button>
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
        email: "",
        mobile: "",
        password: "",
        comfirmPassword: "",
      },
      rules2: {
        email: [
          {
            required: true,
            message: "please enter your email",
            trigger: "blur",
          },
        ],
        contact: [
          { required: true, message: "enter your contact", trigger: "blur" },
        ],
        password: [
          { required: true, message: "enter your password", trigger: "blur" },
        ],
        comfirmPassword: [
          { required: true, message: "enter your password", trigger: "blur" },
        ],
      },
      checked: false,
    };
  },
  created() {
    this.from = this.$route.query.from;
  },
  methods: {
    async handleSubmit() {
      sessionStorage.setItem("username", this.ruleForm2.username);
      if (
        this.ruleForm2.password.trim() !== this.ruleForm2.comfirmPassword.trim()
      ) {
        this.$message.error("两次密码输入不一致");
      }
      let param = {
        email: this.ruleForm2.email.trim(),
        password: this.encryptDes(this.ruleForm2.password.trim()),
        contact: this.ruleForm2.contact.trim(),
      };
      const result = await this.$http.post("/rest/user/forget", param);
      if (result.data.returnCode !== "200") {
        this.$message.error(result.data.message);
        return;
      }
      this.$router.push({ path: "/login", query: { from: this.from } });
    },
    toLogin() {
      this.$router.push({ path: "/login", query: { from: this.from } });
    },
    toRegister() {
      this.$router.push({ path: "/register", query: { from: this.from } });
    },
    encryptDes(message) {
      const keyHex = cryptoJs.enc.Utf8.parse(this.key);
      const option = { mode: cryptoJs.mode.ECB, padding: cryptoJs.pad.Pkcs7 };
      const encrypted = cryptoJs.DES.encrypt(message, keyHex, option);
      return encrypted.toString();
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 100%;
  height: 100%;
}
.login-page {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  margin: 180px auto;
  width: 350px;
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
