<template>
    <canvas
        :id="chartName"
        :height="height || '400'"
        :width="width || '400'"
    ></canvas>
</template>
<script>
import Chart from 'chart.js/auto'
export default {
    props: {
        chartName: { required: true },
        chartData: { required: true },
        height: { required: false },
        width: { required: false },
    },
    data: () => ({
        chartDataClone: {},
    }),
    mounted() {
        const ctx = document.getElementById(this.chartName)
        new Chart(ctx, this.$_.clone(this.chartData))
    },
}
</script>
