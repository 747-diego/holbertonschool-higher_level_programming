#!/usr/bin/node
// Write a Javascript script that fetches and lists all movies title
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (Fetching) {
  for (const Movie of Fetching.results) {
    $('UL#list_movies').append('<li>' + Movie.title + '</li>');
  }
});
