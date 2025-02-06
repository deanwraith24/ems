# Eventopia

[Link to live project](https://git.heroku.com/eventopia.git)

## Introduction

![Image of responsive site](https://github.com/deanwraith24/ems/blob/main/assets/images/cover_image.jpg)

## Table of Contents

- [Planning](#planning)
  - [External User Goals](#external-user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Landing Page](#landing-page)
  - [Event Dashboard](#event-dashboard)
  - [Event Browsing](#event-browsing)
  - [Ticket Purchase](#ticket-purchase)
- [Future Enhancements](#future-enhancements)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validation](#validation)
  - [Issues](#issues)
- [Deployment](#deployment)
- [Credits](#credits)

## Planning

### External User Goals
- Users should be able to browse and discover upcoming events easily.
- Users should be able to register and log in to purchase event tickets.
- Users should receive email notifications after ticket purchases.
- Event creators should be able to create, edit, and manage events via their dashboard.

### Site Owner Goals
- Provide a platform for users to create and manage events efficiently.
- Enable users to purchase event tickets using a seamless checkout process.
- Implement secure authentication and Stripe payment integration.
- Offer a well-structured, user-friendly interface.

### Wireframes

#### Home Page Wireframe
![Home Page Wireframe](https://github.com/deanwraith24/ems/blob/main/assets/images/home_wireframe.jpg)

#### Dashboard Wireframe
![Dashboard Wireframe](https://github.com/deanwraith24/ems/blob/main/assets/images/dashboard_wireframe.jpg)

## Features

### Landing Page
- The landing page welcomes users with a modern, user-friendly design.
- A call-to-action to sign up, log in, or browse events.
- Featured events section highlighting upcoming events.

### Event Dashboard
- Logged-in users can create, edit, and delete their own events.
- Event fields include name, image, description, date, time, venue, ticket price, and availability.
- A summary of all created events is displayed in a table format.

### Event Browsing
- Users can explore upcoming events categorized by type and location.
- A search and filter function is available to refine event searches.
- Each event has a dedicated details page with more information and a purchase button.

### Ticket Purchase
- Secure ticket purchasing powered by Stripe integration.
- Users can add multiple tickets to their cart and view a detailed checkout summary.
- Confirmation emails are sent upon successful ticket purchases.

## Future Enhancements
- **User Profiles:** Allow users to save favorite events and track purchases.
- **Event Reviews:** Enable users to rate and review events they attended.
- **Social Sharing:** Add social media sharing buttons for events.
- **Live Chat Support:** Implement a chatbot for real-time assistance.

## Testing

### Manual Testing
- The app was tested manually on different devices and browsers.
- Various user scenarios were tested, including account creation, event browsing, ticket purchasing, and event management.

### Validation
- **HTML:** Checked with W3C Markup Validation Service.
- **CSS:** Validated using Jigsaw CSS Validator.
- **JavaScript:** Tested with JSHint for code quality.
- **Python/Django:** Checked using Flake8 for syntax errors and best practices.

### Issues
- **Login Redirect Issue:** Initially, users were not redirected correctly after logging in. This was fixed by adjusting the authentication views.
- **Payment Processing Delay:** The checkout process occasionally took too long. Optimized Stripe API calls for better performance.
- **Mobile Responsiveness:** Some elements were not properly displayed on smaller screens. Updated CSS to enhance responsiveness.

## Deployment

The project was deployed using Heroku. The deployment steps are:

1. Install Heroku CLI and log in via the terminal.
2. Initialize a Git repository and connect it to Heroku.
3. Set up environment variables for database and Stripe keys.
4. Deploy the project using `git push heroku main`.
5. Verify deployment by accessing the live site.

## Credits
- **Django Documentation:** Used for authentication and database setup.
- **Bootstrap:** Utilized for styling and responsive design.
- **Stripe API Documentation:** Used for payment integration.
- **W3Schools & MDN Web Docs:** Referenced for various frontend and backend functionalities.