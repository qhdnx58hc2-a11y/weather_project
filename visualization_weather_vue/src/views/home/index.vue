<template>
  <div id="module">
    <el-container>
      <!--左侧导航 -->
      <Nav />
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="modifyPassword"
                >修改密码</el-dropdown-item
              >
              <el-dropdown-item @click.native="logout"
                >退出登录</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
          <span>{{ username }}&nbsp;&nbsp;</span>
          <el-avatar
            :src="user.image"
            style="margin-left: 10px; vertical-align: middle"
          >
            <el-avatar icon="el-icon-user-solid"></el-avatar>
          </el-avatar>
        </el-header>
        <!-- 主体部分 -->
        <el-main>
          <Breadcrumb />
          <br />
          <router-view />
        </el-main>
      </el-container>
    </el-container>
    <el-dialog title="修改密码" :visible.sync="dialogFormVisible">
      <el-form :model="form" :rules="rules" ref="ruleForm">
        <el-form-item
          label="旧密码："
          prop="oldPassword"
          :label-width="formLabelWidth"
        >
          <el-input
            type="password"
            v-model="form.oldPassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="新密码："
          prop="newPassword"
          :label-width="formLabelWidth"
        >
          <el-input
            type="password"
            v-model="form.newPassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="确认新密码："
          prop="confirmPassword"
          :label-width="formLabelWidth"
        >
          <el-input
            type="password"
            v-model="form.confirmPassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="confirmPassword">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import Nav from "./Nav";
import Breadcrumb from "./Breadcrumb";
import cryptoJs from "crypto-js";
export default {
  data() {
    const confirmPass = (rule, value, callback) => {
      if (value) {
        if (this.form.newPassword !== value) {
          callback(new Error("两次输入的密码不一致"));
        } else {
          callback();
        }
      } else {
        callback(new Error("请再次输入密码"));
      }
    };
    return {
      key: "rest@126.com",
      dialogFormVisible: false,
      username: "",
      form: {
        oldPassword: "",
        newPassword: "",
        confirmPassword: "",
      },
      rules: {
        oldPassword: [
          { required: true, message: "请输入旧密码", trigger: "blur" },
        ],
        newPassword: [
          { required: true, message: "请输入新密码", trigger: "blur" },
          { min: 6, message: "密码长度不低于 6 个字符", trigger: "blur" },
        ],
        confirmPassword: [
          { required: true, validator: confirmPass, trigger: "blur" },
        ],
      },
      formLabelWidth: "120px",
      user: {},
    };
  },
  components: { Nav, Breadcrumb },
  created() {
    this.username = sessionStorage.getItem("username");
    this.user = JSON.parse(sessionStorage.getItem("user"));
  },
  methods: {
    forwardIndex() {
      this.$router.push("/operaList");
    },
    async confirmPassword() {
      this.$refs["ruleForm"].validate(async (valid) => {
        if (valid) {
          let user = JSON.parse(sessionStorage.getItem("user"));

          let param = {
            uid: user.uid,
            oldPassword: this.form.oldPassword.trim(),
            newPassword: this.form.newPassword.trim(),
            confirmPassword: this.form.confirmPassword.trim(),
          };
          const result = await this.$http.post("/rest/user/reset", param);
          if (result.data.returnCode !== "200") {
            this.$message.error(result.data.message);
            return;
          }
          this.$message.success("修改成功！");
          this.dialogFormVisible = false;
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    modifyPassword() {
      this.dialogFormVisible = true;
    },
    //退出登录
    logout() {
      sessionStorage.removeItem("username");
      sessionStorage.removeItem("loginToken");
      this.$router.push("/login");
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
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}
.el-avatar {
  box-shadow: 0 0 0 1px #ffffff;
}
</style>
