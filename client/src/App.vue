<template>
    <div id="app">
        <router-view />
    </div>
</template>
<script>
export default {
    created() {
        document.title = 'Twitter Search Engine'
    },
}
</script>
