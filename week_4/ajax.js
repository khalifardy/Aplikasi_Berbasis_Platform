$(document).ready(function () {
  $("#shoutbutton").click(function () {
    $.ajax({
      type: "GET", //change to "POST" for POST request
      url: "http://localhost:8000/server.php",
      data: $("#form1").serialize(),
      success: function (rsp) {
        $("#data").append("<div>" + rsp + "</div>");
      },
      error: function (rsp) {
        alert(rsp);
      },
    });
  });
});
