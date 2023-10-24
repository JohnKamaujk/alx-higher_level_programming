#!/usr/bin/node
const request = require('request');

// Check if the url is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_count.js <url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const filmData = JSON.parse(body);
    const wedgeAntillesFilms = filmData.results.filter(film => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(wedgeAntillesFilms.length);
  }
});
