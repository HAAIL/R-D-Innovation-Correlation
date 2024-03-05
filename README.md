# R-D-Innovation-Correlation

## Objective of the Research
To explore the correlation between the frequency of mentions of the research and development area in quarterly/fiscal reports and the revenue generated from that innovation.

## Methodology

My study focuses on analyzing companies R&D activities for a certain time period through two main approaches.

Approach 1: Analyzing 10-K Filings
1. Extracting Topics: I start by reviewing Microsoft's 10-K filings to pull out key topics from the "Business" and "Risk Factors" sections.
2. Matching Topics with DBPedia: Using OpenAI's GPT model, I link these topics to related DBPedia entries that describe Microsoft's R&D efforts.
3. Organizing R&D Topics: I create a comprehensive dictionary of R&D topics identified from the 10-K filings, organized by year, to track Microsoft's R&D focus over time.

Approach 2: Using ChatGPT and Patent Data
1. Identifying R&D Topics with ChatGPT: I use ChatGPT to list the R&D topics for a specific year.
2. Collecting Patent Filings: I access Microsoft's patent filings through the USPTO API for the selected year to gather additional data.
3. Classifying Patents: Each patent is sorted into a predefined R&D topic category based on its abstract, helping us see how Microsoft's patents align with the R&D topics I've identified. I categorize each patent given its title and description into a specified category, producing a focused output.

## Contents

### Boeing-10k
- Contains  Boeing's 10-K reports for the 2020-2023 years.

### Microsoft-10k
- Contains  Microsoft's 10-K reports for the 2020-2023 years.

### Nvidiat-10k
- Contains  Nvidia's 10-K reports for the 2020-2023 years.

### microsoft_10k Folder
- This code reads HTML documents for different years related to Microsoft, extracts and processes text from these documents, and then uses a language model to extract DBPedia topics related to Microsoft's research and development activities for each year. It organizes and prints these topics with their corresponding years.(subject to change)

### Jupyter Notebook Files

### Link to Google Colab where you can execute code on your own
- https://colab.research.google.com/drive/1QVYr-ResjKPBTRehMSWiIQk5BgyT-TvE#scrollTo=nSp_IdSi7aoZ
