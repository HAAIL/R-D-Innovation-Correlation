# R-D-Innovation-Correlation

## Objective of the Research
To explore the correlation between the frequency of mentions of the research and development area in quarterly/fiscal reports and the revenue generated from that innovation.

## Contents

### HTML Folder
- Contains the 10-K reports for major companies for the year 2022.

### Jupyter Notebook Files

#### `createCompanyTable`
- For a specific company, such as "Dell," this notebook extracts all information mentioned in the "Business" sector of the 10-K report. Using the OpenAI API, it extracts a set of DBpedia topics related to the company's R&D activities and creates a CSV file containing potential R&D topics for that company.

#### `GroupTopics`
- This notebook extracts information from files like "microsoft_response2021.txt." Using the OpenAI API, it organizes a given list of topics into major R&D categories.

#### `AnalyzePatents`
- This notebook gathers information for Microsoft from 2018 to 2022, counting how many times specific topics were mentioned in Microsoft's reports over the years. It filters out topics mentioned fewer than 2 times and plots the most frequently mentioned topics and the number of topics mentioned per year.

#### `GetResearch3.0-2`
- Similar to `createCompanyTable`, for a company like "Dell," this notebook pulls information from the "Business" section of its 10-K report and uses the OpenAI API to extract topics related to the company's R&D activities, including R&D expenses stated in the 10-K.

#### `GetStock`
- Using the yfinance library, this notebook extracts data related to companies' stock prices. It utilizes a hardcoded dictionary containing topics related to Microsoft's R&D and plots the trend of Microsoft's stock price alongside the trends in Microsoft's R&D topics.
