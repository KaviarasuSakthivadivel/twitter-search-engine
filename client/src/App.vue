<template>
    <div id="app">
        <router-view />
    </div>
</template>
<script>
export default {
    created() {
        if (this.$route.path == '/') {
            this.$router.push({ path: 'search' })
        }
    },
}
</script>
