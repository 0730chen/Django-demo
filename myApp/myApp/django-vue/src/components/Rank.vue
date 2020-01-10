<template>
	<div class="Rank">
		<TitleBar/>
		票房排行
	</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios'
import TitleBar from './RankTitle.vue'
@Component({
	components:{
		TitleBar
	}
})
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;
  getApi(){
    // axios.get('http://127.0.0.1:8000/GetMoive').then(res=>{
    //   console.log(res.data)
    // })
  }
  created() {
   this.getApi() 
  }
}
</script>
<style lang="scss">
	
</style>