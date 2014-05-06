#!/usr/bin/python

import sys

contents = open('printed_contacts.txt').read()

contacts = []
current = dict()
for entry in contents.split('\n'):
  if not entry:
    continue
  if '@' not in entry:
    if current:
      contacts.append(current)
    current = dict()
    current['name'] = entry.strip()
  else:
    if 'email' not in current:
      current['email'] = []
    current['email'].append(entry.strip())
if current:
  contacts.append(current)

l = reduce(max, [len(contact['email']) for contact in contacts if 'email' in contact])
if l > 3:
  print 'Unsure how to import >3 emails'
  sys.exit()

header = "Name"
for i in xrange(l):
  if i == 0:
    header += ',E-mail Address'
  else:
    header += ',E-mail %d Address' % (i+1,)

print header
for c in contacts:
  elms = []
  elms.append(c['name'])
  if 'email' in c:
    elms.extend(c['email'])
  while len(elms) < l + 1:
    elms.append('')
  print ','.join(elms)
