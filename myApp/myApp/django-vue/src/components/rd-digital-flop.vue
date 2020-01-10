<template>
  <div class="rd-flop">
    <div class="rd-clock-card" v-if="currData">
      <div
        class="flip"
        :style="{
          width: `${width}px`,
          height: `${height}px`,
          lineHeight: `${height}px`,
          margin: margin,
          fontSize: `${fontSize}px`,
          border: border,
          borderRadius: `${borderRadius}px`,
          boxShadow: boxShadow,
          '--threeColumnMargin': threeColumnMargin
        }"
        v-for="(item, index) in currValue.length"
        :key="index"
      >
        <div
          class="digital front"
          :style="{
            '--pseudoElementColor': pseudoElementColor,
            '--pseudoElementBg': pseudoElementBg,
            '--pseudoElementBorder': pseudoElementBorder,
            '--pseudoElementTopBorderRadius': pseudoElementTopBorderRadius,
            '--pseudoElementBotBorderRadius': pseudoElementBotBorderRadius,
            '--pseudoElementBoxShadow': pseudoElementBoxShadow
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
            '--pseudoElementBoxShadow': pseudoElementBoxShadow
          }"
          data-number="1"
        ></div>
      </div>
    </div>
    <p :style="{ margin: titleMargin, fontSize: `${titleFontSize}px` }">
      {{ category }}
    </p>
  </div>
</template>

<script>
export default {
  name: "",
  props: {
    currData: {
      type: Object,
      default: () => ({ value: "0" })
    },
    nextData: {
      type: Object,
      default: () => ({ value: "0" })
    },
    title: String,
    width: { type: Number, default: 300 },
    height: { type: Number, default: 400 },
    margin: { type: String, default: "5px" },
    threeColumnMargin: { type: String, default: "5px 30px 5px 5px" },
    fontSize: { type: Number, default: 100 },
    border: { type: String, default: "1px solid transparent" },
    borderRadius: { type: Number, default: 30 },
    boxShadow: { type: String, default: "0 0 6px rgba(0, 0, 0, 0.5)" },
    pseudoElementColor: { type: String, default: "#fff" },
    pseudoElementBg: { type: String, default: "#3354e2" },
    pseudoElementBorder: { type: String, default: "1px solid #666" },
    pseudoElementTopBorderRadius: { type: String, default: "30px 30px 0 0" },
    pseudoElementBotBorderRadius: { type: String, default: "0 0 30px 30px" },
    pseudoElementBoxShadow: {
      type: String,
      default: "0 -2px 6px rgba(255, 255, 255, 0.3)"
    },
    titleMargin: { type: String, default: "20px 0 0 0" },
    titleFontSize: {
      type: Number,
      default: 30
    }
  },
  data() {
    return {
      Flipper: null,
      flippers: null
    };
  },
  watch: {
    currData() {
      for (var i = 0; i < this.flippers.length; i++) {
        if (this.currValue[i] === this.nextValue[i]) {
          continue;
        }
        this.flippers[i].flipDown(this.currValue[i], this.nextValue[i]);
      }
    }
  },
  computed: {
    currValue() {
      return this.currData === null || !this.currData.value ? "0" : this.currData.value;
    },
    nextValue() {
      return this.nextData === null || !this.nextData.value ? "0" : this.nextData.value;
    },
    category() {
      return this.currData === null || !this.currData.category
        ? this.title
        : this.currData.category;
    }
  },
  methods: {
    flop() {
      const flips = document.querySelectorAll(".flip");
      this.flippers = Array.from(flips).map((flip, i) => {
        return new this.Flipper(flip, this.currValue[i], this.nextValue[i]);
      });
    }
  },
  mounted() {
    this.Flipper = class Flipper {
      constructor(node, currentTime, nextTime) {
        this.isFlipping = false;
        this.duration = 900;
        this.flipNode = node;
        this.frontNode = node.querySelector(".front");
        this.backNode = node.querySelector(".back");
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
        this.flipNode.classList.add("running");

        setTimeout(() => {
          this.flipNode.classList.remove("running");
          this.isFlipping = false;
          this.setFrontTime(nextTime);
        }, this.duration);
      }
    };
    this.flop();
  }
};
</script>

<style scoped>
.rd-flop {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
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

.flip:nth-of-type(3n) {
  margin: var(--threeColumnMargin) !important;
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

/* .rd-flop p {
  margin-top: 20px;
  font-size: 30px;
} */
</style>
