#quiz game!!!!!!!!!!
import time
import random
from loguru import logger
from models.user import User
from data.database import load_leaderboard, save_leaderboard
from datetime import datetime


class Registration:
    def register(self):
        logger.info("Creating a new account")
        Email=input('Enter an E-mail: ').strip().lower()
        username=input("Create username: ").strip()
        
        while True:
            password=input('Create a password(minimum of 8 characters): ')
            if len(password)<8:
                logger.error("Password length is too short, Must be atleast 8 characters long...")
                continue
            confirm=input('Confirm password: ')
            if password==confirm:
                logger.success("Account created...")
                return User(Email, password,username)
                break
            else:
                logger.error("Password does not match")
          

class Game_rules:
    def show(self):
        logger.success('WELCOME TO FOOTBALL TRIVIA')

        time.sleep(2)

        logger.info('''
        🚨 GAME RULES:
        ♦ You have less than 10 seconds to answer a particular question
        ♦ If the allocated time has been exceeded, you have failed,
        ♦ whether or not you give an answer afterwards

        Goodluck!😁
        ''')

        time.sleep(5)

class Quizgame:
    def __init__(self,quiz):
        self.quiz=quiz.quiz
        self.score=0

    def start(self):
        random.shuffle(self.quiz)  
        for p in self.quiz:
            print("\n" + p['question'])
            for option in p['options']:
                print(option)

            start =time.time()
            answer=input('Your Answer: ').strip().upper()
            elapsed=time.time()-start

            if elapsed>10:
                logger.error(f"🧭 Time's Up! You took {int(elapsed)} seconds")
                logger.info(f"The Correct answer is {p['answer']}")
            elif answer==p['answer']:
                logger.success('✅ Correct!')
                self.score+=1
            else:
                logger.error('❌Wrong Answer')
                logger.info(f"The Correct answer is {p['answer']}")
     
    def result(self, user=Registration().register()):
        total=len(self.quiz)

        logger.info("\n Quiz Completed!")
        logger.info(f"\n{user.username}, your Score: {self.score}/{total}")

        add_score(user.username, self.score)
        logger.info ("\n" + '=' *40)
        logger.info("   CURRENT LEADERBOARD    ")
        logger.info("="*40)

        top=get_top_players(5)
        if not top:
            logger.info("No scores yet! Be the first!")
        else:
            for i, p in enumerate(top, 1):
                logger.info(f"{i:2}, {p["username"]:<15} {p["score"]} pts ({p["date"]})")

        if self.score==total:
            logger.success(f"🏆 Congratulations {user.username}, you had a perfect score!")
        elif self.score>=total//2:
            logger.success("nice!, You passed")
        else:
            logger.error("OOPS... Try again next time..")


def add_score(username: str, score: int):
    board=load_leaderboard
    for entry in board:
        if entry["username"].lower()==username.lower():
            if score>entry.get("score",0):
                entry["score"]=score
                entry["data"]=datetime.now().strftime("%Y-%m-%d")
            save_leaderboard(board)
            return
        
    board.append({
        "username": username,
        "score" : score,
        "date" : datetime.mow().strftime("%Y-%m-%d")
    })
    
    save_leaderboard(board)

def get_top_players(limit=5):
    board = load_leaderboard()
    sorted_board=sorted(board, key=lambda x:x["score"], reverse=True)
    return sorted_board[:limit]
    