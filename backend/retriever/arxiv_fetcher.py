import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_abstracts(query, max_results=5):
    url = f'http://export.arxiv.org/api/query?search_query={query}&max_results={max_results}'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    abstracts = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        abstracts.append(f"Title: {title}\nAbstract: {summary}")
    return abstracts