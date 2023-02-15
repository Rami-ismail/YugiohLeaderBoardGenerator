from PIL import Image, ImageDraw, ImageFont
from datetime import date
import pandas as pd

today = date.today().strftime("%d-%m-%Y")

class Player:
    def __init__(self, name, deck, score):
        self.name = name
        self.deck = deck
        self.score = score
        
def readData():
    data = pd.read_excel('./Input/Leaderboard-Input.xlsx')
    leaderboard_data = []
    for index in range(len(data)):
        row = data.iloc[index].to_numpy()
        leaderboard_data.append(Player(row[0], row[1], row[2]))
    return leaderboard_data

def splitData():
    leaderboard_data = readData()
    if len(leaderboard_data) > 8:
        smaller_arrays = []
        for i in range(0, len(leaderboard_data), 8):
            smaller_arrays.append(leaderboard_data[i:i+8])
        return smaller_arrays
    else:
        return [leaderboard_data]
    
def exportLeaderboard():
    data = splitData()
    for i in range(len(data)):
        leaderboard = str(today) + " - leaderboard pt"+str(i+1)+".png"
        drawLeaderBoard(data[i], leaderboard, i+1)
        
def drawLeaderBoard(leaderboard_data, leaderboardName, counter):
    background_image = Image.open("./Assets/Backgrounds/Bg1.png")
    image_editable = ImageDraw.Draw(background_image)
    fontBig = ImageFont.truetype(".\Assets\Fonts\Archivo_Black\ArchivoBlack-Regular.ttf", 40)
    fontMedium = ImageFont.truetype(".\Assets\Fonts\Archivo_Black\ArchivoBlack-Regular.ttf", 30)
    fontSmall = ImageFont.truetype(".\Assets\Fonts\Archivo_Black\ArchivoBlack-Regular.ttf", 25)
    image_editable.text((620, 115), str(today),("#FFFFFF"), font=fontMedium)
    ranking = 8*(counter - 1)
    for index in range(len(leaderboard_data)):
        item = leaderboard_data[index]
        ranking += 1
        offset = index+1
        row_y = -100 + (offset) * 100
        if ranking > 9:
            image_editable.text((85, 300 + row_y), str(ranking),("#FFFFFF"), font=fontBig)
        else:
            image_editable.text((100, 300 + row_y), str(ranking), ("#FFFFFF"), font=fontBig)
        image_editable.text((220, 275 + row_y+offset*2), item.name,("#FFFFFF"), font=fontBig)
        image_editable.text((220, 330 + row_y), item.deck, ("#FFFFFF"), font=fontSmall)
        image_editable.text((930, 300 + row_y), str(item.score), ("#FFFFFF"), font=fontBig)
        background_image.save('./Output/'+leaderboardName)
        
print("Generating Leaderboard.........")
exportLeaderboard()
