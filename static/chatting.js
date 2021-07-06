$(function() {
    // When we're using HTTPS, use WSS too.
    var  me= $('#msg_from').text()
//    Pusher.logToConsole = true;
    var event = me;
    var pusher = new Pusher('fe20237c51fe22bd59b7', {
      cluster: 'ap2'
    });

    channel = pusher.subscribe('my-channel');
    channel.bind(event, function(data) {
//
//        var data =JSON.stringify(data.text);
        var data = JSON.parse(data.text);
//        var data =JSON.stringify(data);
//
        var chat = $("#chatp")
        var chatp = $('<div class="chat"></div>')
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

    });
//     alert(data);


//    chatsock.onmessage = function(message) {
//        var data = JSON.parse(message.data);
//        var chat = $("#chatp")
//        var chatp = $('<div class="chat"></div>')
//        if (data.m_f_id!=me){
//            var ele = $('<div class="mess"></div>')
//            ele.append(
//                $("<b></b>").text(data.msg_from)
//            )
//            ele.append(
//                $("<p></p>").text(data.msg)
//            )
//            ele.append(
//                $('<span class="time-right"></span>').text(data.time)
//            )
//            ele.append(
//                $('<div class="sp"></div>')
//            )
//
//            chatp.append(ele)
//            chat.append(chatp)
//        }
//        else{
//            var el = $('<div class="sp"></div>')
//            var ele = $('<div class="mess  darker"></div>')
//            ele.append(
//                $("<p></p>").text(data.msg)
//            )
//
//            ele.append(
//                $('<span class="time-right"></span>').text(data.time)
//            )
//
//            chatp.append(el)
//            chatp.append(ele)
//            chat.append(chatp)
//        }
//
//    };

//    $("#chatform").on("submit", function(event) {
//
//        const xhttp = new XMLHttpRequest();
//
//        xhttp.open("POST", "/demo1/");
//        xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
//        xhttp.setRequestHeader('X-CSRFToken', "{{csrf_token}}");
//        var message = {
//            msg_from: $('#msg_from').text(),
//            msg_to : $('#msf_to').text(),
//            msg: $('#msg').val(),
//        };
//        xhttp.onreadystatechange = function() { // Call a function when the state changes.
//            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
//            // Request finished. Do processing here.
//                xhttp.onload = function() {
//                    $("#msg").val('').focus();
//                }
//            }
//        }
//        var data = JSON.stringify({ "name": "nim", "email": "email.value" });
//        xhttp.send(JSON.stringify(data));
//
//
////        $("#msg").val('').focus();
////        return false;
//    });
});