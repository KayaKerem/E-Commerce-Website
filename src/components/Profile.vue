<template>
  <div class="container-fluid">
    <loader v-if="isShow" />

    <div class="section-title" v-if="categories1.length <= 0">
      <h2 style="color: #444444; padding-top: 40px">
        Henüz alışveriş yapmadınız...
      </h2>
    </div>
    <div v-if="categories1.length > 0">
      <div class="section-title" v-if="!isShow">
        <h2 style="color: #444444; padding-top: 40px">Satın Alma Verileri</h2>
      </div>
      <!-- <div class="btn-group">
      <button type="button" class="btn btn-danger">Action</button>
      <button
        type="button"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <span class="sr-only">Toggle Dropdown</span>
      </button>
      <div class="dropdown-menu">
        <a class="dropdown-item" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <a class="dropdown-item" href="#">Something else here</a>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item" href="#">Separated link</a>
      </div>
    </div> -->
      <div class="full-height" v-if="!isShow">
        <div class="row justify-content-center">
          <div class="col-12 col-xs-9 col-sm-9 col-lg-6 col-md-6 pt-3">
            <div class="border">
              <h3
                class="text-primary text-center pb-1"
                style="font-size: bold !important"
              >
                Geçmiş Siparişler (Adet)
              </h3>
              <div id="chart" class="p-1 rounded-lg">
                <apexchart
                  v-if="series.length"
                  type="bar"
                  height="300"
                  width="100%"
                  :options="options"
                  :series="series"
                  class="businessChart"
                ></apexchart>
              </div>
            </div>
          </div>
          <!-- -------------------- -->
          <div class="col-12 col-xs-9 col-sm-9 col-lg-6 col-md-6 pt-3">
            <div class="border">
              <h3
                class="text-primary text-center pb-1"
                style="font-size: bold !important"
              >
                Geçmiş Siparişler (Fiyat)
              </h3>
              <div id="chart" class="p-1 rounded-lg">
                <apexchart
                  v-if="series.length"
                  type="bar"
                  height="300"
                  width="100%"
                  :options="options2"
                  :series="series2"
                  class="businessChart"
                ></apexchart>
              </div>
            </div>
          </div>
          <!-- -------------------- -->

          <div class="col-12 col-xs-9 col-sm-9 col-lg-6 col-md-6 pt-3">
            <div class="border">
              <h3
                class="text-primary text-center pb-1"
                style="font-size: bold !important"
              >
                Ürün Başına Harcamalar
              </h3>
              <div id="chart" class="p-1 rounded-lg">
                <apexchart
                  type="donut"
                  height="300"
                  width="100%"
                  :options="piechart"
                  :series="seriesDonut"
                  class="businessChart"
                ></apexchart>
              </div>
            </div>
          </div>

          <div class="col-12 col-xs-9 col-sm-9 col-lg-6 col-md-6 pt-3">
            <div class="border">
              <h3
                class="text-primary text-center pb-1"
                style="font-size: bold !important"
              >
                Aylara Göre Harcamalar
              </h3>
              <div id="chart" class="p-1 rounded-lg">
                <apexchart
                  type="donut"
                  height="300"
                  width="100%"
                  :options="piechart2"
                  :series="seriesDonut2"
                  class="businessChart"
                ></apexchart>
              </div>
            </div>
          </div>
          <!-- -------------------- -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Loader from "./Loader.vue";
const axios = require("axios");
export default {
  comments: {
    axios,
  },
  components: { Loader },
  data() {
    return {
      isShow: true,
      series: [],
      series2: [],
      categories1: [],
      options2: {},
      options: {
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
        },
        plotOptions: {
          bar: {
            horizontal: false,
          },
        },
        stroke: {
          width: 1,
          colors: ["#fff"],
        },
        title: {
          text: "",
        },
        xaxis: {
          categories: this.categories1,
          //   labels: {
          //     formatter: function (val) {
          //       return val + "K";
          //     },
          //   },
        },
        yaxis: {
          title: {
            text: undefined,
          },
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val + " paket";
            },
          },
        },
        fill: {
          opacity: 1,
        },
        legend: {
          position: "top",
          horizontalAlign: "left",
          offsetX: 40,
        },
      },

      seriesDonut: [],
      piechart: {
        labels: [],
        chart: {
          type: "donut",
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                name: {
                  show: true,
                  fontSize: "22px",
                  fontFamily: "Rubik",
                  color: "#dfsda",
                  offsetY: -10,
                },
                value: {
                  show: true,
                  fontSize: "32px",
                  fontFamily: "Helvetica, Arial, sans-serif",
                  color: undefined,
                  offsetY: 16,
                },
                total: {
                  show: true,
                  label: "Toplam",
                  color: "#373d3f",
                  formatter: function (w) {
                    return w.globals.seriesTotals.reduce((a, b) => {
                      return a + b;
                    }, 0);
                  },
                },
              },
            },
          },
        },
      },

      seriesDonut2: [],
      piechart2: {
        labels: [],
        chart: {
          type: "donut",
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                name: {
                  show: true,
                  fontSize: "22px",
                  fontFamily: "Rubik",
                  color: "#dfsda",
                  offsetY: -10,
                },
                value: {
                  show: true,
                  fontSize: "32px",
                  fontFamily: "Helvetica, Arial, sans-serif",
                  color: undefined,
                  offsetY: 16,
                },
                total: {
                  show: true,
                  label: "Toplam",
                  color: "#373d3f",
                  formatter: function (w) {
                    return w.globals.seriesTotals.reduce((a, b) => {
                      return a + b;
                    }, 0);
                  },
                },
              },
            },
          },
        },
      },
    };
  },
  created() {
    console.log(this.series);
    const user_id = parseInt(localStorage.getItem("user_id"));
    axios
      .post("http://127.0.0.1:5000/showtable/packageoftotalbought", {
        id: user_id,
      })
      .then((res) => {
        console.log("PPPPPPPPPPPPPPPPp");

        this.seriesDonut = res.data["series"];
        this.piechart["labels"] = res.data["labels"];
        // this.$set(this.piechart, 0, res.data["labels"]);

        console.log(this.seriesDonut);
        console.log(this.piechart);
        // console.log(res.data["data"]["labels"]);
        // console.log(res);
      });
    axios
      .post("http://127.0.0.1:5000/showtable/spentmoneyformonths", {
        id: user_id,
      })
      .then((res) => {
        this.seriesDonut2 = res.data["series"];
        this.piechart2["labels"] = res.data["labels"];
        // this.$set(this.piechart, 0, res.data["labels"]);
        console.log("seriesDonut2");
        console.log(this.seriesDonut2);
        console.log("piechart2");
        console.log(this.piechart2);
      });
  },

  mounted() {
    const user_id = parseInt(localStorage.getItem("user_id"));
    console.log(user_id);

    axios
      .post("http://127.0.0.1:5000/showtable/pastorders", { id: user_id })
      .then((res) => {
        let options = {
          chart: {
            type: "bar",
            height: 350,
            stacked: true,
          },
          plotOptions: {
            bar: {
              horizontal: false,
            },
          },
          stroke: {
            width: 1,
            colors: ["#fff"],
          },
          title: {
            text: "",
          },
          xaxis: {
            categories: this.categories1,
            //   labels: {
            //     formatter: function (val) {
            //       return val + "K";
            //     },
            //   },
          },
          yaxis: {
            title: {
              text: undefined,
            },
          },
          tooltip: {
            y: {
              formatter: function (val) {
                return val + " paket";
              },
            },
          },
          fill: {
            opacity: 1,
          },
          legend: {
            position: "top",
            horizontalAlign: "left",
            offsetX: 40,
          },
        };

        for (let i in res.data["pastOrders"]) {
          this.series.push(res.data["pastOrders"][i]);
        }
        for (let k in res.data["dates"]) {
          let a = res.data["dates"][k];
          console.log("Anana");
          console.log(res.data["dates"][k]);

          options["xaxis"]["categories"].push(a.slice(0, 10));
          //   this.categories1.push(parseInt(a));
        }
        // this.$set(this.options, 4, { categories: this.categories1 });
        this.options = options;

        console.log(options["xaxis"]["categories"]);
      });

    axios
      .post("http://127.0.0.1:5000/showtable/pastorders_money", { id: user_id })
      .then((res) => {
        let options = {
          chart: {
            type: "bar",
            height: 350,
            stacked: true,
          },
          plotOptions: {
            bar: {
              horizontal: false,
            },
          },
          stroke: {
            width: 1,
            colors: ["#fff"],
          },
          title: {
            text: "",
          },
          xaxis: {
            categories: this.categories1,
            //   labels: {
            //     formatter: function (val) {
            //       return val + "K";
            //     },
            //   },
          },
          yaxis: {
            title: {
              text: undefined,
            },
          },
          tooltip: {
            y: {
              formatter: function (val) {
                return val + " dolar";
              },
            },
          },
          fill: {
            opacity: 1,
          },
          legend: {
            position: "top",
            horizontalAlign: "left",
            offsetX: 40,
          },
        };

        for (let i in res.data["pastOrders"]) {
          this.series2.push(res.data["pastOrders"][i]);
        }
        for (let k in res.data["dates"]) {
          let a = res.data["dates"][k];
          console.log(a);
          options["xaxis"]["categories"].push(a.slice(0, 10));
          //   this.categories1.push(parseInt(a));
        }
        // this.$set(this.options, 4, { categories: this.categories1 });
        this.options2 = options;

        this.isShow = false;
        console.log(options["xaxis"]["categories"]);
      });
  },
};
</script>


<style>
.border {
  background-color: #fff8cc;
  border-radius: 50px !important;
  /* border-width: 1000px; */
}
</style>