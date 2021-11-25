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
        <div class="flex flex-row justify-between mt-10 tw-results-parent">
            <Filters class="h-full border-r border-color1 w-1/4"></Filters>
            <TweetCardsList
                class="h-full border-r border-color1 w-2/4"
            ></TweetCardsList>
            <QueryAnalytics class="w-1/4"></QueryAnalytics>
        </div>
    </div>
</template>
<script>
import TweetCardsList from './TweetCardsList.vue'
import QueryAnalytics from './QueryAnalytics.vue'
import Filters from './Filters.vue'
export default {
    data: () => ({
        searchQuery: '',
    }),
    created() {
        this.searchQuery = this.$route.query.searchquery
    },
    components: { TweetCardsList, QueryAnalytics, Filters },
    methods: {
        routeToSearchResults() {
            if (
                !this.$_.isEmpty(this.searchQuery) &&
                this.searchQuery != this.$route.query.searchquery
            ) {
                this.$router.push({
                    path: 'searchresults',
                    query: { searchquery: this.searchQuery },
                })
            }
        },
    },
}
</script>
