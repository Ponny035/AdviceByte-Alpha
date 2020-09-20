<template>
    <div class="container p-2 bd-highlight">
        <div class="content-bg bg-white">
            <div class="shadow-sm p-3 mb-5 bg-white rounded">
                <div class="row justify-content-md-center">
                    <div class="navigator-font col-md-3" @click="viewProfile">
                        Profile
                    </div>
                    <div class="navigator-font col-md-3">History</div>
                    <div class="navigator-font col-md-3" @click="viewStat">
                        Stat
                    </div>
                </div>
            </div>
            <div class="content-box">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        viewStat() {
            this.$router.push({ name: 'stat' })
        },
        viewProfile() {
            this.$router.push({ path: '/profile' })
        }
    }
}
</script>

<style></style>
