<template>
  <div class="d-flex flex-column sticky-footer-wrapper">
    <main class="flex-fill">
      <app-header class="fixed-top"></app-header>
      <message-component></message-component>

      <router-view class="pt-5"></router-view>

      <!-- <div class="container mt-3">
        <div class="row">
         
      </div> -->
    </main>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import Header from "./components/Header.vue";
import MessageComponent from "./components/common/MessageComponent.vue";

export default {
  components: {
    appHeader: Header,
    MessageComponent,
  },
  methods: {
    ...mapActions(["getShoppingCart", "listenToProductList"]),
  },
  mounted() {
    console.log(this.listenToProductList());
  },
  created() {
    let uid = this.$store.getters.currentUser.uid;
    this.listenToProductList();
    this.getShoppingCart({
      uid,
      currentCart: this.$store.getters.cartItemList,
    });
  },
};
</script>

<style>
body,
.sticky-footer-wrapper {
  min-height: 100vh;
}

.flex-fill {
  flex: 1 1 auto;
  background-color: rgb(255, 248, 204) !important;
}
footer {
  height: 40px;
  color: #666;
  padding: 10px 0 10px 0;
  font-size: 85%;
}
footer a {
  color: #999;
}
footer a:hover {
  color: #efefef;
}
@media (max-width: 576px) {
  footer {
    height: 50px;
  }
}
#sticky-footer {
  background-color: #091239 !important;
}
</style>
