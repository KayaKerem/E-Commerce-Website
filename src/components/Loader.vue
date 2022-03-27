<template>
  <div id="body">
    <svg
      version="1.1"
      baseProfile="tiny"
      id="Layer_1_copy"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      width="28px"
      height="28px"
      viewBox="0 0 28 28"
      overflow="auto"
      xml:space="preserve"
      class="loader"
    >
      <path
        fill="#F2F2F2"
        class="trail"
        d="M20.827,7.024c-2.512-2.512-6.207-3.507-9.646-2.599l0.442,1.668c2.844-0.751,5.904,0.073,7.982,2.152
	c3.231,3.23,3.231,8.487,0.001,11.718c-3.231,3.23-8.487,3.303-11.718,0.073c-1.426-1.427-2.27-3.225-2.404-5.225H3.755
	c0.137,2,1.162,4.694,2.913,6.444c1.951,1.951,4.515,2.891,7.079,2.891s5.128-0.993,7.08-2.944
	C24.731,17.299,24.731,10.929,20.827,7.024z"
      />
      <g class="plane">
        <polygon
          fill="#DDDDDD"
          points="5.253,7.828 3.692,15.821 5.253,18.461 6.812,15.821 	"
        />
        <g>
          <path
            fill="#EEEEEE"
            d="M5.253,7.966c0,0-5.056,8.846-5,8.846c0.055,0,3.935,0,3.935,0L5.253,7.966z"
          />
          <path
            fill="#EEEEEE"
            d="M5.253,7.968c0,0,5.056,8.845,5,8.845s-3.936,0-3.936,0L5.253,7.968z"
          />
        </g>
      </g>
    </svg>
  </div>
</template>

<script>
export default {};
</script>

<style>
#body {
  background-color: #fff8cc;
}
.loader {
  width: 100px;
  height: 100px;
  -webkit-animation: spin 1.6s infinite linear;
  -moz-animation: spin 1.6s infinite linear;
  display: block;
  margin: 0 auto;
}

.trail {
  fill: rgba(255, 255, 255, 0.1);
  fill: none;
}

@-moz-keyframes spin {
  0% {
    -moz-transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(360deg);
  }
}

@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
</style>