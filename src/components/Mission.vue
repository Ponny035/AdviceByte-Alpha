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

<style>

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


</style>
