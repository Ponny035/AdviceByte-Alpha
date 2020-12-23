<template>
<table class="table table-hover">
  <thead>
    <tr>
      <!-- ชื่อ col -->
      <!-- <th scope="col">*Colors*</th> 
      <th scope="col" colspan="2"> </th>
      <th scope="col">*Bookmark*</th> -->
    </tr>
  </thead>
  <!-- dashboard topic -->
  <tbody class="">
    <tr v-for="(item,i) in activities" :key="i" @click="redirect(item.Forum_ID)">
      <!-- color catagory -->
      <th scope="row">
        <!-- <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 32x32"><title>Placeholder</title><rect width="100%" height="100%" :fill="item.color"></rect><text x="50%" y="50%" :fill="item.color" dy=".3em">32x32</text></svg> -->
      </th>
      <td class="font-test3 text-left" colspan="2">{{item.Activity_Name}}</td>
      <!-- <td class="font-test3 text-left" colspan="2">{{ Title }}</td> -->
      <td></td>
    </tr> 
  </tbody>
  <!-- end -->
  
  
</table>  
</template>

<script>
import axios from 'axios';
export default {
  async mounted() {
    await this.getActivitiyList();
  },
  methods: {
    async getActivitiyList() {
      await axios.post('process.env.API_URI0/forum/forumList')
      .then(response => {
        if (response.status === 200) {
          return this.activities = response.data
        }
      })
      .catch(err => console.log(err));
    },
    redirect(id) {
      this.$router.push({ name: 'response', params: { id: id } });
    },
  },
  data() {
    return {
        activities:[
            {
              Forum_ID: '',
              Activity_Name: ''
            },              
        ]
    }
 }
}
</script>

<style>
.font-test3 { 
    font-family: Poppins;
    color: #37437e;
    font-size: 15px;
    font-weight: bold;

}

</style>