# Indoor Plants Showcase

Welcome to the Indoor Plants Showcase project! This website is designed to help users discover, learn about, and find the perfect indoor plants for their home or office. It features detailed information about various types of indoor plants, categorized by their light requirements, air-purifying qualities, pet-friendliness, and more.

## Features

- **Plant Database:** Comprehensive details about various indoor plants, including care instructions, light and water requirements, and more.
- **Categories:** Plants are categorized for easy browsing (e.g., Low Light, Air Purifying, Pet Friendly).
- **User Reviews:** Users can leave reviews and ratings for plants.
- **Blog:** Informative articles about plant care, tips, and trends.
- **Responsive Design:** Mobile-friendly layout for a seamless experience on any device.

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
    git clone https://github.com/sabbir2609/plantx.git
    ```
2. Navigate to the project directory:
    ```bash
    cd plantx
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

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
