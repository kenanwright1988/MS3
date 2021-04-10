// Materialize CSS Jquery to enable sidenav, tabs, formSelect and modal. From Materialize docs.
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    M.updateTextFields();            
});