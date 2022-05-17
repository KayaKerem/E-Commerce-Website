<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark" role="navigation">
    <div class="container">
      <!-- Brand and toggle get grouped for better mobile display -->
      <router-link to="/home" class="navbar-brand mr-auto"
        >Dunder Mifflin</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarTop"
        aria-controls="navbarTop"
        aria-expanded="false"
        aria-label="Toggle navigation"
        @click="toggleNavbar"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div
        class="collapse navbar-collapse"
        id="navbarTop"
        :class="{ show: isNavOpen }"
      >
        <ul class="navbar-nav mr-auto"></ul>

        <ul class="nav navbar-nav">
          <li>
            <router-link
              id="productbutton"
              to="/"
              class="btn btn-dark navbar-btn"
              tag="button"
            >
              Ürünlerimiz
            </router-link>
          </li>
          <!-- <router-link to="/" tag="li" class="nav-item">
            <a class="nav-link">Ürünlerimiz</a>
          </router-link> -->
          <!--     -------------   -->
          <li>
            <router-link
              id="orderbutton"
              to="/order"
              class="btn btn-dark navbar-btn"
              tag="button"
            >
              Sipariş Takip
            </router-link>
          </li>

          <!-- <router-link v-if="isLoggedIn" to="/order" tag="li" class="nav-item">
            <a class="nav-link">Sipariş Takip</a>
          </router-link> -->
          <!--  -->
          <!-- <router-link
            to="/login"
            tag="li"
            v-if="!isLoggedIn"
            class="nav-item"
            active-class="active"
          >
            <a class="nav-link">Giriş Yap</a>
          </router-link> -->

          <!-- <router-link
            to="/register"
            tag="li"
            v-if="!isLoggedIn"
            class="nav-item"
            active-class="active"
          >
            <a class="nav-link">Üye Ol</a>
          </router-link> -->
          <!-- ---------- -->

          <!-- <li v-if="isLoggedIn" class="li-pointer nav-item">
            <a @click="logout" class="nav-link">Main {{ userEmail }}</a>
          </li> -->
          <!--  sepetim-->
          <li>
            <router-link
              v-if="isLoggedIn"
              to="/cart"
              class="btn btn-light navbar-btn"
              tag="button"
            >
              <a id="sepettitle">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-cart"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l1.313 7h8.17l1.313-7H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"
                  /></svg
                >Sepetim</a
              >
              <span class="badge badge-light"
                >{{ numItems }} ($ {{ cartValue }})</span
              >
            </router-link>
          </li>

          <li>
            <router-link
              v-if="isLoggedIn"
              to="/profile"
              class="btn btn-light navbar-btn"
              tag="button"
            >
              <a id="sepettitle">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-person"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"
                  /></svg
                >{{ this.userName }} {{ this.surname }}.</a
              >
            </router-link>
          </li>

          <!--  -->
          <li>
            <router-link
              v-if="!isLoggedIn"
              to="/login"
              class="btn btn-light navbar-btn"
              tag="button"
            >
              <a id="sepettitle">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-person"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"
                  /></svg
                >{{ this.userName }} {{ this.surname }}</a
              >
              <!-- <span class="badge badge-light"
                >{{ numItems }} ($ {{ cartValue }})</span
              > -->
            </router-link>
          </li>
          <!--  -->

          <!-- ÇIKIŞ YAP BUTONU -->
          <li v-if="isLoggedIn" class="li-pointer nav-item">
            <a @click="logout" class="nav-link">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-power"
                viewBox="0 0 16 16"
              >
                <path d="M7.5 1v7h1V1h-1z" />
                <path
                  d="M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z"
                /></svg
            ></a>
          </li>
        </ul>
      </div>
    </div>
    <!-- /.container -->
  </nav>
</template>

<script>
// import axios from "axios";
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      isNavOpen: false,
      isLoggedIn: false,
      userName: "Giriş Yap",
      surname: "",
      router_link: "/login",
    };
  },
  computed: {
    ...mapGetters(["cartValue", "currentUser", "cartItemList"]),
    numItems() {
      return this.cartItemList.reduce((total, item) => {
        total += item.quantity;
        return total;
      }, 0);
    },
    userEmail() {
      return this.isLoggedIn ? this.currentUser.email : "";
    },
  },
  created() {
    if (localStorage.getItem("user_id") != null) {
      this.isLoggedIn = true;
      this.userName = localStorage.getItem("user_name");

      let surname = this.userName.split(" ")[1].slice(0, 1);
      this.surname = surname;
      this.userName = this.userName.split(" ")[0];
      this.router_link = "/home";
    }
  },
  methods: {
    ...mapActions(["addMessage", "clearMessage"]),
    toggleNavbar() {
      this.isNavOpen = !this.isNavOpen;
    },
    logout() {
      let message_obj = {
        message: "Çıkış Yapıldı",
        messageClass: "danger",
        autoClose: true,
      };
      console.log(message_obj);
      this.addMessage(message_obj);
      localStorage.removeItem("user_id");
      localStorage.removeItem("user_name");
      this.clearMessage();
      this.isLoggedIn = false;
      window.location.href = "/home";
      // this.$router.go();
    },
  },
};
</script>


<style scoped lange="sass">
.navbar-btn a {
  color: white;
}

.li-pointer {
  cursor: pointer;
}

.li-pointer:hover {
  cursor: pointer;
}
.btn-light {
  color: #fff;
  background-color: #fff;
  border-color: #091239;
}
.navbar {
  background-color: #091239 !important;
}
#sepettitle {
  color: #091239 !important;
}
#logo {
  width: 30px;
}
#orderbutton {
  background-color: #091239 !important;
  border-color: #091239;
}
#orderbutton:hover {
  border-color: white;
  transition: 0.3s;
}
#productbutton {
  background-color: #091239 !important;
  border-color: #091239;
}
#productbutton:hover {
  border-color: white;
  transition: 0.3s;
}
</style>
