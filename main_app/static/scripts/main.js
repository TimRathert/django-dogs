$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  
$(".dropdown").click(function (event) {
  $(this).toggleClass("is-active");
});

$(".infotext1").click(function (event) {
  if (!document.querySelector('.infotext1').classList.contains("is-active1")){
    $(this).toggleClass("is-active1");
    $(".infotext1").css({
        opacity: '1',
    });
    $(".slideshow1").css({
      height: '80px'
    })
    $('.infotext-def1').css({
      opacity: '1',
      color: 'whitesmoke'
    })
  }
  else{
    $(this).toggleClass("is-active1");
    $(".infotext1").css({
        opacity: '1',
    });
    $(".slideshow1").css({
      height: '0px'
    })
    $('.infotext-def1').css({
      opacity: '.1',
    })
  }});


$(".infotext2").click(function (event) {
  if (!document.querySelector('.infotext2').classList.contains("is-active2")){
    $(this).toggleClass("is-active2");
    $(".infotext2").css({
        opacity: '1',
    });
    $(".slideshow2").css({
      height: '650px'
    })
    $('.infotext-def2').css({
      opacity: '1',
      color: 'whitesmoke'
    })
  }
  else{
    $(this).toggleClass("is-active2");
    $(".infotext2").css({
        opacity: '1',
    });
    $(".slideshow2").css({
      height: '0px'
    })
    $('.infotext-def2').css({
      opacity: '.1',
    })
  }
});