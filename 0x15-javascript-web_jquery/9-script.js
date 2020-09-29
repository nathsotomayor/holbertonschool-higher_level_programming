$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  dataType: 'text',
  success: function (data) {
    $('div#hello').text(JSON.parse(data).hello);
  }
});
