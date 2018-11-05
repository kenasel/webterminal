<template>
    <div class="webssh-container">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>Web终端</span>
          </div>
          <el-form :inline="true" :model="terminal" class="demo-form-inline">
            <el-form-item label="Hosts">
              <el-input v-model="terminal.hosts" placeholder="Hosts"></el-input>
            </el-form-item>
            <el-form-item label="Port">
              <el-input v-model="terminal.port" placeholder="端口"></el-input>
            </el-form-item>
            <el-form-item label="Username">
              <el-input v-model="terminal.username" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item label="Password">
              <el-input type="password" v-model="terminal.password" placeholder="密码"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onConnect">连接</el-button>
              <el-button type="primary" @click="onReset">重置</el-button>
            </el-form-item>
          </el-form>
          <div v-if="connect" class="web-terminal">
            <my-terminal :terminal="terminal"></my-terminal>
          </div>
        </el-card>
    </div>
</template>

<script>
import Console from '@/components/Console'

export default {
  name: 'webssh',
  data() { 
    return {
      connect: false,
      terminal: {
        pid: 1,
        name: 'terminal',
        cols: 400,
        rows: 400,
        hosts: '',
        port: 22,
        username: '',
        password: ''
      }
    }
  },
  created() {
  },
  methods: {
    onConnect() { 
      this.connect = true
    },
    onReset() { 
      this.terminal.hosts = ''
      this.terminal.port = 22
      this.terminal.username = ''
      this.terminal.password = ''
      this.connect = false
    }
  },
  components: {
    'my-terminal': Console
  }
}
</script>

<style rel="stylesheet/css" lang="css" scoped>
.webssh-container {
    margin-left: 15px;
}
</style>
