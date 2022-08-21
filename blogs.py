from bs4 import BeautifulSoup
import requests

class Blogs():
    
    def get_blogs():
        #first trimester ----------------------
        response1 = requests.get("https://pregnantchicken.com/first-trimester/")
        first_trimester = response1.text
        #print(first_trimester)

        soup1 = BeautifulSoup(first_trimester,"html.parser")
        articles = soup1.find_all(name='a', class_ ="post-card__image")
        #print(articles)

        links1 = []
        titles1 = []
        info1 = []

        for article_tag in articles:
            link= article_tag.get("href")
            article_link = f"https://pregnantchicken.com{link}"
            links1.append(article_link)
            article_title = article_tag.get("title")
            titles1.append(article_title)

            response = requests.get(article_link)
            data = response.text
            
            soup =  BeautifulSoup(data,"html.parser")
            para = soup.find(name='div', class_ = "post__content")
            data = para.find('p')
            info1.append(data.getText())

        images =  soup1.find_all(name="img",class_="lazyload")
        img1 = []

        for image in images:
            link = image.get("data-src")
            img_link= f"https://pregnantchicken.com{link}"
            img1.append(img_link)

        final_list1 = []

        for i in range(len(info1)):
            final_list1.append([titles1[i],links1[i],info1[i],img1[i]])

        # print(final_list1[0])

        return(final_list1)

    def Food():
        response4 = requests.get("https://pregnantchicken.com/food/")
        food = response4.text

        soup4 = BeautifulSoup(food,"html.parser")
        articles = soup4.find_all(name='a', class_ ="post-card__image")
        #print(articles)
        links4 = []
        titles4 = []
        img4 = []
        info4= []
        for article_tag in articles:
            link= article_tag.get("href")
            article_link = f"https://pregnantchicken.com{link}"
            links4.append(article_link)
            article_title = article_tag.get("title")
            titles4.append(article_title)

            response = requests.get(article_link)
            data = response.text
            
            soup =  BeautifulSoup(data,"html.parser")
            para = soup.find(name='div', class_ = "post__content")
            data = para.find('p')
            info4.append(data.getText())
                
        images =  soup4.find_all(name="img",class_="lazyload")

        for image in images:
            link = image.get("data-src")
            img_link= f"https://pregnantchicken.com{link}"
            img4.append(img_link)

        final_list1 = []

        for i in range(len(info4)):
            final_list1.append([titles4[i],links4[i],info4[i],img4[i]])

        # print(final_list1[0])

        return(final_list1)

    def Health():
        response7 = requests.get("https://pregnantchicken.com/mental-health/")
        fun_stuff = response7.text

        soup7 = BeautifulSoup(fun_stuff,"html.parser")
        articles = soup7.find_all(name='a', class_ ="post-card__image")
        #print(articles)
        links7 = []
        titles7 = []
        img7 = []
        info7= []
        for article_tag in articles:
            link= article_tag.get("href")
            article_link = f"https://pregnantchicken.com{link}"
            links7.append(article_link)
            article_title = article_tag.get("title")
            titles7.append(article_title)

            response = requests.get(article_link)
            data = response.text
            
            soup =  BeautifulSoup(data,"html.parser")
            para = soup.find(name='div', class_ = "post__content")
            data = para.find('p')
            info7.append(data.getText())
                
        images =  soup7.find_all(name="img",class_="lazyload")

        for image in images:
            link = image.get("data-src")
            img_link= f"https://pregnantchicken.com{link}"
            img7.append(img_link)

        
        final_list1 = []

        for i in range(len(info7)):
            final_list1.append([titles7[i],links7[i],info7[i],img7[i]])

        # print(final_list1[0])

        return(final_list1)


''''
#second-trimester-------------------------

response2 = requests.get("https://pregnantchicken.com/second-trimester/")
second_trimester = response2.text
#print(first_trimester)
soup2 = BeautifulSoup(second_trimester,"html.parser")
articles = soup2.find_all(name='a', class_ ="post-card__image")
#print(articles)
links2 = []
titles2 = []
img2 = []
info2 = []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links2.append(article_link)
    article_title = article_tag.get("title")
    titles2.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info2.append(data.getText())

images =  soup2.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img2.append(img_link)

#------------------------3rd Trimester------------------------

response3 = requests.get("https://pregnantchicken.com/third-trimester/")
third_trimester = response3.text
#print(first_trimester)
soup3 = BeautifulSoup(third_trimester,"html.parser")
articles = soup3.find_all(name='a', class_ ="post-card__image")
#print(articles)
links3 = []
titles3 = []
img3 = []
info3= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links3.append(article_link)
    article_title = article_tag.get("title")
    titles3.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info3.append(data.getText())
        
    

images =  soup3.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img3.append(img_link)

#-------------FOOD----------------------

response4 = requests.get("https://pregnantchicken.com/food/")
food = response4.text

soup4 = BeautifulSoup(food,"html.parser")
articles = soup4.find_all(name='a', class_ ="post-card__image")
#print(articles)
links4 = []
titles4 = []
img4 = []
info4= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links4.append(article_link)
    article_title = article_tag.get("title")
    titles4.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info4.append(data.getText())
        
    

images =  soup4.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img4.append(img_link)

print(img4)
print(info4)
print(titles4)
print(links4)


#----------C Section--------------

response5 = requests.get("https://pregnantchicken.com/c-section/")
c_section = response5.text

soup5 = BeautifulSoup(c_section,"html.parser")
articles = soup5.find_all(name='a', class_ ="post-card__image")
#print(articles)
links5 = []
titles5 = []
img5 = []
info5= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links5.append(article_link)
    article_title = article_tag.get("title")
    titles5.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info5.append(data.getText())
        
    

images =  soup5.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img5.append(img_link)

#----------FUN-STUFF-------------

response6 = requests.get("https://pregnantchicken.com/fun-stuff/")
fun_stuff = response6.text

soup6 = BeautifulSoup(fun_stuff,"html.parser")
articles = soup6.find_all(name='a', class_ ="post-card__image")
#print(articles)
links6 = []
titles6 = []
img6 = []
info6= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links6.append(article_link)
    article_title = article_tag.get("title")
    titles6.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info6.append(data.getText())
        
    

images =  soup6.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img6.append(img_link)

#------Mental Health-------------

response7 = requests.get("https://pregnantchicken.com/mental-health/")
fun_stuff = response7.text

soup7 = BeautifulSoup(fun_stuff,"html.parser")
articles = soup7.find_all(name='a', class_ ="post-card__image")
#print(articles)
links7 = []
titles7 = []
img7 = []
info7= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links7.append(article_link)
    article_title = article_tag.get("title")
    titles7.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info7.append(data.getText())
        
    

images =  soup7.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img7.append(img_link)


#---------POSTPARTUM------------

response8 = requests.get("https://pregnantchicken.com/postpartum/")
postpartum = response8.text

soup8 = BeautifulSoup(fun_stuff,"html.parser")
articles = soup8.find_all(name='a', class_ ="post-card__image")
#print(articles)
links8 = []
titles8 = []
img8 = []
info8= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links8.append(article_link)
    article_title = article_tag.get("title")
    titles8.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info8.append(data.getText())
        
    

images =  soup8.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img8.append(img_link)

#-----Morning Sickness--------

response9 = requests.get("https://pregnantchicken.com/morning-sickness/")
postpartum = response9.text

soup9 = BeautifulSoup(fun_stuff,"html.parser")
articles = soup9.find_all(name='a', class_ ="post-card__image")
#print(articles)
links9 = []
titles9 = []
img9 = []
info9= []
for article_tag in articles:
    link= article_tag.get("href")
    article_link = f"https://pregnantchicken.com{link}"
    links9.append(article_link)
    article_title = article_tag.get("title")
    titles9.append(article_title)

    response = requests.get(article_link)
    data = response.text
    
    soup =  BeautifulSoup(data,"html.parser")
    para = soup.find(name='div', class_ = "post__content")
    data = para.find('p')
    info8.append(data.getText())
        
    

images =  soup9.find_all(name="img",class_="lazyload")

for image in images:
    link = image.get("data-src")
    img_link= f"https://pregnantchicken.com{link}"
    img9.append(img_link)
'''