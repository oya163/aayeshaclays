<template>
  <div class="home">
      <p class="title text-white text-center mb-6" style="font-weight: 600; text-align: center">
          Welcome to Aayesha Clays
      </p>
      <p class="subtitle" style="font-weight: 600; text-align: center">
          The best earrings store online
      </p>
      <video-background 
        :src="require(`@/assets/butterfly.mp4`)" 
        :poster="require(`@/assets/logo.png`)"
        style="max-height: 500px; height: 100vh;"
        overlay="linear-gradient(45deg,#2a4ae430,#fb949e6b)" 
      >  
      </video-background>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
    <ProductBox
      v-for="product in latestProducts"
      v-bind:key="product.id"
      v-bind:product="product"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ProductBox from '@/components/ProductBox';
import VideoBackground from 'vue-responsive-video-background-player';

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox,
    'video-background': VideoBackground,
  },
  mounted() {
    this.getLatestProducts();

    document.title = 'Home | AayeshaClays';
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true);

      await axios
        .get('/api/v1/latestproducts')
        .then(response => {
          this.latestProducts = response.data;
        })
        .catch(error => {
          console.log(error);
        })
      
      this.$store.commit('setIsLoading', false);
    }
  }
}
</script>


