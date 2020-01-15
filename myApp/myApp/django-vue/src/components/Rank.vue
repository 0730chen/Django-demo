<template>
	<div class="Rank">
		<TitleBar/>
    <div class="container"> 
    <OneMoive :MovieMessage="MovieMessage" :MovieData="MovieData" v-on:DateSelect = "HandleDateSelect"/>
    <div></div>
		<ViewRank v-on:movie="HandleMovie" v-on:Data="HandleDate" :DateSelect="DateSelect"/>
    </div>
	</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios'
import TitleBar from './RankTitle.vue'
import ViewRank from './ViewRank.vue'
import OneMoive from './OneMoive.vue'
import DateSelect from './DaySelect.vue';
@Component({
	components:{
		TitleBar,
    ViewRank,
    OneMoive
	}
})
export default class HelloWorld extends Vue {
  @Prop() 
  private msg!: string;
  MovieMessage!:Array<any>
  MovieData:Object|undefined
  DateSelect:string|undefined  
  private data() {
    return {
      MovieMessage:[],
      MovieData:{},
      DateSelect:''
    }
  }
  HandleMovie(msg:any){
    this.MovieMessage = msg
  }
  HandleDateSelect(msg:any){
    this.DateSelect = msg
  }
  HandleDate(date:any){
    this.MovieData = date
    
  }
  
}
</script>
<style lang="scss">
	.container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: #000;
  }

</style>