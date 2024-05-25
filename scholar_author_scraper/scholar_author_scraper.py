import scholarly
import json

def get_researcher_papers(researcher_name):
    # Search for the researcher
    search_query = scholarly.search_author(researcher_name)
    author = next(search_query, None)
    
    if not author:
        print(f"No researcher found with the name {researcher_name}")
        return
    
    # Fill in the details for the researcher
    author = scholarly.fill(author)
    
    # Extract papers details
    papers = []
    for pub in author['publications']:
        publication = scholarly.fill(pub)
        paper_details = {
            "title": publication.get('bib', {}).get('title', ''),
            "author": publication.get('bib', {}).get('author', ''),
            "venue": publication.get('bib', {}).get('venue', ''),
            "year": publication.get('bib', {}).get('pub_year', ''),
            "abstract": publication.get('bib', {}).get('abstract', ''),
            "url": publication.get('pub_url', ''),
            "citations": publication.get('num_citations', 0),
            "cites_per_year": publication.get('cites_per_year', {})
        }
        papers.append(paper_details)
    
    return papers

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    researcher_name = input("Enter the researcher's name: ")
    papers = get_researcher_papers(researcher_name)
    
    if papers:
        save_to_json(papers, f"{researcher_name.replace(' ', '_')}_papers.json")
        print(f"Details of papers by {researcher_name} saved to {researcher_name.replace(' ', '_')}_papers.json")
    

if __name__ == "__main__":
    main()
    
