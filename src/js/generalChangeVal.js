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
}

export { mouseBtnEv }
