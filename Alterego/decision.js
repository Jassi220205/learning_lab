const personas = {
    disciplined: { short: 1, long: 5, effort: 3, deadline: 4 },
    impulsive: { short: 5, long: 1, effort: 2, deadline: 1 },
    future: { short: 1, long: 6, effort: 2, deadline: 5 },
    balanced: { short: 3, long: 3, effort: 3, deadline: 3 }
};

function calculateScore(data, w) {
    const deadlinePressure = 10 - Math.min(data.deadline, 10);

    return (
        w.short * data.shortReward +
        w.long * data.longReward -
        w.effort * data.effort -
        w.deadline * deadlinePressure
    );
}

function getDecision(score) {
    if (score > 50) return "Do it now";
    if (score > 20) return "Plan it";
    if (score > 0) return "Delay";
    return "Avoid";
}