#!/usr/bin/env node
// script that writes a string to a file.

const fs = require('fs');

// get file_path
const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
