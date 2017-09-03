$(document).ready(function () {
    // mobile nav trigger
    $('#mobile-menu').click(function (e) {
        $('#sidebar').transition('fade right');
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
            $('#sidebar').transition('fade right');
        };
    });
    
    // smooth scrolling
    $("a[href^='#']").on('click', function(e) {
       var hash = this.hash;
       $('html, body').animate({
        scrollTop: $(hash).offset().top
         }, 700, function(){
           window.location.hash = hash;
         });
        e.preventDefault();
    });
    
    // To enable Semantic Modules
    $('.ui.dropdown').dropdown();
    
    // Animations
    $('#splash-logo').transition('fade in', '3s');
    
    
    $('#sidebar').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#sidebar a').transition('fade down in', '2s');
        }
    });
    // animations for sections
    $('#news').visibility({
        once       : true,
        continuous : false,
        onBottomVisible : function(calculations) {
        $('#news .card').transition('fade up in', '1.5s');
        }
    });
    
    /*
    $('#about').visibility({
        once       : true,
        continuous : false,
        onPassing  : function(calculations) {
        $('#about .container').transition('fade right in', '1.5s');
        }
    });
    */
    
    $('#resources').visibility({
        once       : true,
        continuous : false,
        onBottomVisible  : function(calculations) {
        $('#resources .button').transition('fade up in', '1.5s');
        }
    });
    
    $('#team').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#team .cards').transition('fade up in', '3s');
        }
    });
    
    /*
    $('#contact').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#contact #map').transition('fade right in', '1.5s');
        }
    });
    */
    
});

