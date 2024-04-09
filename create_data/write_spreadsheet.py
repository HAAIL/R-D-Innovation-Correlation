import gspread
from google.oauth2.service_account import Credentials
import time

def insert_Topics(sheet, company_name, document_year, topics, num_topics):
    """
    Updates a Google Sheet with a list of topics for a specified company and year.
    Adds the company and year to a new row and topics to the first row if not present.
    Marks the presence of topics for the given year with '1'.

    param: sheet (Worksheet): The worksheet to update.
    param: company_name (str): Company name.
    param: document_year (str): Year of the document.
    param: topics (list of str): Topics to insert or mark.
    returns: None.
    """
    print(num_topics)
    one_percent = num_topics/100
    print(one_percent)
    first_column_values = sheet.col_values(1)
    first_row_values = sheet.row_values(1)

    num_rows = len(first_column_values) # number of rows
    num_columns = len(first_row_values) # num o

    sheet.update_cell(num_rows + 1, 1, company_name)
    sheet.update_cell(num_rows + 1, 2, document_year)
    count = 0
    for topic, num in topics.items():

        if num > one_percent:

            topic = topic.lower()
            cell = sheet.find(topic)

            if count >= 28:
                time.sleep(65)
                count = 0

            count += 1
            try:
                if cell is None: #topic was not yet put in the columns

                    sheet.update_cell(1, num_columns + 1, topic)
                    sheet.update_cell(num_rows + 1, num_columns + 1, num) #topic is presnet for that year in the report
                    num_columns += 1

                else: #toppic is alreadye present in the first row

                    sheet.update_cell(num_rows + 1, cell.col, num)
            except:
                time.sleep(60)

                if cell is None:  # topic was not yet put in the columns

                    sheet.update_cell(1, num_columns + 1, topic)
                    sheet.update_cell(num_rows + 1, num_columns + 1,
                                      num)  # topic is presnet for that year in the report
                    num_columns += 1

                else:  # toppic is alreadye present in the first row

                    sheet.update_cell(num_rows + 1, cell.col, num)

# Google Sheets API credentials and setup
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("axial-matter-417700-fcd9f8f37fd3.json", scopes=scopes)
client = gspread.authorize(creds)


# Open the Google Sheet using its unique ID
sheet_id = "1KEy80XMO1PICRmqYojKFukIYWqVN6yOIP-U7flLFwH4"
workbook = client.open_by_key(sheet_id)


# Access the specific worksheet within the Google Sheet
sheet = workbook.worksheet("Keys")


### Added the following 10-K documents to spreadsheet

import json

file_path = '../create_data/fortune1000/company_with_patents2.0.txt'
company_dict = {}
count_2 = 0
with open(file_path, 'r') as file:
    # for every company
    for company_name in file:
        print(company_name)
        company_name=company_name.strip()
        file_path = '/Users/mikhaillemper/Desktop/GradSchool/Spring24/Research/patent_data/2019.jsonl'
        # Open the file
        count = 0
        #making dictionary where key: company; value dict [key: topic, value: count]
        company_dict[company_name] = {}
        count_2 += 1
        with open(file_path, 'r') as file:
            company_dict[company_name]['topics'] = 0
            for line in file:
                # Parse the JSON data from the current line
                try:
                    data = json.loads(line)
                except json.decoder.JSONDecodeError:
                    pass
                try:
                    if company_name.lower() in data['assignee'].lower() or data['assignee'].lower() in company_name.lower():
                        # print(line)
                        for topic in data['openalex_concepts_with_chains']:
                            if topic in company_dict[company_name]: #topic exsits
                                company_dict[company_name][topic] += 1
                                company_dict[company_name]['topics'] += 1
                            else:
                                company_dict[company_name][topic] = 1
                                company_dict[company_name]['topics'] += 1
                        #count += 1
                        # if 'artificial intelligence' in data['openalex_concepts_with_chains']:
                        #     print(line)
                        #     count += 1
                except:
                    pass
        #break
        if count_2 == 50:
            break
for company, dictionary in company_dict.items():
    year = "2019"
    #topics =  ['Artificial_Intelligence', 'Microsoft_Teams', 'Microsoft_Outlook', 'Bing_(search_engine)', 'Xbox', 'Cloud_Computing', 'Generative_AI', 'Microsoft_Cloud', 'Office_365', 'Dynamics_365', 'LinkedIn', 'Microsoft_Power_Platform', 'Azure_AI', 'OpenAI', 'GitHub', 'Windows_365', 'Azure_Orbital', 'Microsoft_Mesh', 'Microsoft_Intelligent_Data_Platform', 'GitHub_Copilot', 'Microsoft_Fabric', 'Cybersecurity', 'Sustainability', 'Digital_Skills_Initiative']
    insert_Topics(sheet=sheet, company_name=company, document_year=year, topics=company_dict[company], num_topics = company_dict[company]['topics'])
    time.sleep(60)