$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      $.each(data.results, function (i, movie) {
        $('ul#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
