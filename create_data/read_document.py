import openai
from openai import OpenAI
import nltk
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import requests
import os

#note from Microsoft 10-K:
# Research and development expenses include payroll, employee benefits, stock-based compensation expense, and other headcount-related expenses associated with product development.
# Research and development expenses also include third-party development and programming costs and the amortization of purchased software code and services content. 

def open_parse_doc(filename):
    """
    Parse an HTML document from a file and return a BeautifulSoup object.
    
    Args:
        filename (str): The name of the HTML file to be parsed.
    
    Returns:
        BeautifulSoup: A BeautifulSoup object representing the parsed HTML.
    """
    with open(filename, 'r') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_text(soup):
    """
    Extract text between specified sections in a BeautifulSoup object.
    
    Args:
        soup (BeautifulSoup): The BeautifulSoup object representing the HTML document.
    
    Returns:
        str: Extracted text.
    """
    sec_list = ["Business", "Risk Factors"]
    text = ""
    for i in range(len(sec_list) - 1):
        item_1 = sec_list[i]
        item_2 = sec_list[i + 1]
        a_tag = soup.find('a', text=item_1)
        if a_tag:
            href = a_tag['href']
            href = href[1:]  # removing hashtag in front of id
        a_tag = soup.find('a', text=item_2)
        if a_tag:
            href_2 = a_tag['href']
            href_2 = href_2[1:]  # removing hashtag in front of id
        first_div = soup.find('div', id=href)
        second_div = soup.find('div', id=href_2)
        tag = "div"
        if first_div is None:
            first_div = soup.find('p', id=href)
            second_div = soup.find('p', id=href_2)
            tag = "p"
        if first_div is not None:
            next_div = first_div.find_next_sibling(tag)
            while (next_div != second_div):
                text += next_div.get_text(strip=True)
                next_div = next_div.find_next_sibling(tag)
    return text

def get_topics(text):
    """
    Extract DBPedia topics matching the research and development activities of 'Microsoft'
    from the given text using OpenAI's GPT model.
    
    Args:
        text (str): The text describing research and development activities.
    
    Returns:
        list: List of DBPedia topics.
    """
    research_info = []

    prompt = f"""Extract a set of DBPedia topics that match the research and development activities of 'Microsoft',
    as described in the given text:'{text}'. Give only the title of the DBPedia topic. Dont return any sentence but DBPedia topics. Provide output in the same format as:
    '1. BusinessCompany\n2. iPhone\n3. MacBook Air\n4. MacBook Pro\n5.'
    """
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

def sort_topics(research_info):
    """
    Sort and process the extracted DBPedia topics from the research information.
    
    Args:
        research_info (list): List of research-related information.
    """
    my_dict = {}
    my_list = []
    for i, info in enumerate(research_info):
        sentences = sent_tokenize(info)
        research_sentences = []
        for sentence in sentences:
            if sentence != "1.":
                modified_string = sentence.split("\n")[0]
                my_list.append(modified_string)

    return my_list