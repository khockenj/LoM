<template>
  <div class="admin">
    <div class="overlay"></div>
    <b-card style="max-width:1000px;margin:auto;margin-top:2rem;" header-bg-variant="info" header-text-variant="light" border-variant="info">
         <template v-slot:header>
             <i class="fas fa-toolbox no-hover-header"></i>Administration
    </template>
        <b-row class='py-2'>
            <b-col>
                Update API Keys/Patch   <i
                class="fas fa-question-circle textIcon"
                id='popover'
              ></i>: 
              <b-popover target="popover" triggers="hover" placement="top">
    <template v-slot:title>Information</template>
    <b>PATCH:</b> Make sure it's the full patch number (eg. 10.3.1)
  </b-popover>
            </b-col>
        <b-col>
        <b-form-select v-model="keyToUpdate" class="mb-3" @change="keyToUpdate == 'PATCH' ? new_key = patch: new_key = null">
                  <template v-slot:first>
        <b-form-select-option :value="null" disabled>-- Choose a Key --</b-form-select-option>
      </template>
        <b-form-select-option v-for='k in keys' :key='k' :value="k">{{k}}</b-form-select-option>
        </b-form-select>
        </b-col>
        <b-col>
            <b-form-input :placeholder='keyToUpdate' v-if='keyToUpdate != null' type="input" v-model='new_key'></b-form-input>
            </b-col>
        <b-col>
            <b-button v-if='keyToUpdate != null && new_key' v-on:click="setKey" variant='success'><i class="fas fa-save textIcon"></i>Update Key</b-button>
        </b-col>
        </b-row>

        <b-row class='py-2'>
            <b-col>
            <b-button variant='primary' v-on:click='generateCode' block><i class="fas fa-key textIcon"></i>Generate Mentor Code</b-button>
        </b-col>
        <b-col>
            <b-form-input v-if='code' id='copyMe' v-on:click="copyPasta" class='pseudo-disabled' type='text' v-model='code' readonly></b-form-input>
            <b-tooltip :show.sync="show" target="copyMe" placement="top">
      Copied Code
    </b-tooltip>
        </b-col>
        </b-row>

    <b-row class='py-2'>
        <b-col>
        <b-button v-if='!loading' v-on:click="updateLists" variant='warning'><i class="fas fa-list textIcon"></i>Update Skin and Champion List</b-button>
        <i
                class="fas fa-question-circle textIcon"
                id='popover-champ'
              ></i>
              <b-popover target="popover-champ" triggers="hover" placement="top">
    <template v-slot:title>Information</template>
    Before you update this, please make sure the patch is up-to-date. Also, this only will update the lists - the square image for new champions and all splashes need to be downloaded manually for now :(
  </b-popover>
        <b-button v-if='loading' variant='danger' disabled><b-spinner small></b-spinner><span class="sr-only">Loading...</span></b-button>
        </b-col>
        </b-row>
    </b-card>
  </div>
</template>
<script>
import axios from "axios";
import router from "../router";
export default {
  name: "Admin",
  data() {
      return {
          loading: false,
          keys: null,
          keyToUpdate: null,
          new_key: null,
          code: null,
          codeType: 'mentor',
          show: false,
          patch: null
      }
  },
  methods: {
    redirect: function(p1) {
      console.log(p1);
      if (p1.loggedIn == false) {
        router.push({ name: "Login" });
      } else if(!p1.profileData.admin) {
        router.push({ name: "Dashboard" });
      }
    },
    makeToast(title, content, variant = null) {
      this.$bvToast.toast(content, {
        title: `${title}`,
        variant: variant,
        solid: true,
        toaster: "b-toaster-top-center"
      });
    },
      updateLists: function() {
        this.loading = true;
        this.makeToast("Updating", "This will take a few moments. You can leave the page :)", "warning");
        let path = "http://localhost:5000/api/getSkinList"
        axios
        .post(path, {
             did: this.$parent.$parent.profileData.did
        })
        .then(response => {
            console.log(response);
          if(response) {
            this.makeToast("Updated", "Champion and Skin List updated", "success");
            this.loading = false;
          }
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          this.loading = false;
          console.log(error);
        });
      },
      getKeys: function() {
        let path = "http://localhost:5000/api/changeAPIKeys"
        axios
        .post(path, {
             did: this.$parent.$parent.profileData.did,
             keyType: null
        })
        .then(response => {
            console.log(response);
            this.keys = response['data']['keys'];
            this.patch = response['data']['patch'];
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          console.log(error);
        });
      },

  setKey: function() {
        let path = "http://localhost:5000/api/changeAPIKeys"
        axios
        .post(path, {
             did: this.$parent.$parent.profileData.did,
             keyType: this.keyToUpdate,
             new_key: this.new_key
        })
        .then(response => {
            console.log(response);
            if(this.keyToUpdate == "PATCH") this.patch = this.new_key;
            this.keyToUpdate = null;
            this.new_key = null;
            this.makeToast("Updated", "Successfully Updated", "success")
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          console.log(error);
        });
      },
    generateCode: function() {
        let path = "http://localhost:5000/api/generateCode"
        axios
        .post(path, {
             did: this.$parent.$parent.profileData.did,
             codeType: this.codeType,
        })
        .then(response => {
            //this.codeType = null;
            this.makeToast("Updated", "Successfully Created Code", "success")
            this.code = response['data'];
        })
        .catch(error => {
          this.makeToast(
            "Error",
            "Err - there's been an error in the back. Try again or report it - thank you!",
            "danger"
          );
          console.log(error);
        });
    },
    copyPasta: function() {
        let copyText = document.getElementById("copyMe");
        copyText.select();
        copyText.setSelectionRange(0, 99999); 
        document.execCommand("copy");
        this.show = true;
        setTimeout(() => {this.show = false}, 3000);
    }
  },
  mounted: async function() {
        this.p = await this.$parent;
        await this.$parent;
        this.redirect(this.$parent.$parent);
        this.getKeys();
  }
};
</script>

<style scoped>
.overlay {
  background-color: rgba(0, 0, 0, 0.4) !important;
  background-image: url("/static/backgrounds/splash/Teemo_1.jpg");
  background-blend-mode: color;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0px;
  z-index: -1000;
}
.pseudo-disabled {
    background-color:rgba(0, 0, 255, 0.2) !important;
    color:#fff;
    cursor: pointer;
}
.card-header {
  font-size:2rem;
}
.no-hover-header, .no-hover-header:hover {
  cursor:default;
  color:inherit;
  padding-right:.5rem;
}
</style>

