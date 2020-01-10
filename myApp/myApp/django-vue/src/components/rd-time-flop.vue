<template>
    <div class="rd-clock-card">
        <div
            class="flip"
            v-for="(item, index) in cardNum"
            :key="index"
            :style="{
                width: `${width}px`,
                height: `${height}px`,
                lineHeight: `${height}px`,
                margin: margin,
                fontSize: `${fontSize}px`,
                border: border,
                borderRadius: `${borderRadius}px`,
                boxShadow: boxShadow,
            }"
        >
            <div
                class="digital front"
                :style="{
                    '--pseudoElementColor': pseudoElementColor,
                    '--pseudoElementBg': pseudoElementBg,
                    '--pseudoElementBorder': pseudoElementBorder,
                    '--pseudoElementTopBorderRadius': pseudoElementTopBorderRadius,
                    '--pseudoElementBotBorderRadius': pseudoElementBotBorderRadius,
                    '--pseudoElementBoxShadow': pseudoElementBoxShadow,
                }"
                data-number="0"
            ></div>
            <div
                class="digital back"
                :style="{
                    '--pseudoElementColor': pseudoElementColor,
                    '--pseudoElementBg': pseudoElementBg,
                    '--pseudoElementBorder': pseudoElementBorder,
                    '--pseudoElementTopBorderRadius': pseudoElementTopBorderRadius,
                    '--pseudoElementBotBorderRadius': pseudoElementBotBorderRadius,
                    '--pseudoElementBoxShadow': pseudoElementBoxShadow,
                }"
                data-number="1"
            ></div>
        </div>
    </div>
</template>

<script>
export default {
    name: '',
    props: {
        cardNum: { type: Number, default: 3 },
        width: { type: Number, default: 300 },
        height: { type: Number, default: 400 },
        margin: { type: String, default: '20px' },
        fontSize: { type: Number, default: 100 },
        border: { type: String, default: '1px solid transparent' },
        borderRadius: { type: Number, default: 30 },
        boxShadow: { type: String, default: '0 0 6px rgba(0, 0, 0, 0.5)' },
        pseudoElementColor: { type: String, default: '#fff' },
        pseudoElementBg: { type: String, default: '#3354e2' },
        pseudoElementBorder: { type: String, default: '1px solid #666' },
        pseudoElementTopBorderRadius: { type: String, default: '30px 30px 0 0' },
        pseudoElementBotBorderRadius: { type: String, default: '0 0 30px 30px' },
        pseudoElementBoxShadow: {
            type: String,
            default: '0 -2px 6px rgba(255, 255, 255, 0.3)',
        },
    },
    data() {
        return {
            Flipper: null,
            nowTimeStr: '',
            nextTimeStr: '',
        };
    },
    methods: {
        getTimeFromDate(date) {
            return date
                .toTimeString()
                .slice(0, 8)
                .split(':')
                .join('');
        },
        getTime() {
            const now = new Date();
            this.nowTimeStr = this.getTimeFromDate(new Date(now.getTime() - 1000));
            this.nextTimeStr = this.getTimeFromDate(now);
        },
        flop() {
            const flips = document.querySelectorAll('.flip');
            this.getTime();
            const flippers = Array.from(flips).map((flip, i) => {
                return new this.Flipper(
                    flip,
                    this.nowTimeStr.substring(2 * i, 2 * i + 2),
                    this.nextTimeStr.substring(2 * i, 2 * i + 2)
                );
            });
            setInterval(() => {
                this.getTime();
                for (var i = 0; i < flippers.length; i++) {
                    if (this.nowTimeStr.substring(2 * i, 2 * i + 2) === this.nextTimeStr.substring(2 * i, 2 * i + 2)) {
                        continue;
                    }
                    flippers[i].flipDown(
                        this.nowTimeStr.substring(2 * i, 2 * i + 2),
                        this.nextTimeStr.substring(2 * i, 2 * i + 2)
                    );
                }
            }, 1000);
        },
    },
    mounted() {
        this.Flipper = class Flipper {
            constructor(node, currentTime, nextTime) {
                this.isFlipping = false;
                this.duration = 900;
                this.flipNode = node;
                this.frontNode = node.querySelector('.front');
                this.backNode = node.querySelector('.back');
                this.setFrontTime(currentTime);
                this.setBackTime(nextTime);
            }

            setFrontTime(time) {
                this.frontNode.dataset.number = time;
            }

            setBackTime(time) {
                this.backNode.dataset.number = time;
            }

            flipDown(currentTime, nextTime) {
                if (this.isFlipping) {
                    return false;
                }

                this.isFlipping = true;
                this.setFrontTime(currentTime);
                this.setBackTime(nextTime);
                this.flipNode.classList.add('running');

                setTimeout(() => {
                    this.flipNode.classList.remove('running');
                    this.isFlipping = false;
                    this.setFrontTime(nextTime);
                }, this.duration);
            }
        };
        this.flop();
    },
};
</script>

<style scoped>
.rd-clock-card {
    display: flex;
}

.rd-clock-card .flip {
    position: relative;
    text-align: center;
}

.rd-clock-card .flip .digital::before,
.rd-clock-card .flip .digital::after {
    position: absolute;
    content: attr(data-number);
    left: 0;
    right: 0;
    color: var(--pseudoElementColor);
    background: var(--pseudoElementBg);
    overflow: hidden;
    perspective: 160px;
}

.rd-clock-card .flip .digital::before {
    top: 0;
    bottom: 50%;
    border-bottom: var(--pseudoElementBorder);
    border-radius: var(--pseudoElementTopBorderRadius);
}

.rd-clock-card .flip .digital::after {
    top: 50%;
    bottom: 0;
    line-height: 0;
    border-radius: var(--pseudoElementBotBorderRadius);
}

.rd-clock-card .flip .back::before,
.rd-clock-card .flip .front::after {
    z-index: 1;
}

.rd-clock-card .flip .back::after {
    z-index: 2;
}

.rd-clock-card .flip .front::before {
    z-index: 3;
}

.rd-clock-card .flip .back::after {
    transform-origin: center top;
    transform: rotateX(0.5turn);
}

.rd-clock-card .flip.running .front::before {
    transform-origin: center bottom;
    animation: frontFlipDown 1s ease-in-out;
    box-shadow: var(--pseudoElementBoxShadow);
    /* box-shadow: 0 -2px 6px rgba(255, 255, 255, 0.3); */
    backface-visibility: hidden;
}

.rd-clock-card .flip.running .back::after {
    animation: backFlipDown 1s ease-in-out;
}

@keyframes frontFlipDown {
    to {
        transform: rotateX(0.5turn);
    }
}

@keyframes backFlipDown {
    to {
        transform: rotateX(0);
    }
}
</style>
