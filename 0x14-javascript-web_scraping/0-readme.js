#!/usr/bin/node
// reads a file. The first argument is the file path
// The content of the file must be read in utf-8

const fs = require('fs');

// file_path
const args = process.argv.slice(2);
const filePath = args[0];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data.trim());
});
