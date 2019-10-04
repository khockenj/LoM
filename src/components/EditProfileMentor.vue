  <template>
  <span>
  <b-row>
    <b-col lg="12" style="text-align:left;"><h2>Mentor Stuff</h2></b-col>
    </b-row>
  <b-row>
    <b-col lg="2" style="text-align:left;"><label for="aboutme">Your Bio:</label></b-col>
    <b-col><b-form-textarea
        id="aboutme"
        rows="5"
        placeholder="Hello I'm K3Vx and I once solo killed Faker..."
      ></b-form-textarea>
      </b-col>
  </b-row>
  <b-row class="py-2">
    <b-col lg="2" style="text-align:left;"><label for="aboutme">Your Achievements:</label></b-col>
    <b-col><b-form-textarea
        id="aboutme"
        rows="5"
        placeholder="Dabbed on Uzi(please seperate by comma),
Beat Doublelift in arm wrestling"
      ></b-form-textarea>
      </b-col>
  </b-row>
  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourreview">Review Types:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourreview"
        v-model="selectedReview"
        :options="reviewOptions"
        name="yourreview"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>

  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourmoney">Free/Paid:</label></b-col>
    <b-col style="text-align:left;">
      <b-form-checkbox-group
        id="yourmoney"
        v-model="selectedMoney"
        :options="moneyOptions"
        name="yourmoney"
      ></b-form-checkbox-group>
    </b-col>
  </b-row>

  <b-row>
  <b-col lg="2" style="text-align:left;"><label for="yourreq">Requirements:</label></b-col>
    <b-col style="text-align:left;">
      [placeholder]
    </b-col>
  </b-row>
  </span>
  </template>

<script>
export default {
  name: 'EditProfileMentor',
  props: ['selectedMoney', 'selectedReview', 'aboutMe', 'achievements'],
  data() {
      return {
        reviewOptions: [
		  { value: 'live', text: 'Live' },
          { value: 'private', text: 'Private' },
          { value: 'written', text: 'Written' },
	      ],
      	moneyOptions: [
		 { value: 'free', text: 'Free' },
          { value: 'paid', text: 'Paid' },
          ],
      }
  }
}
</script>

<style scoped>
label {
  font-size:17px!important;
}
</style>
