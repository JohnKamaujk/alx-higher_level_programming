#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    const charactersInOrder = [];

    function fetchCharacterName (characterUrl) {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          charactersInOrder.push(characterData.name);

          if (charactersInOrder.length === characterUrls.length) {
            // All character names fetched, print them in order
            charactersInOrder.forEach((name) => {
              console.log(name);
            });
          }
        }
      });
    }

    // Start fetching character names in order
    characterUrls.forEach((characterUrl) => {
      fetchCharacterName(characterUrl);
    });
  }
});
