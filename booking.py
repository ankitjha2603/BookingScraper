import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



class BookingScraper:
    def __init__(self,wait_for_page_to_load:int=7):
        """
        Initialize the BookingScraper class.
        :param headless: Boolean, to run Chrome in headless mode or not.
        """
        self.wait_for_page_to_load=wait_for_page_to_load
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
    def url_gen(self,destination:str, checkin_date:str, checkout_date:str, adults:int, children:int, rooms:int):
        destination = destination.replace(" ", "+")
        return (f"https://www.booking.com/searchresults.html?"
                f"ss={destination}&checkin={checkin_date}&checkout={checkout_date}&"
                f"group_adults={adults}&group_children={children}&no_rooms={rooms}")
    def load_page(self, url:str):
        """
        Load the given URL in the browser and return the page source.
        :param url: The URL of the booking.com page.
        :return: The page source after loading the URL.
        """
        self.driver.get(url)
        time.sleep(self.wait_for_page_to_load)  # Wait for the page to load
        return self.driver.page_source
    def get_review(self,card):
        review_card=card.find_all(attrs={"data-testid": "review-score"})
        if(review_card):
            return {
                "review-score" :review_card[0].find('div', class_='ac4a7896c7').get_text(strip=True),
                "review" :review_card[0].find('div', class_='dc5041d860').find('div', class_='a3b8729ab1').get_text(strip=True),
                "review-count" :review_card[0].find('div', class_='dc5041d860').find('div', class_='abf093bdfe').get_text(strip=True),
            }
        return {"review-score" :"NULL","review" :"NULL","review-count" :0}
    def scrape_properties(self, destination, checkin_date, checkout_date, adults, children, rooms):
        # Define the URL to scrape
        scrape_url = self.url_gen(destination, checkin_date, checkout_date, adults, children, rooms)
        """
        Scrape property details from the booking.com search results page.
        :param url: The URL of the booking.com search page.
        :return: A list of dictionaries containing property details.
        """
        page_source = self.load_page(scrape_url)
        soup = BeautifulSoup(page_source, 'html.parser')
        properties = []   
        for card in soup.find_all(attrs={"data-testid": "property-card"}):
            try:
                properties.append(
                    {
                        "location": card.find(attrs={"data-testid": "title"}).get_text(strip=True),
                        **self.get_review(card),
                        "image-url": card.find(attrs={"data-testid": "image"}).get('src'),
                        "price-x-nights": card.find(attrs={"data-testid": "price-for-x-nights"}).get_text(strip=True),
                        "prize": card.find(attrs={"data-testid": "price-and-discounted-price"}).get_text(strip=True)[2:]
                    }
                )
            except AttributeError:
                continue
        return properties
    def json_to_csv(self,json_data:dict, csv_file:str="save.csv"):
        keys = json_data[0].keys()
        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=keys)
            csvwriter.writeheader()
            for data in json_data:
                csvwriter.writerow(data)
    def close(self):
        """
        Close the browser after scraping.
        """
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    # Create an instance of BookingScraper
    scraper = BookingScraper(3)
    # Scrape the properties
    scraped_properties = scraper.scrape_properties("Pune", "2024-09-24", "2024-09-28", 2, 1, 1)
    # Save to CSV
    scraper.json_to_csv(scraped_properties, 'main.csv')
    # Close the browser
    scraper.close()