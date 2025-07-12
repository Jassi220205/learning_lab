let timerDisplay = document.getElementById("timer");
let startBtn = document.getElementById("startBtn");
let stopBtn = document.getElementById("stopBtn");
let resetBtn = document.getElementById("resetBtn");
let customBtn = document.getElementById("customBtn");
let modeToggle = document.getElementById("modeToggle");

let defaultDuration = 25 * 60;
let duration = defaultDuration;
let timer;
let running = false;

function updateDisplay(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  timerDisplay.textContent = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
}

startBtn.addEventListener("click", () => {
  if (!running) {
    running = true;
    timer = setInterval(() => {
      if (duration > 0) {
        duration--;
        updateDisplay(duration);
      } else {
        clearInterval(timer);
        running = false;
        alert("Time's up! 🐾");
      }
    }, 1000);
  }
});

stopBtn.addEventListener("click", () => {
  clearInterval(timer);
  running = false;
});

resetBtn.addEventListener("click", () => {
  clearInterval(timer);
  running = false;
  duration = defaultDuration;
  updateDisplay(duration);
});

customBtn.addEventListener("click", () => {
  let customMin = prompt("Enter custom duration in minutes:", "25");
  if (customMin && !isNaN(customMin) && customMin > 0) {
    clearInterval(timer);
    running = false;
    defaultDuration = customMin * 60;
    duration = defaultDuration;
    updateDisplay(duration);
  } else {
    alert("Please enter a valid number greater than 0.");
  }
});

modeToggle.addEventListener("change", () => {
  document.body.classList.toggle("dark-mode");
});

updateDisplay(duration);
