from bs4 import BeautifulSoup
import re


#YOUR CODE 1
# open the "samplehtml.html" file and read it into a string
# No ouptput

#handle that points to a file
f = open('samplehtml.html', "r")
#turns pointer into an object that can be scanned etc
text_data_from_file = f.read()
f.close()

#YOUR CODE 2
# create a BeautifulSoup object from the string
# No output
soup = BeautifulSoup(text_data_from_file, "lxml")

#YOUR CODE 3
# Write/plan code to print the URL to the XKCD comic, using BSoup and this file.
imgs = soup.find_all("img")
xkcd_img = imgs[0]

print(xkcd_img["src"])
print("\n")

#YOUR CODE 4
# Write code to grab all the links (URLs) in that html page, but nothing else.
urls = soup.find_all("a")
for url in urls:
	print(url["href"])
print("\n")

#YOUR CODE 5
# Write/plan code to grab the TEXT of all the links in that html page, but nothing else.
for url in urls:
	print(url.text)

print("\n")
#YOUR CODE 6
# Write/plan code to grab the text of each of the items in the ordered list. (Not the 1/2/2, just the text. 
lst = soup.find_all("li")
for item in lst:
	print(item.text)

print("\n")
#YOUR CODE 7
# - Write/plan code to grab the alt text associated with the image of the XKCD comic.
# see way above for accessing xkcd_img...
# OUTPUT - 
print(xkcd_img["aria-text"])


print("\n")
#YOUR CODE 7
# Write  code to assign the BeautifulSoup object holding the div that contains the image to a variable `image_div_obj` 
#Ouput: print image_div_obj
image_div_obj = soup.find_all("img")
print(image_div_obj)


print("\n")
#YOUR CODE 8
# - Write/plan code to add these three strings to a list, using just BSoup and the html doc available…
#   > An image from the comic XKCD below.
#   > Find more similar stuff at the comic web site.
#   > Or just check out your homework after you sign into Canvas.

# first, get the thing that contains them all, the span! store in variable names span_container
span_container = soup.find_all("span")
# print span_conainer
print(span_container)


#second, get all of the paragraphs in the span_container and store in a variable called paragraph_tags
paragraph_tags = []
for tag in span_container:
	if tag == "p":
		paragraph_tags.append(tag)
# print paragraph_tags

#third: print all of the text in the paragraphs.  Consider using strip(), rstrip(), etc.
