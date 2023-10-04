// Use jQuery to make an AJAX GET request
        $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
            // Extract the array from the response data
            const films = data.results;

            // Select the HTML ul element
            const listElement = $('#list_movies');

            // Loop through each film and add its title to the list
            $.each(films, function(index, film) {
                listElement.append('<li>' + film.title + '</li>');
            });
        });
