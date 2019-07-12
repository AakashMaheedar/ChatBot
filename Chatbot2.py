import re
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
f = open('E:\\ProjectWork\\ImranV.1.0\\dataset.txt','r')

train_data = []

for line in f:
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])

chatbot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter", #allows the chat bot to connect to SQL databases
    input_adapter="chatterbot.input.TerminalAdapter", #allows a user to type into their terminal to communicate with the chat bot.
    logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation',],
    output_adapter="chatterbot.output.TerminalAdapter", # print chatbot responce
    #database="../database.db"   # specify the path to the database that the chat bot will use
    database_uri='sqlite:///database.sqlite3'

)



trainer = ListTrainer(chatbot)
trainer.train(train_data)


print("Type your question here...")
while True:
    try:
        chatbot_input = chatbot.get_response(input("Type here: "))
        print(chatbot_input)
    # Press ctrl-c or ctrl-d to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    
