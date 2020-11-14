<template>
    <div class="login">
        <!-- head -->
        <div class="pad-head">
            <div class="container">
                <div class="py-5 text-center">
                    <img
                        class="logo d-block mx-auto mb-4"
                        src="https://i.imgur.com/3DvN4YE.png"
                        alt=""
                    />
                    <h2>Checkout form</h2>
                    <p class="font-head">
                        Level up your coding skills and quickly land a job.
                    </p>
                </div>
            </div>
        </div>
        <!-- content -->
        <div class="container">
            <div class="row">
                <div class="text-md-left col-sm-8">
                    <h4 class="mb-3">Register</h4>
                    <!-- full-name/last-name -->
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="firstName">First name</label>
                            <input
                                type="text"
                                class="form-control"
                                id="firstName"
                                placeholder=""
                                value=""
                                required=""
                            />
                            <div class="invalid-feedback">
                                Valid first name is required.
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="lastName">Last name</label>
                            <input
                                type="text"
                                class="form-control"
                                id="lastName"
                                placeholder=""
                                value=""
                                required=""
                            />
                            <div class="invalid-feedback">
                                Valid last name is required.
                            </div>
                        </div>
                    </div>
                    <!-- username -->
                    <div class="mb-3">
                        <label for="username">Username</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text">@</span>
                            </div>
                            <input
                                type="text"
                                class="form-control"
                                id="username"
                                placeholder="Username"
                                required=""
                            />
                            <div class="invalid-feedback" style="width: 100%">
                                Your username is required.
                            </div>
                        </div>
                    </div>
                    <!-- e-mail -->
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="email"
                                >Email
                                <span class="text-muted"
                                    >(Optional)</span
                                ></label
                            >
                            <input
                                type="email"
                                class="form-control"
                                id="email"
                                placeholder="you@example.com"
                            />
                            <div class="invalid-feedback">
                                Please enter a valid email address for shipping
                                updates.
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="password">Password</label>
                            <input
                                type="text"
                                class="form-control"
                                id="password"
                                placeholder=""
                                value=""
                                required=""
                            />
                            <div class="invalid-feedback">
                                Valid first password is required.
                            </div>
                        </div>
                    </div>
                    <!-- MBTI -->
                    <div class="row">
                        <div class="col-md-3 mb-3">
                            <label for="date">Birthday</label>
                            <select
                                class="custom-select d-block w-100"
                                id="date"
                                required=""
                            >
                                <option value="">day</option>
                                <option>...</option>
                            </select>
                            <!-- <div class="invalid-feedback">
              Please select a valid country.
            </div> -->
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="month">.</label>
                            <select
                                class="custom-select d-block w-100"
                                id="month"
                                required=""
                            >
                                <option value="">month</option>
                                <option>...</option>
                            </select>
                            <!-- <div class="invalid-feedback">
              Please provide a valid state.
            </div> -->
                        </div>
                        <div class="col-md-3 mb-3">
                            <label for="year">.</label>
                            <select
                                class="custom-select d-block w-100"
                                id="year"
                                required=""
                            >
                                <option value="">year</option>
                                <option>...</option>
                            </select>
                            <!-- <div class="invalid-feedback">
              Please provide a valid state.
            </div> -->
                        </div>
                    </div>
                    <!-- เส้นขั้น -->
                    <hr class="mb-4" />
                    <!-- MBTI -->
                    <div class="mb-3">
                        <label for="year">Personality Type</label>
                        <select
                            class="custom-select d-block w-100"
                            id="year"
                            required=""
                        >
                            <option value="">MBTI</option>
                            <option>...</option>
                        </select>
                        <!-- <div class="invalid-feedback">
              Please provide a valid state.
            </div> -->
                    </div>
                    <!-- ปุ่มส่งฟอร์ม -->
                    <br />
                    <div class="pad-head">
                        <button
                            class="btn btn-primary btn-lg btn-block"
                            type="submit"
                        >
                            Get Start
                        </button>
                    </div>
                </div>
                <!-- ฝั่งขวา -->
                <div class="col-sm-4">col-sm-4</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style>
.login {
    background-color: #e4e4e4;
}
.font {
    font-size: 15px;
    padding-top: 0px;
    margin-top: 2px;
    margin-bottom: 2px;
}

.font-head {
    font-size: 16px;
    padding-top: 0px;
    margin-top: 20px;
    margin-bottom: 2px;
}
.pad-head {
    padding-bottom: 50px;
}
.logo {
    height: 12%;
    width: 12%;
}
.container {
}

.btn-color {
    background-color: blue;
}
</style>
