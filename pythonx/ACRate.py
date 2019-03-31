import vim
import requests
from bs4 import BeautifulSoup

def GetRate():
    username = vim.eval('$ATCODER_USERNAME')
    r = requests.get('https://beta.atcoder.jp/users/{0}'.format(username))
    soup = BeautifulSoup(r.text,"html.parser")
    rating = soup.find_all("table",attrs = {'class' : 'dl-table'})[1].find_all("tr")[1].find("span").text
    vim.vars['AtCoderRating'] = rating
    vim.vars['airline_section_c'] = '%<%<%{airline#extensions#fugitiveline#bufname()}%m %#__accent_red#%{airline#util#wrap(airline#parts#readonly(),0)}%#__restore__#[' + str(username) + ':%{g:AtCoderRating}]'
    vim.command('AirlineRefresh')
