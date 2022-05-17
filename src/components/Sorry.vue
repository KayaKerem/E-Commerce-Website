<template>
  <div class="container" id="page">
    <div class="card" id="sorry-card">
      <div
        style="
          border-radius: 200px;
          height: 200px;
          width: 200px;

          margin: 0 auto;
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="128"
          height="128"
          fill="#EFB631"
          class="bi bi-emoji-dizzy"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
          />
          <path
            d="M9.146 5.146a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708.708l-.647.646.647.646a.5.5 0 0 1-.708.708l-.646-.647-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zm-5 0a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 1 1 .708.708l-.647.646.647.646a.5.5 0 1 1-.708.708L5.5 7.207l-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zM10 11a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"
          />
        </svg>
      </div>
      <h1 id="sorry-text">Hay Aksi</h1>
      <p id="sorry-message">
        Yaşanan aksaklık için özür dileriz.<br />
        En kısa sürede sorunu çözeceğiz!
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
#sorry-text {
  color: #091239;
  font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
  font-weight: 900;
  font-size: 40px;
  margin-bottom: 10px;
}
#sorry-message {
  color: #404f5e;
  font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
  font-size: 20px;
  margin: 0;
}

#face {
  color: #efb631;
  font-size: 75px;
  line-height: 200px;
  margin-left: -15px;
}
#sorry-card {
  /* background: white; */
  padding: 60px;
  border-radius: 100px;
  box-shadow: 0 2px 3px #c8d0d8;
  display: inline-block;
  margin-top: 80px !important;
}
</style>