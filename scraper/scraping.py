import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def extract_contact_info(soup):
    phone_numbers = set()
    emails = set()

    text = soup.get_text()
    
    phone_pattern = re.compile(r'\(?\b[2-9][0-9]{2}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    phone_numbers.update(phone_pattern.findall(text))
    emails.update(email_pattern.findall(text))

    return {
        'phone_numbers': list(phone_numbers),
        'emails': list(emails),
    }

def extract_location(soup):
    location_keywords = ['address', 'location', 'headquarters', 'office']
    location_text = ''

    for keyword in location_keywords:
        # Search for keywords in text
        for element in soup.find_all(text=re.compile(keyword, re.IGNORECASE)):
            location_text += ' ' + element.parent.get_text(separator=' ', strip=True)
        
        # Search for keywords in attributes
        for attr in ['class', 'id', 'name', 'itemprop']:
            elements = soup.find_all(attrs={attr: re.compile(keyword, re.IGNORECASE)})
            for element in elements:
                location_text += ' ' + element.get_text(separator=' ', strip=True)
                
    return location_text.strip() if location_text else 'N/A'

def scrape_about_page(base_url):
    about_paths = ['/about/', '/about_us/']
    for path in about_paths:
        try:
            about_url = urljoin(base_url, path)
            response = requests.get(about_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            about_text = soup.find('p').get_text() if soup.find('p') else 'N/A'
            contact_info = extract_contact_info(soup)
            location = extract_location(soup)

            return {
                'about_company': about_text,
                'contact_info': contact_info,
                'location': location,
            }
        except Exception:
            continue
    return {'about_company': 'N/A', 'contact_info': {'phone_numbers': [], 'emails': []}, 'location': 'N/A'}

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        title_tag = soup.find('title')
        company_name = title_tag.get_text() if title_tag else 'N/A'

        logo_url = soup.find('link', rel='icon') or soup.find('link', rel='shortcut icon')
        
        main_contact_info = extract_contact_info(soup)
        main_location = extract_location(soup)
        about_info = scrape_about_page(url)

        # Merge contact info from main page and about page
        all_phone_numbers = set(main_contact_info['phone_numbers']).union(set(about_info['contact_info']['phone_numbers']))
        all_emails = set(main_contact_info['emails']).union(set(about_info['contact_info']['emails']))

        return {
            'company_name': company_name,
            'logo_url': logo_url['href'] if logo_url else 'N/A',
            'about_company': about_info['about_company'],
            'contact_info': {
                'phone_numbers': list(all_phone_numbers),
                'emails': list(all_emails),
            },
            'location': main_location if main_location != 'N/A' else about_info['location'],
        }
    except Exception as e:
        return {'error': str(e)}
