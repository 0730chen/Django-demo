<template>
    <div class="Data" @click.self="HandAll">
        <input type="text" autocomplete="off" placeholder="选择时间" v-model="DatePick" @click="HandleDatePick"
               readonly="true">
        <div class="AllDate" v-if="active">
            <div class="DateHeader">
                <button type="button" aria-label="前一年" class="prevYear" @click="ClickLeft">
                    <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-left-copy"></use>
                    </svg>
                </button>
                <button type="button" aria-label="前一月" class="prevMonth" @click="ClickLeftMouth">
                    <svg class="icon" aria-hidden="true">
                        <use xlink:href="#icon-left-copy"></use>
                    </svg>
                </button>
                <span role="button" class="HeaderYear">{{Year}}</span>
                <span role="button" class="HeaderMouth">{{Mouth}}</span>
                <button type="button" aria-label="后一年" class="nextYear" @click="ClickRightMouth">
                    <svg class="icon right" aria-hidden="true">
                        <use xlink:href="#icon-left-copy"></use>
                    </svg>
                </button>
                <button type="button" aria-label="后一月" class="nextYear" @click="ClickRight">
                    <svg class="icon right" aria-hidden="true">
                        <use xlink:href="#icon-left-copy"></use>
                    </svg>
                </button>
            </div>
            <div class="DateContainer">
                <ul class="WeekHeader">
                    <div v-for="(item,index) in WeekDay" :key="index" class="Headeritem">
                        <li>{{item}}</li>
                    </div>
                </ul>
                <div class="MouthDay" @click="HandleClick">
                    <ul v-for="(item,index) in AllDay" :key="index" @click="SetDate">
                        <li>{{item}}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
    import Vue from 'vue'
    import Component from "vue-class-component"

    @Component({})
    export default class DataPicker extends Vue {
        name: String | undefined
        active: Boolean | undefined
        AllDay: any
        Year: any
        Mouth: any
         strDate:string

        private data() {
            return {
                name: '日历组件',
                DataPicker: '',
                Year: new Date().getFullYear(),
                Mouth: new Date().getMonth() + 1,
                active: false,
                WeekDay: ['一', '二', '三', '四', '五', '六', '日'],
                AllDay: [],
                strDate:''
            }
        }
        HandleClick(e){
            let day = e.target.innerText
            this.strDate = `${this.Year}-${this.Mouth}-${day}`
            let str = ''
            if(this.Mouth<10){
                let str = `${this.Year}0${this.Mouth}${day}`
            }else if(day<10){
                let str = `${this.Year}${this.Mouth}0${day}`
            }else{
                str=`${this.Year}${this.Mouth}${day}`
            }
            this.$emit('Date',this.strDate) 
        }
        HandleDatePick() {
            if (!this.active) {
                this.active = !this.active
            } else {

            }
        }

        HandAll() {
            if (this.active) {
                this.active = !this.active
            } else {

            }
        }

        ClickRight() {
            this.Year = this.Year + 1
            this.FullDay(this.Year, this.Mouth)
        }

        ClickRightMouth() {
            this.Mouth = this.Mouth + 1
            if (this.Mouth === 13) {
                this.Mouth = 1
                this.Year = this.Year + 1
            }
            this.FullDay(this.Year, this.Mouth)
        }

        ClickLeft() {
            this.Year = this.Year - 1
            this.FullDay(this.Year, this.Mouth)
        }

        ClickLeftMouth() {
            this.Mouth = this.Mouth - 1
            if (this.Mouth === 0) {
                this.Mouth = 12
                this.Year = this.Year - 1
            }
            this.FullDay(this.Year, this.Mouth)
        }

        SetDate(e: any) {
            let data = e.target.innerText
        }

        FullDay(Y: undefined, M: undefined) {
            let date = new Date(this.Year, this.Mouth - 1)

            let FirstDay = new Date(date.getFullYear(), this.Mouth - 1, 1)
            date.setMonth(date.getMonth() + 1);
            date.setDate(0);
            //再获取天数即取上个月的最后一天的天数
            let days = date.getDate()//当前月的全部天数
            //获取前一个月的天数
            //当前月的全部天数
            //当前月的第一天
            switch (FirstDay.getDay()) {
                case 0:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay() + 7; i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 1:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay() - 1; i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 2:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay(); i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 3:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay(); i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 4:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay(); i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 5:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay(); i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
                case 6:
                    this.AllDay = []
                    for (let i = 1; i < FirstDay.getDay(); i++) {
                        this.AllDay.push(' ')
                    }
                    for (let i = 1; i < days + 1; i++) {
                        this.AllDay.push(i)
                    }
                    break;
            }
        }

        get DatePick() {
            //得到年
            let Data = new Date()
            let Y = Data.getFullYear()//年份
            let M = Data.getMonth() + 1//月份
            let D = Data.getDate()//日期
            let W = Data.getDay()//星期
            let H = Data.getHours()
            let Min: any = Data.getMinutes()
            let WeekHash: any = {
                0: '星期一',
                1: '星期二',
                2: '星期三',
                3: '星期四',
                4: '星期五',
                5: '星期六',
                6: '星期天',
            }
            if (Min < 10) {
                Min = `0` + Min
            } else {
                Min = Min
            }
            let Week = WeekHash[W]
            return `${Y}-${M}-${D}   ${Week}  ${H}:${Min}`
        }

        set DatePick(param: any) {
            console.log(param);
        }

        // @Watch('DataPick', {immediate: true, deep: true})
        //定义事件获取
        created() {
            this.FullDay(this.Year, this.Mouth)
        }
    }
</script>
<style lang="scss" scoped>
    .Data {
        input {
            height: 30px;
            padding: 0 20px;
            cursor: pointer;
        }

        padding: 100px 20px;
    }

    .right {
        transform: rotate(180deg);
    }

    .DateHeader {
        margin: 12px;
        text-align: center;

        .HeaderYear {
            padding: 0 6px;
            cursor: pointer;
        }

        .HeaderMouth {
            padding: 0 6px;
            cursor: pointer;
        }
    }

    button {
        font-size: 12px;
        border: 0;
        cursor: pointer;
        outline: none;
        margin: 0 20px;
    }

    .AllDate {
        width: 500px;
        margin: 0 auto;
    }

    .WeekHeader {
        display: flex;
        flex-direction: row;
        justify-content: center;

        .Headeritem {
            flex: 1;
        }
    }

    .MouthDay {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;

        ul {
            width: 71px;
            height: 28px;
            padding: 5px 10px;
            cursor: pointer;
        }

        li:hover {
            border: 1px solid black;
            background-color: #00C8D5;
        }
    }

    .active {
        /*background-color:*/
        border: 1px solid black;
    }
</style>