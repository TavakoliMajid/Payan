document.addEventListener("DOMContentLoaded", () => {
    const buyButton = document.getElementById("buy-button");
    const bubbleContainer = document.getElementById("bubble-container");

    const optionsState = {
        firstSelection: null,
        gender: null,
        clothingType: null,
    };

    buyButton.addEventListener("click", () => {
        renderBubbles(["Formal", "Informal"], "firstSelection");
    });

    function renderBubbles(options, type) {
        bubbleContainer.innerHTML = ""; // Clear previous bubbles

        options.forEach(option => {
            const bubble = document.createElement("div");
            bubble.className = "bubble";
            bubble.textContent = option;

            bubble.addEventListener("click", () => {
                handleSelection(type, option);
                bubbleContainer.innerHTML = ""; // Remove bubbles
            });

            bubbleContainer.appendChild(bubble);
        });
    }

    function handleSelection(type, selection) {
        optionsState[type] = selection;
        updateSummary();

        if (type === "firstSelection") {
            if (selection === "Formal") {
                renderBubbles(["Male", "Female", "Child"], "gender");
            } else {
                renderBubbles(["Male", "Female", "Child"], "gender");
            }
        } else if (type === "gender") {
            renderBubbles(["Clothing", "Shoes"], "clothingType");
        }
    }

    function updateSummary() {
        const summary = Object.values(optionsState)
            .filter(value => value)
            .join(", ");

        const summaryDiv = document.querySelector(".selected-options");
        if (!summaryDiv) {
            const newSummaryDiv = document.createElement("div");
            newSummaryDiv.className = "selected-options";
            bubbleContainer.insertAdjacentElement("beforebegin", newSummaryDiv);
        }
        document.querySelector(".selected-options").textContent = summary;
    }
});
