//Code taken but modified https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
let step = 1;
let ing = 1;

$(".add_field_button").click(function () {
    ing++;
    $(".ingredients_list").append('<div class="input-field col s12 "><input id="ing_name' + ing + '" type="text" name="ing_name"/><label class="white-text" for="ing_name' + ing + '">Ingredient ' + ing + '</label><i id="remove_field" class="btn fas fa-minus red right"></i></div></div>');

});

$(".add_step_button").click(function () {
    step++;
    $(".step_list").append('<div class="input-field col s12 "><input type="text" name="steps"/><label class="white-text" for="steps">Step ' + step + '</label><i id="remove_step" class="btn fas fa-minus red right"></i></div></div>');
    
});

$(document).on('click', '#remove_step', function () {
    $(this).parent('div').remove();
    step--;
});

$(document).on('click', '#remove_field', function () {
    $(this).parent('div').remove();
    ing--;
});

