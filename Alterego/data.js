function buildFinalData(data) {
    const finalData = { ...data, results: [] };

    for (let key in personas) {
        const score = Math.round(calculateScore(data, personas[key]));
        const decision = getDecision(score);

        finalData.results.push({
            persona: key,
            score,
            decision
        });
    }

    localStorage.setItem("finalDecision", JSON.stringify(finalData));
    return finalData;
}


// XML generation
function generateXML(data) {
    let xml = "<decisions>";

    data.results.forEach(r => {
        xml += `
        <decision>
            <persona>${r.persona}</persona>
            <score>${r.score}</score>
        </decision>`;
    });

    xml += "</decisions>";
    return xml;
}