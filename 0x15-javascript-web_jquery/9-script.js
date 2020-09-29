$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('div#hello').text(data.hello);
    }
  });
});
