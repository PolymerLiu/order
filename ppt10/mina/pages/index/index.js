//login.js
//获取应用实例
var app = getApp();
Page({
  data: {
    remind: '加载中',
    angle: 0,
    userInfo: {},
    regFlag:true
  },
  goToIndex:function(){
    wx.switchTab({
      url: '/pages/food/index',
    });
  },
  onLoad:function(){
    wx.setNavigationBarTitle({
      title: app.globalData.shopName
    })
  },
  onShow:function(){

  },
  onReady: function(){
    // 进入小程序检验是否已经登录过
    this.checkLogin()
    var that = this;
    setTimeout(function(){
      that.setData({
        remind: ''
      });
    }, 1000);
    wx.onAccelerometerChange(function(res) {
      var angle = -(res.x*30).toFixed(1);
      if(angle>14){ angle=14; }
      else if(angle<-14){ angle=-14; }
      if(that.data.angle !== angle){
        that.setData({
          angle: angle
        });
      }
    });
  },

  checkLogin: function () {
    var data = {}
    var that = this
    wx.login({
      success (res) {
        if (!res.code) {
          app.alert({'content':'登录失败，请再次点击~~'})
          return
        }
        data['code'] = res.code
        wx.request({
          url:app.buildUrl('/member/check-reg'),
          data:data,
          header:app.getRequestHeader(),
          method:'POST',
          success:function (res) {
            if (res.data.code != 200) {
              that.setData({
                regFlag:false
              })
              return
            }
            that.goToIndex()
            app.setCache('token',res.data.data.token)
          }
        })
      }
    })
    
  },
  login:function (e) {
    var data = e.detail.userInfo
    var that = this
    if (!e.detail.userInfo) {
      app.alert({'content':'登录失败，请再次点击~~'})
    }
    wx.login({
      success (res) {
        if (!res.code) {
          app.alert({'content':'登录失败，请再次点击~~'})
          return
        }
        data['code'] = res.code
        wx.request({
          url:app.buildUrl('/member/login'),
          data:data,
          header:app.getRequestHeader(),
          method:'POST',
          success:function (res) {
            if (res.data.code != 200) {
              app.alert({'content':res.data.msg})
              return
            }
            app.setCache('token',res.data.data.token)
            that.goToIndex()
          }
        })
      }
    })
  }
});