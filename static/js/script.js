$(document).ready(function(){
    var bttt = document.getElementById("returnToTop");
            
    window.onscroll = function() {
        showButton();
    };

    function showButton() {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            bttt.style.display = "block";
        } else {
            bttt.style.display = "none";
        }
    };

    function backToTop() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    };

    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "mmm-dd, yyyy",
        yearRange: 3,
        maxDate: +0,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('.preloader-wrapper').fadeOut('slow');
    $('.modal').modal()
});