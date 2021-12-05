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
    <div
        v-else
        class="
            analytics-dashboard
            h-full
            w-full
            grid
            gap-4
            grid-cols-6
            overflow-y-scroll
        "
    >
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">3,77,287</div>
            <div class="title-text-2">Total Tweets</div>
        </div>
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                bg2
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">51</div>
            <div class="title-text-2">POI's</div>
        </div>
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                bg4
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">79,926</div>
            <div class="title-text-2">POI Tweets</div>
        </div>
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                bg3
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">3</div>
            <div class="title-text-2">Languages</div>
        </div>
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                bg5
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">1,62,793</div>
            <div class="title-text-2">Reply Tweets</div>
        </div>
        <div
            class="
                tw-container
                height200px
                col-span-1
                card-1
                bg6
                flex flex-col
                justify-around
            "
        >
            <div class="title-text-1">34,213</div>
            <div class="title-text-2">Replies to POI's</div>
        </div>
        <TwCharts
            :chartName="'poiChart'"
            :chartData="poiChartData"
            class="tw-container height500px col-span-6"
        ></TwCharts>
        <TwCharts
            :chartName="'sentimentChart'"
            :chartData="sentimentChartData"
            class="tw-container height300px col-span-2"
        ></TwCharts>

        <TwCharts
            :chartName="'langChart'"
            :chartData="langChartData"
            class="tw-container height300px col-span-2"
        ></TwCharts>
        <TwCharts
            :chartName="'countryChartData'"
            :chartData="countryChartData"
            class="tw-container height300px col-span-2"
        ></TwCharts>
        <TwCharts
            :chartName="'wordCloud'"
            :chartData="wordCloudData"
            class="tw-container height500px col-span-6"
        ></TwCharts>
        <TwCharts
            :chartName="'timeSeries'"
            :chartData="timeSeriesData"
            class="tw-container height500px col-span-6"
        ></TwCharts>

        <TwCharts
            :chartName="'column'"
            :chartData="vaccineMentionsByCountryData"
            class="tw-container height500px col-span-3"
        ></TwCharts>
        <TwCharts
            :chartName="'rtimeSeries'"
            :chartData="vaccineCompaniesBySentimentData"
            class="tw-container height500px col-span-3"
        ></TwCharts>

        <TwCharts
            :chartName="'stimeSeries'"
            :chartData="sentimentTimeSeriesData"
            class="tw-container height500px col-span-6"
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
    sentimentTimeSeriesData,
    vaccineMentionsByCountryData,
    vaccineCompaniesBySentimentData,
} from '@/helpers/queryChartData'
import analyticsMixinVue from '../helpers/analyticsMixin.vue'
import cloneDeep from 'lodash/cloneDeep'
export default {
    mixins: [analyticsMixinVue],
    data: () => ({
        loading: true,
        langChartData: cloneDeep(langChartData),
        poiChartData: cloneDeep(poiChartData),
        sentimentChartData: cloneDeep(sentimentChartData),
        wordCloudData: cloneDeep(wordCloudData),
        countryChartData: cloneDeep(countryChartData),
        timeSeriesData: cloneDeep(timeSeriesData),
        sentimentTimeSeriesData: cloneDeep(sentimentTimeSeriesData),
        vaccineMentionsByCountryData: cloneDeep(vaccineMentionsByCountryData),
        vaccineCompaniesBySentimentData: cloneDeep(
            vaccineCompaniesBySentimentData
        ),
    }),
    created() {
        Promise.all([
            this.fetchDashboardData(),
            this.fetchDashboardData2(),
        ]).finally(() => {
            this.loading = false
        })
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
        async fetchDashboardData2() {
            try {
                let response = await this.$axios.get(`api/charts`)
                this.formatVaccineChartData(response?.data)
            } catch (error) {
                this.$message.error(error?.message)
            }
        },
    },
}
</script>
