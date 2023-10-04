  // Use jQuery to make an AJAX GET request
        $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
            // Extract the character name from the response data
            const characterName = data.name;

            // Display the character name 
            $('#character').text(characterName);
        });
