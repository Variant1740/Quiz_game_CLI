from services.quiz import Quiz
from services.mainapp import Quizgame, Game_rules, Registration

def start_app():
    user=Registration().register()
    Game_rules().show()

    quiz=Quiz()
    game=Quizgame(quiz)
    game.start()
    game.result(user.username)
    