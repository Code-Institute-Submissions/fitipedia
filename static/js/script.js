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
    $('#flashed_messages').fadeOut(2000);
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

function confirmUpvote() {
    var upvoteAlert = document.querySelector('.upvote-container');

    upvoteAlert.innerHTML += `
        <div class="upvote-alert">Upvoted!</div>
    `;
    $('.upvote-alert').fadeOut(2500);
}

function confirmDownvote() {
    var downvoteAlert = document.querySelector('.downvote-container');

    downvoteAlert.innerHTML += `
        <div class="downvote-alert">Downvoted!</div>
    `;
    $('.downvote-alert').fadeOut(2500);
}