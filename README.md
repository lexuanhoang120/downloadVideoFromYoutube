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

Scrape

Export data


# Step 5a: Download the dl-youtube-videos binary for each platform


Download the binary at 

https://github.com/pnhoang/dl-youtube-videos/releases

Extract the binary

Open terminal window

Navigate to the downloaded folder: 

    $ cd ~/Downloads/dl-youtube-videos
    $ bin/dl-youtube-videos {csv_file}

Voillaaa, all the videos will be downloaded into the current folder in mp4 format. Enjoy the videos and remember to subscribe to the channel you downloaded, also to my channel to receive more update.

# Step 5b: Optional

Check if you have Node installed in your computer

    ➜ node -v
    v10.16.3
    ➜ npx -v
    6.9.0

Use the script with npx:

    ➜ npx dl-youtube-videos {csv_file}
