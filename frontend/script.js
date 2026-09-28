const form = document.getElementById("predictionForm");
const predictionValue = document.getElementById("predictionValue");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const data = {
        MedInc: parseFloat(document.getElementById("MedInc").value),
        HouseAge: parseFloat(document.getElementById("HouseAge").value),
        AveRooms: parseFloat(document.getElementById("AveRooms").value),
        AveBedrms: parseFloat(document.getElementById("AveBedrms").value),
        Population: parseFloat(document.getElementById("Population").value),
        AveOccup: parseFloat(document.getElementById("AveOccup").value),
        Latitude: parseFloat(document.getElementById("Latitude").value),
        Longitude: parseFloat(document.getElementById("Longitude").value)
    };

    predictionValue.textContent = "Predicting...";

    try {

        const response = await fetch("/predict", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Prediction request failed");
        }

        const result = await response.json();

        predictionValue.textContent =
            result.predicted_price.toFixed(4);

    } catch (error) {

        console.error(error);

        predictionValue.textContent =
            "Error: API unavailable";
    }
});