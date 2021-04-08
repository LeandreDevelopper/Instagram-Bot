'''
--------------------------------------------
MADE BY Leandre
02/10/20
--------------------------------------------
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import *
from datetime import datetime
from datetime import date
import os

PATH = "C:\Program Files (x86)\chromedriver.exe" ## PATH of chromedriver

'''
LISTS
'''
comments = ["I like that !", "Very nice","Love your account. Keep posting.","Big Love", "Amazing", "Fantastic", "Cool !!", "Nice Job !", "Good Job !","Cute", "Pretty", "Very Pretty", "Wonderful", "I love", "Big Love", "Cool concept", "So Nice", "Nice", "Whooa", "Beautiful"]
hashtags = ["lowpoly", "lowpolyart", "lowpolygon","lowpolyartwork","lowpoly3d"]
pubText = "Hello man,\nI see you work and I find this really good\n Vue que tu es abonné à mon compte je te propose de faire un echage de pub car ton univer coicide bie navec le mien\n"

'''
CREATION CLASS BOT
'''
class InstagramBot():
    '''
    Init Section
    '''

    def __init__(self,email,password,username):
        print("\n")
        print(" === Welcome On Instagram Bot Made by Leandre Developper === ")

        self.email = email
        self.password = password
        self.username = username
        self.bot = webdriver.Chrome(PATH)
        self.like = 0
        self.commentaires = 0
        self.follow = 0
        self.start = datetime.now()
        self.todayUnFollow = False

    def singIn(self):
        bot = self.bot
        bot.get("https://instagram.com/accounts/login")
        sleep(3)
        bot.find_element_by_name("username").send_keys(self.email)
        bot.find_element_by_name("password").send_keys(self.password + Keys.RETURN)
        sleep(3)

    def searchHashtag(self,hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag)

    '''
    Main / like Section
    '''

    def likePhoto(self,amount):
        bot = self.bot
        bot.find_element_by_class_name("v1Nh3").click()

        i = 0
        while i <= amount:
            sleep(randint(30, 40))
            if random() <= 0.66:

                bot.find_element_by_class_name("fr66n").click()
                self.like +=1
                sleep(randint(4,20))
                print("likes : {}".format(self.like))

                ##Commentaire
                if random() <= 0.15:

                    self.commentPhoto(comments[randint(0, len(comments) - 1)])
                    self.commentaires += 1
                    sleep(randint(2,10))
                    print("commentaires : {}".format(self.commentaires))

                ##Follow
                if random() <= 0.09:

                    self.toFollow()
                    sleep(randint(30,50)/30)
                    print("follow : {}".format(self.follow))

            bot.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            i += 1

        bot.get("https://instagram.com/" + self.username)

    '''
    Comment Section
    '''

    def commentPhoto(self, comment):
        bot = self.bot
        sleep(3)

        try:
            commentBot = bot.find_element_by_css_selector('textarea.Ypffh').click()
            sleep(2)
            ## a revoir pour faire plus humain
            bot.find_element_by_css_selector('textarea.Ypffh').send_keys(comment)
            sleep(randint(1, 7)/30)
            bot.find_element_by_css_selector('textarea.Ypffh').send_keys(Keys.RETURN)
        except:
            print("Boite de commentaire non trouvé")

    '''
    Stat Section
    '''

    def statMaj(self):
        bot = self.bot
        bot.get("https://www.instagram.com/" + self.username)

        sleep(2)
        followers = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
        followersNumber = followers.text

        fichierStat = open("Stat.txt", "a")
        fichierStat.write("Start : {}\nLike : {}\nComments : {}\nfollows : {}\nUnFollow Today : {}\nFollowers At End : {}\nTravel Time : {}\nEnd : {}\n".format(self.start, self.like, self.commentaires, self.follow, self.todayUnFollow, followersNumber,datetime.now() - self.start, datetime.now()))
        fichierStat.write("-------------------------------------\n")
        fichierStat.close()

    '''
    Follow Section
    '''

    def toFollow(self):
        bot = self.bot
        fichierFollow = open("Follow.txt", "a")
        toFollow = bot.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a")
        usernameFollow = toFollow.text
        verification = bot.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
        if(verification.text == "Abonné(e)"):
            print("je suis deja abonné")
        else:
            print("je ne suis pas abonné")
            fichierFollow.write("{}\n".format(usernameFollow))
            verification.click()
            self.follow += 1
        fichierFollow.close()

    def unFollow(self):
        #rentre dans la boucle d'unfollow
        self.todayUnFollow = True
        bot = self.bot
        fichierFollow = open("Follow.txt", "r")
        sleep(5)
        lines = fichierFollow.readlines()
        fichierFollow.close()

        for line in lines:
            sleep(2)
            bot.get("https://www.instagram.com/{}".format(line))
            sleep(randint(3, 10))
            pageDispo = True

            #Verifie que la page est bien disponible
            try:
                bot.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
            except:
                #le nom de la personne avec laquelle la page a eu un Problème
                print("Un probleme a été rencontré : {}".format(line))
                pageDispo = False

            #si c'est la cas unfollow la personne
            if(pageDispo):
                sleep(randint(3, 10))
                bot.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()

                sleep(randint(3,8))


            #ecrit la personne que j'ai unfollow ( une par une)
            ficUnFollow = open("unFollow.txt", "a")
            ficUnFollow.write("{}".format(line))
            ficUnFollow.close()


        if os.path.exists('Follow.txt'):
            os.remove('Follow.txt')
            print("tous est delete")

            ##Recree le fichier une fois supprimé
            with open("Follow.txt", "x") as f:
                return
        else:
            print("Impossible de supprimer le fichier car il n'existe pas")


'''
MAIN PROGRAMME
'''

bot = InstagramBot("email","password","username")
bot.singIn()

unFollowTime = input(" Voulez-vous unFollow les personnes follow lorsque le bot tourne : (Y/N)")
if unFollowTime == "Y":
    print("Go unFollow")
    bot.unFollow()
else:
    print("Pas de unFollow aujourd'hui")

for i in range(0, len(hashtags)):
    if bot.like <= 350:
        bot.searchHashtag(hashtags[i])
        sleep(2)
        bot.likePhoto(randint(80,100))
    print("change hashtag")

bot.statMaj()
