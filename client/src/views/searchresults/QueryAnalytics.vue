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
            :chartData="langChartData"
            :height="300"
            :widht="300"
        ></TwCharts>
        <TwCharts
            :chartName="'poiChart'"
            :chartData="poiChartData"
            :height="300"
            :widht="300"
            class="mt-5"
        ></TwCharts>
    </div>
</template>
<script>
const chartData = {
    type: 'pie',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
            {
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    },
}
import { bus } from '@/components/bus'
export default {
    data: () => ({
        loading: false,
        langChartData: chartData,
        poiChartData: {},
    }),
    created() {
        bus.$on('chartData', (data) => {
            this.formatChartData(data)
        })
    },
    methods: {
        formatChartData(data) {
            console.log('chart data', data)
        },
    },
}
</script>
