<template>
  <div class="row">
    <div class="col-md-6 offset-md-3 col-sm-12 offset-sm-1">
      <form
        id="login-form"
        role="form"
        style="display: block"
        @submit.prevent="onSubmit"
      >
        <div class="container" style="padding-top: 50px; padding-bottom: 30px">
          <div class="section-title">
            <img
              class="col-xs-3 col-s-4 col-md-7 col-lg-7 col-xl-4"
              src="https://images.fineartamerica.com/images/artworkimages/medium/3/the-office-dunder-mifflin-logo-tv-show-andrea-transparent.png"
              alt=""
            />
            <h2></h2>
          </div>
        </div>
        <!-- <div class="container" style="padding-top: 60px">
          <div class="section-title">
            <h2 style="color: rgb(68, 68, 68)">Login</h2>
          </div>
        </div> -->
        <div class="form-group">
          <input
            type="email"
            name="email"
            id="email"
            class="form-control"
            placeholder="Email Address"
            v-model="email"
            required
          />
        </div>
        <div class="form-group">
          <input
            type="password"
            name="password"
            id="password"
            class="form-control"
            placeholder="Password"
            v-model="password"
            required
          />
        </div>

        <div class="form-group">
          <button
            type="submit"
            class="btn btn-primary"
            style="width: 100%; background-color: #091239"
            :disabled="isLoading"
          >
            <i v-if="isLoading" class="fa fa-spinner fa-spin" />
            Log In
          </button>
        </div>
        <div class="form-group">
          <div class="row">
            <div class="col-lg-12">
              <div class="text-center">
                <router-link to="/register">
                  <a>Register</a>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      password: "",
      isLoading: false,
      check: null,
    };
  },
  methods: {
    ...mapActions(["addMessage", "clearMessage", "loginWithEmail"]),
    onSubmit() {
      this.isLoading = true;
      let data = {
        email: this.email,
        password: this.password,
      };
      axios
        .post("http://127.0.0.1:5000/login", data)
        .then((res) => {
          this.check = res.data["data"];
        })
        .then(() => {
          console.log("Check");
          console.log(this.check);
          if (this.check == 0) {
            console.log("geçersiz");
            let message_obj = {
              message:
                "Kullanıcı adı veya şifre yanlış. Lütfen Tekrar Deneyiniz",
              messageClass: "danger",
              autoClose: true,
            };
            console.log(message_obj);
            this.addMessage(message_obj);
          } else if (this.check != null) {
            console.log("geçerli");
            this.clearMessage();
            this.$router.push({
              name: "mainpage",
            });
          } else {
            console.log("arada");
            let message_obj = {
              message: data.res,
              messageClass: "danger",
              autoClose: true,
            };
            this.addMessage(message_obj);
          }
        })
        .then(() => {
          this.isLoading = false;
        });

      // this.loginWithEmail(data)
      //   .then(() => {
      //     console.log("AAAA");
      //     console.log(data.res);
      //     if (data.res == 0) {
      //       let message_obj = {
      //         message: data.res,
      //         messageClass: "danger",
      //         autoClose: true,
      //       };
      //       this.addMessage(message_obj);
      //     } else if (data.res == "null") {
      //       let message_obj = {
      //         message: data.res,
      //         messageClass: "danger",
      //         autoClose: true,
      //       };
      //       this.addMessage(message_obj);
      //     } else {
      //       console.log("sa");
      //       this.clearMessage();
      //       this.$router.push({
      //         name: "mainpage",
      //       });
      //     }
      //   })
      //   .catch((error) => {
      //     let message_obj = {
      //       message: error.message,
      //       messageClass: "danger",
      //       autoClose: true,
      //     };
      //     this.addMessage(message_obj);
      //   })
      // .then(() => {
      //   this.isLoading = false;
      // });
    },
  },
};
</script>

<style>
.btn {
  background-color: blue;
}
</style>