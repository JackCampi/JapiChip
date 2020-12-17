<template class="background">
  <div id="register">
    <h1>JapiChip</h1>
      <div class="row">
        <div class="imput_from">
          <!-- Company fields -->
          <div class="column">
            <!-- Company column1 -->
            <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="bi bi-building" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M14.763.075A.5.5 0 0 1 15 .5v15a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5V14h-1v1.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V10a.5.5 0 0 1 .342-.474L6 7.64V4.5a.5.5 0 0 1 .276-.447l8-4a.5.5 0 0 1 .487.022zM6 8.694L1 10.36V15h5V8.694zM7 15h2v-1.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 .5.5V15h2V1.309l-7 3.5V15z"/>
              <path d="M2 11h1v1H2v-1zm2 0h1v1H4v-1zm-2 2h1v1H2v-1zm2 0h1v1H4v-1zm4-4h1v1H8V9zm2 0h1v1h-1V9zm-2 2h1v1H8v-1zm2 0h1v1h-1v-1zm2-2h1v1h-1V9zm0 2h1v1h-1v-1zM8 7h1v1H8V7zm2 0h1v1h-1V7zm2 0h1v1h-1V7zM8 5h1v1H8V5zm2 0h1v1h-1V5zm2 0h1v1h-1V5zm0-2h1v1h-1V3z"/>
            </svg>
            <h2>Company</h2>
            <div class="input_field">
              <label for="comp_type">Company type <span v-show="!this.comp_type" style="color:red"> *</span></label>
              <input type="text" id="comp_type" name="comp_type" v-model="comp_type" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="comp_country">Country<span v-show="!this.comp_country" style="color:red"> *</span></label>
              <input type="text" id="comp_country" name="comp_country" v-model="comp_country" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="comp_tel">Tel.<span v-show="!this.comp_tel" style="color:red"> *</span></label>
              <input type="text" id="comp_tel" name="comp_tel" v-model="comp_tel" maxlength="10"/>
            </div>
            
          </div>
          <div class="column">
            <!-- Company column2 -->
            <div class="input_field">
              <label for="comp_name">Name<span v-show="!this.comp_name" style="color:red"> *</span></label>
              <input type="text" id="comp_name" name="comp_name" v-model="comp_name" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="comp_id">ID<span v-show="!this.comp_id" style="color:red"> *</span></label>
              <input type="number" id="comp_id" name="comp_id" v-model="comp_id" maxlength="10"/>
            </div>
            <div class="input_field">
              <label for="comp_id_type">ID Type<span v-show="!this.comp_id_type" style="color:red"> *</span></label>
              <input type="text" id="comp_id_type" name="comp_id_type" v-model="comp_id_type" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="comp_city">City<span v-show="!this.comp_city" style="color:red"> *</span></label>
              <input type="text" id="comp_city" name="comp_city" v-model="comp_city" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="comp_address">Address<span v-show="!this.comp_address" style="color:red"> *</span></label>
              <input type="text" id="comp_address" name="comp_address" v-model="comp_address" maxlength="50"/>
            </div>
          </div>
          <div class="input_field2">
              <label for="comp_email">Contact email<span v-show="!this.comp_email" style="color:red"> *</span></label>
              <input type="email" id="comp_email" name="comp_email" style="width:100%" v-model="comp_email" maxlength="50"/>
          </div>
        </div>
        <!-- User fields -->
        <div class="imput_from">
          <!-- User column1 -->
          <div class="column">
            <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg>
            <h2>User</h2>
            <div class="input_field">
              <label for="user_email">Email<span v-show="!this.user_email" style="color:red"> *</span></label>
              <input type="email" id="user_email" name="user_email" v-model="user_email" maxlength="50"/>
            </div>
          </div>
          <!-- User column2 -->
          <div class="column">
            <div class="input_field">
              <label for="user_name">Name<span v-show="!this.user_name" style="color:red"> *</span></label>
              <input type="text" id="user_name" name="user_name" v-model="user_name" maxlength="50"/>
            </div>
            <div class="input_field">
              <label for="user_lastname">Lastname<span v-show="!this.user_lastname" style="color:red"> *</span></label>
              <input type="text" id="user_lastname" name="user_lastname" v-model="user_lastname" maxlength="50"/>
            </div>
            
            <div class="input_field">
              <label for="user_tel">Tel.<span v-show="!this.user_tel" style="color:red"> *</span></label>
              <input type="text" id="user_tel" name="user_tel" v-model="user_tel" maxlength="10"/>
            </div>
          </div>
          <div class="input_field2">
              <label for="user_password">Password<span v-show="!this.user_password" style="color:red"> *</span></label>
              <input type="password" id="user_password" name="user_password" style="width:100%" v-model="user_password"/>
          </div>
          <div class="input_field2">
              <label for="user_password_confirm">Comfirm password<span v-show="!this.user_password_confirm" style="color:red"> *</span></label>
              <input type="password" id="user_password_confirm" name="user_password_confirm" style="width:100%" v-model="user_password_confirm"/>
          </div>

        </div>
      </div>
      <button v-on:click="submit_forms">Start now</button>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      comp_id: null,
      comp_id_type: null,
      comp_name: null,
      comp_type: null,
      comp_city: null,
      comp_country: null,
      comp_tel: null,
      comp_address: null,
      comp_email: null,

      user_name: null,
      user_lastname: null,
      user_email: null,
      user_tel: null,
      user_password: null,
      user_password_confirm: null

    };
  },
  methods: {
    submit_forms(){
      if (this.comp_id  != null && this.comp_id_type  != null && this.comp_name  != null && this.comp_type  != null &&
      this.comp_city  != null && this.comp_country  != null && this.comp_tel  != null && this.comp_address  != null &&
      this.comp_email  != null && this.user_name  != null && this.user_lastname  != null && this.user_email  != null &&
      this.user_tel  != null && this.user_password  != null && this.user_password_confirm != null){
        let company_dic = {
        comp_id : this.comp_id,
        comp_id_type : this.comp_id_type,
        comp_name : this.comp_name,
        comp_type : this.comp_type,
        comp_address : this.comp_address,
        comp_country : this.comp_country,
        comp_city : this.comp_city,
        comp_phone : this.comp_tel,
        comp_email : this.comp_email
        }
        let user_dic = {
          user_name: this.user_name,
          user_last_name: this.user_lastname,
          user_email: this.user_email,
          user_password: this.user_password,
          user_role: "Admin",
          comp_id : this.comp_id
        }

        axios.post('localhost:8000/new_company/', company_dic)
          .then((response) => {
            alert(response)
          }).catch((error) => {alert(error)})
        axios.post('localhost:8000/new_user/', user_dic)
          .then((response) => {
            alert(response)
          }).catch((error) => {alert(error)})
      } else {
        alert("Faltan campos por llenar.")
      }
    }
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');

#register {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #a3cb38;
}


.row {
  align-items: center;
}

.row label {
  vertical-align: middle;
  display: flex;
  text-align: left;
  font-size: 13px;
}

.imput_from {
  border-radius: 20px;
  margin: 0 40px 40px 40px;
  padding: 30px;
  background-color: #ecf0f1;
  display: inline-block;
  flex-direction: row;
}

.column {
  display: inline-block;
  margin: 10px 10px 0px 20px;
  
}
.input_field {
  display: flex;
  margin: 20px 0;
  width: 15vw;
  flex-direction: column;
}

.input_field2 {
  margin: 0px 20px 20px 20px;
}

h1 {
  color:#ecf0f1;
}

.button0 {
  background-color: #eeeeee;
  border-radius: 10px;
  border: none;
  color: rgb(36, 59, 32);
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button0 :focus{
  outline: 0px;
}
.button0:hover {
  background-color: #cacaca;
  color:  rgb(62, 104, 55);
}

</style>
