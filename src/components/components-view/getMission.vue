<template>
    <!-- ไว้เรียก Mission แต่ละอันในแต่ละหมวด ถ้าเขาเข้า /algo ก็โชว์มิชชั่น algo
ถ้าเขา /commu ก็โชว์ Mission commu -->
    <div class="MissionBox" name="stagebox">
        <br />
        <template v-for="(item, i) in data" :key="i">
            <!-- เริ่ม_กล่องโค้ดขาว -->
            <div
                class="shadow-sm mission-stagee bg-white justify-content-sm-center"
            >
                <div class="container">
                    <div class="row">
                        <!-- content mission stage -->
                        <!-- star rate -->
                        <div colspan="2"></div>
                        <!-- mission name -->

                        <div class="col-9 text-left">
                            <p class="font-test1">{{ item.Activity_Name }}</p>
                        </div>
                        <div class="col-9 text-left">
                            <p class="font-test2">
                                {{ item.Activity_Description }}
                            </p>
                        </div>
                        <div class="hastag-mission">
                            <!-- <div class="badge badge-info">#Communication</div>
                    <div class="badge badge-success">#Language</div> -->
                        </div>

                        <!-- button mission -->
                        <div class="col">
                            <button
                                type="button"
                                @click="viewForum(item.Activity_ID)"
                                class="btn btn-primary"
                                data-toggle="button"
                                aria-pressed="false"
                            >
                                Start
                            </button>
                        </div>
                    </div>
                    <br />
                    <!-- จบกล่องโค้ดขาว -->
                </div>
            </div>
        </template>

        <!-- เริ่ม_กล่องโค้ดเขียว
              <div class="shadow-sm mission-stagee bg-green justify-content-sm-center">
            <div class="container">
              <div class="row">
                content mission stage 
                star rate
                <div colspan="2"></div>
               mission name
               
                  <div class="col-9 text-left">
                  <p class="font-test1">x</p>
                  </div>
                  <div class="col-9 text-left">
                  <p class="font-test2">x</p>
                </div>
                <div class="hastag-mission">
                    <div class="badge badge-info">#Communication</div>
                    <div class="badge badge-success">#Language</div>
                  </div>
            
                button mission
                <div class="col">
                  <button
                    type="button"
                    @click="viewForum"
                    class="btn btn-warning"
                    data-toggle="button"
                    aria-pressed="false"
                  >
                    Review
                   
                  </button>
                </div>
              </div>
              <br>
              จบกล่องโค้ดขาว
            </div>
          </div> -->
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            data: []
        }
    },
    mounted() {
        console.log(this.$route.params.id)
        this.mission()
    },
    methods: {
        viewForum(id) {
            this.$router.push({ name: 'activity-id', params: { id: id } })
        },
        async mission() {
            console.log('TEST2')
            try {
                // const data = await fetch(
                //   '${process.env.VUE_APP_API_URI}/activity/recommendation',
                //   {
                //     method: 'POST',
                //     credentials: 'same-origin',
                //     headers: {
                //         'Content-Type': 'application/json'
                //     },
                //     body: JSON.stringify({
                //         skillId: 3,
                //     })
                //   }
                // )
                const response = await axios.post(
                    `${process.env.VUE_APP_API_URI}/activity/recommendation`,
                    {
                        userId: localStorage.userId,
                        skillId: this.$route.params.id
                    }
                )
                console.log(response)
                const res = response.data
                for (const item in res) {
                    console.log(item)
                    this.data.push(res[item])
                }
                // this.data = data.data
                console.log(this.data)
            } catch (error) {
                console.log(error)
            }
        }
    }
}
</script>

<style>
.bg-green {
    background-color: #e7ffcd;
}

.mission-button {
    font-family: Poppins;
    font-size: 14px;
    font-weight: bold;
    margin-top: 0%;
    border-radius: 12px;
}

.hastag-mission {
    margin-left: 2%;
}

.content-box-mission {
    padding: 0.5rem;
    padding-bottom: 4rem;
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

.font-test1 {
    font-family: Poppins;
    color: #37437e;
    font-size: 15px;
    font-weight: bold;
}

.font-test2 {
    font-family: Poppins;
    font-size: 12px;
    color: #575757a1;
}

/* .font-hastag {
    font-family: Poppins;
    font-size: 1px;
    color: #e9e9e9;
} */
</style>
