//Code from https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
let step = 1;
let ing = 1;

$(".add_field_button").click(function () {
    $(".ingredients_list").append('<input id="ing_name' + ing + '" type="text" name="ing_name"/><label class="black-text" for="ing_name' + ing + '">Ingredient ' + ing + '</label><i id="remove_field" class="btn fas fa-minus red right"></i></div>');
    ing++;
});

$(".add_step_button").click(function () {
    $(".step_list").append('<input type="text" name="steps"/><label class="black-text" for="steps">Step ' + step + '</label><i id="remove_step" class="btn fas fa-minus red right"></i></div>');
    step++;
});

$(document).on('click', '#remove_step', function () {
    $(this).parent('div').remove();
    step--;
});

$(document).on('click', '#remove_field', function () {
    $(this).parent('div').remove();
    ing--;
});