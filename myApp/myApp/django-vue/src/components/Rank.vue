<template>
	<div class="Rank">
		<TitleBar/>
    <div class="container"> 
    <OneMoive :MovieMessage="MovieMessage" :MovieData="MovieData"/>
    <div></div>
		<ViewRank v-on:movie="HandleMovie" v-on:Data="HandleDate"/>
    </div>
	</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios'
import TitleBar from './RankTitle.vue'
import ViewRank from './ViewRank.vue'
import OneMoive from './OneMoive.vue'
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
  private data() {
    return {
      MovieMessage:[],
      MovieData:{}
    }
  }
  HandleMovie(msg:any){
    this.MovieMessage = msg
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