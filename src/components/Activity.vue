<template>
    <div class="getAnswer">
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-white">
                <div class="bg-white p-3 mb rounded box-try">
                    <div class="row justify-content-between">
                        <!-- title mission -->
                        <div class="font text-left col-sm-6 col-md-8" style="">
                            the goos doctor never knpw what he deaking with you
                            you with
                        </div>
                        <div class="col col-lg-2">
                            <a
                                @click="viewMission"
                                style="font-size: 15px; color: #37437e"
                            >
                                <img src="~@/assets/Back.svg" class="back" />
                                Back
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Response -->
                <div class="getReponse">
                    <Response></Response>
                </div>
                <div class="Footer" style="padding-bottom: 10%"></div>
            </div>
        </div>
    </div>
</template>

<script>
import Response from './getResponse'

export default {
    methods: {
        viewMission() {
            this.$router.push({ path: '/Mission' })
        }
    },
    components: {
        Response
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