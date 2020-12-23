<template>
    <div class="activityNo">
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-white">
                <div class="bg-white p-3 mb rounded box-try">
                    <div class="row justify-content-between">
                        <!-- ชื่อของ -->
                        <div class="font text-left col-sm-6 col-md-8" style="">
                            {{ forum.Activity_Name }}
                        </div>
                        <div class="col col-lg-2">
                            <a
                                @click="viewDashboard"
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
                    {{ forum.Activity_Description }}
                </div>
                <div class="Footer" style="padding-bottom: 10%"></div>
            </div>
        </div>
        
    
    </div>
</template>

<script>


export default {
    methods: {
        viewDashboard() {
            this.$router.push({ path: '/dashboard' })
        }
    },
    components: {
        
    },
    props: {
        forum: { 
            default(){
                return {
                    Activity_Name: '',
                    Activity_Description: '',
                }
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