document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent default submission

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();
  const errorMsg = document.getElementById('errorMsg');

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!name || !email || !message) {
    errorMsg.textContent = "Please fill in all fields.";
  } else if (!emailPattern.test(email)) {
    errorMsg.textContent = "Please enter a valid email address.";
  } else {
    errorMsg.textContent = "";
    alert("Form submitted successfully!");
    // Optionally reset the form:
    document.getElementById('contactForm').reset();
  }
});
