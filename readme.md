# BookingScraper

## Overview
**BookingScraper** is a web scraping tool designed to extract property details from Booking.com. This project serves as a learning experience to understand web scraping techniques using Python, Selenium, and BeautifulSoup.

## Features
- Generates search URLs for Booking.com based on user input.
- Scrapes property information, including location, review scores, images, and pricing.
- Saves the scraped data into a CSV file for easy analysis and review.
- Option to run in headless mode for background scraping.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup4
- webdriver-manager
- Chrome WebDriver

# BookingScraper

## Usage
1. Open `booking_scraper.py`.
2. Modify the parameters in the example usage section (destination, check-in and check-out dates, number of adults, children, and rooms).
3. Run the script:
   ```bash
   python booking_scraper.py
   ```
4. The scraped data will be saved to a CSV file (e.g., `saved.csv`).

## Credits
- **Author**: Ankit Kumar Jha
- **Libraries Used**:
  - [Selenium](https://www.selenium.dev/) - For automating web browser interaction.
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML and XML documents.
  - [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) - For managing WebDriver binaries.

## Disclaimer
This project is for educational purposes only. Web scraping may violate the terms of service of some websites. Always ensure you have permission to scrape a website and check its `robots.txt` file to understand what is allowed. Use this tool responsibly to learn how web scraping works without violating any website's privacy.
