<template>
    <el-dialog
        title="POI Tweet Replies"
        :visible="visible"
        :before-close="handleClose"
    >
        <div
            @click.stop="openTwitterProfile(tweet.profile_name)"
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
                {{ moment(tweet.tweet_date).utc().format('DD MMM YY') }}
            </div>
        </div>
        <div
            class="mt-2 pb-5 border-bottom-1"
            v-html="tweet.highlightedText"
        ></div>
        <div v-if="loading">
            <el-skeleton :rows="4" animated />
            <el-skeleton :rows="4" animated class="mt-10" />
            <el-skeleton :rows="4" animated class="mt-10" />
        </div>
        <div v-else class="flex flex-row">
            <div
                class="
                    flex flex-col
                    overflow-y-scroll
                    height-d1
                    p-5
                    width60p
                    border-right-d
                "
            >
                <TweetCard2
                    v-for="(tw, index) in replyTweets"
                    :key="`tw-card2-${index}`"
                    :class="['results-card', index != 0 && 'mt-4']"
                    :tweet="tw"
                ></TweetCard2>
            </div>
            <div
                class="
                    width40p
                    p-5
                    grid
                    gap-4
                    grid-cols-1
                    overflow-y-scroll
                    bg-grey
                    height-d1
                "
            >
                <TwCharts
                    :chartName="'sentimentChart2'"
                    :chartData="sentimentChartData"
                    class="q-analytics-container col-span-1 height300px"
                ></TwCharts>
            </div>
        </div>
    </el-dialog>
</template>
<script>
import { sentimentChartData } from '@/helpers/queryChartData'
import analyticsMixinVue from '@/helpers/analyticsMixin.vue'
import clone from 'lodash/clone'
export default {
    props: ['tweet', 'visibility'],
    components: {
        TweetCard2: () => import('./TweetCard.vue'),
    },
    mixins: [analyticsMixinVue],
    data: () => ({
        visible: false,
        loading: true,
        replyTweets: [],
        sentimentChartData: clone(sentimentChartData),
    }),
    mounted() {
        this.visible = true
        this.fetchReplyTweets()
    },
    methods: {
        handleClose() {
            this.$emit('update:visibility', false)
            this.visible = false
        },
        openTwitterProfile(profile) {
            window.open(`http://twitter.com/${profile}`)
        },
        async fetchReplyTweets() {
            try {
                let response = await this.$axios.get(
                    `api/get_replies/${this.tweet.id}`
                )
                this.replyTweets = response?.data?.response?.docs
                this.replyTweets.forEach((tweet) => {
                    let highlightedText = tweet.tweet_text

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
                this.formatChartData(response?.data?.facets)
                this.loading = false
            } catch (error) {
                this.$message.error(error?.message)
            }
        },
    },
}
</script>
