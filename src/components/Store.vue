<template>
  <div class="container" :class="{ loadingItem: isProductLoading }">
    <div class="row text-center" v-if="isProductLoading">
      <grid-loader
        :loading="isProductLoading"
        :color="loaderColor"
        :size="loaderSize"
      ></grid-loader>
    </div>
    <div v-else class="row action-panel">
      <div class="col-12">
        <div class="btn-group btn-group-sm pull-right">
          <button
            id="list"
            class="btn btn-outline-dark"
            @click.prevent="changeDisplay(true)"
          >
            <i class="fa fa-list" aria-hidden="true"></i>
          </button>
          <button
            id="grid"
            class="btn btn-outline-dark"
            @click.prevent="changeDisplay(false)"
          >
            <i class="fa fa-th" aria-hidden="true"></i>
          </button>
        </div>
      </div>
    </div>

    <div class="row" v-if="!isProductLoading">
      <app-product-item
        v-for="prod in products"
        :item="prod"
        :key="prod.id"
        :displayList="displayList"
      ></app-product-item>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import ProductItem from "./product/ProductItem.vue";
import GridLoader from "vue-spinner/src/GridLoader.vue";

export default {
  data() {
    return {
      loaderColor: "#5cb85c",
      loaderSize: "50px",
      displayList: false,
    };
  },
  computed: {
    ...mapGetters(["products", "isProductLoading"]),
  },
  components: {
    appProductItem: ProductItem,
    GridLoader,
  },
  methods: {
    changeDisplay(isList) {
      this.displayList = isList;
    },
  },
};
</script>

<style>
.loadingItem {
  align-items: center;
  justify-content: center;
  display: flex;
}

.action-panel {
  margin-bottom: 10px;
  margin-right: 5px;
}
/* .container{
  background-color: black !important;

} */
.card {
  border: 0px !important;
}
.card-body {
  background-color: rgb(255, 248, 204) !important;
}
.list-group-item {
  background-color: rgb(255, 248, 204) !important;
}
.thumbnail-card {
  background-color: black !important;
}
h5 {
  font-family: "Bangers" !important;
}
.list-group-item .card-body[data-v-ae4ae6fc] {
  height: 100%;
}
</style>
