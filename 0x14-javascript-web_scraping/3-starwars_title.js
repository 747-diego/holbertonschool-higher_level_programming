#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const GettingRequest = require('request');
const MovieID = process.argv[2];
const MovieURL = 'https://swapi-api.hbtn.io/api/films/' + MovieID;

GettingRequest(MovieURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
