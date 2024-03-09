document.getElementById("alignBtn").addEventListener("click", function () {
  var box = document.getElementById("box");
  box.style.textAlign =
    box.style.textAlign === "right" || box.style.textAlign === "center"
      ? "left"
      : "center";
});

document.getElementById("colorBtn").addEventListener("click", function () {
  var box = document.getElementById("box");
  box.style.backgroundColor =
    box.style.backgroundColor === "rgb(255, 165, 0)" ||
    box.style.backgroundColor == "orange"
      ? "#f0f0f0"
      : "orange";
});
