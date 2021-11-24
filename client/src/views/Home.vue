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
}
</script>
