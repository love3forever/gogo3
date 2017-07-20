import Vue from 'vue'
import Router from 'vue-router'
import origin from '@/components/origin'
import foot from '@/components/foot'
import originlist from '@/components/origin-list'
import playlist from '@/components/play-list'
import song from '@/components/song'
import track from '@/components/track'
import user from '@/components/user'
import fans from '@/components/user-fans'
import fav from '@/components/user-fav'
import gens from '@/components/user-general'
import artist from '@/components/artist'
import artisthot from '@/components/artist-hot'
import artistalbum from '@/components/artist-album'

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
			path: '/user/:id',component: user,	
			children :[
				{path:'',component:gens},
				{path:'fans',component:fans},
				{path:'fav',component:fav},
			]		  
		},
		{
			path: '/artist/:id',component: artist,	
			children:[
				{path:'',component:artisthot},
				{path:'hot',component:artisthot},
				{path:'album',component:artistalbum}
			]
		},
		{
			path: '/album/:id',component: track,	
		},
		{
			path: '/playlist/:id',component: playlist,	
		},
		{
			path: '/song/:id',component: song,	
		},
	]
})

