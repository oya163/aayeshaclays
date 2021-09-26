<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Profile</h1>
            </div>

            <hr>

            <div class="column is-12">
                <h3 class="is-size-4 mb-6">Welcome {{ user_profile.first_name }} !</h3>

                <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <form @submit.prevent="submitForm">                    
                    <div class="columns is-multiline">
                        <div class="column is-6">
                            <div class="field">
                                <label>First name</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="user_profile.first_name" placeholder="First Name">
                                </div>
                            </div>

                            <div class="field">
                                <label>Last name</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="user_profile.last_name" placeholder="Last Name">
                                </div>
                            </div>

                            <div class="field">
                                <label>E-mail</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="user_profile.email" placeholder="email@domain.com">
                                </div>
                            </div>

                            <div class="field">
                                <label>Phone</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="account.phone">
                                </div>
                            </div>

                            <div class="field">
                                <label>Birth Date</label>
                                <div class="control">
                                    <input type="date" class="input" v-model="account.birth_date" placeholder="MM/DD/YYYY">
                                </div>
                            </div>
                        </div>

                        <div class="column is-6">
                            <div class="field">
                                <label>Address 1</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="account.address1">
                                </div>
                            </div>

                            <div class="field">
                                <label>Address 2</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="account.address2">
                                </div>
                            </div>

                            <div class="field">
                                <label>Zip code</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="account.zip_code" placeholder="5 digit zip code">
                                </div>
                            </div>

                            <div class="field">
                                <label>City</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="account.city">
                                </div>
                            </div>

                            <div class="field">
                                <label>Country</label>
                                <div class="control">
                                    <country-select class="input dropdown" v-model="account.country" :country="account.country" topCountry="US"/>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Save Changes</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import { vueCountryRegionSelect } from 'vue3-country-region-select';

export default {
    name: 'MyAccount',
    components: {
        vueCountryRegionSelect
    },
    data() {
        return {
            user_profile: Object,
            account: Object,
            errors: []
        }
    },
    mounted() {
        document.title = 'My account | AayeshaClays'

        this.getUserProfile()
    },
    methods: {
        async getUserProfile() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/users/${localStorage.username}`)
                .then(response => {
                    this.user_profile = response.data;
                    this.account = this.user_profile.account;
                })
                .catch(error => {
                    console.error(error);
                })
            this.$store.commit('setIsLoading', false);
        },
        submitForm() {
            this.errors = []

            if (this.user_profile.first_name === '') {
                this.errors.push('The first name is missing')
            }
            if (this.user_profile.last_name === '') {
                this.errors.push('The last name is missing')
            }
            if (this.user_profile.email === '') {
                this.errors.push('The first name is missing')
            }
            if (this.account.phone === '') {
                this.errors.push('The phone number is missing')
            }
            if (this.account.birth_date === '') {
                this.errors.push('The birth date is missing')
            }
            if (this.account.address1 === '') {
                this.errors.push('The address is missing')
            }
            if (this.account.zip_code === '') {
                this.errors.push('The zipcode is missing')
            }
            if (this.account.city === '') {
                this.errors.push('The city is missing')
            }
            if (this.account.country === '') {
                this.errors.push('The country is missing')
            }

            if (!this.errors.length) {
                axios
                    .put(`/users/${localStorage.username}`, this.user_profile)
                    .then(response => {
                        toast({
                            message: 'Form saved',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        // this.$router.push('/')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property} : ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data));
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again');
                            console.log(JSON.stringify(error.response.data));
                        }
                    })
            }
        }
    }
}
</script>