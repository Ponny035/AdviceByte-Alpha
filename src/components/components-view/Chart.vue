<template>
    <div class="spiderChart">
        <spider-graph>

            <canvas id="myChart" width="400" height="400"></canvas>

            <form class="input-custom">
                <div class="input-group flex-nowrap">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="addon-wrapping">Algorithm</span>
                    </div>
                    <input
                        type="number"
                        id="exp-algo"
                        class="validate form-control"
                        placeholder="experience..."
                    />
                </div>
            </form>
        </spider-graph>
    </div>
</template>

<script>
import spiderChart from './chartSpider.js'
export default {
    component: {
        spiderChart
    }



}
</script>

<style>
.spiderChart {
    width: 500px;
    height: 100px;
    margin: auto;
}
.input-custom {
    width: 300px;
    height: 60px;
    margin: auto;
}
</style>