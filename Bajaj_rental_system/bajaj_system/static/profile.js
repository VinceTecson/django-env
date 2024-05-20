document.addEventListener('DOMContentLoaded', function() {
  // Get the button and the rental history popup
  var showHistoryBtn = document.getElementById('showHistoryBtn');
  var rentalHistory = document.getElementById('rental_History');
  
  // Add event listener to the button
  showHistoryBtn.addEventListener('click', function() {
      // Display the rental history popup
      rentalHistory.style.display = 'block';
  });
  
  // Add event listener to the close button in the popup
  var closeButton = rentalHistory.querySelector('.close');
  closeButton.addEventListener('click', function() {
      // Hide the rental history popup when the close button is clicked
      rentalHistory.style.display = 'none';
  });
});



function openClose() {
  document.getElementById("background").style.display = "block";
  document.getElementById("sub_button").style.display = "block";
}

function closeOpen() {
  document.getElementById("background").style.display = "none";
  document.getElementById("sub_button").style.display = "none";
}




