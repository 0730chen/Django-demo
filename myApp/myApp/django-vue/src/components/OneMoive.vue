<template>
	<div class="OneMovie">
		<div class="movieName">
			{{MovieMessage.movieName}}
		</div>
		<div>{{MovieMessage.releaseInfo}}&nbsp;&nbsp;<span>{{MovieMessage.sumBoxInfo}}</span></div>
		<div>综合票房</div>
		<div class="Info">{{MovieMessage.splitBoxInfo}}万</div>
		<div>票房占比<span>&nbsp;&nbsp;{{MovieMessage.splitBoxRate}}</span></div>
		<div>排片场次<span>&nbsp;&nbsp;{{MovieMessage.showInfo}}</span></div>
		<div>排片占比<span>&nbsp;&nbsp;{{MovieMessage.showRate}}</span></div>
		<div class="avgView">
		<div>场均人次<h3>{{MovieMessage.avgShowView}}</h3></div>
		<div>上座率<h3>{{MovieMessage.avgSeatView}}</h3></div>
		</div>
		<DaySelect :MovieData= "MovieData"/>	
	</div>
</template>
<script lang="ts">

import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios'
import DaySelect from './DaySelect.vue'
@Component({
	components:{
		DaySelect
	}
})
export default class OneMoive extends Vue {
  @Prop()
  MovieMessage:Array<any>|undefined
  @Prop()
  MovieData:any
  private data() {
	  return {
	  }
  }
  created() {
	  
  }
}
</script>
<style lang="scss">
	.OneMovie{
		width: 400px;
		position: relative;
		top: 0;
		left: 100px;
		background-color:  #30303b;
		margin-top: 20px;
		color: white;
		display: flex;
		flex-direction: column;
		font-size: 20px;
		div{
			padding: 10px 0;
		}
		.movieName{
			font-size: 35px;

		}
	}
	.avgView{
		display: flex;
		justify-content: center;
		flex-direction: row;
		div{
			padding: 0 10px;
		
		}
	}
	.Info{
		
		color:#ffac00;
	}
</style>