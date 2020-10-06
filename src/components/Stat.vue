<template>
    <div class="stat">
        <!-- award head -->
        <div class="peference">
            <h4 class="font-weight-bold text-left">Peference</h4>
            <div class="text-left">
                <p class="description">Description Coming Later</p>
            </div>
            <hr />
            <!-- end head -->
            <h4 class="font-weight-bold text-left">Spider Graph</h4>
            <div class="row">
                <div class="empty-box">
                    <Chart></Chart>
                </div>
            </div>
        </div>
        <!-- <hr /> -->
        <!-- <h4 class="font-weight-bold text-left">Experience Graph</h4>
        <div class="row">
            <div class="empty-box">
                ..Coming Soon..
            </div>
        </div>
        <hr /> -->
    </div>
</template>

<script>
import Chart from './components-view/Chart';
export default {
    components: { 
        Chart,
    },
    name: 'HelloWorld',
    data() {
        return {
            msg: 'Welcome to Your Vue.js App'
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.stat {
    margin-left: 5%;
}
.empty-box{
    padding-bottom: 25%;
    padding-left: 12%;
    padding-top: 5%;
}
</style>
