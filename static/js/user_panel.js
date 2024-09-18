document.addEventListener("DOMContentLoaded", function () {
  const panelOptions = document.querySelectorAll(".Panel_Options li span");
  const panelContents = document.querySelectorAll(".Panel_Contents > div");
  const logoutOption = document.querySelector(".Panel_Options li span.logout"); // Assuming the logout option has a class of "logout"

  panelOptions.forEach((option) => {
    option.addEventListener("click", function () {
      if (option !== logoutOption) {
        // Remove active class from all options
        panelOptions.forEach((opt) => {
          opt.classList.remove("active");
        });

        // Add active class to the clicked option
        option.classList.add("active");

        // Show the corresponding panel content
        panelContents.forEach((content, index) => {
          if (index === Array.from(panelOptions).indexOf(option)) {
            content.style.display = "block";
          } else {
            content.style.display = "none";
          }
        });
      }
    });
  });

  logoutOption.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default behavior
    event.stopPropagation(); // Prevent event from bubbling up
    // Perform logout operation
    window.location.href = "/logout"; // Replace with your logout URL or function
  });
});

function togglePassword(elem, id) {
  var x = document.getElementById(id);
  if (x.type === "password") {
    x.type = "text";
    elem.classList.replace("fa-eye-slash", "fa-eye");
  } else {
    x.type = "password";
    elem.classList.replace("fa-eye", "fa-eye-slash");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const accountSection = document.querySelector(".Account_Form");
  accountSection.classList.add("active");
});