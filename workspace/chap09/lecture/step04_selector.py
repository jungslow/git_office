from bs4 import BeautifulSoup

# (1) 로컬 파일 읽기
file = open('d:/hello-git/workspace/chap09/data/html03.html', mode = 'r', encoding = 'utf-8')
source = file.read()

# (2) html 파싱
html = BeautifulSoup(source, 'html.parser')

# (3) 선택자 이용 태그 내용 가져오기
# (3-1) id = 'tab' 선택자
print('>> table 선택자 <<')
table = html.select_one('#tab')
print(table)

# (3-2) id 선택자와 계층
print('>> 선택자 & 계층 <<')
ths = html.select('#tab > tr > th')
print(ths)

# (3-3) class 선택자 : tr tag class = 'odd'
trs = html.select('#tab > .odd')
print('>> class 선택자  <<')
print(trs)

# (4) 태그[속성=값] 찾기
trs = html.select('tr[class=odd]')

# (5) td 태그 내용
print('>> tr > td 출력 <<')
for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)

