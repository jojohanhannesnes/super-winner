from bs4 import BeautifulSoup
import os

with open('exercism.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

a_tags = soup.find_all('a')

for a_tag in a_tags:
    href = a_tag.get('href')
    if href:
        exercise_name = os.path.basename(href)
        print(exercise_name)

