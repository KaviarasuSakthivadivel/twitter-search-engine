<template>
    <div v-if="loading" class="p-5 overflow-y-scroll">
        <el-skeleton animated style="width: 100%">
            <template slot="template">
                <el-skeleton-item
                    variant="rect"
                    style="width: 100%; height: 240px"
                    animated
                />
                <div>
                    <el-skeleton-item variant="p" style="width: 50%" />
                    <div class="flex items-center justify-center">
                        <el-skeleton-item
                            variant="text"
                            style="margin-right: 16px"
                        />
                        <el-skeleton-item variant="text" style="width: 30%" />
                    </div>
                </div>
            </template>
        </el-skeleton>
        <el-skeleton animated style="width: 100%" class="mt-10">
            <template slot="template">
                <el-skeleton-item
                    variant="rect"
                    style="width: 100%; height: 240px"
                    animated
                />
                <div>
                    <el-skeleton-item variant="p" style="width: 50%" />
                    <div
                        style="
                            display: flex;
                            align-items: center;
                            justify-items: space-between;
                        "
                    >
                        <el-skeleton-item
                            variant="text"
                            style="margin-right: 16px"
                        />
                        <el-skeleton-item variant="text" style="width: 30%" />
                    </div>
                </div>
            </template>
        </el-skeleton>
    </div>
    <div v-else class="overflow-y-scroll p-5">
        <TwCharts
            :chartName="'langChart'"
            :chartData="poiChartData"
            :height="300"
            :width="300"
        ></TwCharts>
        <TwCharts
            :chartName="'poiChart'"
            :chartData="langChartData"
            :height="300"
            :width="300"
            class="mt-5"
        ></TwCharts>
    </div>
</template>
<script>
const poiChartDataOptions = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'POI stats',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            },
            showInLegend: false,
        },
    },
    series: [
        {
            name: 'POI',
            colorByPoint: true,
            data: [],
        },
    ],
}
const countryChartDataOptions = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'Language wise stats',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
            },
            showInLegend: true,
        },
    },
    series: [
        {
            name: 'Country',
            colorByPoint: true,
            data: [],
        },
    ],
}
const langVsLabel = { en: 'English', es: 'Spanish', hi: 'Hindi' }
import { bus } from '@/components/bus'
export default {
    data: () => ({
        loading: true,
        poiChartData: poiChartDataOptions,
        langChartData: countryChartDataOptions,
    }),
    created() {
        bus.$on('chartData', (data) => {
            this.loading = true
            this.$nextTick(() => {
                this.formatChartData(data)
            })
        })
    },
    methods: {
        formatChartData(data) {
            if (data && data.poi_name) {
                const poiBucketJSON = data.poi_name.buckets
                let poiChartDataArr = []
                poiBucketJSON.forEach((bucket) => {
                    poiChartDataArr.push({ name: bucket.val, y: bucket.count })
                })
                this.poiChartData.series[0].data = poiChartDataArr
            }
            if (data && data.tweet_lang) {
                const tweetLangJSON = data.tweet_lang.buckets
                let tweetLangDataArr = []
                tweetLangJSON.forEach((bucket) => {
                    tweetLangDataArr.push({
                        name: langVsLabel[bucket.val],
                        y: bucket.count,
                    })
                })
                this.langChartData.series[0].data = tweetLangDataArr
            }
            this.loading = false
        },
    },
}
</script>
