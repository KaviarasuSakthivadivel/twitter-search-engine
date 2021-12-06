<template>
    <div class="p-5">
        <div class="flex justify-center chart-title">
            POI persuasion toward Vaccination
        </div>
        <el-table :data="tableData" height="400">
            <el-table-column prop="profileName" label="POI Name">
                <template slot-scope="scope">
                    <div class="flex flex-row items-center">
                        <el-avatar
                            size="medium"
                            icon="el-icon-user-solid"
                            :src="scope.row.profile_url"
                        ></el-avatar>
                        <div class="ml-5">{{ scope.row.profileName }}</div>
                    </div>
                </template>
            </el-table-column>
            <el-table-column
                prop="count"
                sortable
                label="Tweets Count"
            ></el-table-column>
        </el-table>
    </div>
</template>
<script>
export default {
    data: () => ({
        tableData: [
            {
                profileName: 'KamalaHarris',
                profile_url:
                    'https://pbs.twimg.com/profile_images/1377062766314467332/2hyqngJz_normal.jpg',
                count: 1032,
            },
            {
                profileName: 'CDCgov',
                profile_url:
                    'https://pbs.twimg.com/profile_images/880104586211581952/KPwn1JyQ_normal.jpg',
                count: 123,
            },
            {
                profileName: 'KamalaHarris',
                profile_url:
                    'https://pbs.twimg.com/profile_images/1377062766314467332/2hyqngJz_normal.jpg',
                count: 1032,
            },
            {
                profileName: 'CDCgov',
                profile_url:
                    'https://pbs.twimg.com/profile_images/880104586211581952/KPwn1JyQ_normal.jpg',
                count: 123,
            },
            {
                profileName: 'KamalaHarris',
                profile_url:
                    'https://pbs.twimg.com/profile_images/1377062766314467332/2hyqngJz_normal.jpg',
                count: 1032,
            },
            {
                profileName: 'CDCgov',
                profile_url:
                    'https://pbs.twimg.com/profile_images/880104586211581952/KPwn1JyQ_normal.jpg',
                count: 123,
            },
            {
                profileName: 'KamalaHarris',
                profile_url:
                    'https://pbs.twimg.com/profile_images/1377062766314467332/2hyqngJz_normal.jpg',
                count: 1032,
            },
            {
                profileName: 'CDCgov',
                profile_url:
                    'https://pbs.twimg.com/profile_images/880104586211581952/KPwn1JyQ_normal.jpg',
                count: 123,
            },
        ],
    }),
}
</script>
