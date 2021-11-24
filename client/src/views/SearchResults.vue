<template>
    <div class="flex flex-row items-center justify-center">
        <el-input
            v-model="searchQuery"
            class="tw-search-bar mT15 widht96"
            clearable
            placeholder="Search here"
        >
        </el-input>
    </div>
</template>
<script>
export default {
    data: () => ({
        searchQuery: '',
    }),
    created() {
        this.searchQuery = this.$route.query.searchquery
    },
}
</script>
