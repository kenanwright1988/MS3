//Code from https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(".add_field_button").click(function () {
    $(".ingredients_list").append('<div class="row"><div class="input-field col s6 offset-s6"><input type="text" name="ing_name"/><label class="black-text" for="ing_name">Ingredient Name</label><i id="remove_field" class="btn fas fa-minus red"></i></div></div></div>');
});

$(document).on('click', '#remove_field', function () {
    $(this).parent('div').remove();
});