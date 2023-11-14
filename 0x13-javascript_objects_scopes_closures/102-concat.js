#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2], 'utf8'); // Specify 'utf8' encoding
const sArg = fs.readFileSync(process.argv[3], 'utf8'); // Specify 'utf8' encoding
fs.writeFileSync(process.argv[4], fArg + sArg);
