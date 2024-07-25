---

# ScrapEnxor

**Web Scrapper**

ScrapEnxor is a powerful web scrapping application that extracts essential information such as company names, logos, contact information, and more from websites. It's designed to be intuitive and responsive, making web scrapping tasks straightforward and efficient.

![ScrapEnxor Screenshot](screenshots/scrap_enxor_main.png)

## Features

- **Company Name Extraction:** Automatically retrieves the company's name from the website.
- **Logo Retrieval:** Extracts the company's logo, even from relative paths.
- **Contact Information:** Gathers phone numbers and emails scattered across the website.
- **About the Company:** Fetches the first paragraph from the 'About Us' page.
- **Location Detection:** Scraps the website to find location/address details.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Error Handling:** Provides clear error messages when scrapping fails.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/egwimcodes/ScrapEnxor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ScrapEnxor
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and navigate to `http://127.0.0.1:8000/` to start using ScrapEnxor.

## Usage

1. Enter the URL of the website you want to scrape.
2. Click the "Scrape" button.
3. Wait for the app to process the URL and display the results.

### Example

![ScrapEnxor Example](screenshots/scrap_enxor_example.png)

## Technologies Used

- **Django:** Backend framework for handling web requests and data processing.
- **BeautifulSoup & Requests:** Libraries for parsing HTML and making HTTP requests.
- **HTML, CSS & JavaScript:** Frontend technologies for building a responsive user interface.

## Screenshots

### Main Interface
![Main Interface](screenshots/scrap_enxor_main.png)

### Scrapping Results
![Scrapping Results](screenshots/scrap_enxor_results.png)

## Contributing

We welcome contributions to ScrapEnxor! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Create a pull request with a detailed description of your changes.

## License

ScrapEnxor is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, feel free to reach out:

- GitHub: [egwimcodes](https://github.com/egwimcodes)
- LinkedIn: [egwimcodes](https://www.linkedin.com/in/egwimcodes)
- Website: [egwimcodes.dev](https://egwimcodes.dev)

---