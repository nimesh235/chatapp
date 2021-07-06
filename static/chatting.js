$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var  me= $('#msg_from').text()
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname+ me);
    chatsock.debug = true;

    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var chat = $("#chatp")
        var chatp = $('<div class="chat"></div>')
        if (data.m_f_id!=me){
            var ele = $('<div class="mess"></div>')
            ele.append(
                $("<b></b>").text(data.msg_from)
            )
            ele.append(
                $("<p></p>").text(data.msg)
            )
            ele.append(
                $('<span class="time-right"></span>').text(data.time)
            )
            ele.append(
                $('<div class="sp"></div>')
            )

            chatp.append(ele)
            chat.append(chatp)
        }
        else{
            var el = $('<div class="sp"></div>')
            var ele = $('<div class="mess  darker"></div>')
            ele.append(
                $("<p></p>").text(data.msg)
            )

            ele.append(
                $('<span class="time-right"></span>').text(data.time)
            )

            chatp.append(el)
            chatp.append(ele)
            chat.append(chatp)
        }

    };

    $("#chatform").on("submit", function(event) {

        var message = {
            msg_from: $('#msg_from').text(),
            msg: $('#msg').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#msg").val('').focus();
        return false;
    });
});