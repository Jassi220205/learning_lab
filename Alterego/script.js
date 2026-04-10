// =============================
// 1. Form Submission Handler
// =============================
document.getElementById("decisionForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const data = {
        task: document.querySelector('[name="task"]').value.trim(),
        deadline: parseInt(document.querySelector('[name="deadline"]').value),
        effort: parseInt(document.querySelector('[name="effort"]').value),
        shortReward: parseInt(document.querySelector('[name="shortReward"]').value),
        longReward: parseInt(document.querySelector('[name="longReward"]').value),
        energy: parseInt(document.querySelector('[name="energy"]').value)
    };

    if (!validate(data)) {
        alert("Invalid input");
        return;
    }

    // Store data
    localStorage.setItem("decisionData", JSON.stringify(data));

    // Redirect
    window.location.href = "results.html";
});


// =============================
// 2. Validation Function
// =============================
function validate(data) {
    if (!data.task) return false;

    if (data.deadline <= 0 || isNaN(data.deadline)) return false;

    if (data.effort < 1 || data.effort > 10) return false;

    if (data.shortReward < 1 || data.shortReward > 10) return false;

    if (data.longReward < 1 || data.longReward > 10) return false;

    if (data.energy < 1 || data.energy > 10) return false;

    return true;
}


// =============================
// 3. Persona Definitions
// =============================
const personas = {
    disciplined: { short: 1, long: 5, effort: 3, deadline: 4 },
    impulsive: { short: 5, long: 1, effort: 2, deadline: 1 },
    future: { short: 1, long: 6, effort: 2, deadline: 5 },
    balanced: { short: 3, long: 3, effort: 3, deadline: 3 }
};


// =============================
// 4. Scoring Function
// =============================
function calculateScore(data, weights) {

    // Normalize deadline impact (closer deadline = higher pressure)
    const deadlinePressure = 10 - Math.min(data.deadline, 10);

    return (
        (weights.short * data.shortReward) +
        (weights.long * data.longReward) -
        (weights.effort * data.effort) -
        (weights.deadline * deadlinePressure)
    );
}


// =============================
// 5. Decision Logic
// =============================
function getDecision(score, energy) {

    if (score > 50 && energy > 5) {
        return "Do it now";
    } 
    else if (score > 20) {
        return "Plan and start soon";
    } 
    else if (score > 0) {
        return "Delay slightly";
    } 
    else {
        return "Avoid for now";
    }
}


// =============================
// 6. Main Processing Function
// =============================
function processDecision(data) {

    const results = [];

    for (let key in personas) {

        const score = calculateScore(data, personas[key]);

        const decision = getDecision(score, data.energy);

        results.push({
            persona: key,
            decision: decision,
            score: Math.round(score)
        });
    }

    displayResults(results);
}


// =============================
// 7. DOM Rendering
// =============================
function displayResults(results) {

    const container = document.getElementById("results");

    container.innerHTML = ""; // clear previous results

    results.forEach(r => {

        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <h2>${capitalize(r.persona)}</h2>
            <p>${r.decision}</p>
            <span>Score: ${r.score}</span>
        `;

        container.appendChild(card);
    });
}


// =============================
// 8. Utility Function
// =============================
function capitalize(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
}

function toggleTheme() {
    document.body.classList.toggle("alt-theme");
}