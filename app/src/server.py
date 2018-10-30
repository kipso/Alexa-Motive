

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import sys

app = Flask(__name__)

ask = Ask(app, "/motivation_quotes")

def getMotivation():
	url = "http://api.adviceslip.com/advice"
	response = requests.get(url)
	print(response.json()['slip']['advice'])
	return (response.json()['slip']['advice'])

@app.route('/')
def homepage():
	return "Alexa skill is running."

@ask.launch
def startSkill():
    quote = getMotivation()
    response = quote + '...... mmmmmmm ......... Do you want more?'
    print(response)
    return question(response)

@ask.intent("YesIntent")
def shareQuote():
    quote = getMotivation()
    response = quote + '...... mmmmmmm ......... Do you want more?'
    print(response)
    return question(response)

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Bye then...... Have a great day'
    print(byeText)
    return statement(byeText)