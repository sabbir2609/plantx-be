# Viriditas

Welcome to the Viriditas project! This website is designed to help users discover, learn about, and find the perfect indoor plants for their home or office. It features a comprehensive plant database, categorized plant listings, user reviews, and more.

## Features

- **Customer Management:** Manage customer profiles, including user details, memberships, and contact information.
- **Plant Management:** Detailed information on various indoor plants, including their care instructions, categories (e.g., Low Light, Air Purifying), and other attributes.
- **Planter Management:** Information about different planters, including sizes, colors, and custom options.
- **Planting Accessories:** Manage accessories related to plant care.
- **Service Management:** Categories and services offered, including details and associated projects.
- **Content Management:** Ideas, testimonials, team members, and projects to enhance the website's content and showcase.
- **Zone-Based Pricing:** Pricing adjustments based on geographic zones to ensure accurate shipping costs and availability.
- **Tags:** Add and manage tags for plants, planters, and accessories to help users filter and find products more easily.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Homepage Layout](#homepage-layout)
- [Pages](#pages)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sabbir2609/viriditas.git
    ```
2. Navigate to the project directory:
    ```bash
    cd viriditas
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Visit the homepage at `http://127.0.0.1:8000/` to explore the website.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage content.

## Homepage Layout

The homepage of Viriditas showcases featured plants, planters, and accessories. It provides easy navigation to various categories and sections of the website.

## Pages

- **Plant Listings:** View and browse plants by category and tags.
- **Planters:** Browse available planters and their details.
- **Accessories:** Explore planting accessories.
- **Services:** Information on services offered.
- **Blog:** Read articles about plant care and trends.
- **Testimonials:** Read customer reviews and feedback.
- **Team:** Meet the team behind Viriditas.
- **Projects:** View projects and case studies.

## Zone-Based Pricing

Viriditas includes zone-based pricing to accommodate shipping costs and availability. Pricing may vary based on the customer's location, ensuring accurate and fair pricing.

## Tags

Plants, planters, and accessories can be tagged with relevant keywords. Tags help users filter products by characteristics such as type, size, or features.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that you follow the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [your-email@example.com](mailto:your-email@example.com).
