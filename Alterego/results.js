// =====================
// Theme Load
// =====================
const toggle = document.getElementById("themeSwitch");

if (localStorage.getItem("theme") === "alt") {
    document.body.classList.add("alt-theme");
    toggle.checked = true;
}

toggle.addEventListener("change", () => {
    document.body.classList.toggle("alt-theme");

    localStorage.setItem(
        "theme",
        document.body.classList.contains("alt-theme") ? "alt" : "default"
    );
});


// =====================
// Load Input Data
// =====================
const rawData = JSON.parse(localStorage.getItem("decisionData"));

if (!rawData) {
    alert("No data found. Go back and submit the form.");
    window.location.href = "index.html";
}


// =====================
// Process Data (from data.js)
// =====================
const data = buildFinalData(rawData);

// ... (previous code for Theme Load and Processing Data)

// =====================
// Render Results (REPLACE THIS SECTION)
// =====================
const container = document.getElementById("results");
container.innerHTML = "";

data.results.forEach(r => {
    const card = document.createElement("div");
    card.className = "card";

    // Dynamic color based on decision
    const decisionColor = r.decision === "Avoid" ? "#ff4d4d" : "#4dff88";

    card.innerHTML = `
        <h2>${r.persona.toUpperCase()}</h2>
        <p style="color: ${decisionColor}">${r.decision}</p>
        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 10px 0;">
        <span>Score: <strong>${r.score}</strong></span>
    `;

    container.appendChild(card);
});


// =====================
// XML (Console Demo)
// =====================
const xml = generateXML(data);
console.log("XML Output:", xml);


