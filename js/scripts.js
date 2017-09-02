$(document).ready(function () {
    // mobile nav trigger
    $('#mobile-menu').click(function (e) {
        if ($('#sidebar').css('display') == 'none'){
            $('.pushed').css("padding-left", "200px");
        }
        else {
            $('.pushed').css("padding-left", "0px");
        };
        $('#sidebar').animate({width:'toggle'},250);
        e.preventDefault();
    });

    // sidebar active item
    $('#sidebar').on('click', '.item', function() {
        if(!$(this).hasClass('dropdown')) {
            $(this).addClass('active')
            .siblings('.item')
            .removeClass('active');
      };
      // If an item is clicked on mobile then hide the sidebar menu
      if($('#mobile-menu').is(':visible'))
        {
            $("#sidebar").toggle(200);
            $('.pushed').css("padding-left", "0px");
        };
    });
    
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
    
    // To enable Semantic Modules
    $('.ui.dropdown').dropdown();
    
});

