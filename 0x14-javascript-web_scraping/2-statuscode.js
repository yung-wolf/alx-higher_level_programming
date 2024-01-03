#!/usr/bin/env node
// script that display the status code of a GET request.

const request = require('request');

// get URL
const args = process.argv.slice(2);
const url = args[0];

// make GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
