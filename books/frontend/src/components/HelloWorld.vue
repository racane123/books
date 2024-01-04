<template>
  <form @submit.prevent="saveBook" style="max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <div style="margin-bottom: 15px;">
      <label for="title" style="display: block; font-weight: bold; margin-bottom: 5px;">Title:</label>
      <input id="title" v-model="book.title" type="text" style="width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;">
    </div>
    <div style="margin-bottom: 15px;">
      <label for="summary" style="display: block; font-weight: bold; margin-bottom: 5px;">Summary:</label>
      <textarea id="summary" v-model="book.summary" style="width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;"></textarea>
    </div>
    <div style="margin-bottom: 15px;">
      <label for="published_date" style="display: block; font-weight: bold; margin-bottom: 5px;">Published Date:</label>
      <input id="published_date" v-model="book.published_date" type="date" style="width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;">
    </div>
    <div style="margin-bottom: 15px;">
      <label for="genres" style="display: block; font-weight: bold; margin-bottom: 5px;">Genres:</label>
      <select id="genres" v-model="selectedGenres" multiple style="width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;">
        <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{ genre.genre_name }}</option>
      </select>
    </div>
    <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer;">Save</button>
  </form>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {
        title: '',
        summary: '',
        published_date: '',
      },
      selectedGenres: [],
      genres: [],
    };
  },
  mounted() {
    // Fetch genres from the API and populate the genres array
    axios.get('http://127.0.0.1:8000/api/genres/')
      .then(response => {
        this.genres = response.data;
      })
      .catch(error => {
        console.error('Error fetching genres', error);
      });
  },
  methods: {
    saveBook() {
      // Send the selected genres along with book data to the backend to save the book
      const data = {
        ...this.book,
        genre: this.selectedGenres,
      };
      axios.post('http://127.0.0.1:8000/api/books/', data)
        .then(response => {
          console.log('Book saved', response.data);
        })
        .catch(error => {
          console.error('Error saving book', error);
        });
    },
  },
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
