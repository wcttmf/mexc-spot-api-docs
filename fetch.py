import os, shutil, requests, bs4

doc_dir = './docs'

os.makedirs(doc_dir, exist_ok=True)
shutil.rmtree(doc_dir)
os.makedirs(doc_dir, exist_ok=True)

soup = bs4.BeautifulSoup(requests.get('https://mexcdevelop.github.io/apidocs/spot_v3_en').content, 'lxml')

group_count = 0
group_id = None
append_to = None
for e in soup.find('div', { 'class': 'page-wrapper' }).find('div', { 'class': 'content' }):
  if e.name == 'h1':
    group_count += 1
    fcount = 0
    group_id = e['id']
  if not group_id:
    continue
  if e.name == 'h2':
    fcount += 1
    append_to = f'{doc_dir}/{group_count:02}-{group_id}/{fcount:02}-{e['id']}.html'
  if not append_to:
    continue
  os.makedirs(f'{doc_dir}/{group_count:02}-{group_id}', exist_ok=True)
  with open(append_to, 'a') as f:
    f.write(str(e))
