/* NiceScroll */
$(document).ready(
  function() {
    $("html").niceScroll({
      mousescrollstep: 75
    });
  }
);

$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 0) {
    $('.btn-call-modal').fadeIn();
  } else {
    $('.btn-call-modal').fadeOut();
  }
});

$('img').tooltip();

$(function () {
    $("#img-cover-timeline").mouseenter(function () {
      $("#timeline-change-cover").stop().fadeIn();
    });
});

$(function () {
    $("#img-cover-timeline").mouseleave(function () {
      $("#timeline-change-cover").stop().fadeOut();
    });
});
