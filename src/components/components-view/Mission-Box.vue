<template>
  <div class="MissionBox" name="stagebox">
    <br>
    <div class="shadow-sm mission-stagee bg-white justify-content-sm-center">
      <div class="container">
        <div class="row">

          <!-- content mission stage -->
          <!-- star rate -->
          <div class="col">1 of 3</div>
          <!-- mission name -->
          <td class="col-6 font-mission text-left p-2 flex-fill bd-highlight">
            Example Mission With Something
            <p class="font-mission-datail">fake detail</p>
            <div class="row box-try">
              <span class="font-hastag badge badge-info">#Communication</span>
              <span class="font-hastag hastag-mission badge badge-success">#Language</span>
            </div>
          </td>
          <!-- button mission -->
          <div class="col">
            <button
              type="button"
              class="btn btn-danger mission-button"
              data-toggle="button"
              aria-pressed="false"
            >Start
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.mission-button {
  font-family: Poppins;
  color: #ffffff;
  font-size: 14px;
  font-weight: bold;
  padding-left: 25%;
  padding-right: 25%;
  margin-top: 20%;
  border-radius: 12px;
}


</style>