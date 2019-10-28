## VERSION2 --> Now set at what time to send a message :)
## WORKING CHECKED ON 1-12-2019
## Be sure that your chrome driver is upto dated --> This irrated me a lot :/
## Support me plz
"""
On your PC set up everything upto Bar code scaner and then leave your mobile data and PC internet connection live.
It will automatically send the message at the time specified.
Note:--> Time is of your current location or your PC current time.

"""

from time import localtime
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

print("\nEnter year like 2019\nMonth like 1\nDay like 1\nWhere 1 means jan for month\n")

year = int(input("which year to send message? "))
month = int(input("Which month to send message? "))
day = int(input("Which day to send message? "))

hour = int(input("Enter hour of the day in 24 hours format ex 13 for 1 am--> "))
minu = int(input("Minute of the hour 0-59--> "))
sec = int(input("Second of hour 0-59--> "))

work_not_done = True
print("\nScript is running normally\n")
while work_not_done:
    if year == localtime()[0] and month == localtime()[1] and day == localtime()[2] and hour == localtime()[3] and minu == localtime()[4] and sec == localtime()[5]:
        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()
        work_not_done = False
        print("Your message "+str(msg)+" has been sent to "+str(name)+" "+str(count)+" times successfully.")
