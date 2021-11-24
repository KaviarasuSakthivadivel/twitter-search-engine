<template>
    <div class="tw-header">
        <div
            @click="changeTab('search')"
            :class="[
                'tw-tabs ml-10 flex flex-col h-full',
                activeTab == 'search' && 'active',
            ]"
        >
            <div class="flex flex-row items-center justify-between h-full">
                <InlineSvg src="magnifier" iconClass="icon size-sm"></InlineSvg>
                <div class="ml-2">Search</div>
            </div>
            <div v-if="activeTab == 'search'" class="tab-border"></div>
        </div>

        <div
            @click="changeTab('analytics')"
            :class="[
                'tw-tabs ml-10 flex flex-col h-full',
                activeTab == 'analytics' && 'active',
            ]"
        >
            <div class="flex flex-row items-center justify-between h-full">
                <InlineSvg src="analytics" iconClass="icon size-sm"></InlineSvg>
                <div class="ml-2">Analytics</div>
            </div>
            <div v-if="activeTab == 'analytics'" class="tab-border"></div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Header',
    data: () => ({
        activeTab: 'search',
    }),
    methods: {
        changeTab(name) {
            this.activeTab = name
            if (name == 'analytics') {
                this.$router.push({ path: 'analytics' })
            } else if (name == 'search') {
                this.$router.push({ path: 'search' })
            }
        },
    },
}
</script>
