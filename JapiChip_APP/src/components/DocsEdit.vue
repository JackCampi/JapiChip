<template>
<div class="mt-5">
        <b-container fluid>
        <h1>Edit Your Document</h1>
    <b-col sm="10">
        <b-row class="my-1">
            <b-col sm="3">
                <label for="input-name">Document Name:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input id="input-name" type="text" v-model= "Name"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="3">
                <label for="input-ed">Experiration Date:</label>
            </b-col>
            <b-col sm="9">
                <b-form-datepicker id="input-ed" v-model= "ExpirationDate" class="mb-2"> </b-form-datepicker>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="3">
                <label for="input-ec">Creation Date:</label>
            </b-col>
            <b-col sm="9">
                <b-form-datepicker id="input-ec" type="date" v-model= "CreationDate" class="mb-2"></b-form-datepicker>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="3">
                <label for="type">Type:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input id="type" type="text" v-model= "Type"></b-form-input>
            </b-col>
        </b-row>
    </b-col>
    <b-col sm="5">
                <b-embed
                    type="iframe"
                    aspect="16by9"
                    src="http://www.agirregabiria.net/g/sylvainaitor/principito.pdf"
                    allowfullscreen
                ></b-embed>
        <b-row class="my-1">
            <b-form-group label="Update:" label-for="file-default" label-cols-sm="2">
                <b-form-file id="file-default"></b-form-file>
            </b-form-group>
        </b-row>
    </b-col>    
    </b-container>
</div>
</template>

<script>
  export default {
    data() {
      return {
        types: [
            'Name',
            'ExpirationDate',
            'CreationDate',
            'Type'
        ]
      }
    }
  }
</script>
  

