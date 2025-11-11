thonimport json
import requests
from extractors.amazon_scraper import AmazonScraper
from outputs.exporter import Exporter

def run_scraper():
    # Example: Scraping data for a list of seller storefront URLs
    seller_urls = [
        "https://www.amazon.com/sp?seller=AWKG3GL9X9XP2",
        "https://www.amazon.com/sp?seller=ABC123XYZ"
    ]

    amazon_scraper = AmazonScraper(seller_urls)
    scraped_data = amazon_scraper.scrape_seller_data()

    # Export the data to JSON
    exporter = Exporter('output.json')
    exporter.export(scraped_data)

if __name__ == "__main__":
    run_scraper()