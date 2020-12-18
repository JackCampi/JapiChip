<template>
    <section id="login">
        <div id="section_login_prin">
            <div id="section_login_seg">
                <div class="conteiner">
                    <h1>JAPICHIP</h1>
                    <div>
                        <form method="post" v-on:submit.prevent="processAuthUser">
                            <label for="email">Email</label>
                            <input v-model="user_in.user_email" type="email" id="email" class="inputs" name="email" /><br /><br />
                            <label for="password">Password</label>
                            <input v-model="user_in.user_password" type="password" id="password" class="inputs" name="password" /><br /><br />
                            <input type="submit" id="sumit" value="Sing in" />
                        </form>
                    </div>
                    <a id="sing_up" href="http://localhost:8080/Register">Sign up</a>
                </div>
            </div>
            <a id="login_contacts" href="/html/">Contact Us</a>
        </div>
    </section>

</template>

<script>
    import axios from 'axios';

    export default {
        data: function(){
            return {
                user_in: {
                    user_name: "",
                    user_last_name: "",
                    user_email: "",
                    user_password: "",
                    user_role: "",
                    comp_id : 0
                }
            }
        },

        methods: {
            processAuthUser: function(){
                var self = this
                axios.post("http://127.0.0.1:8000/user/auth/", self.user_in)
                    .then((result) => {
                        if (result.data.Authentication){
                            this.$router.push("home")
                        }else{
                            alert("Contraseña Erronea o correo erroneo"); 
                        }
                        
                    })
                    .catch((error) => {
                        
                        if (error.response.status == "404")
                            alert("ERROR 404: Usuario no encontrado.");
                        
                    });
            }
        }
    }  
</script>

<style>
    @font-face {
        font-family: "Lobster";
        src: url("../../static/fonts/Lobster-Regular.ttf");
    }

    @font-face {
        font-family: "Chivo";
        src: url("../../static/fonts/Chivo-Regular.ttf");
    }

    * {
        margin: 0;
        padding: 0;
        font-family: "Chivo";
    }

    #login {
        width: 100%;
        height: 80vh;
        display: flex;
        align-items: center;
        background-color: #A3CB38;
    }

    #section_login_prin {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 0 auto;
        position: relative;
    }

    #section_login_seg {
        display: flex;
        align-items: center;
        height: 60vh;
        width: 40%;
        text-align: center;
        border: 1px solid #666;
        box-shadow: 2px 2px 10px #666;
        background-color: #f5f3f3;
    }

    .conteiner {
        width: 100%;
        height: 37vh;
    }

    #section_login_seg h1 {
        margin-bottom: 30px;
        font-family: "Lobster", cursive;
        letter-spacing: 4px;
        font-size: 30px;
        text-shadow: 0px 0px 3px rgb(189, 188, 188);
        color: #25BEDB;
    }

    #email {
        margin-left: 33px;
    }

    #sumit {
        margin-bottom: 10px;
        padding: 3px;
        width: 30%;
        border: 1px solid black;
        background-color: #b2e4ee;
    }

    #sumit:hover {
        cursor: pointer;
        background-color: #25BEDB;
    }

    #sing_up {
        font-size: 10px;
    }

    #login_contacts {
        position: absolute;
        bottom: 0;
        right: 80px;
    }

    .inputs {
        width: 60%;
    }
</style>