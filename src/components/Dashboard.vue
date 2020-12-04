<template>
    <div class="dashboard">
        <!-- หมุนตอนโหลด -->
        <div class="container p-2 bd-highlight">
            <div class="content-bg bg-white">
                <div class="bg-white p-3 mb rounded box-try">
                    <div class="row">
                        <div class="forum-font">Forum</div>
                        <br />
                    </div>
                    <div class="text-left">
                        <a href="#" class="detail-forum">Bookmark</a>
                    </div>
                </div>
                <div class="cont-forum">
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
.forum-font {
    font-family: poppins;
    font-size: 20px;
    font-weight: bold;
    color: #37437e;
    padding-left: 6%;
}

.detail-forum {
    padding-left: 8%;
    font-family: poppins;
    font-size: 13px;
}

.cont-forum {
    padding: 0.5rem;
    padding-bottom: 4rem;
}
</style>
