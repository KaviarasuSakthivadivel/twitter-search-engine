<template>
    <div v-if="loading" class="p-5 overflow-y-scroll q-bg">
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
    <div v-else class="overflow-y-scroll p-5 grid gap-4 grid-cols-3 h-full">
        <TwCharts
            :chartName="'poiChart'"
            :chartData="poiChartData"
            class="q-analytics-container height400px col-span-3"
        ></TwCharts>
        <TwCharts
            :chartName="'langChart'"
            :chartData="langChartData"
            class="q-analytics-container col-span-1 height300px"
        ></TwCharts>
        <TwCharts
            :chartName="'sentimentChart'"
            :chartData="sentimentChartData"
            class="q-analytics-container col-span-1 height300px"
        ></TwCharts>
        <TwCharts
            :chartName="'wordCloud'"
            :chartData="wordCloudData"
            class="q-analytics-container col-span-3 height500px"
        ></TwCharts>
    </div>
</template>
<script>
const langVsLabel = { en: 'English', es: 'Spanish', hi: 'Hindi' }
import {
    langChartData,
    poiChartData,
    sentimentChartData,
    wordCloudData,
} from '@/helpers/queryChartData'
import { sentimentVsLabel, sentimentVsColor } from '@/helpers/constants'
export default {
    props: ['chartData'],
    data: () => ({
        loading: true,
        poiChartData,
        langChartData,
        sentimentChartData,
        wordCloudData,
    }),
    created() {
        this.formatChartData(this.chartData)
    },
    methods: {
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
                let hastags = data.hashtags.buckets || []
                let hashtagDataArr = []
                hastags.forEach((bucket) => {
                    hashtagDataArr.push({
                        name: bucket.val,
                        weight: bucket.count,
                    })
                })
                this.wordCloudData.series[0].data = hashtagDataArr
            }
            this.loading = false
        },
    },
}
</script>
