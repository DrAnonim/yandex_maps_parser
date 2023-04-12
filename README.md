Webpage Scraper

This is a Python script that uses Selenium and BeautifulSoup to scrape a webpage and extract URLs of items from it.
Installation

Clone the repository to your local machine using the command:

bash

    git clone https://github.com/yourusername/yourrepository.git

Replace 'yourusername' and 'yourrepository' with your account and repository names, respectively.

Install the required packages using the command:

bash
    
    pip install -r requirements.txt

This will install all the necessary packages listed in the requirements.txt file. 
Make sure you have Python 3.x installed on your computer and have access to the command line.
Requirements 

Python 3.10
Selenium
BeautifulSoup

How to use

To use this script, simply run the following command:

python scraper.py

This will run the main function in the scraper.py file, 
which calls the get_data_html function to get HTML data of a webpage and then calls the get_items_urls 
function to extract URLs of items.

Functions

get_data_html(url: str) -> None

This function uses Selenium to get the HTML data of a webpage. It saves the page source to a file named 'index.html'.
get_items_urls(file_path: str) -> str

This function reads HTML data from a file and extracts URLs of items. 
It saves the URLs to a file named 'urls.txt' and returns a string '[INFO Urls collected!]'.
main() -> None

This function is the main entry point of the script. 
It calls the get_data_html function to get HTML data of a webpage and then calls the get_items_urls function 
to extract URLs of items.