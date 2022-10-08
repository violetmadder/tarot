from pprint import pprint
from tkinter import N

#starting with basic lists of card traits

suits= ["Cups", "Wands", "Pentacles", "Swords", "Major Arcana"]

minorRanks= ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

majorRomans= [ "0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI"]

majorNames= ["The Fool", "The Magician", "The Empress", "The Emperor", "The Hierophant", "Justice", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

deckNames= ["Barbara Walker", "Osho Zen", "Robin Wood", "Penny Dreadful", "Shadowscapes", "Thoth", "Unified Esoteric"]

# making the master list defining unique IDs for all of the standard cards in a 79-card tarot deck:
# C01 refers to the Ace of Cups, M00 is The Fool, W14 is the King of Wands, etc
def cardIDs():
    IDs=[] 
    
    for suit in suits:
        suitID= suit[0]
        if suitID != "M":		
            for i in range (len(minorRanks)):
                i = str(i+1) #minor cards start counting from 1
                if len(i) < 2 :
                    i = "0" + i
                IDs.append(suitID + i)
        else:
            for i in range (len(majorRomans)):
                i = str(i) #major cards start counting from 0 
                if len(i) < 2 :
                    i = "0" + i                     
                IDs.append(suitID + i)
                
    return IDs
    
#initializing bare bones structure that will ultimately be dumped to JSON file for import into kumu 	  
kuDict= {
    "version": 1,
    "name": "",
    "description": "",
    "proxyImages": True,
    "defaultMap": "",
    "defaultPerspective": None,
    "attributeRelevance": {},
    "attributes": [],
    "elements": [],
    "connections": [],
    "loops": [],
    "maps": [],
    "perspectives": []
}

#bare structure of a kumu element
kuElement= {
    "_id": "",
    "attributes": {
        "label": "",
        "element type": "",
        "tags" : [],
        "description": "",
        "image": ""
    }
}

def kumuSuits():
    pass
def kumuRanks():
    pass
def kumuCards():
    elements = []
    cards = {}
    for cardID in cardIDs():
        cards[cardID] = kuElement
        cards[cardID]["_id"] = cardID
        print (cards [cardID])
    #for card in cards:
        #elements.append(card)
    return elements
def kumuDecks():
    elements = []
    for deck in deckNames:
        deckID = ""
        deckWords = deck.split(" ")
        if len(deckWords) == 2:
            for word in deckWords:
                deckID = deckID + word[0]
        else:
            deckID = deckwords[0][0:2]
        deckIDs.append(deckID)        
    return elements
        

#pprint (kumuDecks())

