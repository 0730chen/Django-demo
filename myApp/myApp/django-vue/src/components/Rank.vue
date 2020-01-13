<template>
	<div class="Rank">
		<TitleBar/>
    <div class="container"> 
    <OneMoive :MovieMessage="MovieMessage"/>
    <div></div>
		<ViewRank v-on:movie="HandleMovie"/>
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
  private data() {
    return {
      MovieMessage:[]
    }
  }
  HandleMovie(msg:any){
    this.MovieMessage = msg
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