/* NiceScroll */
$(document).ready(
  function() {
    $("html").niceScroll({
      mousescrollstep: 75
    });
  }
);

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
