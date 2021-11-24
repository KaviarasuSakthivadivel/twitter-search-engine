<template>
    <div class="tw-body">
        <InlineSvg src="search-main" iconClass="icon size-120"></InlineSvg>
        <div class="app-name-text">Elixir</div>
        <div class="flex flex-row mt-10">
            <el-input v-model="searchQuery" class="w-full"> </el-input>
            <el-button icon="search">Search</el-button>
        </div>
    </div>
</template>
<script>
export default {
    data: () => ({
        searchQuery: '',
    }),
}
</script>
