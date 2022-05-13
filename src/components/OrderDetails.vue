<template>
  <div>
    <div class="container" :class="{ loadingItem: isLoading }">
      <div class="row text-center" v-if="isLoading">
        <loader></loader>
      </div>
      <div v-else class="row action-panel">
        <div class="container" style="padding-top: 60px">
          <div class="section-title">
            <h2 style="color: #444444">Sipariş Durumu</h2>
          </div>
        </div>
        <!--Google map-->

        <div class="container-fluid" style="margin-top: 30px">
          <div class="row">
            <div class="col-lg-6 col-xl-6">
              <div class="card" style="width: 18rem">
                <img
                  class="card-img-top"
                  src="../assets/car3.png"
                  alt="Card image cap"
                />
                <div class="card-body">
                  <h5 class="card-title">Siparişiniz yolda</h5>
                  <p class="card-text">
                    Siparişiniz yola çıktı. En kısa sürede adresinizde olacağız.
                  </p>
                </div>
              </div>
            </div>
            <div class="col-lg-6 col-xl-6">
              <div class="map-responsive">
                <iframe
                  src="https://maps.google.com/maps?q=Y%C4%B1ld%C4%B1z%20Teknik%20%C3%9Cniversitesi%20Teknopark&t=&z=15&ie=UTF8&iwloc=&output=embed"
                  width="400"
                  height="250"
                  frameborder="0"
                  style="border: 0"
                  scrolling="no"
                  marginheight="0"
                  marginwidth="0"
                ></iframe>
              </div>
            </div>
          </div>
        </div>

        <!--Google Maps-->
      </div>
    </div>
  </div>
</template>

<script>
import Loader from "./Loader.vue";
export default {
  data() {
    return {
      isLoading: false,
    };
  },
  components: {
    Loader,
  },
};
</script>

<style>
.loadingItem {
  align-items: center;
  justify-content: center;
  display: flex;
}
.map-responsive {
  overflow: hidden;
  padding-bottom: 75%;
  position: relative;
  background: none !important;
  height: 0;
}
.map-responsive iframe {
  left: 0;
  top: 0;
  height: 100% !important;
  width: 100% !important;
  position: absolute;
}
.card {
  margin: 0 auto; /* Added */
  float: none; /* Added */
  margin-bottom: 10px; /* Added */
}
.card-img-top {
  width: 100% !important;
  height: 100% !important;
}
.card-text {
  font-family: 'Poppins", sans-serif' !important;
}
.card-title {
  font-family: 'Poppins", sans-serif' !important;
  font-weight: 800;
  font-size: 30px;
}
</style>