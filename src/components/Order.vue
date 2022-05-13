<template>
  <div>
    <div class="container" :class="{ loadingItem: isLoading }">
      <div class="row text-center" v-if="isLoading">
        <loader></loader>
      </div>
      <div v-else class="row action-panel">
        <div class="container" style="padding-top: 60px">
          <div class="section-title">
            <h2 style="color: #444444">Sipariş Takip</h2>
          </div>
        </div>
      </div>
      <form
        v-if="!isLoading"
        id="query-form"
        role="form"
        style="display: block"
        @submit.prevent="onSubmit"
      >
        <div class="form-group">
          <input
            v-model="queryCode"
            class="form-control form-control-lg"
            type="text"
            placeholder="Sipariş Numaranız"
          />
          <div class="row">
            <div class="col text-center">
              <button
                type="submit"
                id="search"
                class="btn btn-primary"
                style="width: 40%; background-color: #091239"
                :disabled="isPageLoading"
              >
                <i v-if="isPageLoading" class="fa fa-spinner fa-spin" />
                Sorgula
              </button>
            </div>
          </div>
        </div>
      </form>
      <!-- End What We Do Section -->
      <!-- ======= About Section ======= -->
      <section id="about" class="about">
        <div class="container pt-5">
          <div class="row">
            <div class="col-lg-6">
              <img
                src="../assets/package4.jpg"
                class="img-fluid"
                id="package"
                alt=""
              />
            </div>
            <div class="col-lg-6 pt-4 pt-lg-0">
              <h3>Some Info</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
              <ul>
                <li>
                  <i class="bx bx-check-double"></i> Ullamco laboris nisi ut
                  aliquip ex ea commodo consequat.
                </li>
                <li>
                  <i class="bx bx-check-double"></i> Duis aute irure dolor in
                  reprehenderit in voluptate velit.
                </li>
              </ul>
              <div class="row icon-boxes">
                <div class="col-md-6">
                  <i class="bx bx-receipt"></i>
                  <h4>Corporis voluptates sit</h4>
                  <p>
                    Consequuntur sunt aut quasi enim aliquam quae harum pariatur
                    laboris nisi ut aliquip
                  </p>
                </div>
                <div class="col-md-6 mt-4 mt-md-0">
                  <i class="bx bx-cube-alt"></i>
                  <h4>Ullamco laboris nisi</h4>
                  <p>
                    Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia deserunt
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End About Section -->
    </div>
  </div>
</template>

<script>
import Loader from "./Loader.vue";
// import axios from "axios";
export default {
  data() {
    return {
      queryCode: null,
      isLoading: false,
      isPageLoading: false,
    };
  },
  components: {
    Loader,
  },
  methods: {
    onSubmit() {
      this.isPageLoading = true;
      //post querycode
      console.log(this.queryCode);
      this.$router.push("/orderdetails");
    },
  },
  created() {
    // const user_id = parseInt(localStorage.getItem("user_id"));
    // console.log(user_id);
  },
  mounted() {
    const user_id = parseInt(localStorage.getItem("user_id"));
    console.log("Order user_id");
    console.log(user_id);
    if (Number.isNaN(user_id)) {
      this.$router.push("/login");
    }
  },
};
</script>

<style>
#search {
  background-color: blue;
  transition: ease-in-out 0.3s !important;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-weight: 400;
  font-size: 13px;
  letter-spacing: 2px;
  display: inline-block;
  padding: 12px 28px;

  border-radius: 4px;
  margin-top: 30px;
}
#search:hover {
  background: #25386d !important;
}

.loadingItem {
  align-items: center;
  justify-content: center;
  display: flex;
}

.about {
  padding: 10px 0;
}
.about h3 {
  font-weight: 600;
  font-size: 32px;
}
.about ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}
.about ul li + li {
  margin-top: 10px;
}
.about ul li {
  position: relative;
  padding-left: 26px;
}
.about ul i {
  position: absolute;
  left: 0;
  top: 0;
  font-size: 22px;
  color: #3498db;
}
.about .icon-boxes {
  padding-top: 10px;
}
.about .icon-boxes h4 {
  font-size: 20px;
  font-weight: 700;
  margin-top: 5px;
}
.about .icon-boxes i {
  font-size: 48px;
  color: #3498db;
}
.about .icon-boxes p {
  font-size: 15px;
  color: #848484;
}
#package {
  border-radius: 20%;
}
</style>