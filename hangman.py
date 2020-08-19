import string
import random
from tkinter import Tk,Button,Entry,Label,END
from tkinter.messagebox import showinfo

class HangmanGUI(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.count=0
        self.title('Hangman')
        self.lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lst1 = ["O", "/", "|", "\\", "|", "/", "\\"]
        self.make_widgets()



    def botPlayer(self):
        wordlist=['Adult', 'Aeroplane', 'Air', 'Aircraft Carrier', 'Airforce', 'Airport', 'Album', 'Alphabet', 'Apple', 'Arm',
        'Army', 'Baby', 'Baby', 'Backpack', 'Balloon', 'Banana', 'Bank', 'Barbecue', 'Bathroom', 'Bathtub', 'Bed', 'Bed', 'Bee',
        'Bible', 'Bible', 'Bird', 'Bomb', 'Book', 'Boss', 'Bottle', 'Bowl', 'Box', 'Boy', 'Brain', 'Bridge', 'Butterfly', 'Button',
        'Cappuccino', 'Car',  'Carpet', 'Carrot', 'Cave', 'Chair', 'Chess Board', 'Chief', 'Child', 'Chisel', 'Chocolates',
        'Church', 'Church', 'Circle', 'Circus', 'Circus', 'Clock', 'Clown', 'Coffee', 'Comet', 'Compact Disc', 'Compass',
        'Computer', 'Crystal', 'Cup', 'Cycle', 'Data Base', 'Desk', 'Diamond', 'Dress', 'Drill', 'Drink', 'Drum', 'Dung', 'Ears', 'Earth',
        'Egg', 'Electricity', 'Elephant', 'Eraser', 'Explosive', 'Eyes', 'Family', 'Fan', 'Feather', 'Festival', 'Film', 'Finger', 'Fire',
        'Floodlight', 'Flower', 'Foot', 'Fork', 'Freeway', 'Fruit', 'Fungus', 'Game', 'Garden', 'Gas', 'Gate', 'Gemstone', 'Girl', 'Gloves',
        'God', 'Grapes', 'Guitar', 'Hammer', 'Hat', 'Hieroglyph', 'Highway', 'Horoscope', 'Horse', 'Hose', 'Ice', 'Insect',
        'Jet fighter', 'Junk', 'Kaleidoscope', 'Kitchen', 'Knife', 'Leather jacket', 'Leg', 'Library', 'Liquid', 'Magnet', 'Man', 'Map', 'Maze',
        'Meat', 'Meteor', 'Microscope', 'Milk', 'Milkshake', 'Mist', 'Money $$$$', 'Monster', 'Mosquito', 'Mouth', 'Nail', 'Navy', 'Necklace',
        'Needle', 'Onion', 'PaintBrush', 'Pants', 'Parachute', 'Passport', 'Pebble', 'Pendulum', 'Pepper', 'Perfume', 'Pillow', 'Plane', 'Planet',
        'Pocket', 'Potato', 'Printer', 'Prison', 'Pyramid', 'Radar', 'Rainbow', 'Record', 'Restaurant', 'Rifle', 'Ring', 'Robot', 'Rock', 'Rocket',
        'Roof', 'Room', 'Rope', 'Saddle', 'Salt', 'Sandpaper', 'Sandwich', 'Satellite', 'School', 'Sex', 'Ship', 'Shoes', 'Shop', 'Shower', 'Signature',
        'Skeleton', 'Slave', 'Snail', 'Software', 'Solid', 'Space Shuttle', 'Spectrum', 'Sphere', 'Spice', 'Spiral', 'Spoon', 'Spot Light',
        'Square', 'Staircase', 'Star', 'Stomach', 'Sun', 'Sunglasses', 'Surveyor', 'Swimming Pool', 'Sword', 'Table', 'Tapestry', 'Teeth',
        'Telescope', 'Television', 'Thermometer', 'Tiger', 'Toilet', 'Tongue', 'Torch', 'Torpedo', 'Train', 'Treadmill', 'Triangle', 'Tunnel', 'Typewriter',
        'Umbrella', 'Vacuum', 'Vampire', 'Videotape', 'Vulture', 'Water', 'Weapon', 'Web', 'Wheelchair', 'Window', 'Woman', 'Worm']
        self.wordSpace = []
        self.wordLetters = []
        self.button1.destroy()
        self.button2.destroy()
        randomWordIndex = random.randint(0,(len(wordlist)-1))  # chooses index of word
        self.randomword = wordlist[randomWordIndex].lower()  # gets random word from list
        for i in self.randomword:
            self.wordLetters.append(i)
        for i in range(len(self.randomword)):
            self.wordSpace.append('_')
        self.wordLabel =Label(self,text=self.wordSpace)
        self.wordLabel.grid(row=16,column=0)  # Shows spaces for randomword

        self.alphabet = list(string.ascii_lowercase) # gets alphabet

        self.letterChoice =Label(self,text=self.alphabet)
        self.letterChoice.grid(row=17,column=0)
        self.playerEntry = Entry(self)
        self.playerEntry.grid(row=18,column =0)
        self.submit = Button(self, text='Submit',command=lambda:self.playWord())
        self.submit.grid(row=18,column=1)

    def playWord(self):
        letter = self.playerEntry.get()
        if letter in self.alphabet:
            if letter in self.wordLetters:
                while letter in self.wordLetters:
                    index = self.wordLetters.index(letter)
                    self.wordSpace[index] = letter
                    self.wordLetters[index] = ''
                self.wordLabel.config(text=self.wordSpace)
                self.result.config(text='Yes!')
            else:
                self.result.config(text='Nope')
                self.lst[self.count] = self.lst1[self.count]
                self.top.config(text='       {}       |'.format(self.lst[0]))
                self.middle.config(text='      {}{}{}      |'.format(self.lst[1],self.lst[2],self.lst[3]))
                self.lower.config(text='       {}       |'.format(self.lst[4]))
                self.bottom.config(text='      {} {}      |'.format(self.lst[5],self.lst[6]))
                self.count+=1
            self.alphabet[self.alphabet.index(letter)] = '_'
            self.letterChoice.config(text=self.alphabet)
            self.playerEntry.delete(0,END)
        else:
            showinfo(title='Invalid Choice', message='You have already picked this letter, please try again.')
        if self.lst[6] == '\\':
            showinfo(title='You Lost', message='You lost, Play Again if you want')
            self.resetGame()
        if '_' not in self.wordSpace:
            showinfo(title='You Won',message="You Won!, Play Again if you want")
            self.resetGame()

    def resetGame(self):
        self.lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.lst1 = ["O", "/", "|", "\\", "|", "/", "\\"]
        self.playerEntry.destroy()
        self.submit.destroy()
        self.result.destroy()
        self.letterChoice.destroy()
        self.wordLabel.destroy()
        self.make_widgets()

        self.alphabet = list(string.ascii_lowercase)

    def playerChoice(self):
        self.playmode.config(text='')
        self.wordSpace = []
        self.wordLetters = []
        self.button1.destroy()
        self.button2.destroy()
        self.playerChosenWord=''

        self.playerWordEntry = Entry(self)
        self.playerWordEntry.grid(row=13,column =0)
        self.button = Button(self, text='Submit', command=lambda: self.buttonGet())
        self.button.grid(row=13, column=1)

        self.alphabet = list(string.ascii_lowercase) # gets alphabet

        for i in self.playerChosenWord:
            self.wordLetters.append(i)

        for i in range(len(self.playerChosenWord)):
            self.wordSpace.append('_')



    def buttonGet(self):
        self.playerChosenWord = self.playerWordEntry.get()
        self.alphabet = list(string.ascii_lowercase)  # gets alphabet

        for i in self.playerChosenWord:
            self.wordLetters.append(i)

        for i in range(len(self.playerChosenWord)):
            self.wordSpace.append('_')

        self.wordLabel = Label(self, text=self.wordSpace)
        self.wordLabel.grid(row=16, column=0)
        self.letterChoice =Label(self,text=self.alphabet)
        self.letterChoice.grid(row=17,column=0)
        self.playerEntry = Entry(self)
        self.playerEntry.grid(row=18,column =0)
        self.submit = Button(self, text='Submit',command=lambda:self.playWord())
        self.button.destroy()
        self.playerWordEntry.destroy()
        self.submit.grid(row=18,column=1)

    def multiPlayer(self):
        print('multi')

    def make_widgets(self):
        Label(self,text='This is Hangman').grid(row=0,column=0)
        Label(self,text='A Game where you choose a word and I or another player will attempt to guess that word.').grid(row=1,column=0)
        Label(self,text='Every time a chosen letter is wrong, one part of the Hangman will be added.').grid(row=2,column=0)
        Label(self,text='If the entire Hangman is drawn before the word is guessed, YOU WIN!!!').grid(row=3,column=0)
        Label(self,text='        _______').grid(row=4,column=0)
        Label(self,text='       |       |').grid(row=5,column=0)
        Label(self,text='       |       |').grid(row=6,column=0)

        self.top = Label(self,text='       {}       |'.format(self.lst[0]))
        self.top.grid(row=7,column=0)
        self.middle = Label(self,text='      {}{}{}      |'.format(self.lst[1],self.lst[2],self.lst[3]))
        self.middle.grid(row=8,column=0)
        self.lower = Label(self,text='       {}       |'.format(self.lst[4]))
        self.lower.grid(row=9,column=0)
        self.bottom = Label(self,text='      {} {}      |'.format(self.lst[5],self.lst[6]))
        self.bottom.grid(row=10,column=0)

        Label(self,text='               |').grid(row=11,column=0)
        Label(self,text='          ===========').grid(row=12,column=0)
        self.result = Label(self, text='')
        self.result.grid(row=19, column=0, columnspan=2)
        self.button1=Button(self,text='Bot Chooses Word',command=lambda:self.botPlayer())
        self.button1.grid(row=14,column=0)


HangmanGUI().mainloop()
