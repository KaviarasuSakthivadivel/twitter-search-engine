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
            if (this.query === 'COVID') {
                let response = {
                    status: 'ok',
                    totalResults: 36587,
                    articles: [
                        {
                            source: { id: null, name: 'New Zealand Herald' },
                            author: 'newsfeeds@nzherald.co.nz',
                            title: "Kiwi Covid denier's Delta hell: 'We were planning my funeral'",
                            description:
                                'Hamilton mum Karina Haira thought she could beat Covid-19 when she first caught the virus. \n\n"I just thought, I can beat this. It\'s just the flu," said 37-year-old Haira, an active asthmatic who played ...',
                            url: 'https://www.nzherald.co.nz/nz/covid-19-delta-outbreak-hamilton-mum-in-denial-until-she-caught-covid/ZWGR5AN6BU7YXJCVKPAJEKWVDY/',
                            urlToImage:
                                'https://www.nzherald.co.nz/resizer/9UAtGFgtDLlbMIb59MEv5ovsovQ=/1200x675/filters:quality(70)/cloudfront-ap-southeast-2.images.arcpublishing.com/nzme/LQXM5ERMZWFZC3RZTSNPXUG3MA.jpg',
                            publishedAt: '2021-12-06T16:07:45Z',
                            content:
                                'COVID-19 patient Karina Hira documents her struggle with the virus. Source / Karina HiraHamilton mum Karina Haira thought she could beat Covid-19 when she first caught the virus.\r\n"I just thought, I … [+4026 chars]',
                        },
                        {
                            source: { id: null, name: 'New Zealand Herald' },
                            author: 'newsfeeds@nzherald.co.nz',
                            title: "Live: Experts warn 'race is on' as new Covid drug set for NZ",
                            description:
                                'A new drug to treat high-risk Covid-19 patients is a "big step forward" in the fight against the pandemic, Prime Minister Jacinda Ardern says. \n\nBut an expert warns the "race is on" for regulatory body ...',
                            url: 'https://www.nzherald.co.nz/nz/covid-19-delta-new-pfizer-antiviral-drug-big-step-forward-ardern-says-in-fight-against-outbreak/OJGLCQFHY4OMP75WFG2H7KC3DU/',
                            urlToImage:
                                'https://www.nzherald.co.nz/resizer/dkHPa2cAINadKQ1lqRG-dfM7JY4=/1200x675/filters:quality(70)/cloudfront-ap-southeast-2.images.arcpublishing.com/nzme/IBQDT6JQ5SY5V4VLYNBII5SKME.jpg',
                            publishedAt: '2021-12-06T16:07:45Z',
                            content:
                                "December 6 2021\r\nPM Jacinda Ardern says Pharmac has secured 60,000 doses of Pfizer's new antiviral medicine. It had up to 90% reduction in death, and could be taken at the first stage of someone gett… [+4444 chars]",
                        },
                        {
                            source: { id: null, name: 'Business Wire' },
                            author: null,
                            title: 'BioGX COVID-19 Tests Detect Omicron SARS-CoV-2 Variant',
                            description:
                                'BIRMINGHAM, Ala.--(BUSINESS WIRE)--BioGX announced that all BioGX SARS-CoV-2 tests will detect the latest emerging Omicron variant of the coronavirus.',
                            url: 'https://www.businesswire.com/news/home/20211206005557/en/BioGX-COVID-19-Tests-Detect-Omicron-SARS-CoV-2-Variant',
                            urlToImage:
                                'https://mms.businesswire.com/media/20211206005557/en/933072/23/BioGX_Logo.jpg',
                            publishedAt: '2021-12-06T16:06:13Z',
                            content:
                                'BIRMINGHAM, Ala.--(BUSINESS WIRE)--BioGX, a global provider of molecular diagnostic solutions, announced that the Omicron (B.1.1.529), the latest emerging SARS-CoV-2 variant of concern, will be detec… [+2747 chars]',
                        },
                        {
                            source: { id: null, name: 'The Punch' },
                            author: 'Agency Report',
                            title: 'De Bruyne to start for Man City in Leipzig after COVID setback',
                            description:
                                'Kevin De Bruyne will make his first Manchester City start for a month in Tuesday’s Champions League trip to RB Leipzig after Pep Guardiola revealed the Belgian was left feeling “empty” by coronavirus. De Bruyne’s season has been heavily disrupted by injury an…',
                            url: 'https://punchng.com/de-bruyne-to-start-for-man-city-in-leipzig-after-covid-setback/',
                            urlToImage:
                                'https://cdn.punchng.com/wp-content/uploads/2018/08/15194507/De-Bruyne.png',
                            publishedAt: '2021-12-06T16:05:32Z',
                            content:
                                'Kevin De Bruyne will make his first Manchester City start for a month in Tuesday’s Champions League trip to RB Leipzig after Pep Guardiola revealed the Belgian was left feeling “empty” by coronavirus… [+1248 chars]',
                        },
                        {
                            source: { id: 'cbc-news', name: 'CBC News' },
                            author: 'Winnipeg Free Press',
                            title: 'Positive COVID test puts RMTC production on hold',
                            description:
                                'Nine days into its first live production in nearly two years, the Royal Manitoba Theatre Centre cancelled weekend shows following a single COVID-19 diagnosis among the cast and crew of Orlando.',
                            url: 'https://www.cbc.ca/news/canada/manitoba/positive-covid-test-puts-rmtc-production-on-hold-wfpcbc-wfp-1.6275006',
                            urlToImage:
                                'https://i.cbc.ca/1.6148361.1629499104!/fileImage/httpImage/image.JPG_gen/derivatives/16x9_620/royal-manitoba-theatre-centre-mainstage-exterior.JPG',
                            publishedAt: '2021-12-06T16:05:16Z',
                            content:
                                'Nine days into its first live production in nearly two years, the Royal Manitoba Theatre Centre cancelled weekend shows following a single COVID-19 diagnosis among the cast and crew of Orlando.\r\nExec… [+583 chars]',
                        },
                        {
                            source: { id: null, name: 'Deadline' },
                            author: 'Greg Evans',
                            title: 'Broadway’s ‘Wicked’ Weekend Performances Canceled Due To Covid',
                            description:
                                'The Broadway production of Wicked canceled three performances over the weekend due to positive Covid tests within the company. The announcement also noted scheduled absences contributed to the cancellations. The musical’s Saturday evening, Sunday matinee and …',
                            url: 'https://deadline.com/2021/12/wicked-broadway-covid-canceled-weekend-performances-1234885446/',
                            urlToImage:
                                'https://deadline.com/wp-content/uploads/2021/12/GINNA-CLAIRE-MASON-and-HANNAH-CORNEAU-in-WICKED-Photo-by-Joan-Marcus-2019.jpg?w=1024',
                            publishedAt: '2021-12-06T16:04:55Z',
                            content:
                                'The Broadway production of Wicked canceled three performances over the weekend due to positive Covid tests within the company. The announcement also noted scheduled absences contributed to the cancel… [+1214 chars]',
                        },
                        {
                            source: { id: null, name: 'Alt-market.us' },
                            author: 'Mike Rivero',
                            title: 'Omicron: We Warned You The Covid Farce Would Never End',
                            description:
                                'Remember when Anthony Fauci and other government paid medical “professionals” said that Americans needed to mask up and stay home for two weeks to “flatten the curve” on the covid pandemic? Remember when they came back two weeks later and said they needed ano…',
                            url: 'https://alt-market.us/omicron-we-warned-you-the-covid-farce-would-never-end/',
                            urlToImage:
                                'https://secureservercdn.net/104.238.68.196/yb3.41b.myftpupload.com/wp-content/uploads/2021/12/CovidFear2.jpg',
                            publishedAt: '2021-12-06T16:04:32Z',
                            content:
                                'By Brandon Smith\r\nRemember when Anthony Fauci and other government paid medical professionals said that Americans needed to mask up and stay home for two weeks to flatten the curve on the covid pande… [+11854 chars]',
                        },
                        {
                            source: { id: null, name: 'Stuff.co.nz' },
                            author: 'JOSEPHINE FRANKS',
                            title: 'Covid-19: Teacher wellbeing plummets and workloads rise due to pandemic',
                            description:
                                "Almost half of teachers say they're unhappy at work, leaving them less satisifed with life than the average Kiwi.",
                            url: 'https://www.stuff.co.nz/national/education/127200329/covid19-teacher-wellbeing-plummets-and-workloads-rise-due-to-pandemic',
                            urlToImage:
                                'https://resources.stuff.co.nz/content/dam/images/4/y/v/f/n/r/image.related.StuffLandscapeSixteenByNine.1420x800.23qceh.png/1638763054374.jpg',
                            publishedAt: '2021-12-06T16:00:00Z',
                            content:
                                'Principals and teachers feel unhappy, overworked and unsupported amid the Covid-19 pandemic, new research from the Education Review Office (ERO) shows.\r\n Wellbeing and workloads have been negatively … [+3072 chars]',
                        },
                        {
                            source: { id: null, name: 'Stuff.co.nz' },
                            author: 'TODD NIALL',
                            title: 'Covid-19: Aucklanders are seeing red, despite traffic light freedoms',
                            description:
                                'Restrictions are eased, but the frustrations built up over months of Covid-19 lockdown are being expressed as aggression and in low-level crime.',
                            url: 'https://www.stuff.co.nz/opinion/127177327/covid19-aucklanders-are-seeing-red-despite-traffic-light-freedoms',
                            urlToImage:
                                'https://resources.stuff.co.nz/content/dam/images/4/y/w/3/x/u/image.related.StuffLandscapeSixteenByNine.1420x800.23punj.png/1638738601960.jpg',
                            publishedAt: '2021-12-06T16:00:00Z',
                            content:
                                'In the first week of Aucklands more relaxed Covid-19 restrictions, some of the sacrifice and dislocation endured during 107 days of alert level life has dissipated.\r\n The world of gym-going, dining a… [+3960 chars]',
                        },
                        {
                            source: {
                                id: null,
                                name: 'American Medical Association',
                            },
                            author: null,
                            title: 'COVID-19 Update: Omicron Variant',
                            description:
                                'Infectious disease experts Adam Lauring, MD, PhD, and Carlos del Rio, MD, join JAMA Associate Editor Preeti Malani, MD, MSJ, for a discussion of the newly emerged Omicron variant, the potential for a 2021-2022 "twindemic" with flu, and the latest COVID-19 cli…',
                            url: 'https://edhub.ama-assn.org/jn-learning/audio-player/18660079',
                            urlToImage:
                                'https://cdn.edhub.ama-assn.org/ama/content_public/multimedia/jsx210060audioa_thumb.jpeg?Expires=2147483647&Signature=G5A4hJ4djyOWIFFmZAsiiIs6NR0ee~FfNuyQ28RPMAMEffbk8E6YvNJPOQNPVxT9qLkU2p663D-PGO0-oWZdyrUc8f94Ihqlo6cNECN1gXQmRGmI-ekE58Yudk~IbeSM6rM4wc0X4mHQkz~7qpMrfrpLJ-CUtRgocWTQsvGuX0MK2LARTvHqMe6PatDaKBDjE-B8GUwTnhLVGRN8JmbXYBJ6UsDv331bsH-S8mlx0tZgQQyhfl18dWBONpe8CYSi~C5m8M8l8-PMcO19N0XyxleDO3Wt5kPE7XrA~j1zTzhH51Xtay-Y3bU9AoKhKYGOeAg4KsZmu5gd-7oMEtN06w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA',
                            publishedAt: '2021-12-06T16:00:00Z',
                            content:
                                'Infectious disease experts Adam Lauring, MD, PhD, and Carlos del Rio, MD, join JAMA Associate Editor Preeti Malani, MD, MSJ, for a discussion of the newly emerged Omicron variant, the potential for a… [+100 chars]',
                        },
                        {
                            source: { id: null, name: 'Raw Story' },
                            author: 'Bob Brigham',
                            title: 'Trump lashes out at Biden after media reports on his positive COVID test before first debate',
                            description:
                                "Donald Trump lashed out at the media on Monday for reporting that former chief of staff Mark Meadows revealed in a new book that the 2020 GOP nominee tested positive for coronavirus before the first debate with Joe Biden.Trump's statement, emailed to reporter…",
                            url: 'https://www.rawstory.com/trump-lashes-out-at-biden-after-media-reported-on-his-positive-test-before-first-debate/',
                            urlToImage:
                                'https://www.rawstory.com/media-library/unstable-and-dangerous-trump-s-unhinged-call-provides-more-evidence-of-his-mental-deterioration.jpg?id=28171792&width=1200&coordinates=0%2C0%2C0%2C61&height=600',
                            publishedAt: '2021-12-06T15:59:37Z',
                            content:
                                'Where Dole became such a hard man\r\nBorn in 1923 in Russell, Kansas, Dole grew up as a boy of the Midwest at a time when a place like rural Kansas seemed like a place of the future America. This did n… [+24175 chars]',
                        },
                        {
                            source: {
                                id: 'business-insider',
                                name: 'Business Insider',
                            },
                            author: 'jlahut@insider.com (Jake Lahut)',
                            title: "Trump responds to report that he tested positive for COVID before debate, says 'Biden goes around coughing on people all over the place'",
                            description:
                                '"Biden goes around coughing on people all over the place, and yet the Corrupt News doesn\'t even cover it," Trump said at one point in the statement.',
                            url: 'https://www.businessinsider.com/trump-covid-positive-biden-statement-meadows-book-coughing-on-people-2021-12',
                            urlToImage:
                                'https://i.insider.com/61ae29ad0b0acf0018c40397?width=1200&format=jpeg',
                            publishedAt: '2021-12-06T15:59:17Z',
                            content:
                                'In a statement Monday morning, former President Donald Trump denied revelations from his own former chief of staff\'s book on the updated timeline of his COVID-19 infection from October 2020.\r\n"The Fa… [+1136 chars]',
                        },
                        {
                            source: { id: 'bbc-news', name: 'BBC News' },
                            author: null,
                            title: 'Covid-19: What do we know about the Omicron variant?',
                            description:
                                'Professor Willem Hanekom says that the Omicron variant "is spreading extraordinarily fast in South Africa".',
                            url: 'https://www.bbc.co.uk/news/av/world-africa-59553131',
                            urlToImage:
                                'https://ichef.bbci.co.uk/news/1024/branded_news/D596/production/_121987645_p0b8dl6z.jpg',
                            publishedAt: '2021-12-06T15:58:21Z',
                            content:
                                'The Omicron variant "is spreading extraordinarily fast in South Africa" and new travel bans are "doing very little to stop the spread" of the new variant, according to a leading vaccines expert.\r\nSpe… [+430 chars]',
                        },
                        {
                            source: { id: null, name: 'Sputnik International' },
                            author: 'James Tweedie',
                            title: 'Boost for Britain! Is the UK’s COVID-19 Third Jab Campaign Saving Lives?',
                            description:
                                'The spread of the new, more-transmissible, yet apparently less virulent, Omicron variant across the globe has raised fears of “breakthrough infections” and a huge fourth wave of COVID-19 over the northern hemisphere winter.',
                            url: 'https://sputniknews.com/20211206/boost-for-britain-is-the-uks-covid-19-third-jab-campaign-saving-lives-1091289488.html',
                            urlToImage:
                                'https://cdnn1.img.sputniknews.com/images/sharing/article/eng/1091289488.jpg?10912891791638806175',
                            publishedAt: '2021-12-06T15:56:14Z',
                            content:
                                'Today the UK has ordered 114 million more Pfizer and Moderna vaccines for the next two years, future proofing our lifesaving vaccine programme. \r\nThese vaccines can also be edited against any future … [+109 chars]',
                        },
                        {
                            source: { id: null, name: 'Republic World' },
                            author: 'Press Trust Of India',
                            title: 'One-time incentive of Rs 6K for home guards on Covid duty in Uttarakhand',
                            description:
                                'Uttarakhand Chief Minister Pushkar Singh Dhami on Monday announced a one-time incentive of Rs 6,000 to all home guard jawans engaged in Covid duty in the state since the pandemic struck.',
                            url: 'https://m.republicworld.com/india-news/general-news/one-time-incentive-of-rs-6k-for-home-guards-on-covid-duty-in-uttarakhand.html',
                            urlToImage:
                                'https://img.republicworld.com/republic-prod/stories/promolarge/xhdpi/dfcfw24xcbqakmwa_1638806069.jpeg',
                            publishedAt: '2021-12-06T15:56:00Z',
                            content:
                                'Uttarakhand Chief Minister Pushkar Singh Dhami on Monday announced a one-time incentive of Rs 6,000 to all home guard jawans engaged in Covid duty in the state since the pandemic struck.\r\nMaking the … [+1156 chars]',
                        },
                        {
                            source: { id: 'independent', name: 'Independent' },
                            author: 'Rebecca Black',
                            title: 'Stormont Assembly debate on Covid certification ‘absolutely should happen’',
                            description:
                                'DUP MLA Christopher Stalford said MLAs must have the opportunity to debate the requirement for Covid certification to enter some hospitality venues.',
                            url: 'https://www.independent.co.uk/news/uk/dup-belfast-city-hall-northern-ireland-rebecca-black-b1970584.html',
                            urlToImage:
                                'https://static.independent.co.uk/2021/12/06/13/907228254feb00777b1d6ef973da622eY29udGVudHNlYXJjaGFwaSwxNjM4ODgyODMx-2.64121832.jpg?width=1200&auto=webp&quality=75',
                            publishedAt: '2021-12-06T15:55:59Z',
                            content:
                                'The Covid certification scheme absolutely should be brought to the Stormont Assembly for debate, a DUP MLA has said.\r\nChristopher Stalford expressed disappointment in the Assembly on Monday that ther… [+2834 chars]',
                        },
                        {
                            source: { id: null, name: 'Worldsoccertalk.com' },
                            author: 'AFP',
                            title: 'De Bruyne to start for Man City in Leipzig after Covid setback',
                            description:
                                'Manchester (United Kingdom) (AFP) – Kevin De Bruyne will make his first Manchester City start for a month in Tuesday’s Champions League trip to RB Leipzig after Pep Guardiola revealed the Belgian was left feeling...',
                            url: 'https://worldsoccertalk.com/2021/12/06/de-bruyne-to-start-for-man-city-in-leipzig-after-covid-setback/',
                            urlToImage:
                                'https://worldsoccertalk.com/wp-content/uploads/2021/12/d8f3ea46816894d9434b427b925428ffc61d1b0f.jpg',
                            publishedAt: '2021-12-06T15:55:56Z',
                            content:
                                'Manchester (United Kingdom) (AFP) – Kevin De Bruyne will make his first Manchester City start for a month in Tuesday’s Champions League trip to RB Leipzig after Pep Guardiola revealed the Belgian was… [+1278 chars]',
                        },
                        {
                            source: { id: null, name: 'Forbes' },
                            author: 'Nicholas Reimann, Forbes Staff, \n Nicholas Reimann, Forbes Staff\n https://www.forbes.com/sites/nicholasreimann/',
                            title: 'Covid Outbreak From Norwegian Cruise Grows To 17 Cases—With At Least 1 Omicron',
                            description:
                                'The probable omicron case was among a crew member who "was in isolation for the entirety of the cruise," according to Norwegian.',
                            url: 'https://www.forbes.com/sites/nicholasreimann/2021/12/06/covid-outbreak-from-norwegian-cruise-grows-to-17-cases-with-at-least-1-omicron/',
                            urlToImage:
                                'https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F61ae306fecfb264069897731%2F0x0.jpg%3FcropX1%3D0%26cropX2%3D5112%26cropY1%3D285%26cropY2%3D3161',
                            publishedAt: '2021-12-06T15:55:01Z',
                            content:
                                'At least 17 people who were aboard a Norwegian Cruise Line ship in New Orleans have tested positive for Covid-19, according to the Louisiana Department of Health, including one "probable case of Omic… [+2615 chars]',
                        },
                        {
                            source: { id: null, name: 'menshealth.com' },
                            author: 'Philip Ellis',
                            title: 'Hugh Jackman Just Got His Covid Vaccine Booster Shot',
                            description:
                                'The actor shared the moment he got his third dose of the Covid vaccine on Instagram.',
                            url: 'https://www.menshealth.com/health/a38439359/hugh-jackman-vaccine-booster/',
                            urlToImage:
                                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/jackman-1638805107.png?crop=1.00xw:0.408xh;0,0.0756xh&resize=1200:*',
                            publishedAt: '2021-12-06T15:55:00Z',
                            content:
                                'Hugh Jackman is best known for playing Wolverine, a superhero whose mutant abilities mean he is impervious to harm and can heal from any injury immediately. In real life, however, Jackman is taking e… [+1888 chars]',
                        },
                        {
                            source: { id: null, name: 'Slashdot.org' },
                            author: 'feedfeeder',
                            title: 'Stocks and Oil Rise on Hopes of Milder Covid Variant - The Wall Street Journal',
                            description:
                                'Stocks and Oil Rise on Hopes of Milder Covid VariantThe Wall Street Journal Dow jumps 600 points as Monday rally accelerates, investors look past omicron threatCNBC Opening Bell: US Futures, European Stocks Bounce On Positive Omicron HeadlinesInvesting.com Do…',
                            url: 'https://slashdot.org/firehose.pl?op=view&amp;id=156273735',
                            urlToImage: null,
                            publishedAt: '2021-12-06T15:54:37Z',
                            content:
                                'The Fine Print: The following comments are owned by whoever posted them. We are not responsible for them in any way.',
                        },
                    ],
                }
                this.allArticles = response?.articles || []
            } else {
                try {
                    let response = await axios({
                        method: 'get',
                        url: `https://newsapi.org/v2/everything?qInTitle=${this.query}&sortBy=publishedAt&apiKey=1e51b53cb2d3419e9c8a52c4ac3a9c60&language=en&language=es`,
                    })
                    this.allArticles = response?.data?.articles || []
                } catch (error) {
                    this.$message.error(error?.message)
                }
            }
        },
        openNews(url) {
            window.open(url)
        },
    },
}
</script>
