<script>
    import { Line, mixins } from 'vue-chartjs'
    const { reactiveProp } = mixins;


    export default {
        extends: Line,
        mixins: [reactiveProp],
        props: ['chartData', 'title'],
        mounted () {
            this.renderChart({
                datasets: [
                    {
                        label: this.title,
                        backgroundColor: '#38AEA3',
                        data:  this.chartData,
                    }
                ]
            }, {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    xAxes: [{
                        type: 'time',
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            })
        }
    }
</script>

<style>

</style>