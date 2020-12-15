<template>
  <div id="app">
    <div class="header">

      <h1>JAPICHIP</h1>
      <h1>LA COMERCIALIZADORA</h1>
      <nav>
        <button > Home </button>
        <button > Documents </button>
        <button > Contact Us </button>
        <button >Log Out</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view></router-view>
    </div>
    <div class="footer">
      <h2>@JAPICHIP 2020 MISIONTIC</h2>
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

<style>
  body{
    margin: 0 0 0 0;
  }
  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;

    background-color: #1D7905;
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
    color: #1D7905;
    background: #E5E7E9;
    border: 1px solid #1D7905;
    border-radius: 5px;
    padding: 10px 20px;
  }
  .header nav button:hover{
    color: #1D7905;
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
    background-color: #1D7905;
    color: #E5E7E9;
  }
  .footer h2{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
