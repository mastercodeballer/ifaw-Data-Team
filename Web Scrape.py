from bs4 import BeautifulSoup
import requests
animal_list = []
for i in range (1,55): #looping through each page of the animal for sale listings
    
    html_text = requests.get('https://www.exoticanimalsforsale.net/animalsforsale.asp?page=' + str(i)).text #getting to the right url depending on which page
    soup = BeautifulSoup(html_text, 'lxml') #defining beautifulsoup object to allow for easy parsing of html text
    animals = soup.find_all('div', class_ = "classifiedsListingRight") #finding every instance of class classifiedListingRight
    for animal in animals: 
        animal_name = animal.find('h2').text #the animal name was held under the html tag h2, so i'm pulling the name from there
        print(animal_name) #printing the name of each animal in the listings
        animal_list.append(animal_name)


