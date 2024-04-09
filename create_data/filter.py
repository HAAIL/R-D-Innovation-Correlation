import json

file_path = '../create_data/fortune1000/test.txt'

with open(file_path, 'r') as file:
    # for every company
    for company_name in file:
        company_name=company_name.split()
        if company_name[-1] != '0':
            separator = ' '  # Define the separator you want; in this case, a space character
            string_company_name = separator.join(company_name[0:-2])
            print(string_company_name)