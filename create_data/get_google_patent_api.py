from serpapi import GoogleSearch

params = {
  "engine": "google_patents",
  "q": "(Coffee)",
  "before" : "publication:20240101",
  "after":"publication:20230101",
  "assignee":"Microsoft",
  "patent_status":"GRANT",
  "type":"PATENT",
  "dups": "language",
  "api_key": "API-KEY"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(organic_results)






# Documentation:
#https://serpapi.com/google-patents-api