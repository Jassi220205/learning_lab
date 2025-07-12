// script.js

function generateSgpaInputs() {
    const totalSem = document.getElementById("totalSem").value;
    const sgpaInputsDiv = document.getElementById("sgpaInputs");

    sgpaInputsDiv.innerHTML = ""; // Clear previous inputs

    for (let i = 1; i <= totalSem; i++) {
        const label = document.createElement("label");
        label.textContent = `SGPA for Semester ${i}:`;

        const input = document.createElement("input");
        input.type = "number";
        input.step = "0.01";
        input.min = "0";
        input.max = "10";
        input.id = `sgpa${i}`;

        sgpaInputsDiv.appendChild(label);
        sgpaInputsDiv.appendChild(input);
    }
}

function calculateCgpa() {
    const totalSem = parseInt(document.getElementById("totalSem").value);
    const prevCgpa = parseFloat(document.getElementById("prevCgpa").value) || 0;
    const targetCgpa = parseFloat(document.getElementById("targetCgpa").value) || null;

    let sumSgpa = 0;
    let countEntered = 0;

    for (let i = 1; i <= totalSem; i++) {
        const sgpaVal = parseFloat(document.getElementById(`sgpa${i}`).value);
        if (!isNaN(sgpaVal)) {
            sumSgpa += sgpaVal;
            countEntered++;
        }
    }

    let cgpa = 0;
    if (countEntered > 0) {
        if (prevCgpa > 0) {
            cgpa = (prevCgpa * (totalSem - countEntered) + sumSgpa) / totalSem;
        } else {
            cgpa = sumSgpa / countEntered;
        }
    }

    let resultText = `🌸 Current CGPA: <b>${cgpa.toFixed(2)}</b> 🌸`;

    if (targetCgpa && countEntered < totalSem) {
        const remainingSem = totalSem - countEntered;
        const requiredTotalPoints = targetCgpa * totalSem;
        const currentPoints = sumSgpa + (prevCgpa > 0 ? prevCgpa * (totalSem - countEntered) : 0);
        const neededPoints = requiredTotalPoints - currentPoints;
        const requiredSgpa = neededPoints / remainingSem;

        if (requiredSgpa > 10) {
            resultText += `<br>❌ You would need an impossible SGPA of ${requiredSgpa.toFixed(2)} to reach ${targetCgpa}.`;
        } else if (requiredSgpa < 0) {
            resultText += `<br>✅ You have already surpassed your target CGPA of ${targetCgpa}!`;
        } else {
            resultText += `<br>⭐ To reach ${targetCgpa}, aim for SGPA: <b>${requiredSgpa.toFixed(2)}</b> in the remaining ${remainingSem} semester(s).`;
        }
    }

    document.getElementById("result").innerHTML = resultText;
    document.getElementById("downloadBtn").style.display = "inline-block";
}

function resetForm() {
    document.getElementById("gpaForm").reset();
    document.getElementById("sgpaInputs").innerHTML = "";
    document.getElementById("result").innerHTML = "";
    document.getElementById("downloadBtn").style.display = "none";
}

function downloadPdf() {
    const resultElement = document.getElementById("result");
    const opt = {
        margin:       1,
        filename:     'GPA_Result.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(resultElement).save();
}

function toggleMode() {
    const body = document.body;
    const modeLabel = document.getElementById("modeLabel");
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
        modeLabel.textContent = "🌙 Dark Mode";
    } else {
        modeLabel.textContent = "☀️ Light Mode";
    }
}
