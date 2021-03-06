<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr 
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                            <div class="field">
                                <label>Address 1*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="address1">
                                </div>
                            </div>

                            <div class="field">
                                <label>Address 2</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="address2">
                                </div>
                            </div>

                            <div class="field">
                                <label>Zip code*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="zip_code" placeholder="5 digit zip code">
                                </div>
                            </div>

                            <div class="field">
                                <label>City*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="city">
                                </div>
                            </div>

                            <div class="field">
                                <label>Country*</label>
                                <div class="control">
                                    <country-select class="input dropdown" v-model="country" :country="country" topCountry="US"/>
                                </div>
                            </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>
                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address1: '',
            address2: '',
            zip_code: '',
            city: '',
            country: 'US',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Aayesha Clays'

        this.cart = this.$store.state.cart;

        if(this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51I5JahLap9jZpLfWFCKDHAlbUSS4EMZcsxi9dozJAjtPtqnkb7TZ08oHFHmlm2DXFLm0f9OD51pmWVHKQNlE8kp800aqP1OjoV')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true})

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = [];
            
            if (this.first_name === '') {
                this.errors.push('The first name field is missing!')
            }
            if (this.last_name === '') {
                this.errors.push('The last name field is missing!')
            }
            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.phone === '') {
                this.errors.push('The phone field is missing!')
            }
            if (this.address1 === '') {
                this.errors.push('The address1 field is missing!')
            }
            if (this.zip_code === '') {
                this.errors.push('The zip_code field is missing!')
            }
            if (this.city === '') {
                this.errors.push('The city field is missing!')
            }
            if (this.country === '') {
                this.errors.push('The country field is missing!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items=[]

            for(let i=0; i < this.cart.items.length; i++){
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'phone': this.phone,
                'items': items,
                'address': {
                    'address1': this.address1,
                    'address2': this.address2,
                    'zip_code': this.zip_code,
                    'city': this.city,
                    'country': this.country,
                },
                'stripe_token': token.id
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart');
                    this.$router.push('/cart/success');
                })
                .catch(error => {
                    this.errors.push(`${error}`)
                    console.log(error);
                })

            this.$store.commit('setIsLoading', false)
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>