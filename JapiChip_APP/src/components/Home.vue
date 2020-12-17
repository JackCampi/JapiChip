<template>
    <div id="home">
        <div class="welcome">
            <h1>Welcome to JapiChip, <span>{{username}}</span></h1>
            
        </div>
        <div class="modules">
            <a href="https://www.w3schools.com/">Module 1</a>
            <div class="vertical-line" style="height: 3vh;" />
            <a href="https://www.w3schools.com/">Module 2</a>
            <div class="vertical-line" style="height: 3vh;" />
            <a href="https://www.w3schools.com/">Module 3</a>
            <div class="vertical-line" style="height: 3vh;" />
            <a href="https://www.w3schools.com/">Module 4</a>
        </div>
        <div class="body">
            <div class="expiration">
                <h1>Next Expirations</h1>
                <div class="expiration-container">
                    <!--<h2>expiration</h2>
                    <h2>expiration</h2>
                    <h2>expiration</h2>-->
                    <h2 v-for="expiration in expirations" :key="expiration.doc_name">
                        {{expiration.doc_name}}, {{expiration.exp_date}}
                    </h2>
                </div>
            </div>
            <div class="documents">
                <h1>documentos</h1>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    //name: Home
    data: function(){
        return{
            username: "",
            expirations: [
                {'doc_name': 'doc 1', 'exp_date': '06-03-2002'},
                {'doc_name': 'doc 2', 'exp_date': '06-03-2002'}
            ]
        }
    },
    created: function(){
        this.email = this.$route.params.email
        let self = this
        //this.username = this.email
        axios.get("http://127.0.0.1:8000/user/" + this.email)
        .then((result) =>{
            self.username = result.data.username
            
        })
        .catch((error) => {
            alert(error)
            //console.log(error)
        });

        axios.get("http://127.0.0.1:8000/docs/" + this.email)
        .then(result => {

            let expiration_list = []
            let items = result.data.items
            for(var i = 0; i < items.length ; i++){

                expiration_list.push({'doc_name': items[i]['doc_name'], 'exp_date': items[i]['exp_date']})

            }

            self.expirations = expiration_list

        })
        .catch(error => {
            alert(error)
            //console.log(error)
        })
    }
}
</script>

<style>
/*@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');*/
body{
    height: 80vh;
    width: 100%;
    /*font-family: 'Open Sans', sans-serif;*/
}
.welcome{
    width: 100%;
    height: 15vh;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    background-color: blue;
}
.modules{
    width: 100%;
    height: 15vh;
    display: flex;
    justify-content: center;
    background-color: brown;
}
.body{
    width: 100%;
    height: 50vh;
    display: flex;
    justify-content: space-around;
    background-color: aquamarine;
}
.expiration{
    background-color: blueviolet;
    border-radius: 20px;
    padding: 10px 10px 10px 10px;
    height: 45vh;
    width: 40%;
}
.expiration-container{
    background-color: darkgoldenrod;
}
.documents{
    background-color: chocolate;
    height: 45vh;
    width: 40%;
}
div.vertical-line{ 
    margin-right: 15px;
    margin-left: 15px;
    width: 1px; /* Line width */ 
    background-color: black; /* Line color */ 
    height: 100%; /* Override in-line if you want specific height. */ 
    float: left; /* Causes the line to float to left of content. You can instead use position:absolute or display:inline-block if this fits better with your design */ 
}

</style>