


// function that popup for adding new units.
function add_new_units() {
    document.getElementById("add_unit_form").style.display = "block";
}

function close_box() {
    document.getElementById("add_unit_form").style.display = "none";
}


// function update popup box.

function update(unitId) {
    document.getElementById('unit_id').value = unitId;
    document.getElementById('update_unit_form').style.display = 'block';
}

function close_box_update() {
    document.getElementById('update_unit_form').style.display = 'none';
}


// function for pricing popup.

document.addEventListener('DOMContentLoaded', function () {
    const showFormButton = document.getElementById('showFormButton');
    const popupBackground = document.getElementById('popupBackground');
    const popup = document.getElementById('pricingPopup');
    const closeButton = document.querySelector('.close');

    showFormButton.addEventListener('click', function () {
        popup.style.display = 'block';
        popupBackground.style.display = 'block';
    });

    closeButton.addEventListener('click', function () {
        popup.style.display = 'none';
        popupBackground.style.display = 'none';
    });

    popupBackground.addEventListener('click', function () {
        popup.style.display = 'none';
        popupBackground.style.display = 'none';
    });
});


//function for pricing popup update.

