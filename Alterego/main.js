document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("decisionForm");
    const themeSwitch = document.getElementById("themeSwitch");

    // =============================
    // 1. Theme Toggle Logic
    // =============================
    if (localStorage.getItem("theme") === "alt") {
        document.body.classList.add("alt-theme");
        if (themeSwitch) themeSwitch.checked = true;
    }

    if (themeSwitch) {
        themeSwitch.addEventListener("change", () => {
            document.body.classList.toggle("alt-theme");
            localStorage.setItem(
                "theme",
                document.body.classList.contains("alt-theme") ? "alt" : "default"
            );
        });
    }

    // =============================
    // 2. Form Submission Logic
    // =============================
    if (form) {
        form.addEventListener("submit", function(e) {
            e.preventDefault();

            const data = {
                task: document.querySelector('[name="task"]').value.trim(),
                deadline: parseInt(document.querySelector('[name="deadline"]').value),
                effort: parseInt(document.querySelector('[name="effort"]').value),
                shortReward: parseInt(document.querySelector('[name="shortReward"]').value),
                longReward: parseInt(document.querySelector('[name="longReward"]').value),
                energy: parseInt(document.querySelector('[name="energy"]').value)
            };

            // Basic Validation
            if (!data.task || isNaN(data.deadline)) {
                alert("Please fill in all fields correctly.");
                return;
            }

            // Store for results page
            localStorage.setItem("decisionData", JSON.stringify(data));

            // Redirect
            window.location.href = "results.html";
        });
    }
});