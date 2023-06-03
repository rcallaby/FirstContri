import requests
from bs4 import BeautifulSoup

username = input("Username/Org: ")
repo = input("Repo: ")
print("1. Good First Issue\n2. Documentation\n3. All Issues")
inp = input("Type No: ")

iurl = f'https://github.com/{username}/{repo}'
all_url = f'{iurl}/issues'
gfi_url = f'{iurl}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22'
doc_url = f'{iurl}/issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation'

res_all = requests.get(all_url)
res_gfi = requests.get(gfi_url)
res_doc = requests.get(doc_url)

if inp == '1':
    soup_gfi = BeautifulSoup(res_gfi.text, 'html.parser')
    issues = soup_gfi.find_all('a', {'class': 'Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title'})

    print(f'{len(issues)} good first issues found:\n')
    for issue in issues:
        title = issue.text.strip()
        number = int(issue['href'].split('/')[-1])
        url = f'{iurl}/issues/{number}'
        tags = issue.parent.find_all('a', {'class': 'IssueLabel hx_IssueLabel'})
        tags_str = ', '.join([tag.text for tag in tags])
        print(f'Issue No: {number}\nTitle: {title}\nLink: {url}\n')

elif inp == '2':
    soup_doc = BeautifulSoup(res_doc.text, 'html.parser')
    issues = soup_doc.find_all('a', {'class': 'Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title'})

    print(f'{len(issues)} documentation issues found:\n')
    for issue in issues:
        title = issue.text.strip()
        number = int(issue['href'].split('/')[-1])
        url = f'{iurl}/issues/{number}'
        tags = issue.parent.find_all('a', {'class': 'IssueLabel hx_IssueLabel'})
        tags_str = ', '.join([tag.text for tag in tags])
        print(f'Issue No: {number}\nTitle: {title}\nLink: {url}\n')

elif inp == '3':
    page = 1
    while True:
        url = f'{all_url}?page={page}'
        res_all = requests.get(url)
        soup_all = BeautifulSoup(res_all.text, 'html.parser')
        issues = soup_all.find_all('a', {'class': 'Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title'})

        if not issues:
            break

        print(f'{len(issues)} total issues found on page {page}:\n')
        for issue in issues:
            title = issue.text.strip()
            number = int(issue['href'].split('/')[-1])
            url = f'{iurl}/issues/{number}'
            tags = issue.parent.find_all('a', {'class': 'IssueLabel hx_IssueLabel'})
            tags_str = ', '.join([tag.text for tag in tags])
            print(f'Issue No: {number}\nTitle: {title}\nLink: {url}\n')

        page += 1

else:
    print("Type the correct number.")
