<template>
    <div class="p-2 overflow-y-scroll h-full">
        <div
            v-for="(article, index) in allArticles"
            :key="index"
            class="news-container results-card flex"
            @click="openNews(article.url)"
        >
            <div>
                <el-image
                    fit="cover"
                    :src="article.urlToImage"
                    class="image-container"
                    ><div slot="error" class="image-slot">
                        <i class="el-icon-picture-outline"></i></div
                ></el-image>
            </div>
            <div class="ml-5 flex flex-col">
                <div class="author-txt">
                    {{ article.source.name || article.author }}
                </div>
                <div class="mt-2">{{ article.title }}</div>
                <div class="mt-3 desc-text">{{ article.description }}</div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    props: ['query'],
    data: () => ({
        allArticles: [],
    }),
    created() {
        this.fetchNews()
    },
    methods: {
        async fetchNews() {
            try {
                let response = await axios({
                    method: 'get',
                    url: `https://newsapi.org/v2/everything?qInTitle=${this.query}&sortBy=publishedAt&apiKey=1e51b53cb2d3419e9c8a52c4ac3a9c60&language=en&language=es`,
                })
                this.allArticles = response?.data?.articles || []
            } catch (error) {
                this.$message.error(error?.message)
            }
        },
        openNews(url) {
            window.open(url)
        },
    },
}
</script>
