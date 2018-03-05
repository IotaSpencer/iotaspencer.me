---
---

$(window).scroll(function () {
  if ($(document).scrollTop() > 50) {
    $('nav').addClass('shrink');
  } else {
    $('nav').removeClass('shrink');


  }
});

$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function () {
  $('#projects-dropdown').hover(function () {
    $('.dropdown-toggle').dropdown("toggle")
  }, function () {
    $('.dropdown-toggle').dropdown("toggle")
  })
});