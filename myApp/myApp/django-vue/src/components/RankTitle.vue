<template>
	<div class="titleBar">
		<div class="log">
			<div class="logPic"></div>
			<span>{{Time}}</span>
		</div>
		<div class="barNav" @click="HandleActive">
			<span :class="{active:isActive}">综合票房</span>
			<span :class="{active:!isActive}">
				<router-link :to="{name:'chart',params:{query:Time}}" @click="SelectChart">切换图表</router-link>
				</span>
		</div>
		<div class="full" @click="fullScreen">
			<svg class="icon" aria-hidden="true">
    		<use xlink:href="#icon-quanping"></use>
			</svg>
			</div>
	</div>
</template>
<script lang="ts">
import Vue from 'vue'
import {Component, Watch,Prop} from 'vue-property-decorator'
import screenfull from 'screenfull'

@Component({

})
export default class TitleBar extends Vue {
	@Prop()
	DateSelect:any
	isActive:Boolean = true
	Time:any
	timer:any
	private data(){
		return {
			Time:this.GetTime(),
			screenfull:false,
		}
	}
	 fullScreen() {
            if (!screenfull.isEnabled) {
                return false
            }
            screenfull.toggle()
        }
	SelectChart(){
		console.log('haha')
		console.log(this)
	}
	filterDate(date:any){
		console.log(date)
		let Y = date.FullYear().toString()
		let M = date.getMonth()
		let D = date.getdate()
		M = M.length === 1?`0${M}`:`${M}`
		D = D.lenght === 1?`0{D}`:`${D}`
		return `${Y}${M}${D}`
	}
	HandleActive(){
		this.isActive = !this.isActive
	}

	GetTime(){
		this.Time = new Date()
		let Year = this.Time.getFullYear()
		let Month = this.Time.getMonth()
		let Days = this.Time.getDate()
		let Hours = this.Time.getHours()
		let Min = this.Time.getMinutes()
		let sec = this.Time.getSeconds()
		let Click = `${Year}年${Month+1}月${Days}日${Hours}:${Min}:${sec}`
		if(Hours<10){
			Click = `${Year}年${Month+1}月${Days}日0${Hours}:${Min}:${sec}`
		}else if(Min<10){
			Click = `${Year}年${Month+1}月${Days}日${Hours}:0${Min}:${sec}`
		} else if(sec<10){
			Click = `${Year}年${Month+1}月${Days}日${Hours}:0${Min}:0${sec}`
		}else{

		}
		return Click
	}
	created() {
		let timer = setTimeout(() => {
                   this.Time = this.GetTime()
                },1000);
	}
  updated() {
	   this.timer = setTimeout(() => {
                   this.Time = this.GetTime()
                },1000)
  			}
	destroyed() {
		clearTimeout(this.timer)	
	}
}
</script>
<style lang="scss">
	.titleBar{
	height: 50px;
	line-height: 30px;
    background-color: #30303b;
    position: relative;
    text-align: center;
    font-size: 18px;
	color: whitesmoke;
	.barNav{
	cursor: pointer;
    background-color: #000;
    border-radius: 1rem;
    display: inline-block;
    vertical-align: middle;
	transform: translateY(10px);
		span{
			padding: 0 20px;
			border-radius:20px; 
			margin: 0 5px;
		}
	} 
	.log{
		position: absolute;
		top:0;
		left: 30px;
		transform: translateY(10px);
		display: flex;
		flex-direction: row;
		.logPic{
			border: 1px solid white;
			width: 100px;
			height: 40px;
			display: inline-block;
			background:url(https://i.loli.net/2020/01/10/l7DFVbIHsSrYGLZ.jpg);
			background-size: 50%;
		}
		span{
			padding-left: 20px;
			font-size: 20px;
		}
	}
	.full{
		cursor: pointer;
		position: absolute;
		top:0;
		right: 30px;
		transform: translateY(10px);
	}
	}
	.active{
		background-color: #464556;
	}
</style>