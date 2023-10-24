#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const filmData = JSON.parse(body);
    const wedgeAntillesFilms = filmData.results.filter(film => {
      return film.characters.some((character) => character === 'https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(wedgeAntillesFilms.length);
  }
});
