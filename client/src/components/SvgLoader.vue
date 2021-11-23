<template>
  <div>
    Helloo
    <component :is="SvgComponent"></component>
  </div>
</template>

<script>
// import { defineAsyncComponent } from 'vue'
import * as SvgComponent from '@/assets/search-main.svg'
export default {
  props: {
    src: {
      type: String,
      required: true,
    },
    iconClass: {
      type: String,
    },
    iconStyle: {
      type: String,
    },
  },
  components: {
    SvgComponent,
  },
  created() {
    console.log(SvgComponent)
  },
}
</script>
