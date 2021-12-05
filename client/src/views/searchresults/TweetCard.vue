<template>
    <div>
        <PoiTweetDialog
            v-if="dialogVisibility"
            :visibility.sync="dialogVisibility"
            :tweet="tweet"
            :key="tweet.id"
        ></PoiTweetDialog>
        <div @click.stop="openTweet({ profile: tweet.username, id: tweet.id })">
            <InlineSvg
                src="new-tab"
                iconClass="icon size-m new-tab-icon svg-color-blue"
            />
        </div>
        <div
            @click.stop="openTwitterProfile(tweet.username)"
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
        <div class="mt-2" v-html="tweet.highlightedText"></div>
        <div class="mt-5 flex justify-between custom-width1 items-center">
            <el-tag :type="getTagType(tweet.sentiment)" effect="plain">{{
                sentimentVsLabel[tweet.sentiment] || 'Neutral'
            }}</el-tag>
            <div class="flex items-center tw-grey1">
                <InlineSvg src="reply" iconClass="icon size-sm mr-5px" />{{
                    tweet.replies_count || '0'
                }}
            </div>
            <div class="flex items-center tw-grey1">
                <InlineSvg src="retweets" iconClass="icon size-sm mr-5px" />{{
                    tweet.retweets_count || '0'
                }}
            </div>
            <div class="flex items-center tw-grey1">
                <InlineSvg src="likes" iconClass="icon size-sm mr-5px" />{{
                    tweet.likes_count || '0'
                }}
            </div>
            <div
                @click="openDialog"
                v-if="tweet.poi_name"
                class="flex items-center tw-blue1 hover:underline replies-class"
            >
                Open Replies
            </div>
        </div>
    </div>
</template>
<script>
import { sentimentVsLabel } from '@/helpers/constants'
import PoiTweetDialog from './PoiTweetDialog.vue'
export default {
    name: 'TweetCard',
    props: ['tweet'],
    components: {
        PoiTweetDialog,
    },
    data: () => ({
        sentimentVsLabel,
        dialogVisibility: false,
    }),
    methods: {
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
        openDialog() {
            this.dialogVisibility = true
        },
    },
}
</script>
