import Vue from 'vue'
import Router from 'vue-router'
import origin from '@/components/origin'
import foot from '@/components/foot'
import originlist from '@/components/origin-list'
import playlist from '@/components/play-list'

Vue.use(Router)

export default new Router({
	mode:'history',//切换路径模式，变成history模式,不然路径为/#/home
	scrollBehavior:()=>({ //滚动条滚动的行为，不加这个默认就会记忆原来滚动条的位置
		y:0
	}),
	routes: [
		{
			path: '/',component: origin,		  
		},
		{
			path: '/home',component: origin,
			children:[
				{path:'discover',component:origin},
				{path:'foot',component:foot},
			]
		},   
		{
			path: '/use/playlist',component: originlist,		  
		},
		{
			path: '/use/playlist/:id',component: playlist,	
		},
	]
})

