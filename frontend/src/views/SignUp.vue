<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="username" name="username" class="input" v-model="username">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="firstname" name="firstname" class="input" v-model="firstname">
                        </div>
                    </div>
                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="lastname" name="lastname" class="input" v-model="lastname">
                        </div>
                    </div> -->
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="errors">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default{
        name:'SignUp',
        data(){
            return{
                username: '',
                /*firstname:'',
                lastname:'',*/
                email : '',
                password1 : '',
                password2 : '',
                errors : [],
            }
        },
        methods: {
            async submitForm() {
                
                this.errors = []
                if(this.username === ''){
                    this.errors.push("The username is missing")
                }
                
                /*
                if(this.firstname === ''){
                    this.errors.push("The firstname is missing")
                }

                if(this.lastname === ''){
                    this.errors.push("The lastname is missing")
                }*/

                if(this.email === ''){
                    this.errors.push("The email is missing")
                }

                if(this.password1.length < 5 ){
                    this.errors.push("The password is too short")
                }

                if(this.password1 !== this.password2){
                    this.errors.push("The passwords are not matching")
                }

                //console.log(!this.errors.length)

                if(!this.errors.length){

                    this.$store.commit('setIsLoading', true)

                    const formData = {
                        username: this.username,
                        //first: this.firstname,
                        //last: this.lastname,
                        email: this.email,
                        password: this.password1,
                    }
                    
                    await axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'Account was created, please log in',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })

                    .catch(error =>{
                        if (error.response){
                            for(const property in error.response.data){
                                this.errors.push('Response Error: Something went wrong. Please try again. Maybe your password is too weak.')
                            }
                        } else if (error.message) {
                            this.errors.push("Something went wrong. Please try again.")
                        }
                    })

                    this.$store.commit('setIsLoading', false)
                }

            }
        }
    }
</script>