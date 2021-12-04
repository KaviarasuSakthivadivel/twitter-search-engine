<template>
    <div class="flex flex-col tw-results">
        <div class="flex flex-row items-center justify-center">
            <el-input
                v-model="searchQuery"
                class="tw-search-bar mT15 widht96 mr-2"
                clearable
                placeholder="Search here"
                @keyup.native.enter="routeToSearchResults"
            >
            </el-input>
            <el-button
                @click="routeToSearchResults"
                icon="search"
                class="tw-search-button mT15"
                >Search</el-button
            >
        </div>
        <div class="flex flex-row justify-between mt-5 tw-results-parent">
            <Filters class="h-full border-r border-color1 w-1/4"></Filters>
            <TweetCardsList
                class="h-full border-color1 w-3/4"
                @setParams="setParams"
            ></TweetCardsList>
        </div>
    </div>
</template>
<script>
import TweetCardsList from './TweetCardsList.vue'
import Filters from './Filters.vue'
export default {
    data: () => ({
        searchQuery: '',
        count: null,
        timeTaken: null,
    }),
    created() {
        this.searchQuery = this.$route.query.searchquery
    },
    components: {
        TweetCardsList,
        Filters,
    },
    methods: {
        routeToSearchResults() {
            if (
                !this.$_.isEmpty(this.searchQuery) &&
                this.searchQuery !== this.$route.query.searchquery
            ) {
                this.$router.push({
                    path: 'searchresults',
                    query: { searchquery: this.searchQuery },
                })
            }
        },
        setParams({ count, timeTaken }) {
            this.count = count
            this.timeTaken = timeTaken
        },
        handleClick() {},
    },
}
</script>
