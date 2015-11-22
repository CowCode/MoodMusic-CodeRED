import "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"

function respondify(){
  $('iframe[src*="embed.spotify.com"]').each( function() {
    $(this).css('width',$(this).parent(1).css('width'));
    $(this).attr('src',$(this).attr('src'));
  });
}

$(document).ready(function(){
  respondify();
});
$(window).resize(function() {
  respondify();
});