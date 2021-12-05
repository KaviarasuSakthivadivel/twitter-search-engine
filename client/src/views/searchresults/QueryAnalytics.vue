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
            :chartName="'sentimentChart'"
            :chartData="sentimentChartData"
            class="q-analytics-container col-span-1 height300px"
        ></TwCharts>

        <TwCharts
            :chartName="'langChart'"
            :chartData="langChartData"
            class="q-analytics-container col-span-1 height300px"
        ></TwCharts>
        <TwCharts
            :chartName="'countryChartData'"
            :chartData="countryChartData"
            class="q-analytics-container col-span-1 height300px"
        ></TwCharts>
        <TwCharts
            :chartName="'wordCloud'"
            :chartData="wordCloudData"
            class="q-analytics-container col-span-3 height500px"
        ></TwCharts>
        <TwCharts
            :chartName="'timeSeries'"
            :chartData="timeSeriesData"
            class="q-analytics-container col-span-3 height500px"
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
import analyticsMixinVue from '../../helpers/analyticsMixin.vue'
export default {
    props: ['chartData'],
    mixins: [analyticsMixinVue],
    data: () => ({
        loading: true,
        poiChartData,
        langChartData,
        sentimentChartData,
        wordCloudData,
        countryChartData,
        timeSeriesData,
    }),
    created() {
        this.formatChartData(this.chartData)
        this.loading = false
    },
    methods: {},
}
</script>
