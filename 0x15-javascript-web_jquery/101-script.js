$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
    $('li').remove('li:last-child');
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
