import json

file_path = '../create_data/fortune1000/fortune1000_2019.txt'

with open(file_path, 'r') as file:
    # for every company
    for company_name in file:
        company_name=company_name.strip()
        file_path = '/Users/mikhaillemper/Desktop/GradSchool/Spring24/Research/patent_data/2019.jsonl'
        # Open the file
        count = 0
        with open(file_path, 'r') as file:

            for line in file:
                # Parse the JSON data from the current line
                try:
                    data = json.loads(line)
                except json.decoder.JSONDecodeError:
                    pass
                #        data = json.loads(line)
                try:
                    # print(data['assignee'])
                    # print(company_name.lower())
                    # print(data['assignee'].lower())
                    if company_name.lower() in data['assignee'].lower() or data['assignee'].lower() in company_name.lower():
                        # print(line)
                        count += 1
                        # if 'artificial intelligence' in data['openalex_concepts_with_chains']:
                        #     print(line)
                        #     count += 1
                except:
                    pass

        print(company_name, ":", count)
