// error message popup display.
function displayPopup() {
    var new_background = document.getElementById('new_background');
    var message_error = document.getElementById('errorMessage');
    new_background.style.display = 'block'; 
    message_error.style.display = 'block'; 
}

function closePopup() {
    var new_background = document.getElementById('new_background');
    var message_error = document.getElementById('errorMessage');
    new_background.style.display = 'none';
    message_error.style.display = 'none'; 
}

window.onload = function() {
    displayPopup();
};
