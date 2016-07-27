import vocab
from Tkinter import *
import tkFont

BASE = RAISED
SELECTED = FLAT

class Tab(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.tab_name = name

class TabBar(Frame):
    def __init__(self, master=None, init_name=None):
        Frame.__init__(self, master)
        self.tabs = {}
        self.buttons = {}
        self.current_tab = None
        self.init_name = init_name
    
    def show(self):
        self.pack(side=TOP, expand=NO, fill=X)
        self.switch_tab(self.init_name or self.tabs.keys()[-1])
    
    def add(self, tab):
        tab.pack_forget()                                   
        self.tabs[tab.tab_name] = tab                       
        b = Button(self, text=tab.tab_name, relief=BASE,command=(lambda name=tab.tab_name: self.switch_tab(name)),bg="white")  
        b.pack(side=LEFT)                                               
        self.buttons[tab.tab_name] = b                                          
    
    def delete(self, tabname):
        if tabname == self.current_tab:
            self.current_tab = None
            self.tabs[tabname].pack_forget()
            del self.tabs[tabname]
            self.switch_tab(self.tabs.keys()[0])
        else:
            del self.tabs[tabname]
        self.buttons[tabname].pack_forget()
        del self.buttons[tabname] 
        
    def switch_tab(self, name):
        if self.current_tab:
          self.buttons[self.current_tab].config(relief=BASE,bg="white")
          self.tabs[self.current_tab].pack_forget()           
        self.tabs[name].pack(side=BOTTOM)                           
        self.current_tab = name                                 
        self.buttons[name].config(relief=SELECTED,bg="light cyan")


 
class RESULT():
    def __init__(self,query):
        result=vocab.create_result(query)
        #result={'synonyms': u'good day,howdy,hi,hey,so long', 'meaning': u'interjection:Used to greet someone, answer the telephone, or express surprise.\n\n', 'antonyms': 'N/A', 'usage': u'Hello Sara.  How are you?Hello Danny.  I am good.\n\n"Hello, It\'s you!!"\n\n1.  \'HELLO!!!!!!\'2.  \'I satyed at home last night watching movies\'     \'... HELLO!!?!! You were supposed to come to my party last night!\'\n\n-Hot person walks into the room-Adoring member of the opposite sex: "hello"\n\n(1)Bob (sees Bill on street): "Hello, Bill!"Bill: "Well, hello, Bob."(2)(Phone rings loudly) Jim: "Hello?"James Watson from AT&T: "Hi, this is James Watson from AT&T.  I\'m calling to talk to you about your long distance plan."\n\nWhat\'s the field integral of the magnetic flux of the solenoid?Do you understand this?hEllo?\n\n<<<CRREEEEAAAAKKKK>>>> ...Hell-O.\n\nWhat the hell(mom enters)-o mom.\n\nperson 1: helloPerson 2: hiPerson 1: goodbyePerson 2: Farewell, and may the forces of evil become confused in their eternal search for you*person 1 runs away*\n\nhello im silly\n\n', 'translation': u'\u0939\u0932\u094b,\u0928\u092e\u0938\u094d\u0924\u0947,\u0928\u092e\u0938\u094d\u0915\u093e\u0930,kya,\u0939\u0947\u0932\u094b,\u0938\u0924\u094d\u092f,satya,\u0938\u0941\u0928\u093f\u092f\u0947,\u0938\u0932\u093e\u092e,\u0928\u092e\u0938\u0924\u0947,\u0939\u0948\u0932\u094b,\u0938\u0924 \u0936\u094d\u0930\u0940 \u0905\u0915\u093e\u0932', 'pronunciation': '(h\xc4\x95-l\xc5\x8d\xcb\x88, h\xc9\x99-)'}
        self.root = Tk()
        self.root.title("Dictionary")
        self.root["pady"] = 30
        self.root.minsize(width=800, height=200)
        self.customFont = tkFont.Font(family="Andalus", size=12,weight="bold")

        self.titleFrame = Frame(self.root)
        self.titleFrame["pady"]=20
        self.titleLabel = Label(self.titleFrame,fg="blue",background="yellow")
        self.titleLabel["text"] = "DICTIONARY"
        self.titleLabel["font"] = tkFont.Font(family="Castellar", size=30,weight="bold") 
        self.titleLabel["relief"] = RIDGE
        self.titleLabel["padx"]=10
        self.titleLabel.pack()
        self.titleFrame.pack()

        
        self.backFrame= Frame(self.root)
        self.button = Button(self.backFrame,text="Go back",command=self.searchagain)
        self.button.pack()
        self.backFrame["pady"]=5
        self.backFrame["padx"]=5
        self.backFrame.pack(side=BOTTOM,anchor=E)
        
        self.titleFrame = Frame(self.root)
        self.titleFrame["pady"]=20
        self.titleLabel = Label(self.titleFrame,fg="white",background="SlateBlue1")
        self.titleLabel["text"] = query
        self.titleLabel["font"] = tkFont.Font(family="Arial Rounded MT Bold", size=25,weight="bold")
        self.titleLabel["relief"] = SUNKEN
        self.titleLabel["padx"]=10
        self.titleLabel.pack()
        self.titleFrame.pack()

        
        
        self.bar = TabBar(self.root,"meaning")
        self.bar.config(bd=2, relief=FLAT)
        
        self.tab1 = Tab(self.root,"meaning")
        Label(self.tab1, text=result['meaning'], bg="turquoise", fg="white",font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=Y)
        self.bar.add(self.tab1)
        
        self.tab2 = Tab(self.root,"translation")
        Label(self.tab2, text=result['translation'], bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab2)
        
        self.tab3 = Tab(self.root,"usage")
        Label(self.tab3, text=result['usage'],pady=10, bg="turquoise", fg="white",font=self.customFont,wraplength=700, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab3)
        
        self.tab4 = Tab(self.root,"antonyms")
        Label(self.tab4, text=result['antonyms'], bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab4)

        self.tab5 = Tab(self.root,"synonyms")
        Label(self.tab5, text=result['synonyms'],  bg="turquoise", fg="white", font=self.customFont,wraplength=800, width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab5)

        self.tab6 = Tab(self.root,"pronunciation")
        Label(self.tab6, text=result['pronunciation'],  bg="turquoise", fg="white",font=self.customFont, wraplength=800,width=80).pack(side=TOP, expand=NO, fill=BOTH)
        self.bar.add(self.tab6)
        
        self.bar.show()
        
        self.root.mainloop()

    def searchagain(self):
        self.root.destroy()
        SEARCH()



class SEARCH():
    def __init__(self):
        self.root = Tk()
        self.root.title("Dictionary")
        self.root["padx"] = 50
        self.root["pady"] = 30

        self.customFont = tkFont.Font(family="Castellar", size=30,weight="bold") 

        self.titleFrame = Frame(self.root)
        self.titleFrame["pady"]=20
        self.titleLabel = Label(self.titleFrame,fg="blue",background="yellow")
        self.titleLabel["text"] = "DICTIONARY"
        self.titleLabel["font"] = self.customFont
        self.titleLabel["relief"] = RIDGE
        self.titleLabel["padx"]=10
        self.titleLabel.pack()
        self.titleFrame.pack()
        

        self.textFrame = Frame(self.root)
        self.entryLabel = Label(self.textFrame)
        self.entryLabel["text"] = "Enter the word here:"
        self.entryLabel.pack(side=LEFT)
        self.entryWidget = Entry(self.textFrame)
        self.entryWidget["width"] = 40
        self.entryWidget.pack(side=LEFT)
        self.entryFrame= Frame(self.textFrame)
        self.button = Button(self.entryFrame,text="Search",command=self.displayresult)
        self.button.pack()
        self.entryFrame["padx"]=15
        self.entryFrame.pack()
        self.textFrame.pack()
        self.root.mainloop()
        

    def displayresult(self):
            query=self.entryWidget.get().strip()
            self.root.destroy()
            RESULT(query)
        

        
        
if __name__ == "__main__":
  SEARCH()       
