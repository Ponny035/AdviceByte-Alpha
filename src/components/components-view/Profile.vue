<template>
    <div class="profile">
        <!-- tree -->
        <Tree></Tree>
        <!-- award head -->
        <div class="container">
            <div class="colorTag">
                <div class="row">
                    <template v-for="(item, i) in color" :key="i">
                        <div class="col-6 col-md-4">
                            <svg
                                class="bd-placeholder-img mr-2 rounded"
                                width="15"
                                height="15"
                                xmlns="http://www.w3.org/2000/svg"
                                preserveAspectRatio="xMidYMid slice"
                                focusable="false"
                                role="img"
                                aria-label="Placeholder: 32x32"
                            >
                                <title>Placeholder</title>
                                <rect
                                    width="100%"
                                    height="100%"
                                    :fill="item.color"
                                ></rect>
                            </svg>
                            {{ item.skill }}
                        </div>
                    </template>
                </div>
            </div>
        </div>
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
import axios from 'axios'
import Tree from '../getTree'
export default {
    components: {
        Tree
    },
    async created() {
        try {
            console.log(localStorage.userId)

            const response = await axios.post(
                `${process.env.API_URI}/user/tree`,
                {
                    userId: localStorage.userId
                    // skillId: this.$route.params.id
                }
            )
            console.log(response)

            let data = response.data
            let [colorTag] = data

            colorTag = colorTag.substring(1, colorTag.length - 1)
            colorTag = colorTag.split(', ')
            colorTag = colorTag.map(elm => elm.substring(1, elm.length - 1))

            console.log(data)
            const returnArray = []
            for (let i = 0; i < colorTag.length; i++) {
                let a = colorTag[i].split("': '")
                returnArray.push({
                    skill: a[0],
                    color: a[1]
                })
            }
            this.color = returnArray
            console.log(this.color)
        } catch (error) {
            console.log(error)
        }
    },
    data() {
        return {
            color: []
        }
    }
}
</script>

<style>
.colorTag {
    padding-bottom: 5%;
}

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
