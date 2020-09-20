from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='SamBot' read_only=True,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch']) 
list_trainer = ListTrainer(my_bot)
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


    
print(my_bot.get_response("hi")