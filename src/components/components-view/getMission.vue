<template>
<!-- ไว้เรียก Mission แต่ละอันในแต่ละหมวด ถ้าเขาเข้า /algo ก็โชว์มิชชั่น algo
ถ้าเขา /commu ก็โชว์ Mission commu -->
  <div class="MissionBox" name="stagebox">
    <br>
    <!-- เริ่ม_กล่องโค้ดขาว -->
    <div class="shadow-sm mission-stagee bg-white justify-content-sm-center">
      <div class="container">
        <div class="row">
          <!-- content mission stage -->
          <!-- star rate -->
          <div class="col-3 font-test2"></div>
          <!-- mission name -->
          <td>
            <div class="col-9 text-left">
            <p class="font-test1">The Secret Rule of Modern Living AI</p>
            <p class="font-test2">Example Mission With Something</p>
          </div>
          <div class="hastag-mission">
              <!-- <div class="badge badge-info">#Communication</div>
              <div class="badge badge-success">#Language</div> -->
            </div>
          </td>
          <!-- button mission -->
          <div class="col">
            <button
              type="button"
              @click="viewForum"
              class="btn mission-button"
              data-toggle="button"
              aria-pressed="false"
            >Start
            </button>
          </div>
        </div>
        <br>
        <!-- จบกล่องโค้ดขาว -->
      </div>
    </div>
        <!-- เริ่ม_กล่องโค้ดเขียว -->
    <div class="shadow-sm mission-stagee bg-green justify-content-sm-center">
      <div class="container">
        <div class="row">
          <!-- content mission stage -->
          <!-- star rate -->
          <div class="col-3 font-test2"></div>
          <!-- mission name -->
          <td>
            <div class="col-9 text-left">
            <p class="font-test1">The Secret Rule of Modern Living AI</p>
            <p class="font-test2">Example Mission With Something</p>
          </div>
          <div class="hastag-mission">
              <!-- <div class="badge badge-info">#Communication</div>
              <div class="badge badge-success">#Language</div> -->
            </div>
          </td>
          <!-- button mission -->
          <div class="col">
            <button
              type="button"
              @click="viewForum"
              class="btn mission-button"
              data-toggle="button"
              aria-pressed="false"
            >Start
            </button>
          </div>
        </div>
        <br>
        <!-- จบกล่องโค้ดขาว -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
    methods: {
        viewForum() {
            this.$router.push({ name: 'forum' })
        }
    }
}
</script>

<style>
.bg-green {
  background-color:#e7ffcd;
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