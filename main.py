from web_scraper_for_emails import web_scrape_emails_into_list

# main script
if __name__ == "__main__":
    # calling web scrape emails into csv file
    site = (
        "https://wikileaks.org/clinton-emails/?q=printing&mfrom=&mto=&title=&notitle=&date_from=&date_to=&nofrom"
        "=&noto=&count=200&sort=0#searchresult")
    message = "Web scraping emails from wikileaks site: " + site
    print(message)
    print("Getting emails ...")
    # getting the emails from the web scraped site
    emails = web_scrape_emails_into_list()
    print("Done web scraping emails!")
    for email in emails:
        print(email)

    # extracting information from each email

