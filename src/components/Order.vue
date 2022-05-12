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
</style>