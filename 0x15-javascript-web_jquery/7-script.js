#!/usr/bin/node
// Write a Javascript script that fetches and replaces
// the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (Fetching) {
  $('DIV#character').text(Fetching.name);
});
