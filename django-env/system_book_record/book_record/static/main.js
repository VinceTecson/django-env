// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

// pop-up function
function addCustomerModal() {
  const overlay = document.getElementById('overlay');
  overlay.style.display = 'flex';
}

document.getElementById('addCustomerBtn').addEventListener('click', addCustomerModal);

document.getElementById('closeModalBtn').addEventListener('click', function() {
  const overlay = document.getElementById('overlay');
  overlay.style.display = 'none';
});

document.getElementById('customerForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const overlay = document.getElementById('overlay');
  overlay.style.display = 'none';
});

// customer information 


