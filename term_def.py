from bs4 import BeautifulSoup
import requests

def get_term_definition(fin_term):

    url = "https://www.investopedia.com/terms/" + fin_term[0].lower() + "/" + fin_term.lower() + ".asp"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    s = soup.find('p', id = "mntl-sc-block_1-0-1", class_ = "comp mntl-sc-block finance-sc-block-html mntl-sc-block-html")

    #print(s.prettify())
    definition = ''.join(s.stripped_strings)

    #print(definition)

    return definition

#print(get_term_definition("gametheory"))
