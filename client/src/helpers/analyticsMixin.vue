<script>
import {
    sentimentVsLabel,
    sentimentVsColor,
    countryVsColor,
    langVsLabel,
} from '@/helpers/constants'
import moment from 'moment'

export default {
    methods: {
        formatChartData(data) {
            if (data?.poi_name) {
                const poiBucketJSON = data.poi_name.buckets
                let poiChartDataArr = []
                poiBucketJSON.forEach((bucket) => {
                    poiChartDataArr.push({ name: bucket.val, y: bucket.count })
                })
                this.poiChartData.series[0].data = poiChartDataArr
            }
            if (data?.tweet_lang) {
                const tweetLangJSON = data.tweet_lang.buckets
                let tweetLangDataArr = []
                tweetLangJSON.forEach((bucket) => {
                    tweetLangDataArr.push({
                        name: langVsLabel[bucket.val],
                        y: bucket.count,
                    })
                })
                this.langChartData.series[0].data = tweetLangDataArr
            }
            if (data?.country) {
                const tweetcountryJSON = data.country.buckets
                let tweetcountryDataArr = []
                tweetcountryJSON.forEach((bucket) => {
                    tweetcountryDataArr.push({
                        name: bucket.val,
                        y: bucket.count,
                        color: countryVsColor[bucket.val],
                    })
                })
                this.countryChartData.series[0].data = tweetcountryDataArr
            }
            if (data?.sentiment) {
                let sentiments = data.sentiment.buckets || []
                let sentimentDataArr = []
                sentiments.forEach((bucket) => {
                    sentimentDataArr.push({
                        name: sentimentVsLabel[bucket.val],
                        y: bucket.count,
                        color: sentimentVsColor[bucket.val],
                    })
                })
                this.sentimentChartData.series[0].data = sentimentDataArr
            }
            if (data?.hashtags) {
                let hashtags = data.hashtags.buckets || []
                let hashtagDataArr = []
                hashtags.forEach((bucket) => {
                    hashtagDataArr.push({
                        name: bucket.val,
                        weight: bucket.count,
                    })
                })
                this.wordCloudData.series[0].data = hashtagDataArr
            }
            if (data?.tweet_date) {
                let tweetDates = data.tweet_date.buckets || []
                let tweetDateDataArr = []
                tweetDates.forEach((bucket) => {
                    if (moment(bucket.val).valueOf() > 1630468800000) {
                        tweetDateDataArr.push([
                            moment(bucket.val).valueOf(),
                            bucket.count,
                        ])
                    }
                })
                this.timeSeriesData.series[0].data = tweetDateDataArr
                    .sort((a, b) => {
                        return b[0] - a[0]
                    })
                    .reverse()
            }
        },

        formatVaccineChartData(data) {
            if (data?.time_with_sentiment) {
                let sentimentTweetDate =
                    data.time_with_sentiment['tweet_date,sentiment']
                let positiveDataArr = []
                let negativeDataArr = []
                let neutralDataArr = []
                sentimentTweetDate.forEach((bucket) => {
                    if (moment(bucket.value).valueOf() > 0) {
                        bucket.pivot.forEach((pi) => {
                            if (pi.value == 'positive') {
                                positiveDataArr.push([
                                    moment(bucket.value).valueOf(),
                                    pi.count,
                                ])
                            }
                            if (pi.value == 'negative') {
                                negativeDataArr.push([
                                    moment(bucket.value).valueOf(),
                                    pi.count,
                                ])
                            }
                            if (pi.value == 'neutral') {
                                neutralDataArr.push([
                                    moment(bucket.value).valueOf(),
                                    pi.count,
                                ])
                            }
                        })
                    }
                })
                positiveDataArr = positiveDataArr
                    .sort((a, b) => {
                        return b[0] - a[0]
                    })
                    .reverse()
                negativeDataArr = negativeDataArr
                    .sort((a, b) => {
                        return b[0] - a[0]
                    })
                    .reverse()
                neutralDataArr = neutralDataArr
                    .sort((a, b) => {
                        return b[0] - a[0]
                    })
                    .reverse()
                this.sentimentTimeSeriesData.series
                this.sentimentTimeSeriesData.series.push(
                    {
                        data: positiveDataArr,
                        name: 'Postive',
                        color: sentimentVsColor['positive'],
                    },
                    {
                        data: negativeDataArr,
                        name: 'Negative',
                        color: sentimentVsColor['negative'],
                    },
                    {
                        data: neutralDataArr,
                        name: 'Neutral',
                        color: sentimentVsColor['neutral'],
                    }
                )
            }

            if (data?.vaccine_countries) {
                let categories = []
                let vaccineByCountries = data.vaccine_countries
                let usaArr = []
                let indiaArr = []
                let mexicoArr = []
                vaccineByCountries.forEach((vC) => {
                    categories.push(vC.val)
                    for (let i = 0; i <= 6; i += 2) {
                        if (vC.country[i] == 'USA') {
                            usaArr.push(vC.country[i + 1])
                        } else if (vC.country[i] == 'India') {
                            indiaArr.push(vC.country[i + 1])
                        } else if (vC.country[i] == 'Mexico') {
                            mexicoArr.push(vC.country[i + 1])
                        }
                    }
                })

                let seriesData = []
                seriesData.push({ name: 'USA', data: usaArr })
                seriesData.push({ name: 'India', data: indiaArr })
                seriesData.push({ name: 'Mexico', data: mexicoArr })

                this.vaccineMentionsByCountryData.xAxis.categories = categories
                this.vaccineMentionsByCountryData.series = seriesData
            }

            if (data?.vaccine_sentiment) {
                let categories = []
                let vaccineBySentiment = data.vaccine_sentiment
                let neutralArr = []
                let negativeArr = []
                let positiveArr = []
                vaccineBySentiment.forEach((vS) => {
                    categories.push(vS.val)
                    for (let i = 0; i <= 6; i += 2) {
                        if (vS.sentiment_score[i] == 'neutral') {
                            neutralArr.push(vS.sentiment_score[i + 1])
                        } else if (vS.sentiment_score[i] == 'negative') {
                            negativeArr.push(vS.sentiment_score[i + 1])
                        } else if (vS.sentiment_score[i] == 'positive') {
                            positiveArr.push(vS.sentiment_score[i + 1])
                        }
                    }
                })

                let seriesData = []
                seriesData.push({
                    name: 'Neutral',
                    data: neutralArr,
                    color: sentimentVsColor['neutral'],
                })
                seriesData.push({
                    name: 'Negative',
                    data: negativeArr,
                    color: sentimentVsColor['negative'],
                })
                seriesData.push({
                    name: 'Positive',
                    data: positiveArr,
                    color: sentimentVsColor['positive'],
                })

                this.vaccineCompaniesBySentimentData.xAxis.categories =
                    categories
                this.vaccineCompaniesBySentimentData.series = seriesData
            }
        },
    },
}
</script>
