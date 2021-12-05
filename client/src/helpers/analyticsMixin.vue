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
			if(data?.time_with_sentiment) {
				let sentimentTweetDate = data.time_with_sentiment['tweet_date,sentiment']
				let tweetDateDataArr = []
				sentimentTweetDate.forEach((bucket) => {
					if (moment(bucket.val).valueOf() > 1630468800000) {
                        tweetDateDataArr.push([
                            moment(bucket.val).valueOf(),
                            bucket.count,
                        ])
                    }
				})
				this.sentimentTimeSeriesData.series[0].data = tweetDateDataArr
					.sort((a, b) => {
					    return b[0] - a[0]
					})
					.reverse()
			}

			if(data?.vaccine_countries) {
				let categories = []
				let vaccineByCountries = data.vaccine_countries;
				let usaArr = []
				let indiaArr = []
				let mexicoArr = []
				vaccineByCountries.forEach((vC) => {
					categories.push(vC.val);
					for(let i = 0; i < 6; i++) {
						if(i === 0) {
							usaArr.push(vC.country[i + 1]);
						} else if(i === 2) {
							indiaArr.push(vC.country[i + 1]);
						} else if(i === 4){
							mexicoArr.push(vC.country[i + 1]);
						}
					}
				})

				let seriesData = [];
				seriesData.push({'name': "USA", 'data': usaArr})
				seriesData.push({'name': "India", 'data': indiaArr})
				seriesData.push({'name': "Mexico", 'data': mexicoArr})

				this.vaccineMentionsByCountryData.xAxis.categories = categories
				this.vaccineMentionsByCountryData.series = seriesData;
			}

			if(data?.vaccine_sentiment) {
				let categories = []
				let vaccineBySentiment = data.vaccine_sentiment;
				let neutralArr = []
				let negativeArr = []
				let positiveArr = []
				vaccineBySentiment.forEach((vS) => {
					categories.push(vS.val);
					for(let i = 0; i < 6; i++) {
						if(i === 0) {
							neutralArr.push(vS.sentiment_score[i + 1]);
						} else if(i === 2) {
							negativeArr.push(vS.sentiment_score[i + 1]);
						} else if(i === 4){
							positiveArr.push(vS.sentiment_score[i + 1]);
						}
					}
				})

				let seriesData = [];
				seriesData.push({'name': "Neutral", 'data': neutralArr})
				seriesData.push({'name': "Negative", 'data': negativeArr})
				seriesData.push({'name': "Positive", 'data': positiveArr})

				this.vaccineCompaniesBySentimentData.xAxis.categories = categories
				this.vaccineCompaniesBySentimentData.series = seriesData;
			}


		}
    },
}
</script>
