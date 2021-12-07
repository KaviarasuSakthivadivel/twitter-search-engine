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
                    :src="article.image"
                    class="image-container"
                    ><div slot="error" class="image-slot">
                        <i class="el-icon-picture-outline"></i></div
                ></el-image>
            </div>
            <div class="ml-5 flex flex-col">
                <div class="author-txt">
                    {{ article.source || article.author }}
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
                    url: `http://api.mediastack.com/v1/news?keywords=${this.query}&sort=published_desc&access_key=bfa2fb1ebf4ff8bcf95a3ff1e201924b&language=en,es&countries=us,in,mx`,
                })
                this.allArticles = response?.data?.data || []
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
