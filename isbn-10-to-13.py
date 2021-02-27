#! /usr/bin/env python

# This python script converts ISBN-10 to ISBN-13 code
# Based on information found here :
#   https://isbn-information.com/convert-isbn-10-to-isbn-13.html
# 
# Usage : isbn-10-to-13 code code code ...
#
# Created by Jose-Marcio Martins da Cruz
#    martins@jose-marcio.org
# Distributed under GPL licence

import sys
import re

def isbn10to13(si):
  s = si.replace("-", "")
  if not re.match("^[0-9]{9}[0-9X]$", s):
    s = "This isn't an ISBN-10 code"
    return s
  s = "978" + s[:-1]
  sum = 0
  for i in range(0, len(s)):
    m = 1 + 2 * (i % 2)
    sum += m * int(s[i])
  sum = (10 - sum % 10) % 10
  sout = '978-' + si[:-1] + str(sum)
  return sout

sys.argv.pop(0)
for arg in sys.argv:
  print("{:<13s} {:s}".format(arg, isbn10to13(arg)))


