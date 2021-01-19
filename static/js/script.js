$(document).ready(function(){
    window.scroll({
        top: 2500, 
        left: 0, 
        behavior: 'smooth'
    }); 

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

    function backToTop() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

    $('.sidenav').sidenav();
    $('#flashed_messages').fadeOut(4000);
    $('.tooltipped').tooltip();
    $('.modal').modal();
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

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

function resetSearch() {
    document.getElementById("search_bar").reset();
}

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