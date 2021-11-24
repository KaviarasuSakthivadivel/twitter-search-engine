<template>
    <div class="tw-main-wrapper">
        <Header></Header>
        <AppBody></AppBody>
    </div>
</template>

<script>
import Header from '@/views/Header.vue'
import AppBody from '@/views/AppBody.vue'
export default {
    name: 'Home',
    components: {
        Header,
        AppBody,
    },
}
</script>
