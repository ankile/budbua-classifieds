<!--

This component contains logic, styling and structure for the owner to see statistics about the platform.

-->

<template lang="html">
    <div class="analytics-container">
        <h1 class="analytics-header">Eierdashboard</h1>
        <sui-grid :columns="4" centered vertical-align="middle" :stackable="true">
            <sui-grid-row stretched>

                <sui-grid-column stretched>
                    <sui-card>
                        <sui-card-content>
                            <div class="statistic-card">
                                <sui-statistic>
                                    <sui-statistic-value>{{analytics.userCount}}</sui-statistic-value>
                                    <sui-statistic-label>Brukere</sui-statistic-label>
                                </sui-statistic>
                            </div>

                        </sui-card-content>
                        <sui-card-content extra>
                            <span slot="right">
                                Oppdatert: Akkurat nå
                            </span>
                        </sui-card-content>
                    </sui-card>
                </sui-grid-column>

                <sui-grid-column stretched>
                    <sui-card>
                        <sui-card-content>
                            <div class="statistic-card">
                                <sui-statistic>
                                    <sui-statistic-value>{{analytics.adCount}}</sui-statistic-value>
                                    <sui-statistic-label>Annonser</sui-statistic-label>
                                </sui-statistic>
                            </div>

                        </sui-card-content>
                        <sui-card-content extra>
                            <span slot="right">
                                Oppdatert: Akkurat nå
                            </span>
                        </sui-card-content>
                    </sui-card>
                </sui-grid-column>

                <sui-grid-column stretched>
                    <sui-card>
                        <sui-card-content>
                            <div class="statistic-card">
                                <sui-statistic>
                                    <sui-statistic-value>{{analytics.bidCount}}</sui-statistic-value>
                                    <sui-statistic-label>Bud</sui-statistic-label>
                                </sui-statistic>
                            </div>

                        </sui-card-content>
                        <sui-card-content extra>
                            <span slot="right">
                                Oppdatert: Akkurat nå
                            </span>
                        </sui-card-content>
                    </sui-card>
                </sui-grid-column>

                <sui-grid-column stretched>
                    <sui-card>
                        <sui-card-content>
                            <div class="statistic-card">
                                <sui-statistic>
                                    <sui-statistic-value>{{analytics.reportCount}}</sui-statistic-value>
                                    <sui-statistic-label>Rapporter</sui-statistic-label>
                                </sui-statistic>
                            </div>

                        </sui-card-content>
                        <sui-card-content extra>
                            <span slot="right">
                                Oppdatert: Akkurat nå
                            </span>
                        </sui-card-content>
                    </sui-card>
                </sui-grid-column>

            </sui-grid-row>
        </sui-grid>
    </div>
</template>

<script>

    import {Api} from "../../api";

    export default {

        data() {
            return {
                analytics: null,
            }
        },

        components: {},

        created() {
            Api.get('/analytics/')
                .then(resp => this.analytics = resp.data)
        }

    }

</script>

<style lang="scss" scoped>
    @import './../../common.scss';

    .analytics-container {
        margin-top: 10px;
        width: 100%;
        text-align: center;
        height: 100%;

        @include respond-to(wide) {
            width: 1000px;
        }
        @include respond-to(medium) {
            max-width: 800px;
        }
        @include respond-to(phone) {
            max-width: 300em;
        }
    }

    .statistic-card {
        padding: 1em;
        text-align: center;
    }

    .analytics-header {
        margin-bottom: 1.2em;
        font-size: 2.5em;
    }
</style>
