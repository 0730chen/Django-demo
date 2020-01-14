<template>
	<div class="dateSelect">
		<input type="text" autocomplete="off" placeholder="选择时间" v-model="DatePicker" readonly="true">
		<div class="nowData">实时数据:&nbsp;&nbsp;{{MovieData.Total}}万</div>	
	</div>
</template>
<script lang="ts">
import Vue from 'vue'
import {Component, Watch,Prop} from 'vue-property-decorator'
@Component({

})
export default class DateSelect extends Vue {
	@Prop()
	MovieData:any
	private data() {
		return {
			name:'日历',
		}
	}
	get DatePicker(){
			let Data = new Date()
         let Y = Data.getFullYear()//年份  例如2020判断年份
         let M = Data.getMonth() + 1//月份 0-11判断当前月份
         let D = Data.getDate()//日期
         let W = Data.getDay()//星期
         let H = Data.getHours()
         let Min:any = Data.getMinutes()
		 let Sec:any = Data.getSeconds()
         let WeekHash: any = {
                0: '星期一',
                1: '星期二',
                2: '星期三',
                3: '星期四',
                4: '星期五',
                5: '星期六',
                6: '星期天',
                    }
                if (Min < 11) {
                    Min = `0` + Min
                    } else {
                        Min = Min
                    }
				if(Sec<10){
					Sec = `0`+Sec
				}else{
					Sec = Sec
				}
                let Week = WeekHash[W]
        return `${Y}-${M}-${D} ${Week}  ${H}:${Min}:${Sec}`
	}
}
</script>
<style lang="scss">
	.dateSelect{
		margin-top: 20px;
		input{
			font-size: 18px;
			background-color: #535265 ;
			color: white;
			border: none;
			height: 50px;
			border-radius: 20px;
		}
		.nowData{
			color:rgb(255,131,68)
		}
	}
</style>