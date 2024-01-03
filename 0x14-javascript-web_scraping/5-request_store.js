#!/usr/bin/env node
// script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response

const request = require('request');
const fs = require('fs');

// get URL and file path from args
const args = process.argv.slice(2);
const url = args[0];
const filePath = args[1];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(response.statusCode);
  }
});
