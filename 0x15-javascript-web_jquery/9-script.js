        $(document).ready(function() {
               $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
               const translation = data.hello;

                // Display the translation in the HTML div with id "hello"
                $('#hello').text(translation);
            });
        });
