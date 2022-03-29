<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark" role="navigation">
    <div class="container">
      <!-- Brand and toggle get grouped for better mobile display -->
      <router-link to="/home" class="navbar-brand mr-auto"
        ><img id="logo" class="col-md-4" src="../assets/img/logo.png" />Dunder
        Mifflin</router-link
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
          <router-link
            to="/"
            tag="li"
            v-if="!isLoggedIn"
            class="nav-item"
            active-class="active"
          >
            <a class="nav-link">Ürünlerimiz</a>
          </router-link>
          <!--  -->
          <router-link
            to="/login"
            tag="li"
            v-if="!isLoggedIn"
            class="nav-item"
            active-class="active"
          >
            <a class="nav-link">Giriş Yap</a>
          </router-link>
          <li v-if="isLoggedIn" class="li-pointer nav-item">
            <a @click="logout" class="nav-link">Logout {{ userEmail }}</a>
          </li>
          <router-link
            to="/register"
            tag="li"
            v-if="!isLoggedIn"
            class="nav-item"
            active-class="active"
          >
            <a class="nav-link">Üye Ol</a>
          </router-link>
          <!-- ---------- -->

          <!-- <li v-if="isLoggedIn" class="li-pointer nav-item">
            <a @click="logout" class="nav-link">Main {{ userEmail }}</a>
          </li> -->

          <li>
            <router-link
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
        </ul>
      </div>
    </div>
    <!-- /.container -->
  </nav>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      isNavOpen: false,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "cartValue", "currentUser", "cartItemList"]),
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
  methods: {
    ...mapActions(["logout"]),
    toggleNavbar() {
      this.isNavOpen = !this.isNavOpen;
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
</style>
