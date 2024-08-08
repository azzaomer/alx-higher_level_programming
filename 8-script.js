$(document).ready(function(){
    // Fetch the list of movies from the API
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        // Iterate through each film in the results array
        data.results.forEach(function(film) {
            // Append each film title as a list item to UL#list_movies
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        });
    });
});