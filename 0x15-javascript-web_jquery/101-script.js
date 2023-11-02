/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    if ($('ul.my_list li').length > 0) {
      $('ul.my_list li').last().remove();
    }
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
