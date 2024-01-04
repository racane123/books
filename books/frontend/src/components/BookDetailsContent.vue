<template>
  <div class="data-display">
    <h1>Data Display</h1>

    <div v-if="books.length > 0">
      <ul>
        <li v-for="book in books" :key="book.id">
          <!-- Display book information here -->
          <p><strong>Title:</strong> {{ book.title }}</p>
          <p><strong>Summary:</strong> {{ book.summary }}</p>
          <p><strong>Published Date:</strong> {{ book.published_date }}</p>

          <p>{{ book.genre.genre_name }}</p>

          <!-- Add more fields as needed -->
        </li>
      </ul>
    </div>

    <div v-else>
      <p>No books available.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/books/')
      .then(response => {
        console.log('Books data:', response.data);
        this.books = response.data;
      })
      .catch(error => {
        console.error('Error fetching books', error);
      });
  },
};
</script>

<style scoped>
.data-display {
  max-width: 600px;
  margin: 20px auto;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 10px;
}

/* Add more styles as needed */
</style>
