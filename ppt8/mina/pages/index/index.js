//login.js
//获取应用实例
var app = getApp();
Page({
  data: {
    remind: '加载中',
    angle: 0,
    userInfo: {}
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
  login:function (e) {
    if (!e.detail.userInfo) {
      app.alert({'content':'登录失败，请再次点击~~'})
    }
    var data = e.detail.userInfo
    wx.login({
      success (res) {
        if (!res.code) {
          app.alert({'content':'登录失败，请再次点击~~'})
          return
        }
        data['code'] = res.code
        wx.request({
          url:'http://192.168.1.8:8000/api/member/login',
          data:data,
          header:app.getRequestHeader(),
          method:'POST',
          success:function (res) {
            app.console(res)
          },
          fail:function () {
          
          }
        })
      }
    })
  }
});