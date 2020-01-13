<template>
	<div class="viewRank">
		<table class="rankTitle movieTitle active">
			<thead>
				<tr>
					<th class="name">影片名称
						<svg class="icon" aria-hidden="true">
    					<use xlink:href="#icon-zu"></use>
						</svg>
					</th>
					<th>综合票房(万)</th>
					<th>票房占比</th>
					<th>排片场次</th>
					<th>排片占比</th>
					<th>场均人次</th>
					<th>上座率</th>			
				</tr>
			</thead>
		</table>
		<table class="rankTitle MovieList">
		<thead  class="movie" v-for=" (item,index) in MovieList" :key="index" :class="{active:index===current}"	@click.prevent="HandleColor(index,$event)">
			<tr>
				<th>{{index+1}}</th>
			<th class="movieName" :title="item.movieName"><p>{{item.movieName}}</p></th>
			<th class="realtime">{{item.boxInfo}}</th>
			<th>{{item.boxRate}}</th>
			<th>{{item.showInfo}}</th>
			<th>{{item.showRate}}</th>
			<th>{{item.avgShowView}}</th>
			<th class="sit">{{item.avgSeatView}}</th>
			</tr>
		</thead>
		</table>			
		</div>
</template>
<script lang="ts">

import Vue from 'vue'
import {Component, Watch,Prop} from 'vue-property-decorator'
import axios from 'axios'

@Component({
	
})
export default class ViewRank extends Vue{
	MovieList:Array<any>|undefined
	flag:Boolean|undefined
	current:number| undefined
	timer:any
	private data(){
		return 	{
		MovieList:[],
		flag:false,
		current:0
		}
	}
  getApi(){
	  return new Promise((resolve,reject)=>{
		  	axios.get('http://127.0.0.1:8000/GetMoive').then(res=>{
	   		this.MovieList = res.data.data.list
	  		resolve()
     	})
	  })
  }
  HandleColor(index:number,e:any){
	  this.current = index
	  const List = (this as any)["MovieList"][index]
	  this.$emit('movie',List)
  }
  created() {
   this.getApi().then(()=>{
	   this.HandleColor(0,event)
   })
  }
  updated() {
		
		//  this.timer = setTimeout(()=>{
		
		// 	this.getApi()
	 	// 	},30000)  
  }
//   destroyed() {
// 	clearTimeout(this.timer)	
//   }
}
</script>
<style lang="scss">
	.viewRank{
		position: relative;
		right:100px;
		top: 0;
		font-size: 25px;
		font-weight: 100;
		height: 700px !important;
		margin-top: 20px;
		background-color:  #30303b;
		color: white;
		border-radius: 10px;
		height: 100vh;
		min-height: 0;
    	overflow: auto;
		display: flex;
		flex-direction: column;
		.movieTitle{
			width: 875px;
			position:fixed;
			height: 100px;
			white-space: nowrap;
			table-layout: fixed;
			margin-top: 0px;
			z-index:100;
			thead{
				tr{
					display: flex;
					flex-direction: row;
					th{
						padding: 0 10px !important;
					}
				}
			}
		}
	}
	.viewRank::-webkit-scrollbar{/*滚动条里面小方块*/
           display: none;
	}

	.movie{
		cursor: pointer;
		tr{
			height: 50px;
		}
	}
	.name{
		width: 220px;
		display: flex;
		flex-direction: row;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}

	.movieName{
		p{
		width: 92px;
		line-height: 1.4;
    	white-space: nowrap;
    	text-overflow: ellipsis;
    	overflow: hidden;
		text-align: start;
		}
	}
	.rankTitle{
		width: 100%;
		border-collapse: separate;
		th{
			padding: 0 20px;
		}
		.realtime{
			color: #ffac00;
		}
		.sit{
			transform: translateX(20px)
		}
		
	}
	.active{
		background-color: #535265 !important;
		border-radius: 10px;
	}
	.MovieList{
		margin-top: 70px;
	}

</style>