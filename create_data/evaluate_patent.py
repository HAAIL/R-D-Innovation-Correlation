import openai
from openai import OpenAI
import nltk
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import requests
import os
import urllib3
import gspread
from google.oauth2.service_account import Credentials
from read_document import open_parse_doc, get_text, get_topics, sort_topics

# Dictionary that is going to contain year as a key, list of topics for that year as a value
my_dict = {}
soup = open_parse_doc("Microsoft-10K/Microsoft2023.html")
text = get_text(soup)
research_info = get_topics(text)
list_of_topics = sort_topics(research_info)
my_dict[2023] = list_of_topics

# soup = open_parse_doc("Microsoft-10K/Microsoft2022.html")
# text = get_text(soup)
# research_info = get_topics(text)
# list_of_topics = sort_topics(research_info)
# my_dict[2022] = list_of_topics

# soup = open_parse_doc("Microsoft-10K/Microsoft2021.html")
# text = get_text(soup)
# research_info = get_topics(text)
# list_of_topics = sort_topics(research_info)
# my_dict[2021] = list_of_topics

# soup = open_parse_doc("Microsoft-10K/Microsoft2020.html")
# text = get_text(soup)
# research_info = get_topics(text)
# list_of_topics = sort_topics(research_info)
# my_dict[2020] = list_of_topics

for key,val in my_dict.items():
    print("Year: ", key)
    print("Topics: ", val)


def categorize_patent(title, text, year, my_dict):
    research_info = []
    #topics = ['Artificial_Intelligence', 'Microsoft_Teams', 'Microsoft_Outlook', 'Bing_(search_engine)', 'Xbox', 'Cloud_Computing', 'Generative_AI', 'Microsoft_Cloud', 'Office_365', 'Dynamics_365', 'LinkedIn', 'Microsoft_Power_Platform', 'Azure_AI', 'OpenAI', 'GitHub', 'Windows_365', 'Azure_Orbital', 'Microsoft_Mesh', 'Microsoft_Intelligent_Data_Platform', 'GitHub_Copilot', 'Microsoft_Fabric', 'Cybersecurity', 'Sustainability', 'Digital_Skills_Initiative']
    topics = my_dict[year]
    prompt = f"""Given title: {title} and description {text} of the patent, categorize it into one of the major categories from this list: {topics}. Please provide only category as the output."""
    client = OpenAI(
        api_key="API-KEY"
    )

    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    # print(completion.choices[0].message)

    # Extract the generated research-related information
    generated_text = completion.choices[0].message.content
    # Append the generated information to the research_info list
    research_info.append(generated_text)
    return research_info



def evaluate_patents(year, my_dict):
    # Disable SSL verification warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    publication_from_date = str(year)+"-01-01"
    publication_to_date = str(year+1)+"-01-01"
    print(publication_from_date)
    print(publication_to_date)
    # Define the USPTO API endpoint and parameters for searching publication data
    url = 'https://developer.uspto.gov/ibd-api/v1/application/publications'
    params = {
        'publicationFromDate': publication_from_date,
        'publicationToDate': publication_to_date,
        'assigneeEntityName': 'Microsoft'  # Adjusted for specificity
    }
    headers = {'accept': 'application/json'}

    # Make the GET request to the USPTO API
    response = requests.get(url, params=params, headers=headers, verify=False)

    # Initialize variables for processing the response
    count = 0
    patent_dict = {}
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if 'results' key exists in the response data
        if 'results' in data:
            for item in data['results']:
                patent_number = item.get('patentApplicationNumber', 'N/A')
                title = item.get('inventionTitle', 'N/A')
                abstractText = item.get('abstractText', 'N/A')
                
                # Print the retrieved patent data
                print('Patent Number:', patent_number)
                print('Title:', title)
                print('Abstract:', abstractText)
                print("Category: ")
                patent_topic = categorize_patent(title, abstractText, year, my_dict)
                print(patent_topic)
                patent_topic = str(patent_topic).lower()

                if patent_topic not in patent_dict:
                    patent_dict[patent_topic] = 1
                else:
                    patent_dict[patent_topic] += 1
                print('-----')
                
                # Increment the counter for each patent found
                count += 1
        else:
            print('No results found in the response data.')
    else:
        print('Request failed with status code:', response.status_code)


    # Print the total count of patents retrieved
    print('Total patents found:', count)
    new_dict = {} #new dictionary that calculates percnetage of topics mentioned
    for key,val in patent_dict.items():

        new_dict[key] = val/count

    for key,val in new_dict.items():

        print(key, " - ", val)


evaluate_patents(2023, my_dict=my_dict)