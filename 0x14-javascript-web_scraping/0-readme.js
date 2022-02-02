#!/usr/bin/node

const fs = require('fs')
const file_names = process.argv[2];

fs.readFile(file_names, 'utf8', function (err, line) {
    if (err)
    {
        console.log(err);
    }
    else
    {
        console.log(line);
    }
});