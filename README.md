# R-D-Innovation-Correlation

Objective of the research: To find a correlation between the number of times the research and development area was mentioned in the quarter/fiscal report and the revenue that came from that innovation.


HTML Folder:
-Contains major companies 10-K for the year of 2022.

Jupyter Notebook files:
    -createCompnayTable:
        For a specific company, such as "Dell," I extract all the information mentioned in the "Business" sector of the 10-K report. Using the OpenAI API, I prompt it to extract a set of DBpedia topics from the text related to the company's R&D activities. I then create a CSV file that holds potential topics for the R&D of that company.
    -GroupTopics:
        Extract information from files like "microsoft_response2021.txt." Utilizing the OpenAI API, I prompt it to organize a provided list of topics into major R&D categories.
    -AnalyzePatents:
        I collected information for Microsoft from 2018 to 2022. I counted how many times specific topics were mentioned throughout those years in Microsoft's reports. I filtered the data by removing all topics that were mentioned fewer than 2 times. I then plotted the topics that were mentioned most frequently, as well as the number of topics mentioned per year.
    -GetResearch3.0-2:
        For a company like "Dell," I pull  information from the "Business" section of its 10-K report. Then, using the OpenAI API, I extract topics related to the company's R&D activities.(This step is used in createCompanyTable) I also extract companies R&D expenses that are stated in the 10-K.
    -GetStock:
        Using the yfinance library, I extract data related to companies' stock prices. I've created a hardcoded dictionary containing topics related to Microsoft's R&D. I then plot the trend of Microsoft's stock price alongside the trends in Microsoft's R&D topics.
