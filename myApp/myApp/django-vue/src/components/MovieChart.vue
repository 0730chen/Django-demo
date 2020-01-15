<template>
	<div class="MovieChart">
		<div class="back"><router-link to="/">返回首页</router-link></div>
		<div id ="main"></div>
	</div>
</template>

<script lang="ts">
import Vue from 'vue'
import {Component, Watch} from 'vue-property-decorator'
import Echarts from 'echarts'
import axios from 'axios'
@Component({

})
export default class MovieChart extends Vue{
	$route:any
	allMovieData:Object|undefined
	res:any
	list:Array<any>
	private data() {
		return {
			allMovieData:{}
		}
	}

	filterDate(date:any = new Date()){

		let Y = date.getFullYear()
		let M = date.getMonth().toString()
		let D = date.getDate().toString()
		M = M.length === 1?`${M+1}`:`${M+1}`
		D = D.lenght === 1?`0${D}`:`${D}`

		return `${Y}${M}${D}`
	}

	  getApi(arg:any){
	  return new Promise((resolve,reject)=>{
		  	axios.get(`http://127.0.0.1:8000/GetMoive?beginDate=${arg}`).then(res=>{
			   let result = res.data.data
	  		   resolve(result)
     	})
	  })
  }
	CreateEchart(data){
		let myChart = Echarts.init(document.getElementById('main'));
		myChart.setOption({data});
	}
	created() {
		let date = this.$route.params.query
		let arg = this.filterDate(date)
		this.getApi(arg).then(res=>{
			let Xname = []
			let Obj = {
				title:{
					text:''
				},
				xAxis:{
					data:[]
				},
					series: [{
        			name: '销量',
        			type: 'bar',
        			data: [5, 20, 36, 10, 10, 20]
    			}]
				
			};
			(res as any).list.forEach((item,index)=>{
				Xname.push(item.movieName)
			})

			Obj.title.text= (res as any).updateInfo
			Obj.xAxis.data = Xname
			this.allMovieData = Obj
		})
	}
	mounted() {
		console.log(this.allMovieData)
		let options = this.allMovieData
		this.CreateEchart(options)	
	}
	// @Watch('$route',{deep:true})
	// getRouter(){

	// 	console.log(this)
	// }
}

</script>
<style lang="scss">
.MovieChart{
	background-color: white !important
}
	.back{
		position: fixed;
		left: 10;
		top: 10;
	}
	#main{
		margin: 0 auto;
	}
</style>