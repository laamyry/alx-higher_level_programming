/* global $ */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      $('#list_movies').append($('<li>').text(movie.title));
    });
  });
});
