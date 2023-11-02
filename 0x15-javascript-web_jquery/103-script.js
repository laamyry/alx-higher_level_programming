/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  }
});
