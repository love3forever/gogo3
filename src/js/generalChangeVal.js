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
