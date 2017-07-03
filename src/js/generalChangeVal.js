/**
 * 
 * @authors loliSuri
 * @date    2017-05-31 11:01:47
 * @version $001$
 */
let mouseBtnEv = {
    /**
     * [setNewVal 改变对象或数组中一个元素的值]
     * @AuthorHTL loliSuri
     * @DateTime  2017-05-31T14:15:21+0800
     * @param     {[obj]}                 data   [对象或数组]
     * @param     {[string/number]}       key    [键/索引]
     * @param     {[all]}                 newVal [新值]
	 /**   
     * 受JS限制，Vue 不能检测以下变动的数组：
     * 1.arr[index]=newValue; 2.arr.length = newLength;
     * 上述两种情况可用arr.splice()解决，其中1.还可以使用vue.set方法
     */
	setNewVal: function(data,key,newVal){
		if (typeof key === "string"){//改变对象中元素的值
			data[key] = newVal;
		} else if (typeof key === "number"){//改变数组中元素的值
			data.splice(key, 1, newVal);//this.$set(data, key, newVal);也可实现
		} else {
			console.log("类型错误");
		};
	},
  stopBubble: function(e){
      if ( e && e.stopPropagation ) {
           e.stopPropagation();
      } else { 
           window.event.cancelBubble = true;
      }
  },
  changeTime:function(time){//毫秒数转为XX:XX:XX
    var newtime = new Date(time),
        hours = newtime.getUTCHours(),
        minSecs = newtime.toLocaleTimeString().substr(-5);
    if (hours==0){
         return minSecs;
    } else if (hours<10) {
         return `0${hours}:${minSecs}`;
    } else {
         return `${hours}:${minSecs}`;
    };
  },
  setCommentTime:function(time){
    var presentTime = new Date(),//当前时间
        cmtTime =new Date(time),//评论时间
        diff = presentTime-cmtTime;//当前时间与评论时间差

    //今天
    var today = new Date();
    today.setHours(0);
    today.setMinutes(0);
    today.setSeconds(0);
    //昨天
    var yestoday = new Date(today.getTime()-24*60*60*1000);
    //今年
    var thisYear = new Date(today.getTime());
    thisYear.setMonth(0);
    thisYear.setDate(1);
    
    var timePara = {
      year:cmtTime.getFullYear(),
      month:cmtTime.getMonth()+1,
      date:cmtTime.getDate(),
      hour:cmtTime.getHours()>9?cmtTime.getHours():`0${cmtTime.getHours()}`,
      minute:cmtTime.getMinutes()>9?cmtTime.getMinutes():`0${cmtTime.getMinutes()}`
    };

    if (diff<2*1000){
      return `1秒前` 
    } else if(diff<60*60*1000){
      return `${parseInt(diff/(60*1000))}分钟前`
    } else if(diff<60*60*2*1000) {
      return `1小时前`
    } else {
      if(cmtTime>today||cmtTime==today){
        return `${timePara.hour}:${timePara.minute}`
      } else if(cmtTime>yestoday){
        return `昨天${timePara.hour}:${timePara.minute}`
      } else if(cmtTime>thisYear){
        return `${timePara.month}月${timePara.date}日 ${timePara.hour}:${timePara.minute}`
      } else {
        return `${timePara.year}年${timePara.month}月${timePara.date}日 ${timePara.hour}:${timePara.minute}`
      }
    };
  }
}

export { mouseBtnEv }
