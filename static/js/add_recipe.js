//Code taken but modified from https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery to add and remove input fields

//variables to keep track of how many ingredients and steps
let step = 1;
let ing = 1;

// Adds another input field when you click the + button to ingredient name section of form
$(".add_field_button").click(function () {
    ing++;
    $(".ingredients_list").append('<div class="input-field col s12 "><input id="ing_name' + ing + '" type="text" name="ing_name"/><label class="white-text" for="ing_name' + ing + '">Ingredient ' + ing + '</label><i id="remove_field" class="btn fas fa-minus red right"></i></div></div>');
});

// Adds another input field when you click the + button to step name section of form
$(".add_step_button").click(function () {
    step++;
    $(".step_list").append('<div class="input-field col s12 "><input type="text" name="steps"/><label class="white-text" for="steps">Step ' + step + '</label><i id="remove_step" class="btn fas fa-minus red right"></i></div></div>');   
});

// Removes a step input when clicking the - button
$(document).on('click', '#remove_step', function () {
    $(this).parent('div').remove();
    step--;
});

// Removes an ingredient input when clicking the - button
$(document).on('click', '#remove_field', function () {
    $(this).parent('div').remove();
    ing--;
});