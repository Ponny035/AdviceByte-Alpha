<template>
    <div class="spiderChart">
        <canvas id="myChart" ref="myChart" width="400" height="400"></canvas>

        <button @click="increment">Click me</button>
    </div>
</template>

<script>
import Chart from 'chart.js'

export default {
    mounted() {
        var options = {
            responsive: false,
            maintainAspectRatio: true,
            scale: {
                ticks: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
        var ctx = document.getElementById('myChart').getContext('2d')
        // eslint-disable-next-line
        var myChart = new Chart(ctx, {
            type: 'radar',
            options: options,
            data: {
                ...this.myChart
            }
        })
    },
    data() {
        return {
            myChart: {
                labels: [
                    'Algorithm',
                    'Data Structure',
                    'Mathematic',
                    'Coding',
                    'Communication',
                    'Language',
                    'Self-motivation',
                    'Problem Solivg'
                ],
                datasets: [
                    {
                        label: 'Username',
                        backgroundColor: 'rgb(35, 50, 120, 0.5)',
                        data: [20, 10, 10, 10, 10, 10, 10, 10]
                    },
                    {
                        label: 'Base Line',
                        backgroundColor: 'rgb(195, 195, 245, 0.3)',
                        data: [40, 40, 40, 40, 40, 40, 40, 40]
                    }
                ]
            },
            i: 0
        }
    },
    methods: {
        increment() {
            this.i += 1

            var options = {
                responsive: false,
                maintainAspectRatio: true,
                scale: {
                    ticks: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }

            var ctx = document.getElementById('myChart').getContext('2d')
            // eslint-disable-next-line
            var myChart = new Chart(ctx, {
                type: 'radar',
                options: options,
                data: {
                    labels: [
                        'Algorithm',
                        'Data Structure',
                        'Mathematic',
                        'Coding',
                        'Communication',
                        'Language',
                        'Self-motivation',
                        'Problem Solivg'
                    ],
                    datasets: [
                        {
                            label: 'Username',
                            data: this.chartData
                        }
                    ]
                }
            })
            console.log(ctx)
            console.log(myChart)
        }
    },
    computed: {
        chartData() {
            return [
                this.i,
                this.i,
                this.i,
                this.i,
                this.i,
                this.i,
                this.i,
                this.i
            ]
        }
    }
}
</script>

<style>
.spiderChart {
    width: 400px;
    height: 300px;
    margin: auto;
}
.input-custom {
    width: 300px;
    height: 60px;
    /* background: rgb(35, 50, 120); */
    margin: auto;
}
</style>