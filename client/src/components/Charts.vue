<template>
    <div :id="chartName" style="width:100%; height:200px;"></div>
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
    data: () => ({
        chartDataClone: {},
    }),
    mounted() {
        Highcharts.chart(this.chartName, this.chartData);
    },
}
</script>
