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
                        <div class="ml-5">{{ scope.row.profile_name }}</div>
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
import { poiPersuasion } from '@/helpers/constants'
import cloneDeep from 'lodash/cloneDeep'
export default {
    data: () => ({
        tableData: cloneDeep(poiPersuasion),
    }),
}
</script>
