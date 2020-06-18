$( document ).ready(function() {

$('.add-table-row').click(function() {
  $('.editable-row').addClass('toggle-row-none');
  $('.showtable-row').removeClass('toggle-row-none');
  $('.input-row').toggleClass('toggle-row-none')
  $('.add-table-row').addClass('toggle-row-none')
});

$('.canceltable-newrow').click(function() {
    $('.input-row').addClass('toggle-row-none')
    $('.add-table-row').removeClass('toggle-row-none')
    
});

$('.edit-table-row').click(function() {
    $('.showtable-row').addClass('toggle-row-none');
    $('.editable-row').removeClass('toggle-row-none');
    $('.input-row').addClass('toggle-row-none')
    $('.add-table-row').removeClass('toggle-row-none')
});

$('.canceltable-row').click(function() {
    $('.showtable-row').removeClass('toggle-row-none');
    $('.editable-row').addClass('toggle-row-none');
    
});



});