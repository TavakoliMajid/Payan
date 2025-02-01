document.addEventListener("DOMContentLoaded", function () {
    const buyButton = document.getElementById("buy-button");
    const bubblesContainer = document.getElementById("bubbles-container");

    // Show bubbles when clicking the Buy button
    buyButton.addEventListener("click", function (event) {
        event.stopPropagation(); // Prevent immediate hiding when clicking the button
        bubblesContainer.classList.toggle("show");
    });

    // Hide bubbles when clicking outside of them
    document.addEventListener("click", function (event) {
        if (!bubblesContainer.contains(event.target) && event.target !== buyButton) {
            bubblesContainer.classList.remove("show");
        }
    });
});
