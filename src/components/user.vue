<template>
  <div class="main">
    <div class="userhome" v-if="user">
      <div class="uh-head">
        <img :src="user.img">
        <div class="uh-des">
          <div class="uhd-head">
            <h2>
              <span>{{user.name}}</span>
              <span class="userLv">
                <em>{{user.level}}</em>
                <i></i>
              </span>
              <i :class="user.gender"></i>
              <a href="javascript:;" class="sendMsg"><i>发私信</i></a>
              <a href="javascript:;" class="follow"><i>关&nbsp&nbsp注&nbsp</i></a>
            </h2>
          </div>
          <ul class="uhd-conect">
            <li id="li-frt">
              <a href="javascript:;"><strong>{{user.events}}</strong></br>动态</a>
            </li>
            <li>
              <router-link :to="`/user/${this.$route.params.id}/fav`"><strong>{{user.follows}}</strong></br>关注</router-link>
            </li>
            <li>
             <router-link :to="`/user/${this.$route.params.id}/fans`"><strong>{{user.fans}}</strong></br>粉丝</router-link>
            </li>
          </ul>
          <!-- <p class="self-intro" v-if="user.signature">{{`个人介绍：${user.signature}`}}</p> -->
          <p class="uh-loca"><span>{{user.location}}</span><span>年龄：95后</span></p>
          <p class="uh-social">社交网络：<a href="" title="新浪微博" class="weibo"></a></p>
        </div>
      </div>
      <router-view></router-view>
    </div>
    <div class="loading" v-if="!user">
      <i></i>
      加载中...
    </div> 
  </div>
</template>

<script>

export default {
  name: 'user',
  data () {
    return {
      user:null,
      userUrl: `http://123.206.211.77:33333/api/v1/user/${this.$route.params.id}/detail`,
      reg: /\d+/g,
    }
  },
  created:function(){
    //请求歌单数据
    this.$http.get(this.userUrl)
      .then(response => {
          this.user = response.data.detail;//初始化用户基本信息
          //更改页面title
          document.title = `${this.user.name} - 网易云音乐`;
      })
      .catch(response => {
        console.log(response)
    });
  },
  watch:{
    '$route' (to, from) {
      var reg = this.reg,
          toUser = to.path.match(reg),
          fromUser = from.path.match(reg);

      if (toUser[0] !== fromUser[0]){//从当前用户页面跳转至另一个用户页面
        this.user = null;

        this.$http.get(`http://123.206.211.77:33333/api/v1/user/${toUser}/detail`)
          .then(response => {
              this.user = response.data.detail;//初始化用户基本信息
              //更改页面title
              document.title = `${this.user.name} - 网易云音乐`;
          })
          .catch(response => {
            console.log(response)
          });
      }
    }
  }
}
</script>

<style>
.weibo{
  background: url(../assets/logo.png) no-repeat scroll 0 0;
}
.uh-social a{
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-right: 20px;
  vertical-align: middle;
}
.uh-loca{
  overflow: hidden;
}
.uh-loca span{
  margin-right: 20px;
}
.uhd-conect{
  list-style-type: none;
  padding: 0;
  overflow: hidden;
}
.uhd-conect li{
  float: left;
  padding:0 40px 0 20px;
  border-left: 1px solid rgb(221,221,221);
  text-align: center;
}
.uhd-conect strong{
  font-size: 24px;
  font-weight: normal;
}
.uhd-conect a:hover{
  color: #4996d1;
}
#li-frt{
  border:0;
}
.uhd-head{
  overflow: hidden;
  padding-bottom: 10px;
  border-bottom: 1px solid rgb(221,221,221);
}
.follow{
  float: left;
  width: 40px;
  height: 31px;
  margin: 4px 0 0 15px;
  padding-left: 30px;
  background: url(../assets/button.png) no-repeat scroll 0 -720px;
  line-height: 31px;
  color: white;
}
.sendMsg{
  float: left;
  width: 75px;
  height: 31px;
  margin: 4px 0 0 15px;
  background: url(../assets/button.png) no-repeat scroll 0 -810px;
  line-height: 31px;
}
.sendMsg i,.follow i{
  float: right;
  margin-right: 8px;
}
.female{
  float: left;
  width: 20px;
  height: 20px;
  margin: 8px 0 0 9px;
  background: url(../assets/icon.png) no-repeat scroll -41px -27px;
}
.male{
  float: left;
  width: 20px;
  height: 20px;
  margin: 8px 0 0 9px;
  background: url(../assets/icon.png) no-repeat scroll -41px -57px;
}
.userLv{
  height: 19px;
  padding-left: 29px;
  margin: 8px 0 0 10px;
  background: url(../assets/icon2.png) no-repeat scroll -135px -190px;
  color: rgb(224,58,36);
  font-size: 14px;
  line-height: 21px;
  font-weight: bold;
  vertical-align: middle;
}
.userLv em{
  float: left;
}
.userLv i{
  float: right;
  width: 9px;
  height: 19px;
  background: url(../assets/icon2.png) no-repeat scroll -191px -190px;
}
.uh-des{
  padding-left: 228px;
  height: 197px;
}
.uh-des p{
  font-size: 12px;
  line-height: 21px;
  margin: 0 0 5px 0;
}
.uh-des h2{
  float: left;
  margin: 0;
  font-size: 22px;
  font-weight: normal;
  color: black;
  line-height: 35px;
}
.uh-des span{
  float: left;
}
.uh-head{
  position: relative;
  margin-bottom: 43px;
  text-align: left;
}
.uh-head img{
  position: absolute;
  top:0;
  width: 188px;
  height: 188px;
  padding: 3px;
  border: 1px solid rgb(213,213,213);
}
.userhome{
  padding: 40px;
}
</style>

