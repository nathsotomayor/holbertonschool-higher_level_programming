$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const language = $('input#language_code');
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/?lang=' + language.val(),
      method: 'GET',
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
