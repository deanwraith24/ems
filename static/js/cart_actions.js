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
