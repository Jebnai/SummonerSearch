# using selenium for browser automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# user input for summoner name
search = input("Enter summoner name: ")

# opens the browser
driver = webdriver.Chrome()

# opens the website and makes sure the <title> tag is specified
driver.get("https://euw.op.gg/")
assert "OP.GG" in driver.title

# locate the summoner search bar
element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/input")

# types in the user input and "hits" the enter key to search
element.send_keys(search)
element.send_keys(Keys.RETURN)

# stall the execution to allow the full page to load
time.sleep(2)

# locates the rank and the lp the summoner is on
rank = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[2]')
if rank.text != "Unranked":
    lp = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[1]')

    # prints out the rank and the lp
    print("Your rank is: " + rank.text + " " + lp.text)
else:
    print("You are unranked")
# for loop to go through summoners most played champions and their win ratios
for i in range(1, 8):
    champion_xpath = '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[{0}]/div[2]/div[1]'
    win_rate_xpath = '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[{0}]/div[4]/div[1]'
    champions = driver.find_element_by_xpath(champion_xpath.format(i))
    win_rate = driver.find_element_by_xpath(win_rate_xpath.format(i))
    print(champions.text + ": " + win_rate.text + " win ratio")

# close the browser driver
driver.close()
