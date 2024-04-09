import json

file_path = '../create_data/fortune1000/company_with_patents.txt'
company_dict = {}
with open(file_path, 'r') as file:
    # for every company
    for company_name in file:
        company_name=company_name.strip()
        file_path = '/Users/mikhaillemper/Desktop/GradSchool/Spring24/Research/patent_data/2019.jsonl'
        # Open the file
        count = 0
        #making dictionary where key: company; value dict [key: topic, value: count]
        company_dict[company_name] = {}
        with open(file_path, 'r') as file:

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
                            else:
                                company_dict[company_name][topic] = 1
                        #count += 1
                        # if 'artificial intelligence' in data['openalex_concepts_with_chains']:
                        #     print(line)
                        #     count += 1
                except:
                    pass
        break
    for key,val in company_dict.items():
        print(key, ": ", val)
        #print(company_name, ":", count)
