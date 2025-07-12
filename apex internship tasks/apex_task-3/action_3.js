function getJoke() {
  fetch("https://official-joke-api.appspot.com/random_joke")
    .then((response) => response.json())
    .then((data) => {
      const jokeElement = document.getElementById("joke");
      jokeElement.innerHTML = `${data.setup}<br><strong>${data.punchline}</strong>`;
    })
    .catch((error) => {
      document.getElementById("joke").innerText = "Oops! Something went wrong.";
      console.error("Error fetching joke:", error);
    });
}
