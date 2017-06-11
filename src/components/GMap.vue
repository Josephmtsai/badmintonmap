<template>
  <div id="app">
    <gmap-map class="gmap" :center="center" :zoom="zoom">
      <gmap-info-window :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen" :content="infoContent" @closeclick="infoWinOpen=false"></gmap-info-window>
      <gmap-marker v-for="(marker,index) in markers" @click="clickMarker(marker, index)" :key="index" :position="marker.position" :clickable="true"></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
import * as VueGoogleMaps from 'vue2-google-maps'
import Vue from 'vue'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBW6jkW1QIMpjw5SUIytKmuQ40emkWLgM8',
    v: '3'
    // libraries: 'places', //// If you need to use place input
  }
})

export default {
  name: 'app',
  async created () {
    try {
      const res = await fetch('/api/locationInfo');
      const locationInfo = await res.json();
      this.markers = locationInfo.map(({ lng, lat, name, address }) => {
        return {
          position: { lng, lat },
          infoText: name
        }
      })
    } catch (ex) {

    }
  },
  data () {
    return {
      infoContent: '',
      infoWindowPos: {
        lat: 0,
        lng: 0
      },
      infoWinOpen: false,
      // optional: offset infowindow so it visually sits nicely on top of our marker
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -35
        }
      },
      center: { lat: 23.6052631, lng: 120.1412734 },
      zoom: 7,
      markers: [{
        position: {
          lat: 25.0781209,
          lng: 121.5730155
        },
        infoText: 'Marker 1'
      }],
      markersList: function () {

      }
    }
  },
  methods: {
    clickMarker: function (marker, index) {
      this.center = marker.position
      this.zoom = 15
      this.infoWindowPos = marker.position
      this.infoContent = marker.infoText
      this.infoWinOpen = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.gmap {
  width: 100%;
  height: 100%;
  position: absolute !important;
  left: 0;
  top: 0
}
</style>
