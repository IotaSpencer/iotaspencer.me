$(document).ready(function(){
  var element = $('#gnupg-key');
  $.get("/assets/files/gnupg.asc", function(data) {
    element.text(data);
  });
});
