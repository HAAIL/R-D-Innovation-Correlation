from sec_edgar_downloader import Downloader
import os
import shutil
from read_document import open_parse_doc, get_text, get_topics, sort_topics

# Initialize a downloader instance
dl = Downloader("Microsoft", "your_email@example.com")

# Download the latest 10-K filing for Microsoft
dl.get("10-K", "MSFT", limit=1)

my_dict = {}
soup = open_parse_doc("sec-edgar-filings/MSFT/10-K/0000950170-23-035122/full-submission.txt") #path to the donwloaded document
text = get_text(soup)
research_info = get_topics(text)
list_of_topics = sort_topics(research_info)
my_dict[2023] = list_of_topics

for key,val in my_dict.items():
    print("Year: ", key)
    print("Topics: ", val)


