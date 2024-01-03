#!/usr/bin/env node
// script that computes the number of tasks completed by user id.

const request = require('request');

// get URL from CLI
const args = process.argv.slice(2);
const url = args[0];
const records = {};
let count = 0;
let j = 0;

// make GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.length; i++) {
      // set usrId to check at the end if each group
      // userId == 1 ... userId == 2 (new group)
      const usrIdCheck = obj[j].userId;

      // check if newUserId
      if (obj[i].userId !== usrIdCheck && count > 0) {
        records[String(usrIdCheck)] = count;
        j = i;
        count = 0;
      }

      // if task completed, count it
      if (obj[i].completed === true) {
        count++;
      }

      // Add last entry to dict record
      if (i === (obj.length - 1)) {
        records[String(usrIdCheck)] = count;
      }
    }
    console.log(records);
  } else {
    console.log(response.statuscode);
  }
});
