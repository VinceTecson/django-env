function openPopup(event) {
  event.preventDefault(); // Prevent the default action
  var background = document.getElementById("background");
  var popup = document.getElementById("sub_button");
  background.style.display = "block";
  popup.style.display = "block";
}
