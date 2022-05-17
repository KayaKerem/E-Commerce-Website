<template>
  <div class="container" id="page">
    <div class="card" id="success-card">
      <div
        style="
          border-radius: 200px;
          height: 200px;
          width: 200px;

          margin: 0 auto;
        "
      >
        <i class="checkmark">✓</i>
      </div>
      <h1 id="success-text">28756 numaralı siparişiniz alındı</h1>
      <p id="response-message">
        Siparişiniz başarıyla tarafımıza ulaşmıştır;<br />
        En kısa sürede teslim edeceğiz!
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  created() {},
  methods: {},
  mounted() {},
};
</script>

<style >
#page {
  text-align: center;
  /* padding: 40px 0; */
}
#success-text {
  color: #091239;
  font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
  font-weight: 900;
  font-size: 40px;
  margin-bottom: 10px;
}
#response-message {
  color: #404f5e;
  font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
  font-size: 20px;
  margin: 0;
}

.checkmark {
  color: #efb631;
  font-size: 200px;
  line-height: 200px;
  margin-left: -15px;
}
#success-card {
  /* background: white; */
  padding: 60px;
  border-radius: 100px;
  box-shadow: 0 2px 3px #c8d0d8;
  display: inline-block;
  margin-top: 80px !important;
}
</style>