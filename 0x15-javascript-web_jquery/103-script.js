$('document').ready(function () {
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        fetchTranslation();
      }
    });
  });
});

function fetchTranslation () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const languageCode = $('INPUT#language_code').val();
  const fullUrl = url + $.param({ lang: languageCode });
  $.get(fullUrl, function (data) {
    $('DIV#hello').html(data.hello);
  });
}
