$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    const fullUrl = url + $.param({ lang: languageCode });
    $.get(fullUrl, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
