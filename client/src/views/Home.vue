<template>
    <div class="tw-main-wrapper">
        <Header></Header>
        <router-view />
    </div>
</template>
<script>
import Header from './Header.vue'
export default {
    name: 'Home',
    components: {
        Header,
    },
    title() {
        return 'Twitter Search Engine'
    },
    mounted() {
        if (this.$route.name === 'Home') {
            this.$router.push({ path: 'search' })
        }
    },
}
</script>
