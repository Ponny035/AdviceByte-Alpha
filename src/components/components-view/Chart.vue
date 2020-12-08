<template>
    <div class="spiderChart">
        <canvas id="myChart" ref="myChart" width="400" height="400"></canvas>

        <!-- <button @click="increment" class="btn btn-success">Click me</button> -->
    </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'

export default {
    async created(){
        const response = await axios.post('http://localhost:3000/user/information',
           {
                userId:localStorage.userId
                // skillId: this.$route.params.id
            })
        // console.log(this.myChart.datasets[0].data[0] = res.Algorithm_Score)
            console.log(response)
            const res = response.data
            this.myChart.datasets[0].data[0] = res.Algorithm_Score
            this.myChart.datasets[0].data[1] = res.Data_Structure_Score
            this.myChart.datasets[0].data[2] = res.Programming_Score
            this.myChart.datasets[0].data[3] = res.Mathematic_Score
            this.myChart.datasets[0].data[4] = res.Language_Score
            this.myChart.datasets[0].data[5] = res.Communication_Score
            this.myChart.datasets[0].data[6] = res.Self_Motivation_Score
            this.myChart.datasets[0].data[7] = res.Problem_Solving_Score

            const baseline = await axios.post('http://localhost:3000/user/avginformation',
           {
                userId:localStorage.userId
                // skillId: this.$route.params.id
            })

            console.log(baseline)
            const base = baseline.data
            this.myChart.datasets[1].data[0] = base.Algorithm_Score
            this.myChart.datasets[1].data[1] = base.Data_Structure_Score
            this.myChart.datasets[1].data[2] = base.Programming_Score
            this.myChart.datasets[1].data[3] = base.Mathematic_Score
            this.myChart.datasets[1].data[4] = base.Language_Score
            this.myChart.datasets[1].data[5] = base.Communication_Score
            this.myChart.datasets[1].data[6] = base.Self_Motivation_Score
            this.myChart.datasets[1].data[7] = base.Problem_Solving_Score

            this.chartView.update()
    },
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
        this.chartView = new Chart(ctx, {
            type: 'radar',
            options: options,
            data: {
                ...this.myChart
            }
        })
        
    },
    data() {
        return {
            chartView:null,
            myChart: {
                labels: [
                    'Algorithm',
                    'Data Structure',
                    'Programming',
                    'Mathematic',
                    'Language',
                    'Communication',
                    'Problem Solivg',
                    'Self-motivation'
                ],
                datasets: [
                    {
                        label: 'Kritchagamol',
                        backgroundColor: [
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)'],
                        data: []
                    },
                    {
                        label: 'Base Line',
                        backgroundColor: 'rgb(195, 195, 245, 0.3)',
                        data: []
                    }
                ]
            },
            i: 5,
        };
    },
    methods: {
        increment() {
            this.i += 5

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
                        'Programming',
                        'Mathematic',
                        'Language',
                        'Communication',
                        'Problem Solivg',
                        'Self-motivation'
                    ],
                    datasets: [
                        {
                            label: 'Kritchagamol',
                            backgroundColor: [
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(35, 50, 120, 0.5)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)',
                            'rgb(255, 170, 0, 1)'],
                            data: this.chartData
                        },
                        {
                            label: 'Base Line',
                            backgroundColor: 'rgb(195, 195, 245, 0.3)',
                            data: [47.29, 57.29, 70.52, 47.29, 71.67, 71.35, 69.38, 63.96]
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
            return [this.i, 40, 75, 45, 50, 75, 65, 55]
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
