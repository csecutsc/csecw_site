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
    $('#splash-logo').transition('fade in', '3s');
    
    
    $('#sidebar').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#sidebar a').transition('slide down in', '2s');
        }
    });
    // animations for sections
    $('#news').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#news .container').transition('fade right in', '1.5s');
        $('#news .card').transition('fade in', '3s');
        }
    });
    
    $('#about').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#about .container').transition('fade right in', '1.5s');
        }
    });
    
    $('#resources').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#resources .container').transition('fade right in', '1.5s');
        }
    });
    
    $('#team').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#team .container').transition('fade right in', '1.5s');
        }
    });
    
    $('#contact').visibility({
        once       : true,
        continuous : false,
        onTopVisible  : function(calculations) {
        $('#contact .container').transition('fade right in', '1.5s');
        }
    });
    
});

