$(document).ready(function () {

    $('#controls').on('click', '#deal', function () {
        var bet = $('#bet-amount').val();
        console.log(bet);
        $.ajax({
            url: "/start_round",
            type: "post",
            data: { "bet": bet },
            success: function (game_data) {
                $("#dealer-cards div.card-placeholder").removeClass();
                $("#player-cards div.card-placeholder").removeClass();

                for (var i = 0; i < 2; i++) {
                    var card_id = game_data["dealer"]["hand"]["cards"][i];
                    $('#dealer-cards').append('<div class="card" id=' + card_id + '></div>');
                    $("#dealer-cards").children(":last-child")
                        .css("background-image", "url('static/images/cards/" + card_id + ".png')")
                        .css("background-size", "cover");
                }

                for (var i = 0; i < 2; i++) {
                    var card_id = game_data["player"]["hand"]["cards"][i];
                    $('#player-cards').append('<div class="card" id=' + card_id + '></div>');
                    $("#player-cards").children(":last-child")
                        .css("background-image", "url('static/images/cards/" + card_id + ".png')")
                        .css("background-size", "cover");
                }

                if (game_data["player"]["hand"]["soft"]) {
                    $("#player-total").text(game_data["player"]["hand"]["total"] + " soft");
                } else {
                    $("#player-total").text(game_data["player"]["hand"]["total"]);
                }
                $("#stake").text(game_data["pot"]);


                $("#chips").text(game_data["player"]["chips"]);
                for (var i = 0; i < game_data["messages"].length; i++) {
                    $("#messages").append(game_data["messages"][i] + "<br>");
                }
                $("#controls").empty();
                $("#controls").append('<button class="control_button" id="hit" name="hit">Hit</button>');
                $("#controls").append('<button class="control_button" id="stand" name="stand">Stand</button>');
            },

        });
    });

    $('#controls').on('click', '#hit', function () {
        var val = $(this).attr('name');
        $.ajax({
            url: "/hit",
            type: "post",
            data: { "input": val },
            success: function (game_data) {
                var new_card_id = game_data["player"]["hand"]["cards"][game_data["player"]["hand"]["cards"].length - 1];
                $('#player-cards').append('<div class="card" id=' + new_card_id + '></div>');
                $("#player-cards").children(":last-child")
                    .css("background-image", "url('static/images/cards/" + new_card_id + ".png')")
                    .css("background-size", "cover");

                $("#player-total").text(game_data["player"]["hand"]["total"]);
                $("#messages").text(game_data["messages"]);

                if (game_data["status"] == 5) {
                    $('#stand').click();
                }


            },
        });
    });

    $('#controls').on('click', '#stand', function () {
        var val = $(this).attr('name');
        $.ajax({
            url: "/stand",
            type: "post",
            data: { "input": val },
            success: function (game_data) {

                var hidden_card_id = game_data["dealer"]["hand"]["cards"][1];

                $("#dealer-cards").children(":last-child")
                    .css("background-image", "url('static/images/cards/" + hidden_card_id + ".png')")
                    .css("background-size", "cover");

                for (var i = 2; i < game_data["dealer"]["hand"]["cards"].length; i++) {
                    var card_id = game_data["dealer"]["hand"]["cards"][i];
                    setTimeout(function () {
                        $('#dealer-cards').append('<div class="card" id=' + card_id + '></div>');
                        $("#dealer-cards").children(":last-child")
                            .css("background-image", "url('static/images/cards/" + card_id + ".png')")
                            .css("background-size", "cover");
                    }, 500);
                }
                setTimeout(function () {
                    $("#dealer-total").text(game_data["dealer"]["hand"]["total"]);
                }, 500 * (game_data["dealer"]["hand"]["cards"].length - 2));


                $("#controls").empty();
                $("#controls").append('<form action="/" method="get"><button class="control_button" id="new-round" name="new-round">New Round</button></form>');
                $("#messages").text(game_data["messages"]);
            },
        });
    });
});

function test() {
    console.log("test");
}