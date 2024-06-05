import requests
from bs4 import BeautifulSoup


def web_scrape_emails_into_list():
    # Define the URL
    base_url = "https://wikileaks.org"
    search_url = (
        "https://wikileaks.org/clinton-emails/?q=printing&mfrom=&mto=&title=&notitle=&date_from=&date_to=&nofrom"
        "=&noto=&count=200&sort=0#searchresult")

    # Send a GET request to the search URL
    response = requests.get(search_url)
    if response.status_code != 200:  # status was successful
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links that match the pattern of the email links
    all_links = soup.find_all('a', href=True)
    email_links = []
    # only adding links that have email id but these links repeat 3 times for each unique link so will only add them
    # once
    counter = 1
    for link in all_links:
        # skipping first 2 link to only append the unique link
        if counter == 3:
            counter = 0  # resetting counter
            # only appending links that have"emailid"
            if 'emailid' in link['href']:
                email_link = base_url + "/clinton-emails/" + link['href']
                email_links.append(email_link)
        counter += 1

    # will store all emails in a list
    email_content_list = []
    for link in email_links:
        # Send a request to the link
        response_email = requests.get(link)

        # Check if the request was successful
        if response_email.status_code == 200:
            # Parse the HTML content of the page
            soup_email = BeautifulSoup(response_email.text, 'html.parser')

            # Find the div with id "uniquer"
            email_content_div = soup_email.find('div', id='uniquer')

            # Check if the div exists
            if email_content_div:
                # Extract and store the email content
                email_content = email_content_div.get_text()
                email_content_list.append(email_content)
            else:
                print("No email content found on", link)

    return email_content_list
