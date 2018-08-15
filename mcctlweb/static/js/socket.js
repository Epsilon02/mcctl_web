$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var output = $("#output");
    var cmdline = $("#cmdline");

    socket.on('connect', function() {
        socket.send('Terminal connected!');
        });

    socket.on('message', function(msg) {
        output.append('[Send]: ' + msg + '\n');
    });

    $('#send-button').on('click', function() {
        socket.send(cmdline.val());
        cmdline.val('');
    });

    var terminalSocket = io.connect('http://' + document.domain + ':' + location.port + '/terminal');
    terminalSocket.on('terminal', function(terminalMsg) {
        output.append(terminalMsg);
    });
});