import re


m = re.match('([0-9]+) ([0-9]+)', '10 295')
print(m)
print(m.groups())

m = re.search('(?P<we>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<ew>\w+)\)', 'print(1234)')
print(m)
print(m.group('we'))
print(m.group('ew'))

r = re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
print(r)

print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))
print(re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8'))

a=re.sub('([a-z]+) ([0-9]+)', r"\2 \1 \2 \1", 'hello 1234')
print(a)

a = re.sub('(\{\s*)"(\w+)":\s*"(\w+)"(\s*\})', r'<\2>\3</\2>', '{ "name": "james" }')
print(a)

a = re.sub(r'(\{\s*)\"(?P<key>\w+)\"\:\s*\"(?P<value>\w+)\"(\s*\})',
           r'<\g<key>>\g<value></\g<key>>', '{ "name": "james" }')
print(a)

a = re.sub(r'(\{\s*)\"(?P<key>\w+)\"\:\s*\"(?P<value>\w+)\"(\s*\})',
           r'<\g<2>>\g<3></\g<2>>', '{ "name": "james" }')
print(a)

a = re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})',
           r'<\2>\3</\2>', '{ "name": "james" }')
print(a)
print("wow")

print(re.match('[$()a-zA-Z0-9]+', '$(document)'))
print(re.match('({\$\([a-zA-Z0-9]+\)})', '{$(document)}'))

p = re.compile("^[a-zA-Z0-9+_.-]+@[a-zA-Z.-]+\.[a-z.]+")
emails = ['python@mail.example.com', 'python+kr@example.com',
          'python-dojang@example.co.kr', 'python_10@example.info',
          'python.dojang@e-xample.com',
          '@example.com', 'python@example', 'python@example=com']
for email in emails:
    print(p.match(email) != None, end=' ')

#print(re.search("Hello", ' Hello world!'))
print(re.match(r"\s*[a-zA-Z!]+", ' Hello world!'))

pattern=re.compile("^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+/[a-zA-Z0-9-_.?=/]+")
strs= ['http://www.example.com/hello/world.do?key=python', 'https://example/hello/world.html']
for str in strs:
    print(pattern.search(str) != None)