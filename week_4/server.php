<?php
header("Access-Control-Allow-Origin: *");
if (isset($_GET["pesan"])) {
    echo "reply: ".$_GET["pesan"];
};

?>