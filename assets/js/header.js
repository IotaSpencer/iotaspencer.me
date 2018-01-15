---
---
$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav').addClass('shrink');
  } else {
    $('nav').removeClass('shrink');
    $('div.wrapper').css('top', 120);

  }
});

$(document).ready(function() {
  $('[data-toggle="tooltip"]').tooltip();
  $('div.wrapper').css('top', 120);

});