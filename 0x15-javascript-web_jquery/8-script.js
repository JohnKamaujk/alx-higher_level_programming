$.get('https://swapi.co/api/films/?format=json', function (data) {
  const listMovies = $('UL#list_movies');
  data.results.forEach(function (movie) {
    listMovies.append(`<li>${movie.title}</li>`);
  });
});
