<template>
    <div id="app" class="bg-custom">
        <!-- navbar -->
        <nav
            class="d-flex bd-highlight shadow-sm p-3 mb-5 bg-white rounded navbar navbar-expand-lg navbar-light bg-light"
        >
            <div class>
                <a class="navbar-brand" href="#">
                    <div class="navbnd">AdviceByte</div>
                </a>
            </div>
        </nav>
        <!-- content -->
        <div class="container-fluid">
            <div class="container"></div>
            <div class="row">
                <!-- first col -->
                <div class="col-md-3">
                    <div class="container">
                        <div class="first-space">
                            <div class="card-nav navigator-font-side">
                                <div class>
                                    <h3>
                                        <i class></i>
                                    </h3>
                                </div>
                                <div class="body">
                                    <ul>
                                        <li @click="viewProfile">
                                            <img
                                                src="../image/home.svg"
                                                alt
                                                class="svg"
                                            />
                                            <br />Home
                                        </li>
                                        <li @click="viewMission">
                                            <img
                                                src="../image/list.svg"
                                                alt
                                                class="svg"
                                            />
                                            <br />Mission
                                        </li>
                                        <li @click="viewDashboard">
                                            <img
                                                src="../image/dashboard.svg"
                                                alt
                                                class="svg"
                                            />
                                            <br />Dashboard
                                        </li>
                                        <li @click="viewProfile">
                                            <img
                                                src="../image/profile.svg"
                                                alt
                                                class="svg"
                                            />
                                            <br />Profile
                                        </li>
                                        <li @click="logout">
                                            <svg
                                                src="../image/logout.svg"
                                                alt
                                                class="svg"
                                                style="color:white"
                                            />
                                            <br />Logout
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- sec (Center) col -->
                <div class="col-md-6 d-flex flex-column bd-highlight mb-3">
                    <router-view></router-view>
                </div>
                <!-- third col -->
                <div class="col-md-3">
                    <!-- ranking card list -->
                    <div class="card" style="width: 18rem;">
                        <!-- topic ranking -->
                        <div class="border-custom-up">
                            <p class="cardhd">Monthly Ranking</p>
                        </div>

                        <table class="table table-hover table-light">
                            <tbody>
                                <template v-for="(item, i) in ranks" :key="i">
                                    <tr>
                                        <!-- ลำดับ user -->
                                        <th
                                            scope="row"
                                            class="font-custom-list"
                                        >
                                            {{ item.rank }}
                                        </th>
                                        <td class>
                                            <img
                                                src="../image/1.jpg"
                                                alt
                                                class="rounded-circle"
                                            />
                                        </td>
                                        <!-- ชื่อ users -->
                                        <td class="font-custom-list">
                                            {{ item.user }}
                                        </td>
                                        <!-- ช่องว่างหลังชื่อไว้ก่อน -->
                                        <td class="font-custom-list"></td>
                                    </tr>
                                </template>
                            </tbody>
                        </table>
                        <!-- จบไส้แรงค์ -->

                        <div class="border-custom">
                            <a href="#" class="seemore">See more</a>
                        </div>
                    </div>

                    <div class="boxspace-card"></div>
                    <!-- เว้นบรรทัด -->
                    <div class="card" style="width: 18rem;">
                        <div class="border-custom-up">
                            <p class="cardhd">Missions For You</p>
                        </div>
                        <table
                            class="table table-hover table-light"
                            style="width: 18rem;"
                        >
                            <template v-for="(item, i) in data" :key="i">
                                <tbody class="d-flex bd-highlight">
                                    <tr>
                                        <th scope="row" class="type-mission">
                                            [Daily]
                                        </th>
                                        <td
                                            class="text-left font-custom-list p-2 flex-fill bd-highlight"
                                        >
                                            {{ item.Activity_Name }}
                                            <!-- <p class="mission-detail">
                                            fake detail
                                        </p> -->
                                        </td>
                                    </tr>
                                </tbody>
                            </template>
                        </table>
                        <div class="border-custom">
                            <a href="#" class="seemore">See more</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            ranks: [],
            data: []
        }
    },
    mounted() {
        console.log(this.$route.params.id)
        this.ranking()
        this.generalMission()
    },
    methods: {
        logout() {
            localStorage.removeItem('userId')
            this.$router.push({
                name: 'Login'
            })
        },
        viewMission() {
            this.$router.push({ path: '/mission' })
        },
        viewHome() {
            this.$router.push({ name: 'home' })
        },
        viewProfile() {
            this.$router.push({ path: '/profile' })
        },
        viewDashboard() {
            this.$router.push({ path: '/dashboard' })
        },
        async ranking() {
            try {
                await axios
                    .post(`${process.env.VUE_APP_APIURI}/user/ranking`, {
                        userId: localStorage.userId
                    })
                    .then(response => {
                        const returnArray = []
                        const id = JSON.parse(response.data[0])
                        const rank = JSON.parse(response.data[1])
                        for (let i = 0; i < id.length; i += 1) {
                            returnArray.push({
                                user: id[i],
                                rank: rank[i]
                            })
                        }
                        this.ranks = returnArray
                    })
            } catch (error) {
                console.log(error)
            }
        },
        async generalMission() {
            try {
                const general = await axios.post(
                    `${process.env.VUE_APP_APIURI}/activity/generalRecommendation`,
                    {
                        userId: localStorage.userId
                    }
                )
                const geRec = general.data

                let DATA = []
                for (let i = 0; i < 3; i++) {
                    DATA.push(geRec[i])
                }

                this.data = DATA
            } catch (error) {
                console.log(error)
            }
        }
    }
}
</script>

<style>
@import '../styles/custom.min.css';
@import '../styles/custom.scss';
@import '../styles/custom.css';

.svg {
    fill: #ffffff;
}

.type-mission {
    font-family: Poppins;
    color: rgb(255, 170, 0);
    font-size: 12px;
    font-weight: bold;
}
.navbnd {
    /* logo advicebyte font */
    font-weight: bold;
    color: #0c4377;
    /* padding: 10%; */
    margin-left: 20%;
    margin-right: 5%;
}
.navigator-font {
    padding: 0.25rem;
    font-family: poppins;
    font-size: 14px;
    font-weight: bold;
    color: #a3aac1;
}

.content-bg {
    border-bottom-right-radius: 18px;
    border-bottom-left-radius: 18px;
}
.content-box {
    padding: 2rem;
    padding-bottom: 4rem;
}

.card-nav {
    height: 380px;
}

.spacenav {
    /* ระยะ margin padding ห่างระหว่างโลโก้กับเมนู */
    margin-left: 30px;
    /* margin-right: 20%; */
}
.cardhd {
    float: left;
    font-weight: bold;
    font-family: Poppins;
    padding-top: 1rem;
    font-size: 16px;
    color: white;
}
.mission-detail {
    font-family: Poppins;
    font-size: 12px;
    color: #e4e4e4a1;
}
.font-custom-list {
    align-self: center;
    font-family: Poppins;
    padding-top: 10px;
    color: white;
    font-size: 12px;
}
.font-mission {
    font-family: Poppins;
    color: #ffaa00;
    font-size: 12px;
}
#card-header {
    border-radius: 100px;
}
/* ------------------------------------------------------- */
html {
    height: 140%;
    background-color: #e4e4e4;
}
#app {
    color: #2c3e50;
    max-width: 400%;
    font-family: 'Poppins', Source Sans Pro, Helvetica, sans-serif;
    text-align: center;
}
.slide-fade-enter-active {
    transition: all 0.2s ease;
}
.slide-fade-leave-active {
    transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-active {
    padding-left: 10px;
    opacity: 0;
}
</style>
