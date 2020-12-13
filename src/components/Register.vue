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
                    <h2>Registeration</h2>
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
                    <form class="needs-validation" novalidate>
                    <!-- full-name/last-name -->
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="firstName">First name</label>
                            <input
                                type="text"
                                class="form-control"
                                id="firstname"
                                placeholder=""
                                value=""
                                required=""
                            />
                            <div class="invalid-feedback">
                                Valid first name is required.
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="lastname">Last name</label>
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
                    <!-- เส้นขั้น -->
                    <hr class="mb-4" />
                    <!-- MBTI -->
                    <div class="mb-3">
                        <label for="mbti">Personality Type</label>
                            <select class="custom-select d-block w-100" aria-label="mbtiSelect">
                            <option selected>MBTI (Select)</option>
                            <option id="mbtiid" value="0">N/A</option>
                            <option id="mbtiid" value="1">INTJ</option>
                            <option id="mbtiid" value="2">INTP</option>
                            <option id="mbtiid" value="3">ENTJ</option>
                            <option id="mbtiid" value="4">ENTP</option>
                            <option id="mbtiid" value="5">INFJ</option>
                            <option id="mbtiid" value="6">INFP</option>
                            <option id="mbtiid" value="7">ENFJ</option>
                            <option id="mbtiid" value="8">ENFP</option>
                            <option id="mbtiid" value="9">ISTJ</option>
                            <option id="mbtiid" value="10">ISFJ</option>
                            <option id="mbtiid" value="11">ESTJ</option>
                            <option id="mbtiid" value="12">ESFJ</option>
                            <option id="mbtiid" value="13">ISTP</option>
                            <option id="mbtiid" value="14">ISFP</option>
                            <option id="mbtiid" value="15">ESTP</option>
                            <option id="mbtiid" value="16">ESFP</option>
                            </select>
                    </div>
                    <div class="mb-3">
                        <label for="learingstyle">Learning Style</label>
                            <select class="custom-select d-block w-100" aria-label="learningStyle">
                            <option selected>Learing Style (Select)</option>
                            <option id="learingstyleid" value="0">N/A</option>
                            <option id="learingstyleid" value="1">Visual</option>
                            <option id="learingstyleid" value="2">Aural</option>
                            <option id="learingstyleid" value="3">Verbal</option>
                            <option id="learingstyleid" value="4">Physical</option>
                            <option id="learingstyleid" value="5">Logical</option>
                            <option id="learingstyleid" value="6">Social</option>
                            <option id="learingstyleid" value="7">Solitary</option>
                            </select>
                    </div>
                    <!-- ปุ่มส่งฟอร์ม -->
                    <br />
                    <div class="pad-head">
                        <button
                            class="btn btn-primary btn-lg btn-block"
                            type="submit"
                            onclick=""
                        >
                            Get Start
                        </button>
                        
                    </div>
                    </form>
                </div>
                <!-- ฝั่งขวา -->
                <div class="col-sm-4">col-sm-4</div>
            </div>
        </div>
    </div>
</template>

<script>
// import {register} from '../API/User';

//get input
// register(username,password)

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
