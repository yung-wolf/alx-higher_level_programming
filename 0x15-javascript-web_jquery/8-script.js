$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    const movieList = $('#list_movies');
    movieList.empty();
    $.each(data.results, function (index, movie) {
      movieList.append('<li>' + movie.title + '</li>');
    });
  },
  error: function (error) {
    console.error('Error getting movie list', error);
  }
});
