<template>
    <div v-if="loading" class="p-5 overflow-y-scroll">
        <el-skeleton :rows="4" animated />
        <el-skeleton :rows="4" animated class="mt-10" />
        <el-skeleton :rows="4" animated class="mt-10" />
    </div>

    <el-tabs v-else v-model="currentTab" class="pl-3 pr-3">
        <el-tab-pane
            label="Tweet Results"
            name="tweet"
            class="overflow-y-scroll tab-height1"
        >
            <div
                v-if="totalDocs && timeTaken"
                class="mt-3 flex items-center justify-center fetched-tweet-text"
            >
                {{ `Fetched ${totalDocs} tweets in ${timeTaken}` }}
            </div>
            <div class="flex flex-col p-5">
                <div
                    v-for="(tweet, index) in tweetsList"
                    :key="`tw-card-${index}`"
                    :class="['results-card', index != 0 && 'mt-5']"
                >
                    <div
                        @click="
                            openTweet({ profile: tweet.username, id: tweet.id })
                        "
                    >
                        <InlineSvg
                            src="new-tab"
                            iconClass="icon size-m new-tab-icon svg-color-blue"
                        />
                    </div>
                    <div
                        @click="openTwitterProfile(tweet.profile_name)"
                        class="flex flex-row items-center tw-name-parent"
                    >
                        <el-avatar
                            size="small"
                            icon="el-icon-user-solid"
                            :src="tweet.profile_url"
                        ></el-avatar>
                        <div class="ml-3 tw-id-name">
                            {{ tweet.profile_name || 'Unknown' }}
                        </div>

                        <InlineSvg
                            v-if="tweet.verified"
                            src="verified"
                            iconClass="icon size-sm ml-2px svg-color-blue"
                        />
                        <div class="ml-4px tw-handle-name">
                            {{ `@${tweet.username}` || '@unknown' }}
                        </div>
                        <div class="tw-dot plr-4px">·</div>
                        <div class="tw-handle-name">
                            {{ moment(tweet.tweet_date).format('DD MMM YY') }}
                        </div>
                    </div>
                    <div class="mt-2" v-html="tweet.highlightedText"></div>
                    <div class="mt-5 flex justify-between w-5/12 items-center">
                        <el-tag
                            :type="getTagType(tweet.sentiment)"
                            effect="plain"
                            >{{
                                sentimentVsLabel[tweet.sentiment] || 'Neutral'
                            }}</el-tag
                        >
                        <div class="flex items-center tw-grey1">
                            <InlineSvg
                                src="reply"
                                iconClass="icon size-sm mr-5px"
                            />{{ tweet.reply_count || '0' }}
                        </div>
                        <div class="flex items-center tw-grey1">
                            <InlineSvg
                                src="retweets"
                                iconClass="icon size-sm mr-5px"
                            />{{ tweet.retweet_count || '0' }}
                        </div>
                        <div class="flex items-center tw-grey1">
                            <InlineSvg
                                src="likes"
                                iconClass="icon size-sm mr-5px"
                            />{{ tweet.like_count || '0' }}
                        </div>
                    </div>
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
                </div></div
        ></el-tab-pane>
        <el-tab-pane
            label="Analytics"
            name="analytics"
            class="bg-grey tab-height2 rounded-xl"
        >
            <QueryAnalytics :chartData="chartData"></QueryAnalytics>
        </el-tab-pane>
        <el-tab-pane label="News Articles" name="news"
            >News Articles</el-tab-pane
        >
    </el-tabs>
</template>
<script>
import {
    filterFields,
    arrayFields,
    sentimentVsLabel,
} from '@/helpers/constants'
import QueryAnalytics from './QueryAnalytics.vue'
export default {
    components: {
        QueryAnalytics,
    },
    data: () => ({
        tweetsList: [],
        loading: true,
        pageNo: 1,
        totalDocs: null,
        chartData: [],
        currentTab: 'tweet',
        timeTaken: null,
        sentimentVsLabel,
    }),
    created() {
        this.fetchResults()
    },
    computed: {
        routeQueries() {
            return this.$route.query || {}
        },
    },
    watch: {
        routeQueries() {
            this.pageNo = 1
            this.fetchResults()
        },
    },
    methods: {
        async fetchResults() {
            let { queryParams } = this.constructQueries()
            this.loading = true
            try {
                let response = await this.$axios.post(`api/search`, queryParams)
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
                        '<span style="color: rgb(29, 155, 240);">$1<a target="_blank" href="http://localhost:8080/searchresults?searchquery=$2">#$2</a></span>'

                    highlightedText = highlightedText.replace(
                        hashtags_regex,
                        replaceHashTags
                    )

                    this.$set(tweet, 'highlightedText', highlightedText)
                })
                this.totalDocs = response?.data?.response?.numFound || 0
                this.timeTaken = response?.data?.time_taken
                this.chartData = response?.data?.facets
                this.loading = false
            } catch (error) {
                this.$message.error(error?.message || 'Server Error')
            }
        },
        nextPage() {
            this.fetchResults()
        },
        constructQueries() {
            let params = {}
            params.query = this.routeQueries.searchquery
            params.pageNo = this.pageNo
            params.pageSize = 20
            filterFields.forEach((field) => {
                if (!this.$_.isEmpty(this.routeQueries[field])) {
                    if (arrayFields.includes(field)) {
                        this.$set(
                            params,
                            `${field}`,
                            JSON.parse(
                                decodeURIComponent(this.$route.query[field])
                            )
                        )
                    } else {
                        this.$set(
                            params,
                            field,
                            decodeURIComponent(this.$route.query[field])
                        )
                    }
                }
            })
            return { queryParams: params }
        },
        openTwitterProfile(profile) {
            window.open(`http://twitter.com/${profile}`)
        },
        openTweet({ profile, id }) {
            window.open(`http://twitter.com/${profile}/status/${id}`)
        },
        getTagType(sentiment) {
            if (sentiment == 'positive') {
                return 'success'
            } else if (sentiment == 'neutral') {
                return 'info'
            } else if (sentiment == 'negative') {
                return 'danger'
            }
        },
    },
}
</script>
