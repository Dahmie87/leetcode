from bs4 import BeautifulSoup
import requests
my_url = "https://www.w3schools.com/django/django_intro.php"
my_reponse = requests.get(my_url)
# print(my_reponse.content)
my_soup = BeautifulSoup(my_reponse.content, "html.parser")

# print(my_soup.find("head"))
url_body = my_soup.body
print(url_body.get_text())
