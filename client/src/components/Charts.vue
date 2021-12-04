<template>
    <div :id="chartName"></div>
</template>
<script>
import Highcharts from 'highcharts'
require('highcharts/highcharts-more')(Highcharts)
require('highcharts/modules/exporting')(Highcharts)
require('highcharts/modules/export-data')(Highcharts)
require('highcharts/modules/wordcloud')(Highcharts)

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
