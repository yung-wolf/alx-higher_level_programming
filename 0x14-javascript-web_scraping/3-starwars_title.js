#!/usr/bin/env node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');

// movie id
const args = process.argv.slice(2);
const movieId = args[0];

// get URL
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  // Convert response (str) to object
  if (response.statusCode === 200) {
    const glossary = JSON.parse(body);
    console.log(glossary.title);
  }
});
