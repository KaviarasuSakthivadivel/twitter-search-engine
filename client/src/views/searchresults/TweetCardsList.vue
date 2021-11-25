<template>
    <div v-if="loading" class="p-5 overflow-y-scroll">
        <el-skeleton :rows="4" animated />
        <el-skeleton :rows="4" animated class="mt-10" />
        <el-skeleton :rows="4" animated class="mt-10" />
    </div>
    <div v-else class="flex flex-col p-5 overflow-y-scroll">
        <el-pagination
            :hide-on-single-page="value"
            :total="tweetsList.length"
            layout="prev, pager, next"
        >
        </el-pagination>
        <div @click="nextPage()">Next page</div>
        <div
            v-for="(tweet, index) in tweetsList"
            :key="`tw-card-${index}`"
            class="border results-card mt-5"
        >
            <div class="flex flex-row">
                {{ tweet.poi_name || 'Unknown' }}
            </div>
            <div class="mt-2" v-html="tweet.tweet_text"></div>
        </div>
    </div>
</template>
<script>
export default {
    data: () => ({
        tweetsList: [],
        loading: true,
        pageNo: 1,
        totalDocs: null,
        value: 0,
    }),
    created() {
        this.fetchResults()
    },
    computed: {
        searchQuery() {
            return this.$route.query.searchquery
        },
    },
    watch: {
        searchQuery() {
            this.fetchResults()
        },
    },
    methods: {
        async fetchResults() {
            let response = await this.$axios.get(
                `api/search?query=${
                    this.searchQuery
                }&start=${0}&row=${20}&pageNo=${this.pageNo}&pageSize=${20}`
            )
            console.log(response)
            this.tweetsList = response?.data?.response?.docs || []
            this.tweetsList.forEach((tweet) => {
                let regex = /(^|[^@\w])@(\w{1,15})\b/g
                let replace =
                    '<span style="color: rgb(29, 155, 240);">$1<a target="_blank" href="http://twitter.com/$2">@$2</a></span>'

                tweet.tweet_text = tweet.tweet_text.replace(regex, replace)
            })
            this.totalDocs = response?.data?.response?.numFound || 0
            this.loading = false
        },
        nextPage() {
            this.pageNo = this.pageNo + 1
            this.fetchResults()
        },
    },
}
</script>
