<template>
    <div class="login">
        <div class="pad-head"></div>
        <!-- content -->
        <div class="container">
            <div class="row">
                <div class="col">
                    
                </div>
                <div class="col">
                    <div class="text-center mb-4">
                        <img
                            class="mb-4"
                            src="https://i.imgur.com/3DvN4YE.png"
                        />
                        <h1 class="h3 mb-3 font-weight-normal">
                            Hello, Bibbudi
                        </h1>
                        <p>
                            Level up your knowledge and get prepared for your career path.
                            <a href="https://caniuse.com/#feat=css-placeholder-shown">
                            Sign up!</a>
                        </p>
                    </div>
                    <div class="form-label-group">
                        <input
                            type="email"
                            id="inputEmail"
                            class="form-control"
                            placeholder="Email address"
                            required=""
                            autofocus=""
                        />
                        <label for="inputEmail"></label>
                    </div>
                    <div class="form-label-group">
                        <input
                            type="password"
                            id="inputPassword"
                            class="form-control"
                            placeholder="Password"
                            required=""
                        />
                        <label for="inputPassword"></label>
                    </div>
                    <div class="Box">
                        <div class="">
                            <div class="checkbox">
                                <label>
                                    <input
                                        type="checkbox"
                                        value="remember-me"
                                    />
                                    Remember me
                                </label>
                            </div>
                        </div>
                    </div>
                    <button
                        class="btn btn-lg btn-success btn-block"
                        type="submit"
                    >
                        <p class="font">Sign in</p>
                    </button>
                </div>
                <div class="col">
                   
                </div>
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

.pad-head {
    padding-bottom: 150px;
}
.container {
}

.btn-color { 
    background-color: blue;
}
</style>
