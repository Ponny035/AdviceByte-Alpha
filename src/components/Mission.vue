<template>
    <div class="mission">
        <div class="progress">
            <div
                class="progress-bar"
                role="progressbar"
                style="width: 50%;"
                aria-valuenow="25"
                aria-valuemin="0"
                aria-valuemax="100"
            >
                Test Progress Bar (50%)
            </div>
        </div>
        <br />
        <!-- หมุนตอนโหลด -->
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-lightblue">
                <div class="bg-blue shadow-sm p-3 mb rounded box-try">
                    <div class="row justify-content-md-center">
                        <div class="topic-font col-md-6">
                            Topic Mission Example
                        </div>
                    </div>
                </div>
                <div class="content-box-mission">
                    <!-- mission-stage -->
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style lang="css">
/* .mission {

} */

.topic-font {
    padding: 0.25rem;
    font-family: poppins;
    font-size: 20px;
    font-weight: bold;
    color: #37437e;
}

.bg-blue {
    background: #c3c3f5;
}
.bg-lightblue {
    background: #d0d3e0;
}

/* .box-try {
  margin-bottom: ;
} */

.hastag-mission {
    margin-left: 2%;
}

.mission-stagee {
    margin: 10px;
    padding: 3%;
    padding-left: 8%;
    border-bottom-right-radius: 12px;
    border-bottom-left-radius: 12px;
    border-top-right-radius: 12px;
    border-top-left-radius: 12px;
}

.font-mission {
    font-family: Poppins;
    color: #37437e;
    font-size: 16px;
    font-weight: bold;
}

.font-mission-datail {
    font-weight: lighter;
    font-family: Poppins;
    font-size: 13px;
    color: #575757a1;
}

.font-hastag {
    font-weight: lighter;
    font-family: Poppins;
    font-size: 12px;
    color: #e9e9e9;
}
.content-box-mission {
    padding: 0.5rem;
    padding-bottom: 4rem;
}
</style>
