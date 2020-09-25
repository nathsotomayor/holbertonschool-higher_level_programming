$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  dataType: 'text',
  success: function (data) {
    $('div#character').text(JSON.parse(data).name);
  }
});
