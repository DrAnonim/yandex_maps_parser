from typing import Dict, List
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


def get_data_html(url: str) -> None:
    '''
    This function uses Selenium to get the HTML data of a webpage.
    It saves the page source to a file named 'index.html'.
    '''
    # Set up the Chrome options and driver
    options = webdriver.ChromeOptions()
    options.binary_location = "[path to chrome-unstable]"
    chrome_driver_binary = "[path to driver]"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    driver.maximize_window()

    try:
        # Load the URL in the driver and wait for 5 seconds
        driver.get(url=url)
        time.sleep(5)
        # While loop to keep scrolling the page until all items are loaded
        while True:
            end_block = driver.find_element(By.CLASS_NAME, 'search-list-meta-view')
            # If all items are loaded, save the page source to 'index.html' and break the loop
            if driver.find_elements(By.CLASS_NAME, 'add-business-view'):
                with open('index.html', 'w') as file:
                    file.write(driver.page_source)
                break
            # Otherwise, move the mouse to the end of the page and wait for 5 seconds
            else:
                action = ActionChains(driver)
                action.move_to_element(end_block).perform()
                time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        # Close the driver
        driver.close()
        driver.quit()


def get_items_urls(file_path: str) -> str:
    '''
    This function reads HTML data from a file and extracts URLs of items.
    It saves the URLs to a file named 'urls.txt' and returns a string '[INFO Urls collected!]'
    '''
    # Read the page source from the file and parse it using BeautifulSoup
    with open(file_path) as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    # Find all items on the page
    items = soup.find_all(class_='search-snippet-view')

    # Extract URLs of items and save them to 'urls.txt'
    urls: List[str] = []
    for item in items:
        item_url = item.find('a', class_='search-snippet-view__link-overlay _focusable').get('href')
        urls.append('https://yandex.ru' + item_url)
    with open('urls.txt', 'w') as file:
        for url in urls:
            file.write(f'{url}\n')

    return '[INFO Urls collected!]'


def main() -> None:
    '''
    This function is the main entry point of the script.
    It calls the 'get_data_html' function to get HTML data of a webpage
    and then calls the 'get_items_urls' function to extract URLs of items.
    '''
    # Call the 'get_data_html' function to get HTML data
    get_data_html(url='https://yandex.ru/maps/213/moscow/search/%D0%BE%D1%81%D0%B0%D0%B3%D0%BE%20%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/?ll=37.650216%2C55.724799&page=28&sll=37.576943%2C55.724799&sspn=1.966553%2C0.847911&z=10')
    get_items_urls(file_path='[file_path]')


if __name__ == '__main__':
    main()
