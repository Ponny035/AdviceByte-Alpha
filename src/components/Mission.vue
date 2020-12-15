<template>
    <div class="mission">
        <!-- <div class="progress">
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
        </div> -->
        <br />
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-lightblue">
                <div class="bg-blue shadow-sm p-3 mb rounded box-try">
                    <div class="row justify-content-md-center">
                        <!-- หัวข้อ Categories -->
                        <div class="topic-font col-md-6">
                            Topic Mission Example
                        </div>
                    </div>
                </div>
                <div class="content-box-mission">
                    <!-- mission-stage -->
                    <router-view></router-view>
                </div>
                <div class="catagory">
                    <div class="container">
                    <div calss="row">
                        <button @click="path(1)" type="button" class="button btn btn-light">Algorithm</button>
                        <button @click="path(2)" type="button" class="button btn btn-light">Data Structure</button>
                        <button @click="path(3)" type="button" class="button btn btn-light">Coding</button>
                    </div>
                    <div calss="row">
                        <button @click="path(4)" type="button" class="button btn btn-light">Mathematic</button>
                        <button @click="path(6)" type="button" class="button btn btn-light">Communicate</button>
                        <button @click="path(5)" type="button" class="button btn btn-light">Laguage</button>
                    </div>
                    <div calss="row">
                        <button @click="path(8)" type="button" class="button btn btn-light">Self-Motivation</button>
                        <button @click="path(7)" type="button" class="button btn btn-light">Problem Solving</button>
                        
                    </div>
                    
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
     methods: {
         path(n){
             this.$router.push({path: `/mission/${n}`});
         }
     }

}
</script>

<style>

/* .mission {

} */
.btn-catagory { 
    background-color: #5f6b93;
}

.catagory {
    padding-bottom: 10%
}

.button { 
    width: 150px;
    height: 150px;
    margin-left: 20px;
    margin-top: 20px;
}


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
