import feedparser
import sys

def read_rss_feed(url, show_description=True):
    # Parse the RSS feed from the provided URL
    feed = feedparser.parse(url)
    
    # Display feed title
    print(f"Feed Title: {feed.feed.title}\n")
    
    # Get the last 5 entries (or fewer if there are less than 5 entries)
    latest_entries = feed.entries[:5]  # Slice the first 5 entries
    
    # Loop through the last 5 entries and display details
    for entry in latest_entries:
        print(f"Title: {entry.title}")
        
        # Check if 'dcterms_creator' exists (country field)
        creator = entry.get('dcterms_creator', 'No Country Info')
        print(f"Country: {creator}")
        
        # Optionally display 'description' field based on argument
        if show_description:
            description = entry.get('description', 'No Description')
            print(f"Description: {description}")
        
        # Check if 'link' exists
        link = entry.get('link', 'No Link Available')
        print(f"Link: {link}")
        
        print(f"Published: {entry.published}\n")

# Main function to handle arguments
if __name__ == "__main__":
    rss_url = "https://globalrecalls.oecd.org/ws/rss.xqy"
    
    # Check if "/s" argument is provided to skip description
    if len(sys.argv) > 1 and sys.argv[1] == "/s":
        read_rss_feed(rss_url, show_description=False)
    else:
        read_rss_feed(rss_url)
