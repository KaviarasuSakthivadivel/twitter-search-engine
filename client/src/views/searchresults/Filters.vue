<template>
    <div class="p-5 overflow-y-scroll filters-wrapper">
        <div class="font-bold">Filters</div>
        <div class="mt-5">
            <div>
                <div>POI Name</div>
                <el-select
                    class="mt-5"
                    v-model="selectedPois"
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
                    class="mt-5"
                    v-model="selectedLang"
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
                    class="mt-5"
                    v-model="selectedCountry"
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
                    class="mt-5"
                    v-model="selectedSentiment"
                    clearable
                    multiple
                    collapse-tags
                >
                    <el-option
                        v-for="(sent, index) in sentiments"
                        :key="index"
                        :label="sent"
                        :value="sent"
                    >
                    </el-option>
                </el-select>
                <div class="mt-5">Hashtags</div>
                <el-input v-model="hashtags"></el-input>
                <div class="mt-5">Mentions</div>
                <el-input v-model="mentions"></el-input>
                <div class="mt-5">Created at date range</div>
                <el-date-picker
                    class="mt-5"
                    v-model="dateRange"
                    type="daterange"
                    range-separator="-"
                    start-placeholder="Start date"
                    end-placeholder="End date"
                >
                </el-date-picker>
                <div class="mt-5">Minimum replies</div>
                <el-input type="number" v-model="minimumReplies"></el-input>
                <div class="mt-5">Show only POI Tweets</div>
                <el-switch class="mt-5" v-model="showOnlyPoiTweets">
                </el-switch>
                <div class="mt-5">Show only Replies</div>
                <el-switch class="mt-5" v-model="showOnlyReplyTweets">
                </el-switch>
                <div class="mt-5">Show only Tweets with link</div>
                <el-switch class="mt-5" v-model="showOnlyLinkTweets">
                </el-switch>
                <div class="mt-5">
                    <el-button type="primary" round>Apply</el-button>
                    <el-button round>Clear</el-button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
const poiList = ['CDCGov', 'narendramodi']
export default {
    data: () => ({
        selectedPois: [],
        selectedLang: [],
        selectedSentiment: [],
        selectedCountry: [],
        showOnlyPoiTweets: false,
        showOnlyReplyTweets: false,
        showOnlyLinkTweets: false,
        dateRange: null,
        hashtags: '',
        mentions: '',
        minimumReplies: null,
        poiList,
        languages: [
            { displayName: 'English', value: 'eng' },
            { displayName: 'Spanish', value: 'es' },
            { displayName: 'Hindi', value: 'hi' },
        ],
        countries: ['USA', 'India', 'Mexico'],
        sentiments: ['Positive', 'Negative', 'Neutral'],
    }),
}
</script>
