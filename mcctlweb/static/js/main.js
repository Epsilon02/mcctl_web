$(document).ready(function () {
    var start = $("#start");
    var stop = $("#stop");
    var restart = $("#restart");

    var output = $("#output");

    stop.click(function () {
        start.attr("disabled", true).removeClass("active");
        stop.attr("disabled", true).removeClass("active");
        restart.attr("disabled", true);
        $.ajax({
            url: "/stop", success: function (result) {
                console.log(result);
                start.attr("disabled", false);
                stop.addClass("active");
                output.append(result.key);
            }
        });
    });

    restart.click(function () {
        start.attr("disabled", true).removeClass("active");
        stop.attr("disabled", true).removeClass("active");
        restart.attr("disabled", true).addClass("active");
        $.ajax({
            url: "/restart", success: function (result) {
                console.log(result);
                stop.attr("disabled", false);
                restart.attr("disabled", false);
                start.addClass("active");
                restart.attr("disabled", false).removeClass("active");
                output.empty();
            }
        });
    });

    start.click(function () {
        start.attr("disabled", true).removeClass("active");
        stop.attr("disabled", true).removeClass("active");
        restart.attr("disabled", true);
        output.empty();
        $.ajax({
            url: "/start", success: function (result) {
                console.log(result);
                stop.attr("disabled", false);
                restart.attr("disabled", false);
                start.addClass("active");
                output.text(result.key + "\n");
            }
        });
    });
});