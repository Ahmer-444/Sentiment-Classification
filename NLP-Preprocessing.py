'''
Description:    Standalone file can be used for text pre-processing in NLP. 
'''


import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer


html_tag = '<[^<>]+>'
number_tag = '[0-9]+'
url_tag = '(http|https)://[^\s]*'
emailaddr_tag ='[^\s]+@[^\s]+'
currency_tag = '[$]+'
alphanumeric_tag = '[^a-zA-Z0-9]'

f = open('emailSample1.txt','r')
email = f.read()
f.close()

email = email.lower()

'''
% Strip all HTML
% Looks for any expression that starts with < and ends with > and replace
% and does not have any < or > in the tag it with a space
'''
email = re.sub(html_tag,' ', email)

'''
% Handle Numbers
% Look for one or more characters between 0-9
'''
email = re.sub(number_tag,'number', email)

'''
% Handle URLS
% Look for strings starting with http:// or https://
'''
email = re.sub(url_tag,'httpaddr', email)

'''
% Handle Email Addresses
% Look for strings with @ in the middle
'''
email = re.sub(emailaddr_tag,'emailaddr', email)

'''
Handle $ sign
'''
email = re.sub(currency_tag,'dollar', email)

'''
% Remove any non alphanumeric characters
'''
#email = re.sub(alphanumeric_tag,'', email) 

tokenizer = RegexpTokenizer(r'\w+')
email = tokenizer.tokenize(email)
 
ps = PorterStemmer()
email = [ps.stem(word).encode('utf-8') for word in email]
    
#print email

print(' '.join(email))
