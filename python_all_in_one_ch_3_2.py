from urllib import request
# URL (address) of the desired page.
sample_url = 'https://www.google.com/search?q=python%20web%20scraping%20tutorial'
# Request the page and put it in a variables named the page.
thepage = request.urlopen(sample_url)
# Put the response code in a variable named status.
status = thepage.code
# What is the data type of the page?
print(f'Type: "{type(thepage)}"')
# What is the status code?
print(f'Status: "{status}"')