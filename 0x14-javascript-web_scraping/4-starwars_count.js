#!/usr/bin/node
// script that prints the number of movies where the
// character “Wedge Antilles” is present.

const request = require('request');

// get URL
const args = process.argv.slice(2);
const url = args[0];
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // get links to characters
  if (response.statusCode === 200) {
    const glossary = JSON.parse(body);

    // run thru result == movie list
    for (let j = 0; j < glossary.results.length; j++) {
      const chars = glossary.results[j].characters;
      for (let i = 0; i < glossary.results[j].characters.length; i++) {
        // use link to find character ID
        if (chars[i] === wedge) {
          count++;
        }
      }
    }
    // print count === number of movies with wedge in it
    console.log(count);
  }
});
