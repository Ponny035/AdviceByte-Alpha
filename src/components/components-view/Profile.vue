<template>
    <div class="profile">
        <!-- tree -->
        <div class="tree">
            <img
                alt=""
                class=""
                src="https://i.imgur.com/eyJFtdT.png"
            />
        </div>
        <br>
        <br>
        <br>
        <!-- award head -->
        <div class="award">
            <div class="container">
                <h4 class="font-weight-bold text-left">Awards</h4>
                <div class="text-left">
                    <p class="description">Description Coming Later</p>
                </div>
                <div class="container">
                    <div class="row">
                        <img
                            alt=""
                            class="cusReward2"
                            src="https://i.imgur.com/Xfy0DiP.png"
                        />
                        <img
                            alt=""
                            class="cusReward1"
                            src="https://i.imgur.com/2UdBR38.png"
                        />
                        <!-- <img :src="require('./assets/')"/> -->
                        <!-- <img :src="getReward" alt class="cusReward"/> -->
                    </div>
                </div>
                <hr />
            </div>
            <!-- end head -->

            <h4 class="font-weight-bold text-left">
                Limited Edition Challenges
            </h4>
            <div class="container">
                <div class="row">
                    <img
                        alt=""
                        class="cusReward2"
                        src="https://i.imgur.com/DoZwbo4.png"
                    />
                    <img
                        alt=""
                        class="cusReward2"
                        src="https://i.imgur.com/bX6sBlT.png"
                    />
                </div>
            </div>
        </div>
        <hr />
        <h4 class="font-weight-bold text-left">Monthly Challenges</h4>
        <div class="container">
            <div class="row">
                <img
                    alt=""
                    class="cusReward2"
                    src="https://i.imgur.com/MA0Y0IN.png"
                />
                <img
                    alt=""
                    class="cusReward1"
                    src="https://i.imgur.com/aR7l1j6.png"
                />
            </div>
        </div>
        <hr />
    </div>
</template>

<script>
export default {}
</script>

<style>
.profile {
    margin-left: 5%;
}

.empty-box {
    margin-bottom: 10%;
}

.description {
    padding-left: 0%;
    font-family: 'Poppins';
    font-size: 14px;
}

.cusReward1 {
    width: 15%;
    height: 15%;
    margin-left: 5%;
}
.cusReward2 {
    width: 9%;
    height: 9%;
    margin-left: 5%;
}
</style>