document.addEventListener('DOMContentLoaded', () => {
    const confirmModal = document.getElementById('confirmModal');
    let currentForm = null;

    if (confirmModal) {
        const bootstrapModal = new bootstrap.Modal(confirmModal);
        const confirmActionButton = document.getElementById('confirmAction');

        // Handle Confirm Action
        confirmActionButton.addEventListener('click', () => {
            if (currentForm) {
                currentForm.submit();
            }
        });

        // Attach Modal to Forms
        document.querySelectorAll('.decrease-quantity-form, #clear-cart-form').forEach(form => {
            form.addEventListener('submit', event => {
                event.preventDefault(); // Prevent immediate submission
                currentForm = form; // Store the form
                bootstrapModal.show(); // Show confirmation modal
            });
        });
    } else {
        // Fallback to browser confirm dialog if modal is not available
        document.querySelectorAll('#clear-cart-form').forEach(form => {
            form.addEventListener('submit', event => {
                const confirmClear = confirm("Are you sure you want to clear all items from the cart?");
                if (!confirmClear) {
                    event.preventDefault();
                }
            });
        });

        document.querySelectorAll('.decrease-quantity-form').forEach(form => {
            form.addEventListener('submit', event => {
                const confirmDecrease = confirm("Are you sure you want to decrease the ticket quantity?");
                if (!confirmDecrease) {
                    event.preventDefault();
                }
            });
        });
    }
});

// Function to display a success message as a popup
function showPopupMessage(message) {
    // Create a popup div
    const popup = document.createElement('div');
    popup.className = 'popup-message alert alert-success';
    popup.innerText = message;

    // Add the popup to the body
    document.body.appendChild(popup);

    // Remove the popup after 3 seconds
    setTimeout(() => {
        popup.remove();
    }, 3000);
}

// Event listener for forms submitting to add to cart
document.querySelectorAll('.add-to-cart-form').forEach((form) => {
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the default form submission

        // Get the form data
        const formData = new FormData(form);

        // Send the POST request via fetch
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    // Show popup message
                    showPopupMessage(data.message);
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch((error) => {
                console.error('Error adding to cart:', error);
            });
    });
});
