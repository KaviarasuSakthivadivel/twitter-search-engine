<template>
    <div v-if="loading" class="p-5 overflow-y-scroll">
        <el-skeleton :rows="4" animated />
        <el-skeleton :rows="4" animated class="mt-10" />
        <el-skeleton :rows="4" animated class="mt-10" />
    </div>
    <div v-else class="flex flex-col p-5 overflow-y-scroll">
        <div
            v-for="(tweet, index) in tweetsList"
            :key="`tw-card-${index}`"
            :class="['border results-card', index != 0 && 'mt-5']"
        >
            <div class="flex flex-row">
                {{ tweet.poi_name || 'Unknown' }}
            </div>
            <div class="mt-2" v-html="tweet.highlightedText"></div>
        </div>

        <div class="flex justify-center w-full mt-5">
            <el-pagination
                background
                @current-change="nextPage"
                :current-page.sync="pageNo"
                :page-size="20"
                layout="prev, pager, next"
                :total="totalDocs"
            >
            </el-pagination>
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
            this.loading = true
            let response = await this.$axios.get(
                `api/search?query=${this.searchQuery}&pageNo=${
                    this.pageNo
                }&pageSize=${20}`
            )
            console.log(response)
            this.tweetsList = response?.data?.response?.docs || []
            let allHighlights = response?.data?.highlighting
            this.tweetsList.forEach((tweet) => {
                let highlightedText =
                    this.$_.get(allHighlights, [
                        `${tweet.id}`,
                        'tweet_text',
                        '0',
                    ]) || tweet.tweet_text

                let urls_regex = /((https?:\/\/\S+))/g
                let replaceUrls = '<a target="_blank" href="$1">$1</a>'
                highlightedText = highlightedText.replace(
                    urls_regex,
                    replaceUrls
                )

                let mentions_regex = /(^|[^@\w])@(\w{1,15})\b/g
                let replace =
                    '<span style="color: rgb(29, 155, 240);">$1<a target="_blank" href="http://twitter.com/$2">@$2</a></span>'

                highlightedText = highlightedText.replace(
                    mentions_regex,
                    replace
                )

                let hashtags_regex =
                    /(^|[^#\w])#(\w{1,100}|<em>\w{1,100}<\/em>)/g
                let replaceHashTags =
                    '<span style="color: rgb(29, 155, 240);">$1<a target="_blank" href="http://localhost:8080/searchresults?searchquery=#$2">#$2</a></span>'

                highlightedText = highlightedText.replace(
                    hashtags_regex,
                    replaceHashTags
                )

                this.$set(tweet, 'highlightedText', highlightedText)
            })
            this.totalDocs = response?.data?.response?.numFound || 0
            this.loading = false
        },
        nextPage() {
            this.fetchResults()
        },
    },
}
</script>
