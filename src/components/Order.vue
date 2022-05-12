<template>
  <div>
    <div class="container">
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
    </div>
  </div>
</template>

<script>
import Loader from "./Loader.vue";
// import axios from "axios";
export default {
  data() {
    return {
      isLoading: false,
    };
  },
  components: {
    Loader,
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
</style>