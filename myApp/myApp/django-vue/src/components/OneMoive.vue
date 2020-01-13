<template>
	<div class="OneMovie">
		<div class="movieName">{{MovieMessage.movieName}}</div>
		<div>{{MovieMessage.releaseInfo}}</div>
		<div>{{MovieMessage.sumBoxInfo}}</div>
		<div>综合票房</div>
		<div>{{MovieMessage.splitBoxInfo}}万</div>
		<div>票房占比{{MovieMessage.splitBoxRate}}</div>
		<div>排片场次{{MovieMessage.showInfo}}</div>
		<div>排片占比{{MovieMessage.showRate}}</div>
		<div>场均人次{{MovieMessage.avgShowView}}</div>
		<div>上座率{{MovieMessage.avgSeatView}}</div>
	</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios'
import TitleBar from './RankTitle.vue'
import ViewRank from './ViewRank.vue'
@Component({

})
export default class OneMoive extends Vue {
  @Prop()
  MovieMessage:Array<any>|undefined
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
	}
</style>