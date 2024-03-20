import gspread
from google.oauth2.service_account import Credentials


def insert_Topics(sheet, company_name, document_year, topics):
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
    first_column_values = sheet.col_values(1)
    first_row_values = sheet.row_values(1)

    num_rows = len(first_column_values) # number of rows
    num_columns = len(first_row_values) # num o

    sheet.update_cell(num_rows + 1, 1, company_name)
    sheet.update_cell(num_rows + 1, 2, document_year)

    for topic in topics:

        topic = topic.lower()
        cell = sheet.find(topic)

        if cell is None: #topic was not yet put in the columns

            sheet.update_cell(1, num_columns + 1, topic)
            sheet.update_cell(num_rows + 1, num_columns + 1, 1) #topic is presnet for that year in the report
            num_columns += 1

        else: #toppic is alreadye present in the first row

            sheet.update_cell(num_rows + 1, cell.col, 1)



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

# company_name = "Microsoft"
# year = "2023"
# topics =  ['Artificial_Intelligence', 'Microsoft_Teams', 'Microsoft_Outlook', 'Bing_(search_engine)', 'Xbox', 'Cloud_Computing', 'Generative_AI', 'Microsoft_Cloud', 'Office_365', 'Dynamics_365', 'LinkedIn', 'Microsoft_Power_Platform', 'Azure_AI', 'OpenAI', 'GitHub', 'Windows_365', 'Azure_Orbital', 'Microsoft_Mesh', 'Microsoft_Intelligent_Data_Platform', 'GitHub_Copilot', 'Microsoft_Fabric', 'Cybersecurity', 'Sustainability', 'Digital_Skills_Initiative']
# insert_Topics(sheet=sheet, company_name=company_name, document_year=year, topics=topics)

# company_name = "Microsoft"
# year = "2022"
# topics = ['Cloud_computing', 'Artificial_intelligence', 'Mixed_reality', 'Video_game_console', 'Software_development', 'Sustainability', 'Digital_transformation', 'Azure_(cloud_service)', 'Microsoft_Teams', 'LinkedIn', 'Quantum_computing', 'Cybersecurity', 'Xbox_(console)', 'Operating_system']
# insert_Topics(sheet=sheet, company_name=company_name, document_year=year, topics=topics)

# company_name = "Microsoft"
# year = "2021"
# topics =  ['Cloud_computing', 'Artificial_intelligence', 'Internet_of_Things', 'Mixed_reality', 'Azure_(cloud_service)', 'Microsoft_365', 'Microsoft_Teams', 'LinkedIn', 'Dynamics_365', 'Windows_10', 'Xbox_(console)', 'Microsoft_Surface', 'Microsoft_Research', 'Digital_transformation']
# insert_Topics(sheet=sheet, company_name=company_name, document_year=year, topics=topics)

# company_name = "Microsoft"
# year = "2020"
# topics = ['Artificial_intelligence', 'Internet_of_Things', 'Mixed_reality', 'Cloud_computing', 'Machine_learning', 'Software_development', 'Video_games', 'Digital_transformation', 'Cybersecurity', 'Quantum_computing', 'Remote_work', 'Virtual_reality', 'Big_data', 'Sustainability']
# insert_Topics(sheet=sheet, company_name=company_name, document_year=year, topics=topics)