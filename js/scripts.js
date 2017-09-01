$(document).ready(function () {
    // smooth scrolling
    $("a[href^='#']").on('click', function(e) {
       var hash = this.hash;
       $('html, body').animate({
        scrollTop: $(hash).offset().top
         }, 800, function(){
           window.location.hash = hash;
         });
        e.preventDefault();
    });
    // sidebar active item
    $('#sidebar').on('click', '.item', function() {
        if(!$(this).hasClass('dropdown')) {
            $(this).addClass('active')
            .siblings('.item')
            .removeClass('active');
      }
    });
    
    $('.ui.dropdown').dropdown();
    
    $('#news')
    .visibility({
    transition : 'fade in',
    duration   : 1000
    });
});

