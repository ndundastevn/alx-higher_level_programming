// Use jQuery to add a click event listener to the div with id "add_item"
        $('#add_item').click(function() {
            // Create a new <li> element with the text "Item"
            const newItem = $('<li>Item</li>');
            
            // Add the new <li> element 
	$('ul.my_list').append(newItem);
