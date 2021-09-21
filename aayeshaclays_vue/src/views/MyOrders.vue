<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Orders</h1>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My Orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order"/>
            </div>

        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyOrders',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My orders | AayeshaClays'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')
            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders')
                .then(response => {
                    this.orders = response.data;
                })
                .catch(error => {
                    console.error(error);
                })

            this.$store.commit('setIsLoading', false);
        }
    },
}
</script>