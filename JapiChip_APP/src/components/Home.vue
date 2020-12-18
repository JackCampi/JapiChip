<template>
    <div id="home">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
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
                    <div class="expiration-item" v-for="expiration in expirations" :key="expiration.doc_name">
                        <div class="exp-name">
                            {{expiration.doc_name}}
                        </div>
                        <div class="exp-date" v-bind:style="{color: getColor()}">
                            {{expiration.exp_date}}
                        </div>
                    </div>
                </div>
            </div>
            <div class="documents">
                <h1>Your Docs...</h1>
                <div class="docs-container">
                    <div v-for="expiration in expirations" :key="expiration.doc_name" class="document">
                        <div class="doc-image">
                            <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" class="bi bi-file-earmark-text" viewBox="0 0 16 16">
  <path d="M4 0h5.5v1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h1V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2z"/>
  <path d="M9.5 3V0L14 4.5h-3A1.5 1.5 0 0 1 9.5 3z"/>
  <path fill-rule="evenodd" d="M5 11.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5zm0-2a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0-2a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
</svg>
                            <div class="docs-buttons">
                                <button class="l-button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-arrow-down-fill" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2zm2.354 6.854l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 1 1 .708-.708L7.5 9.293V5.5a.5.5 0 0 1 1 0v3.793l1.146-1.147a.5.5 0 0 1 .708.708z"/>
</svg></button>
                                <button class="r-button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cursor-fill" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M14.082 2.182a.5.5 0 0 1 .103.557L8.528 15.467a.5.5 0 0 1-.917-.007L5.57 10.694.803 8.652a.5.5 0 0 1-.006-.916l12.728-5.657a.5.5 0 0 1 .556.103z"/>
</svg></button>
                            </div>
                        </div>
                        <div class="document-tag">{{expiration.doc_name}}</div>
                    </div>
                </div>
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
    },
    methods: {
        getColor(){
            //var toDate = Date.parseDate(date, "d-m-Y")
            //var curDate = Date.

            return "black"
        }
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
    /*background-color: blue;*/
}
.modules{
    width: 100%;
    height: 15vh;
    display: flex;
    justify-content: center;
    /*background-color: brown;*/
}
.modules a{
    color: #A3CB38;
}
.body{
    width: 100%;
    height: 50vh;
    display: flex;
    justify-content: space-around;
    /*background-color: aquamarine;*/
}
.expiration{
    background-color: #f6ffde;
    border-radius: 20px;
    padding: 20px;
    height: 45vh;
    width: 40%;
}
.expiration-item{
    /*background-color: azure;*/
    margin-bottom: 10px;
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.exp-name, .exp-date{
    /*background-color: aquamarine;*/
    font-size: 12pt;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1; /* number of lines to show */
    -webkit-box-orient: vertical;
}

.documents{
    /*background-color: chocolate;*/
    height: 45vh;
    width: 40%;
}
.docs-container{
    /*background-color: fuchsia;*/
    display: flex;
    flex-wrap: wrap;
}
.document{
    width: 15vh;
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    /*background-color: chartreuse;*/
}
.document-tag{
    font-size: 8pt;
    overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 2; /* number of lines to show */
   -webkit-box-orient: vertical;
   text-align: center;
}
.doc-image{
    background-color: #f6ffde;
    margin-bottom: 10px;
    height: 15vh;
    width: 15vh;
    padding: 7px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
}
.docs-buttons{
    width: 100%;
    margin-top: 20%;
    display: flex;
    justify-content: flex-end;

}
/*.docs-buttons button{
    background-color: azure;
    border: 1px solid black;
    border-radius: 10px;
}
.docs-buttons button:hover{
    border: 0px solid #e5e7e9;
  }*/
.r-button{
    background-color: #f6ffde;
    border: 0px solid black;
    /*border: 1px solid black;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;*/
}
.l-button{
    background-color: #f6ffde;
    border: 0px solid black;
    /*border: 1px solid black;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;*/
}
.r-button:hover{
    background-color: #f6ffde;
    border: 0px solid black;
    /*border: 1px solid black;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;*/
}
.l-button:hover{
    background-color: #f6ffde;
    border: 0px solid black;
    /*border: 1px solid black;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;*/
}
.l-button:focus{
    outline: 0;
}
.r-button:focus{
    outline: 0;
}
div.vertical-line{ 
    margin-right: 15px;
    margin-left: 15px;
    width: 1px; /* Line width */ 
    background-color: lightgrey; /* Line color */ 
    height: 100%; /* Override in-line if you want specific height. */ 
    float: left; /* Causes the line to float to left of content. You can instead use position:absolute or display:inline-block if this fits better with your design */ 
}

</style>