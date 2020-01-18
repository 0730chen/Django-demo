<template>
    <div class="MovieChart">
        <div class="back">
            <router-link to="/">返回首页</router-link>
        </div>
        <div id="main" ref='main' style="width: 1200px;height:400px;"></div>
    </div>
</template>

<script lang="ts">
    import Vue from 'vue'
    import {Component, Watch} from 'vue-property-decorator'
    import Echarts from 'echarts'
    import axios from 'axios'

    @Component({})
    export default class MovieChart extends Vue {
        $route: any
        allMovieData: any | undefined
        res: any
        list: Array<any> | undefined

        private data() {
            return {
                allMovieData: {}
            }
        }

        filterDate(date: any = new Date()) {

            let Y = date.getFullYear()
            let M = date.getMonth().toString()
            let D = date.getDate().toString() as string
            M = M.length === 1 ? `${M + 1}` : `${M + 1}`
            D = D.length === 1 ? `0${D}` : `${D}`

            return `${Y}${M}${D}`
        }

        getApi(arg: any) {
            return new Promise((resolve, reject) => {
                axios.get(`http://127.0.0.1:8000/GetMoive?beginDate=${arg}`).then(res => {
                    let result = res.data.data
                    resolve(result)
                })
            })
        }

        CreateEchart(data: any) {
            let myChart = Echarts.init(this.$refs.main as any)
            console.log(data);
            myChart.setOption(data)
        }

        created() {
            let date = this.$route.params.query
            let arg = this.filterDate(date)
            this.getApi(arg).then(res => {
                let setOptions = {
                    title: {
                        text: '电影票房'
                    },
                    tooltip: {},
                    legend: {
                        data: ['票房']
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        interval: 0,
                        data: []
                    },
                    yAxis: {},
                    series: [
                        {
                            name: '票房',
                            type: 'line',
							data:[]
                        },
                    ]
                };
                (res as any).list.forEach((item: any, index: number) => {
                    // Xname.push(item.movieName)
                    console.log(item);
                    (setOptions.xAxis.data as any).push(item.movieName);
					(setOptions.series[0].data as any).push(parseInt(item.sumBoxInfo))
                })
                // Obj.title.text= (res as any).updateInfo
                // Obj.xAxis.data = Xname
                this.allMovieData = setOptions
            }).then(() => {
                let date = this.allMovieData
                this.CreateEchart(date)
            })
        }

        mounted() {

        }

        // @Watch('$route',{deep:true})
        // getRouter(){

        // 	console.log(this)
        // }
    }

</script>
<style lang="scss">
    .MovieChart {
    }

    .back {
        position: fixed;
        left: 10px;
        top: 10px;

        a {
            color: #1f1f1f;
        }
    }

    #main {
        margin: 0 auto;
    }
</style>