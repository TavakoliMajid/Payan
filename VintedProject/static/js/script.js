document.addEventListener('DOMContentLoaded', () => {
    const sellButton = document.querySelector('area[alt="Sell"]');
    const buyButton = document.querySelector('area[alt="Buy"]');
    const popupWindow = document.getElementById('popup-window');

    // Display the popup when Sell or Buy is clicked
    sellButton.addEventListener('click', (event) => {
        event.preventDefault();
        popupWindow.style.display = 'block';
    });

    buyButton.addEventListener('click', (event) => {
        event.preventDefault();
        popupWindow.style.display = 'block';
    });

    // Close the popup when clicking outside of it
    document.addEventListener('click', (event) => {
        if (!popupWindow.contains(event.target) && !sellButton.contains(event.target) && !buyButton.contains(event.target)) {
            popupWindow.style.display = 'none';
        }
    });
});
