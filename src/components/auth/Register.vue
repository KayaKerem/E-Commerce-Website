<template>
  <div class="row">
    <div class="col-md-6 offset-md-3 col-sm-10 offset-sm-1">
      <form id="register-form" role="form" @submit.prevent="onSubmit">
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
        <div class="form-group">
          <input
            type="email"
            name="email"
            id="email"
            class="form-control"
            placeholder="Email"
            value
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
            placeholder="Şifre"
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
            Üye Ol
          </button>
        </div>
        <div class="form-group">
          <div class="row">
            <div class="col-lg-12">
              <div class="text-center">
                <router-link to="/login">
                  <a>Giriş Yap</a>
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
export default {
  data() {
    return {
      email: "",
      password: "",
      isLoading: false,
    };
  },
  methods: {
    ...mapActions(["clearMessage", "addMessage", "registerByEmail"]),
    onSubmit() {
      this.isLoading = true;
      let data = {
        email: this.email,
        password: this.password,
      };
      this.registerByEmail(data)
        .then(() => {
          this.clearMessage();
          this.$router.push({ name: "mainpage" });
        })
        .catch((error) => {
          // console.log('register error', error);
          let message_obj = {
            message: error.message,
            messageClass: "danger",
            autoClose: true,
          };
          this.addMessage(message_obj);
        })
        .then(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>
