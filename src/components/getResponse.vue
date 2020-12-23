<template>
    <div class="getReponse">
        <template v-for="(item, i) in responses" :key="i">
            <div class="container">
                <div
                    class="shadow-sm mission-stagee bg justify-content-sm-center"
                >
                    <div class="container">
                        <div class="row">
                            <div class="text-left">
                                {{ item.Comment }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    async mounted() {
        await this.getResponse()
    },
    methods: {
        async getResponse() {
            await axios
                .post(`${process.env.VUE_APP_API_URI}/forum/commentInformation`, {
                    forumId: parseInt(this.$route.params.id, 10)
                })
                .then(response => {
                    if (response.status === 200) {
                        this.responses = response.data
                    }
                })
                .catch(err => {
                    console.log(err)
                })
        }
    },
    data() {
        return {
            responses: []
        }
    }
}
</script>

<style>
.bg {
    background-color: rgb(248, 248, 248);
}
</style>
