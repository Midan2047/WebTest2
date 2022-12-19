#!C:\Users\KIM\AppData\Local\Programs\Python\Python39\python.exe
print("content-type: text/html; charset=utf-8\n")

import cgi, os

tag_id = 'id'
def getList():
    files = os.listdir('data/')
    listStr = ""
    for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr

form = cgi.FieldStorage()
if tag_id in form:
    pageId = form[tag_id].value
    description = open('data/'+pageId, 'r', encoding='UTF-8').read()
else:
    pageId = 'Welcome'
    description='Hello!'

html = '''<!DOCTYPE html>
  <html>
  <head>
    <title>WEB1.Home</title>
    <meta charset="utf-8">
  </head>

  <body>
    <h1><a href="index.py"><p style = "margin-top:25px;">WEB</p></a></h1>
    <ol>
      {listStr}
    </ol>
    <p style = "margin-top:35px;"> </p>  
    <h2>{title}</h2>
    <p>{desc}</P>
    <p style = "margin-top:100px;"> </p> 
    <form action="process_create.py" method="post">
        <p><input type = "text" name = "title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
  </body>
</html>
'''.format(title=pageId, desc=description, listStr=getList()) ##개미친 파이썬ㅗ^^ㅗ

print(html)

