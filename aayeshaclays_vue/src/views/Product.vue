<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-7">
                <div class="columns">
                    <class class="column is-1">
                        <figure class="image is-64x64 thumbnail" v-for="img in product.images" :key="img.id">
                            <img :src="img.get_image" @click="main_image=img"/>
                        </figure>
                    </class>
                    <class class="column">
                        <figure class="image main-image">
                            <img v-bind:src="main_image.get_image">
                        </figure>
                    </class>
                </div>

            </div>
            <div class="column">
                <h2 class="subtitle">Information</h2>
                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>

                <p><strong>Price: </strong>${{ product.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default{
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1,
            main_image: {}
        }
    },
    mounted() {
        this.getProduct();
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data
                    this.main_image = this.product.images[0];

                    document.title = this.product.name + ' | AayeshaClays';
                })
                .catch(error => {
                    console.log(error);
                })
            
            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if(isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1;
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item);

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>

<style lang="scss">
.main-image {
    width: 50%
}

.thumbnail {
    margin-bottom: 80px;
    cursor: pointer;
}
</style>