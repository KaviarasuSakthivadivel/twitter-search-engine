<template>
    <div class="p-5">
        <div class="flex justify-center chart-title">Top Influencers</div>
        <el-table
            :data="tableData"
            height="410"
            :default-sort="{ prop: 'percentage', order: 'descending' }"
        >
            <el-table-column prop="profileName" label="POI Name" width="300">
                <template slot-scope="scope">
                    <div class="flex flex-row items-center">
                        <el-avatar
                            size="medium"
                            icon="el-icon-user-solid"
                            :src="scope.row.profile_url"
                        ></el-avatar>
                        <div class="ml-5">{{ scope.row.profile_name }}</div>
                    </div>
                </template>
            </el-table-column>
            <el-table-column
                prop="positive_count"
                label="Positive Reply Tweets"
            ></el-table-column>
            <el-table-column prop="percentage" label="Impact in %">
                <template slot-scope="scope">
                    {{ scope.row.percentage }}
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
import { topInfluencers } from '@/helpers/constants'
import cloneDeep from 'lodash/cloneDeep'
export default {
    data: () => ({
        tableData: cloneDeep(topInfluencers),
    }),
}
</script>
