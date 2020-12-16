<template>
    <div class="getAnswer">
        <!-- หมุนตอนโหลด -->
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-white">
                <div class="bg-white p-3 mb rounded box-try">
                    <div class="row justify-content-between">
                        <!-- ชื่อของ -->
                         <div class="getActivity" v-if="forum.Is_Forum">
                             <!-- <div class="getActivity" v-if="isForum in data === '1'"> -->
                            <Activity :forum="forum"></Activity>
                        </div>
                <div class="getActivity" v-else>
                    <!-- <div class="getActivity" v-else-if="isForum in data === '0'"> -->
                    <Activito :forum="forum"></Activito>
                </div>
                    </div>
                </div>
                <!-- Response -->
               
                <div class="Footer" style="padding-bottom: 10%"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Activity from './getActivity' //มีปุ่มส่ง
import Activito from './Activity_0' // ไม่มีปุ่มส่ง

export default {
     data() {
        return {
            forum:{
                Is_Forum: 1
            },
            forumId:''
        };
    },
    async mounted() {
      console.log(this.$route.params.id)
      console.log("HEELOO")
      await this.activities()
      console.log("HEELOO ISUS")
    },
    components: {
        Activito,
        Activity
    },
    methods: {
        async activities() {
            console.log("avtivities")
                try {
                    const response = await axios.post('http://localhost:3000/forum/herderInformation',
                    {
                    forumId: this.$route.params.id
                    })
                    console.log(response)
                    const res = response.data

                    this.forum = res[0]
                    console.log(res)

                } catch (error) {
                  console.log(error)
                }
        }

    }
}
</script>

<style>
.font {
    font-family: poppins;
    font-size: 18px;
    font-weight: bold;
    /* align-content: left; */
    color: #37437e;
    padding-left: 7%;
}

.back {
    height: 30%;
    width: 30%;
    margin-left: 10%;
}
</style>