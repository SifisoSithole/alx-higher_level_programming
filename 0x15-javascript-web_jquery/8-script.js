$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      const lst = $('UL#list_movies');
      for (let i in data.results) {
        lst.append($('<li></li>').append(data.results[i].title));
      }
    }
  });
});
