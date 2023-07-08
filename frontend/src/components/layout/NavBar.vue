<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Nico CRM</strong>
            </router-link>
            <div class="navbar-item">
                <figure class=" image is-32x32 navbar-logo">
                    <img src="../../assets/logo.png">
                </figure>
            </div>
            <template v-if="$store.state.isAuthenticated">
                <div class="navbar-item">Welcome {{ $store.state.user.username }}</div>
            </template>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                <router-link to="/dashboard/team" class="navbar-item">Team</router-link>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Log In</router-link>
                        </template>

                        <template v-else>
                            <router-link to="/dashboard/my-account" class="button is-info">My Account</router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>

    </nav>
</template>

<script>
    export default{
        name: 'NavBar'
    }
</script>