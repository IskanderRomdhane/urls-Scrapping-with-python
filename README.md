# urls-Scrapping-with-python
This Python program utilizes a PyQt5 interface to scrape Google search results based on user-defined keywords and the number of pages needed.

Overview
The application is designed to efficiently retrieve search results from Google. It consists of two main components:

PyQt5 Interface: Allows users to input a keyword and specify the number of pages to scrape.
Scraper: Utilizes Python libraries like requests and BeautifulSoup to extract search results based on the provided keyword.
Features
Keyword Input: Users can enter the keyword(s) they want to search for.
Page Number Input: Users can specify the number of pages to scrape for search results.
Fast Results: Provides search results within seconds for the specified parameters.
Technologies Used
Python Libraries: requests, BeautifulSoup
GUI Framework: PyQt5
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/google-search-scraper.git
cd google-search-scraper

Install Dependencies:

Ensure you have Python installed.
Install the required libraries:
pip install requests beautifulsoup4 PyQt5

Run the Application:

Execute the Python script:
python main.py

Input the keyword(s) and number of pages required.
Click the "Scrape" button to initiate the scraping process.
View the results displayed within the interface.
File Structure:

google-search-scraper/
│
├── main2.py
├── fetch.py
└── url.txt
Contributors
Iskander Romdhane
