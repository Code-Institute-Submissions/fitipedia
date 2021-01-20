$(document).ready(function(){
    // displays return to top button
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
    }

    // takes user back to top of page when button is clicked
    function backToTop() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

    // initialises navbar for mobile and tablet devices
    $('.sidenav').sidenav();

    // makes flashed messages disappear from the screen after 4 seconds
    $('#flashed_messages').fadeOut(4000);

    // displays text to the user when hovering over an element with the tooltipped class
    $('.tooltipped').tooltip();

    // generates a pop-up box for the user when they click on the modal trigger
    $('.modal').modal();

    // prevents input of two consecutive whitespaces in textarea and input fields
    $("#term_definition").on("keydown", function (e) {
        var inputValue = $("#term_definition").val();
        if (inputValue.length == 0 || inputValue.slice(-1) == " ") {
            return e.which !== 32;
        }
    });
    $("input").on("keydown", function (e) {
        var inputValue = $("input").val();
        if (inputValue.length == 0 || inputValue.slice(-1) == " ") {
            return e.which !== 32;
        }
    });
});

// clears the search bar without refreshing the page
function resetSearch() {
    document.getElementById("search_bar").reset();
}

// flashes an upvote alert to the user that fades out after 2.5 seconds
function confirmUpvote() {
    var upvoteAlert = document.querySelector('.upvote-container');

    upvoteAlert.innerHTML += `
        <div class="upvote-alert">Upvoted!</div>
    `;
    $('.upvote-alert').fadeOut(2500);
}

// flashes a downvote alert to the user that fades out after 2.5 seconds
function confirmDownvote() {
    var downvoteAlert = document.querySelector('.downvote-container');

    downvoteAlert.innerHTML += `
        <div class="downvote-alert">Downvoted!</div>
    `;
    $('.downvote-alert').fadeOut(2500);
}