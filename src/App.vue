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
                    <i class=""></i>
                  </h3>
                </div>
                <div class="body">
                  <ul>
                    <li>
                      <img src="./image/home.svg" alt class="svg"/>
                      <br>
                      Home
                    </li>
                    <li>
                      <img src="./image/list.svg" alt class="svg"/> 
                      <br> 
                      Mission
                    </li>
                    <li>
                      <img src="./image/dashboard.svg" alt class="svg"/> 
                      <br>
                      Dashboard
                    </li>
                       <li>
                      <img src="./image/profile.svg" alt class="svg"/> 
                      <br> Profile
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- sec (Center) col -->
        <div class="col-md-6 d-flex flex-column bd-highlight mb-3">
          <div class="container p-2 bd-highlight">
            <div class="content-bg bg-white">
              <!-- content background box -->
              <div class="shadow-sm p-3 mb-5 bg-white rounded">
                <div class="row justify-content-md-center">
                  <div class="navigator-font col-md-3">Profile</div>
                  <div class="navigator-font col-md-3">History</div>
                  <div class="navigator-font col-md-3">Stat</div>
                </div>
              </div>
              <div class="content-box">
                <!-- content box -->
                <div class>kuy gu yak tai</div>
              </div>
            </div>
          </div>
        </div>

        <!-- third col -->
        <div class="col-md-3">
          <!-- ranking card list -->
          <div class="card" style="width: 18rem;">
            <div class="border-custom-up">
              <p class="cardhd">Weekly Ranking</p>
            </div>
            <table class="table table-hover table-light">
              <tbody>
                <tr>
                  <th scope="row" class="font-custom-list">1</th>
                  <td class>
                    <img src="./image/1.jpg" alt class="rounded-circle" />
                  </td>
                  <td class="font-custom-list">Kritchagamol</td>
                  <td class="font-custom-list">isus</td>
                </tr>
              </tbody>
            </table>
            <div class="border-custom">
              <a href="#" class="seemore">See more</a>
            </div>
          </div>
          <div class="boxspace-card"></div>
          <!-- เว้นบรรทัด -->
          <div class="card" style="width: 18rem;">
            <div class="border-custom-up">
              <p class="cardhd">Daily Mission</p>
            </div>
            <table class="table table-hover table-light" style="width: 18rem;">
              <tbody class="d-flex bd-highlight">
                <tr>
                  <th scope="row" class="font-mission">[Daily]</th>
                  <td class="text-left font-custom-list p-2 flex-fill bd-highlight">
                    Example Mission With Something
                    <p class="mission-detail">fake detail</p>
                  </td>
                </tr>
              </tbody>
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
</script>

<style>
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
  font-family: Source Sans Pro, Helvetica, sans-serif;
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
