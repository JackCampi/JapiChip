<template>
  <div id="app">
    <div class="header">
      <div class="name">
        <h1>JapiChip</h1>
        <h2>La comercializadora</h2>
      </div>
      <!--<h1>LA COMERCIALIZADORA</h1>-->
      <nav>
        <button v-on:click="init"> Home </button>
        <button > Docs </button>
        <button > Contact Us </button>
        <button >Log Out</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view></router-view>
    </div>
    <div class="footer">
      <h2>JapiChip 2020 ©</h2>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'App',

    components: {},

    data: function(){
      return {
        is_auth: localStorage.getItem('isAuth') || false
      }
    },

    methods: {

      init: function(){
        if(this.$route.name != "root"){
          let username = localStorage.getItem("current_username")
          this.$router.push({name: "", params:{ username: username }})
        }
      },

    },

    beforeCreate: function(){

    }
  }
</script>

<!--<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
  body{
    margin: 0 0 0 0;
    font-family: 'Open Sans', sans-serif;
  }
  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;

    background-color: #A3CB38;
    color:#E5E7E9  ;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header h1{
    width: 20%;
    text-align: center;
  }
  .header nav {
    height: 100%;
    width: 45%;

    display: flex;
    justify-content: space-around;
    align-items: center;

    font-size: 20px;
  }
  .header nav button{
    color: #A3CB38;
    background: #E5E7E9;
    border: 1px solid #A3CB38;
    border-radius: 5px;
    padding: 10px 20px;
  }
  .header nav button:hover{
    color: #A3CB38;
    background: #A2CB38;
    border: 1px solid #E5E7E9;
  }
  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;
    background: #FDFEFE ;
  }
  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: #A3CB38;
    color: #E5E7E9;
  }
  .footer h2{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>-->
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
  body{
    margin: 0;
    padding: 0;
    height: 100vh;
    width: 100%;
    font-family: 'Open Sans', sans-serif;
  }
  .header{
    /*margin: 0%;
    padding: 0 0 0 0;*/
    width: 100%;
    height: 12vh;
    /*min-height: 100 px;*/
    background-color: #A3CB38;
    color: #e5e7e9;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  .name{
    align-items: center;
  }
  .name h1{
    width: 15%;
    font-size: 24pt;
    text-align: center;
  }
  .name h2{
    font-size: 15pt;
  }
  .header nav{
    height: 100%;
    width: 45%;

    display: flex;
    justify-content: flex-end;
    align-items: center;
    font-size: 20px;
  }
  .header nav button{
    color: #e5e7e9;
    background: #A3CB38;
    border: 0px solid #e5e7e9;
    border-radius: 5px;
    padding: 10px 20px;
  }
  .header nav button:hover{
    color: #A3CB38;
    background: #e5e7e9;
    border: 0px solid #e5e7e9;
  }
  .header nav button:focus{
    outline: 0;
  }
  .header button{
    color: #e5e7e9;
    background: #A3CB38;
    border: 0px solid #e5e7e9;
    border-radius: 5px;
    padding: 10px 20px;
  }
  .header button:hover{
    color: #A3CB38;
    background: #e5e7e9;
    border: 0px solid #e5e7e9;
  }
  .header button:focus{
    outline: 0;
  }
  .main-component{
    height: 80vh;
    margin: 0%;
    padding: 0%;
    background: #fdfefe;
  }
  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 8vh;
    /*min-height: 100px;*/
    background-color: #A3CB38;
    color: #e5e7e9;
  }
  .footer h2{
    width: 100%;
    height: 100%;
    font-size: 15pt;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
