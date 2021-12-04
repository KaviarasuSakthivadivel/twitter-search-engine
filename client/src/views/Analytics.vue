<template>
    <div v-if="loading"></div>
    <div
        v-else
        class="
            analytics-dashboard
            h-full
            w-full
            grid
            gap-4
            grid-cols-3
            overflow-y-scroll
        "
    >
        <TwCharts
            :chartName="'poiChart'"
            :chartData="poiChartData"
            class="tw-container height500px col-span-3"
        ></TwCharts>
        <TwCharts
            :chartName="'sentimentChart'"
            :chartData="sentimentChartData"
            class="tw-container height300px col-span-1"
        ></TwCharts>

        <TwCharts
            :chartName="'langChart'"
            :chartData="langChartData"
            class="tw-container height300px col-span-1"
        ></TwCharts>
        <TwCharts
            :chartName="'countryChartData'"
            :chartData="countryChartData"
            class="tw-container height300px col-span-1"
        ></TwCharts>
        <TwCharts
            :chartName="'wordCloud'"
            :chartData="wordCloudData"
            class="tw-container height500px col-span-3"
        ></TwCharts>
        <TwCharts
            :chartName="'timeSeries'"
            :chartData="timeSeriesData"
            class="tw-container height500px col-span-3"
        ></TwCharts>
    </div>
</template>
<script>
import {
    langChartData,
    poiChartData,
    sentimentChartData,
    wordCloudData,
    countryChartData,
    timeSeriesData,
} from '@/helpers/queryChartData'
import {
    sentimentVsLabel,
    sentimentVsColor,
    countryVsColor,
    langVsLabel,
} from '@/helpers/constants'
import moment from 'moment'
export default {
    data: () => ({
        loading: true,
        langChartData,
        poiChartData,
        sentimentChartData,
        wordCloudData,
        countryChartData,
        timeSeriesData,
    }),
    created() {
        this.fetchDashboardData()
    },
    methods: {
        async fetchDashboardData() {
            try {
                let response = await this.$axios.get(`api/dashboard`)
                this.formatChartData(response?.data?.facets)
            } catch (error) {
                this.$message.error(error?.message)
            }
        },
        formatChartData(data) {
            if (data?.poi_name) {
                const poiBucketJSON = data.poi_name.buckets
                let poiChartDataArr = []
                poiBucketJSON.forEach((bucket) => {
                    poiChartDataArr.push({ name: bucket.val, y: bucket.count })
                })
                this.poiChartData.series[0].data = poiChartDataArr
            }
            if (data?.tweet_lang) {
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
            if (data?.country) {
                const tweetcountryJSON = data.country.buckets
                let tweetcountryDataArr = []
                tweetcountryJSON.forEach((bucket) => {
                    tweetcountryDataArr.push({
                        name: bucket.val,
                        y: bucket.count,
                        color: countryVsColor[bucket.val],
                    })
                })
                this.countryChartData.series[0].data = tweetcountryDataArr
            }
            if (data?.sentiment) {
                let sentiments = data.sentiment.buckets || []
                let sentimentDataArr = []
                sentiments.forEach((bucket) => {
                    sentimentDataArr.push({
                        name: sentimentVsLabel[bucket.val],
                        y: bucket.count,
                        color: sentimentVsColor[bucket.val],
                    })
                })
                this.sentimentChartData.series[0].data = sentimentDataArr
            }
            if (data?.hashtags) {
                let hashtags = data.hashtags.buckets || []
                let hashtagDataArr = []
                hashtags.forEach((bucket) => {
                    hashtagDataArr.push({
                        name: bucket.val,
                        weight: bucket.count,
                    })
                })
                this.wordCloudData.series[0].data = hashtagDataArr
            }
            if (data?.tweet_date) {
                let tweetDates = data.tweet_date.buckets || []
                let tweetDateDataArr = []
                tweetDates.forEach((bucket) => {
                    if (moment(bucket.val).valueOf() > 1630468800000) {
                        tweetDateDataArr.push([
                            moment(bucket.val).valueOf(),
                            bucket.count,
                        ])
                    }
                })
                this.timeSeriesData.series[0].data = tweetDateDataArr
                    .sort((a, b) => {
                        return b[0] - a[0]
                    })
                    .reverse()
            }
            this.loading = false
        },
    },
}
</script>
