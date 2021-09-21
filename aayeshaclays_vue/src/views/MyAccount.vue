<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Profile</h1>
            </div>

            <hr>

            <div class="column is-12">
                <h3 class="is-size-4 mb-6">User #{{ user_profile.id }}</h3>
                
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name</label>
                            <div class="control">
                                <input type="text" class="input" v-model.lazy="user_profile.first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="user_profile.last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail</label>
                            <div class="control">
                                <input type="email" class="input" v-model="user_profile.email">
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
                                <input type="text" class="input" v-model="account.birth_date">
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
                                <input type="text" class="input" v-model="account.zip_code">
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
                                <input type="text" class="input" v-model="account.country">
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    
</template>

<script>
import axios from 'axios';
import UserProfile from '@/components/UserProfile.vue'

export default {
    name: 'MyAccount',
    components: {
        UserProfile
    },
    data() {
        return {
            user_profile: Object,
            account: Object
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
        }
    },
}
</script>