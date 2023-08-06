
import pyautogui
import os
from time import sleep
import pyperclip

def startupChrome(link):
    os.system("chrome "+link)
    sleep(5)

def webaction():
    while True:
        try:
            pyautogui.click("codePoint.png")
            break
        except:
            sleep(1)
    
    pyautogui.hotkey("ctrl","a")
    pyperclip.copy("""
    function start(){
    // Create a new form, then add a checkbox question, a multiple choice question,
// a page break, then a date question and a grid of questions.
var form = FormApp.create('New Form');
var item = form.addCheckboxItem();
item.setTitle('What condiments would you like on your hot dog?');
item.setChoices([
        item.createChoice('Ketchup'),
        item.createChoice('Mustard'),
        item.createChoice('Relish')
    ]);
form.addMultipleChoiceItem()
    .setTitle('Do you prefer cats or dogs?')
    .setChoiceValues(['Cats','Dogs'])
    .showOtherOption(true);
form.addPageBreakItem()
    .setTitle('Getting to know you');
form.addDateItem()
    .setTitle('When were you born?');
form.addGridItem()
    .setTitle('Rate your interests')
    .setRows(['Cars', 'Computers', 'Celebrities'])
    .setColumns(['Boring', 'So-so', 'Interesting']);
Logger.log('Published URL: ' + form.getPublishedUrl());
Logger.log('Editor URL: ' + form.getEditUrl());
}
    """)
    sleep(1)
    pyautogui.hotkey("ctrl","v")
    pyautogui.hotkey("ctrl","s")
    sleep(1)
    while True:
        try:
            pyautogui.click("runpicture.png")
            break
        except:
            sleep(1)
    sleep(1)
    while True:
        try:
            pyautogui.click("certification.png")
            break
        except:
            sleep(1)
    #認証の続きは後で書く

if __name__ == "__main__":
    startupChrome("https://script.google.com/home/projects/create")
    webaction()



