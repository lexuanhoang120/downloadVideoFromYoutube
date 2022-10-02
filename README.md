Download all video from one channel in youutube
# Step 1: Download Google Chrome

https://www.google.com/chrome/

# Step 2: Install Web Scraper extension

https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn

More tutorials: https://www.webscraper.io/

https://www.webscraper.io/tutorials

# Step 3: Find the Channel you want to download

deutsch lernen

go to channel

go to Videos tab

copy the URL

# Step 4: Download the video list as CSV

Right click to Inspect

## Navigate to Web Scraper tab

Create new sitemap
ID: name of channel
Start URL: the URL you copied above

## Add new selector

    Id: videos
    Type: Element scroll down
    Selector: .ytd-grid-renderer div#meta
    Multiple: checked
    Parent Selectors: _root

Click on videos selector

## Add new selector

    Id: link
    Type: Link
    Selector: a
    Multiple: checked
    Parent selectors: videos

Optional preview

Scrape on sitemap 'your channel'

Export data to csv


# Step 5: Download and run


Download the binary at 

https://github.com/lexuanhoang120/downloadVideoFromYoutube

Extract the binary

prepare: python , pip , copy .csv file to downloadVideoFromYoutube

Open terminal window

Navigate to the downloaded folder: 

    $ cd downloadVideoFromYoutube
    $ pip install -r requirements.txt
    $ python main.py "your .csv file" "which folder do you want to save videos"

log.txt: status when download
