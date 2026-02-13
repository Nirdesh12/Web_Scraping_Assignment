# Web_Scraping_Assignment
news article web scraping

This Python program is a simple web scraping script that collects news articles related to the topic “Election” from three Nepali news websites: The Kathmandu Post, The Himalayan Times, and Onlinekhabar.
In this code, I used the requests library to send HTTP requests to each website and download their homepage content. Then, I used BeautifulSoup to parse the HTML structure of the page. The program searches through all the anchor (<a>) tags and checks if the word “Election” appears in the title of the link. If the keyword is found, the article title and its link are stored in a list. Finally, the program prints the matching articles.
To make the request look like it is coming from a real browser, I added a user-agent header. I also used exception handling so that the program does not crash if a website fails to respond. Overall, this script demonstrates basic web scraping, HTML parsing, keyword filtering, and structured data extraction using Python.
