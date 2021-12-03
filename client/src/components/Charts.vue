<template>
    <div :id="chartName"></div>
</template>
<script>
import Highcharts from 'highcharts'
export default {
    props: {
        chartName: { required: true },
        chartData: { required: true },
        height: { required: false },
        width: { required: false },
    },
    mounted() {
        Highcharts.chart(this.chartName, this.$_.clone(this.chartData))
    },
}
</script>
