<template>
    <div class="p-5 filters-wrapper">
        <div class="flex justify-between items-center filters-border">
            <div class="font-bold">Filters</div>
            <div>
                <el-button @click="applyFilters" type="primary" round
                    >Apply</el-button
                >
                <el-button @click="removeFilter" round>Clear</el-button>
            </div>
        </div>
        <div class="mt-5 overflow-y-scroll filter-height text-sm">
            <div>POI Name</div>
            <el-select
                class="mt-5 w-full"
                v-model="poiName"
                clearable
                multiple
                collapse-tags
            >
                <el-option
                    v-for="(poi, index) in poiList"
                    :key="index"
                    :label="poi"
                    :value="poi"
                >
                </el-option>
            </el-select>
            <div class="mt-5">Languages</div>
            <el-select
                class="mt-5 w-full"
                v-model="tweetLang"
                clearable
                multiple
                collapse-tags
            >
                <el-option
                    v-for="(lang, index) in languages"
                    :key="index"
                    :label="lang.displayName"
                    :value="lang.value"
                >
                </el-option>
            </el-select>
            <div class="mt-5">Country</div>
            <el-select
                class="mt-5 w-full"
                v-model="country"
                clearable
                multiple
                collapse-tags
            >
                <el-option
                    v-for="(country, index) in countries"
                    :key="index"
                    :label="country"
                    :value="country"
                >
                </el-option>
            </el-select>
            <div class="mt-5">Sentiment</div>
            <el-select
                class="mt-5 w-full"
                v-model="sentiment"
                clearable
                multiple
                collapse-tags
            >
                <el-option
                    v-for="(sent, index) in sentiments"
                    :key="index"
                    :label="sentimentVsLabel[sent]"
                    :value="sent"
                >
                </el-option>
            </el-select>
            <div class="mt-5">Hashtags</div>
            <el-input class="mt-5" v-model="hashtags"></el-input>
            <div class="mt-5">Mentions</div>
            <el-input class="mt-5" v-model="mentions"></el-input>
            <div class="mt-5">Created at date range</div>
            <el-date-picker
                class="mt-5 w-full"
                v-model="timestamp"
                type="daterange"
                range-separator="-"
                start-placeholder="Start date"
                end-placeholder="End date"
                value-format="timestamp"
            >
            </el-date-picker>
            <div class="mt-5">Minimum replies</div>
            <el-input-number
                class="mt-5"
                v-model="replyCount"
                :min="0"
            ></el-input-number>
            <div class="mt-5">Show only POI Tweets</div>
            <el-switch class="mt-5" v-model="showOnlyPoi"> </el-switch>
            <div class="mt-5">Show only Replies</div>
            <el-switch class="mt-5" v-model="showOnlyReplies"> </el-switch>
            <div class="mt-5">Show only Tweets with link</div>
            <el-switch class="mt-5 mb-10" v-model="showTweetsWithLinks">
            </el-switch>
        </div>
    </div>
</template>
<script>
import {
    filterFields,
    arrayFields,
    poiList,
    sentimentVsLabel,
} from '@/helpers/constants'
export default {
    data: () => ({
        poiName: [],
        tweetLang: [],
        sentiment: [],
        country: [],
        showOnlyPoi: false,
        showOnlyReplies: false,
        showTweetsWithLinks: false,
        timestamp: [],
        hashtags: '',
        mentions: '',
        replyCount: null,
        poiList,
        languages: [
            { displayName: 'English', value: 'en' },
            { displayName: 'Spanish', value: 'es' },
            { displayName: 'Hindi', value: 'hi' },
        ],
        countries: ['USA', 'India', 'Mexico'],
        sentiments: ['positive', 'negative', 'neutral'],
        sentimentVsLabel,
    }),
    created() {
        this.initFilterFields()
    },
    methods: {
        initFilterFields() {
            filterFields.forEach((field) => {
                if (
                    this.$_.isArray(this[field]) &&
                    !this.$_.isEmpty(this.$route.query[field])
                ) {
                    this.$set(
                        this,
                        `${field}`,
                        JSON.parse(decodeURIComponent(this.$route.query[field]))
                    )
                } else if (
                    this.$route.query[field] &&
                    this.$route.query[field] != ''
                ) {
                    if (
                        decodeURIComponent(this.$route.query[field]) == 'true'
                    ) {
                        this[field] = true
                    } else {
                        this.$set(
                            this,
                            field,
                            decodeURIComponent(this.$route.query[field])
                        )
                    }
                }
            })
        },
        applyFilters() {
            let query = { searchquery: this.$route.query.searchquery }
            filterFields.forEach((field) => {
                if (
                    this.$_.isArray(this[field]) &&
                    !this.$_.isEmpty(this[field])
                ) {
                    this.$set(
                        query,
                        field,
                        encodeURIComponent(JSON.stringify(this[field]))
                    )
                } else if (this[field] && this[field] != '') {
                    this.$set(query, field, encodeURIComponent(this[field]))
                }
            })
            this.$router.replace({
                query: query,
            })
        },
        removeFilter() {
            let query = { searchquery: this.$route.query.searchquery }
            this.$router.replace({
                query: query,
            })
            this.$nextTick(() => {
                filterFields.forEach((field) => {
                    if (arrayFields.includes(field)) {
                        this.$set(this, field, [])
                    } else {
                        this.$set(this, field, null)
                    }
                })
            })
        },
    },
}
</script>
