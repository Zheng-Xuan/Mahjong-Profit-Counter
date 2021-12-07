import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Interface Set Up
class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        img = tk.PhotoImage(file = 'mahjong.png')
        self.iconphoto(False, img)
        self.title('Mahjong Counter')
        self.resizable(0,0)

        window = tk.Frame(self)
        window.pack() 
        window.grid_rowconfigure(0, minsize= 600)
        window.grid_columnconfigure(0, minsize= 700)

        self.shared_data = {
            'player_info': {},
            'player_list': [],
            'yao_amt': 0,
            'anyao_amt': 0,
            'gang_amt': 0,
            'angang_amt': 0,
            'zimoBonus_amt': 0,
            'event_count': 0,
            'event_number': [0],
            'p1_events': [0],
            'p2_events': [0],
            'p3_events': [0],
            'p4_events': [0]
        }

        self.frames_dict = {}
        for F in (startPage, playerDetails, countMethodPage, oneTwoGameSettings, oneTwoMainPage,
            oneTwoYaoPage, oneTwoAnYaoPage, oneTwoGangPage, oneTwoAnGangPage, oneTwoHuPage, oneTwoZimoPage,
            sanliuGameSettings, sanliuMainPage, sanliuYaoPage, sanliuAnYaoPage, sanliuGangPage, sanliuAnGangPage,
            sanliuHuPage, sanliuZimoPage, endPage, statsPage):
            frame = F(window, self)
            self.frames_dict[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(startPage)

    def show_frame(self, page):
        frame = self.frames_dict[page]
        frame.tkraise()

#Start Page
class startPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #Start Page Design
        self.configure(bg= 'green', highlightbackground= 'saddle brown', highlightthickness= 20)
        logo = Image.open('logo.png')
        logo = logo.resize((350, 300))
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self, image= logo)
        logo_label.configure(bg= 'green')
        logo_label.image = logo
        logo_label.place(relx= 0.5, rely= 0.4, anchor= 'center')

        #Create Start Button
        start_button = tk.Button(self, text= 'START', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(playerDetails))
        start_button.place(relx= 0.5, rely= 0.75, anchor= 'center')

class playerDetails(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Enter Player Names', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        player1_label = tk.Label(self, text= 'Player 1', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        player1_label.place(relx= 0.15, rely= 0.3, anchor= 'center')

        player2_label = tk.Label(self, text= 'Player 2', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        player2_label.place(relx= 0.15, rely= 0.4, anchor= 'center')

        player3_label = tk.Label(self, text= 'Player 3', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        player3_label.place(relx= 0.15, rely= 0.5, anchor= 'center')

        player4_label = tk.Label(self, text= 'Player 4', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        player4_label.place(relx= 0.15, rely= 0.6, anchor= 'center')

        #Entries
        p1_entry = tk.Entry(self, textvariable = tk.StringVar())
        p1_entry.place(relx= 0.6, rely= 0.3, anchor= 'center', height= 30, width= 400)

        p2_entry = tk.Entry(self, textvariable = tk.StringVar())
        p2_entry.place(relx= 0.6, rely= 0.4, anchor= 'center', height= 30, width= 400) 

        p3_entry = tk.Entry(self, textvariable = tk.StringVar())
        p3_entry.place(relx= 0.6, rely= 0.5, anchor= 'center', height= 30, width= 400) 

        p4_entry = tk.Entry(self, textvariable = tk.StringVar())
        p4_entry.place(relx= 0.6, rely= 0.6, anchor= 'center', height= 30, width= 400)

        #Button Commands
        def details_next():
            p1 = p1_entry.get()
            p2 = p2_entry.get()
            p3 = p3_entry.get()
            p4 = p4_entry.get()
            if p1 and p2 and p3 and p4 != '':
                controller.shared_data['player_info'] = {p1: 0, p2: 0, p3: 0, p4: 0}
                controller.shared_data['player_list'] = [p1, p2, p3, p4, 'ALL']
                controller.show_frame(countMethodPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= "Please fill up the names of all players")

        #Button
        next_button = tk.Button(self, text= "Next >", font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= details_next)
        next_button.place(relx= 0.5, rely= 0.8, anchor= 'center')
          
class countMethodPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= "Counting Method", font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        #Buttons
        oneTwo_button = tk.Button(self, text= '1/2 Counting Method', font= ('MS Sans Serif', 32, 'bold'), 
            height= 2, bd= 5, command= lambda: controller.show_frame(oneTwoGameSettings))
        oneTwo_button.place(relx= 0.5, rely= 0.3, anchor= 'center')

        sanliu_button = tk.Button(self, text= '3/6 Counting Method', font= ('MS Sans Serif', 32, 'bold'), 
            height= 2, bd= 5, command= lambda: controller.show_frame(sanliuGameSettings))
        sanliu_button.place(relx= 0.5, rely= 0.6, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(playerDetails))
        back_button.place(relx= 0.5, rely= 0.8, anchor= 'center')

#One Two
class oneTwoGameSettings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Game Settings', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        yao_label = tk.Label(self, text= 'Yao Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        yao_label.place(relx= 0.25, rely= 0.2, anchor= 'center')

        anyao_label = tk.Label(self, text= 'An Yao Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        anyao_label.place(relx= 0.25, rely= 0.3, anchor= 'center')

        gang_label = tk.Label(self, text= 'Gang Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        gang_label.place(relx= 0.25, rely= 0.4, anchor= 'center')

        angang_label = tk.Label(self, text= 'An Gang Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        angang_label.place(relx= 0.25, rely= 0.5, anchor= 'center')

        zimoBonus_label = tk.Label(self, text= 'Zi Mo Bonus', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        zimoBonus_label.place(relx= 0.25, rely= 0.6, anchor= 'center')

        #Entries 
        yao_entry= tk.Entry(self, textvariable= tk.StringVar())
        yao_entry.place(relx= 0.7, rely= 0.2, anchor= 'center', height= 30, width= 300)

        anyao_entry= tk.Entry(self, textvariable= tk.StringVar())
        anyao_entry.place(relx= 0.7, rely= 0.3, anchor= 'center', height= 30, width= 300)

        gang_entry= tk.Entry(self, textvariable= tk.StringVar())
        gang_entry.place(relx= 0.7, rely= 0.4, anchor= 'center', height= 30, width= 300)

        angang_entry= tk.Entry(self, textvariable= tk.StringVar())
        angang_entry.place(relx= 0.7, rely= 0.5, anchor= 'center', height= 30, width= 300)

        zimoBonus_entry= tk.Entry(self, textvariable= tk.StringVar())
        zimoBonus_entry.place(relx= 0.7, rely= 0.6, anchor= 'center', height= 30, width= 300)

        def settings_next():
            yao_amt = yao_entry.get()
            anyao_amt = anyao_entry.get()
            gang_amt = gang_entry.get()
            angang_amt = angang_entry.get()
            zimoBonus_amt = zimoBonus_entry.get()
            if yao_amt and anyao_amt and gang_amt and angang_amt and zimoBonus_amt != '':
                try:
                    yao_amt = float(yao_amt)
                    anyao_amt = float(anyao_amt)
                    gang_amt = float(gang_amt)
                    angang_amt = float(angang_amt)
                    zimoBonus_amt = float(zimoBonus_amt)
                    controller.shared_data['yao_amt'] = yao_amt
                    controller.shared_data['anyao_amt'] = anyao_amt
                    controller.shared_data['gang_amt'] = gang_amt
                    controller.shared_data['angang_amt'] = angang_amt
                    controller.shared_data['zimoBonus_amt'] = zimoBonus_amt
                    controller.show_frame(oneTwoMainPage)
                except ValueError:
                    tk.messagebox.showerror(title= 'Error', message= "Invalid Input")
            else:
                tk.messagebox.showerror(title= 'Error', message= "One or more fields are not filled")

        #Buttons
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= settings_next)
        next_button.place(relx= 0.7, rely = 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(countMethodPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')


class oneTwoMainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Main Page', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        #Buttons
        yao_button = tk.Button(self, text= 'Yao', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15, 
            command= lambda: controller.show_frame(oneTwoYaoPage))
        yao_button.place(relx= 0.3, rely= 0.25, anchor= 'center')

        anyao_button = tk.Button(self, text= 'An Yao', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda: controller.show_frame(oneTwoAnYaoPage))
        anyao_button.place(relx= 0.7, rely= 0.25, anchor= 'center')
        
        gang_button = tk.Button(self, text= 'Gang', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda: controller.show_frame(oneTwoGangPage))
        gang_button.place(relx= 0.3, rely= 0.4, anchor= 'center')

        angang_button = tk.Button(self, text= 'An Gang', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda: controller.show_frame(oneTwoAnGangPage))
        angang_button.place(relx= 0.7, rely= 0.4, anchor= 'center')

        hu_button = tk.Button(self, text= 'Hu', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda: controller.show_frame(oneTwoHuPage))
        hu_button.place(relx= 0.3, rely= 0.55, anchor= 'center')

        zimo_button = tk.Button(self, text= 'Zi Mo', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda: controller.show_frame(oneTwoZimoPage))
        zimo_button.place(relx= 0.7, rely= 0.55, anchor= 'center')

        back_button = tk.Button(self, text= 'Back to Settings', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda : controller.show_frame(oneTwoGameSettings))
        back_button.place(relx= 0.3, rely= 0.80, anchor= 'center')

        endGame_button = tk.Button(self, text= 'End Game', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
            command= lambda : controller.show_frame(endPage))
        endGame_button.place(relx= 0.7, rely= 0.80, anchor= 'center')

class oneTwoYaoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Yao', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        biter_label = tk.Label(self, text= 'Choose Biter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        biter_label.place(relx= 0.2, rely = 0.3, anchor= 'center')

        bitee_label = tk.Label(self, text= 'Choose Bitten', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        bitee_label.place(relx= 0.2, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            biter_droplist['values'] = players

        biter_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 50)
        biter_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        def updateBitee():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != biter]
            bitee_droplist['values'] = new_list
        
        bitee_droplist = ttk.Combobox(self, postcommand= updateBitee, width= 50)
        bitee_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        def next():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            bitee = tk.StringVar()
            bitee = bitee_droplist.get()
            players = self.controller.shared_data['player_list']
            yao = self.controller.shared_data['yao_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if biter and bitee in players:
                if bitee == 'ALL':
                    player_details[biter] += 3*yao
                    for player in player_details:
                        if player != biter:
                            player_details[player] -= yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                else:
                    player_details[biter] += yao
                    player_details[bitee] -= yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class oneTwoAnYaoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'An Yao', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        biter_label = tk.Label(self, text= 'Choose Biter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        biter_label.place(relx= 0.2, rely = 0.3, anchor= 'center')

        bitee_label = tk.Label(self, text= 'Choose Bitten', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        bitee_label.place(relx= 0.2, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            biter_droplist['values'] = players

        biter_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 50)
        biter_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        def updateBitee():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != biter]
            bitee_droplist['values'] = new_list
        
        bitee_droplist = ttk.Combobox(self, postcommand= updateBitee, width= 50)
        bitee_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        def next():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            bitee = tk.StringVar()
            bitee = bitee_droplist.get()
            players = self.controller.shared_data['player_list']
            an_yao = self.controller.shared_data['anyao_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if biter and bitee in players:
                if bitee == 'ALL':
                    player_details[biter] += 3*an_yao
                    for player in player_details:
                        if player != biter:
                            player_details[player] -= an_yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                else:
                    player_details[biter] += an_yao
                    player_details[bitee] -= an_yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class oneTwoGangPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Gang', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        ganger_label = tk.Label(self, text= 'Choose Who Gang', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        ganger_label.place(relx= 0.3, rely = 0.3, anchor= 'center')

        gangee_label = tk.Label(self, text= 'Choose Shooter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        gangee_label.place(relx= 0.3, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            ganger_droplist['values'] = players

        ganger_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 40)
        ganger_droplist.place(relx= 0.75, rely= 0.3, anchor= 'center')

        def updateGangee():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != ganger]
            gangee_droplist['values'] = new_list
        
        gangee_droplist = ttk.Combobox(self, postcommand= updateGangee, width= 40)
        gangee_droplist.place(relx= 0.75, rely= 0.5, anchor= 'center')

        def next():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            gangee = tk.StringVar()
            gangee = gangee_droplist.get()
            players = self.controller.shared_data['player_list']
            gang = self.controller.shared_data['gang_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if ganger and gangee in players:
                if gangee == 'ALL':
                    player_details[ganger] += 3*gang
                    for player in player_details:
                        if player != ganger:
                            player_details[player] -= gang
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                else:
                    player_details[ganger] += 3*gang
                    player_details[gangee] -= 3*gang
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class oneTwoAnGangPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'An Gang', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        ganger_label = tk.Label(self, text= 'Choose Who Gang', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        ganger_label.place(relx= 0.3, rely = 0.3, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            ganger_droplist['values'] = players

        ganger_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 40)
        ganger_droplist.place(relx= 0.75, rely= 0.3, anchor= 'center')

        def next():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            players = self.controller.shared_data['player_list']
            an_gang = self.controller.shared_data['angang_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if ganger in players:
                player_details[ganger] += 3*an_gang
                for player in player_details:
                    if player != ganger:
                        player_details[player] -= an_gang
                #Event Logging
                p1_profit = controller.shared_data['player_info'][p1_name]
                p2_profit = controller.shared_data['player_info'][p2_name]
                p3_profit = controller.shared_data['player_info'][p3_name]
                p4_profit = controller.shared_data['player_info'][p4_name]

                self.controller.shared_data['event_count'] += 1
                self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                self.controller.shared_data['p1_events'].append(p1_profit)
                self.controller.shared_data['p2_events'].append(p2_profit)
                self.controller.shared_data['p3_events'].append(p3_profit)
                self.controller.shared_data['p4_events'].append(p4_profit)
                self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class oneTwoHuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Hu', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        winner_label = tk.Label(self, text= 'Select Winner', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        winner_label.place(relx= 0.25, rely= 0.2, anchor= 'center')

        shooter_label = tk.Label(self, text= 'Select Shooter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        shooter_label.place(relx= 0.25, rely= 0.4, anchor= 'center')

        tai_label = tk.Label(self, text= 'Tai', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        tai_label.place(relx= 0.25, rely= 0.6, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            winner_droplist['values'] = players

        winner_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width= 40)
        winner_droplist.place(relx= 0.7, rely= 0.2, anchor= 'center')

        def updateShooter():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            new_list = list(self.controller.shared_data['player_info'].keys())
            new_list = [i for i in new_list if i != winner]
            shooter_droplist['values'] = new_list 

        shooter_droplist = ttk.Combobox(self, postcommand= updateShooter, width= 40)
        shooter_droplist.place(relx= 0.7, rely= 0.4, anchor= 'center')

        tai_droplist = ttk.Combobox(self, values= [1, 2, 3, 4, 5], width= 40)
        tai_droplist.place(relx= 0.7, rely= 0.6, anchor= 'center')

        #Buttons
        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

        def next():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            shooter = tk.StringVar()
            shooter = shooter_droplist.get()
            tai = int(tai_droplist.get())
            possible_tai = [1, 2, 3, 4, 5]
            players = list(self.controller.shared_data['player_info'].keys())
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if (winner and shooter in players) and (tai in possible_tai):
                if tai == 1:
                    player_details[winner] += 4
                    player_details[shooter] -= 4
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 2:
                    player_details[winner] += 8
                    player_details[shooter] -= 8
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 3:
                    player_details[winner] += 16
                    player_details[shooter] -= 16
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 4:
                    player_details[winner] += 32
                    player_details[shooter] -= 32
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(oneTwoMainPage)
                else:
                    player_details[winner] += 64
                    player_details[shooter] -= 64
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit) 
                    self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Invalid input in one or more fields')

        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

class oneTwoZimoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Zi Mo', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        winner_label = tk.Label(self, text= 'Select Winner', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        winner_label.place(relx= 0.25, rely= 0.3, anchor= 'center')

        tai_label = tk.Label(self, text= 'Tai', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        tai_label.place(relx= 0.25, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            winner_droplist['values'] = players

        winner_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width= 40)
        winner_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        tai_droplist = ttk.Combobox(self, values= [1, 2, 3, 4, 5], width= 40)
        tai_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        #Buttons
        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(oneTwoMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

        def next():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            tai = int(tai_droplist.get())
            possible_tai = [1, 2, 3, 4, 5]
            zimoBonus_amt = self.controller.shared_data['zimoBonus_amt']
            players = list(self.controller.shared_data['player_info'].keys())
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if (winner in players) and (tai in possible_tai):
                if tai == 1:
                    player_details[winner] += 3*(2 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (2 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 2:
                    player_details[winner] += 3*(4 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (4 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 3:
                    player_details[winner] += 3*(8 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (8 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 4:
                    player_details[winner] += 3*(16 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (16 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(oneTwoMainPage)
                elif tai == 5:
                    player_details[winner] += 3*(32 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (32 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(oneTwoMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Invalid input in one or more fields')

        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

#San Liu
class sanliuGameSettings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Game Settings', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        yao_label = tk.Label(self, text= 'Yao Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        yao_label.place(relx= 0.25, rely= 0.2, anchor= 'center')

        anyao_label = tk.Label(self, text= 'An Yao Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        anyao_label.place(relx= 0.25, rely= 0.3, anchor= 'center')

        gang_label = tk.Label(self, text= 'Gang Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        gang_label.place(relx= 0.25, rely= 0.4, anchor= 'center')

        angang_label = tk.Label(self, text= 'An Gang Payout', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        angang_label.place(relx= 0.25, rely= 0.5, anchor= 'center')

        zimoBonus_label = tk.Label(self, text= 'Zi Mo Bonus', font= ('MS Sans Serif', 28), bg= 'papaya whip')
        zimoBonus_label.place(relx= 0.25, rely= 0.6, anchor= 'center')

        #Entries 
        yao_entry = tk.Entry(self, textvariable= tk.StringVar())
        yao_entry.place(relx= 0.7, rely= 0.2, anchor= 'center', height= 30, width= 300)

        anyao_entry = tk.Entry(self, textvariable= tk.StringVar())
        anyao_entry.place(relx= 0.7, rely= 0.3, anchor= 'center', height= 30, width= 300)

        gang_entry = tk.Entry(self, textvariable= tk.StringVar())
        gang_entry.place(relx= 0.7, rely= 0.4, anchor= 'center', height= 30, width= 300)

        angang_entry = tk.Entry(self, textvariable= tk.StringVar())
        angang_entry.place(relx= 0.7, rely= 0.5, anchor= 'center', height= 30, width= 300)

        zimoBonus_entry = tk.Entry(self, textvariable= tk.StringVar())
        zimoBonus_entry.place(relx= 0.7, rely= 0.6, anchor= 'center', height= 30, width= 300)

        def settings_next():
            yao_amt = yao_entry.get()
            anyao_amt = anyao_entry.get()
            gang_amt = gang_entry.get()
            angang_amt = angang_entry.get()
            zimoBonus_amt = zimoBonus_entry.get()
            if yao_amt and anyao_amt and gang_amt and angang_amt and zimoBonus_amt != '':
                try:
                    yao_amt = float(yao_amt)
                    anyao_amt = float(anyao_amt)
                    gang_amt = float(gang_amt)
                    angang_amt = float(angang_amt)
                    zimoBonus_amt = float(zimoBonus_amt)
                    controller.shared_data['yao_amt'] = yao_amt
                    controller.shared_data['anyao_amt'] = anyao_amt
                    controller.shared_data['gang_amt'] = gang_amt
                    controller.shared_data['angang_amt'] = angang_amt
                    controller.shared_data['zimoBonus_amt'] = zimoBonus_amt
                    controller.show_frame(sanliuMainPage)
                except ValueError:
                    tk.messagebox.showerror(title= 'Error', message= "Invalid Input")
            else:
                tk.messagebox.showerror(title= 'Error', message= "One or more fields are not filled")


        #Buttons
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= settings_next)
        next_button.place(relx= 0.7, rely = 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(countMethodPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')


class sanliuMainPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.configure(bg= 'papaya whip')

            #Labels
            header_label = tk.Label(self, text= 'Main Page', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
            header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

            #Buttons
            yao_button = tk.Button(self, text= 'Yao', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                 command= lambda: controller.show_frame(sanliuYaoPage))
            yao_button.place(relx= 0.3, rely= 0.25, anchor= 'center')

            anyao_button = tk.Button(self, text= 'An Yao', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(sanliuAnYaoPage))
            anyao_button.place(relx= 0.7, rely= 0.25, anchor= 'center')
            
            gang_button = tk.Button(self, text= 'Gang', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(sanliuGangPage))
            gang_button.place(relx= 0.3, rely= 0.4, anchor= 'center')

            angang_button = tk.Button(self, text= 'An Gang', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(sanliuAnGangPage))
            angang_button.place(relx= 0.7, rely= 0.4, anchor= 'center')

            hu_button = tk.Button(self, text= 'Hu', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(sanliuHuPage))
            hu_button.place(relx= 0.3, rely= 0.55, anchor= 'center')

            zimo_button = tk.Button(self, text= 'Zi Mo', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(sanliuZimoPage))
            zimo_button.place(relx= 0.7, rely= 0.55, anchor= 'center')

            back_button = tk.Button(self, text= 'Back to Settings', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda : controller.show_frame(sanliuGameSettings))
            back_button.place(relx= 0.3, rely= 0.80, anchor= 'center')

            endGame_button = tk.Button(self, text= 'End Game', font= ('MS Sans Serif', 20, 'bold'), bd= 5, width= 15,
                command= lambda: controller.show_frame(endPage))
            endGame_button.place(relx= 0.7, rely= 0.80, anchor= 'center')

class sanliuYaoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Yao', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        biter_label = tk.Label(self, text= 'Choose Biter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        biter_label.place(relx= 0.2, rely = 0.3, anchor= 'center')

        bitee_label = tk.Label(self, text= 'Choose Bitten', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        bitee_label.place(relx= 0.2, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            biter_droplist['values'] = players

        biter_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 50)
        biter_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        def updateBitee():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != biter]
            bitee_droplist['values'] = new_list
        
        bitee_droplist = ttk.Combobox(self, postcommand= updateBitee, width= 50)
        bitee_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        def next():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            bitee = tk.StringVar()
            bitee = bitee_droplist.get()
            players = self.controller.shared_data['player_list']
            yao = self.controller.shared_data['yao_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if biter and bitee in players:
                if bitee == 'ALL':
                    player_details[biter] += 3*yao
                    for player in player_details:
                        if player != biter:
                            player_details[player] -= yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                else:
                    player_details[biter] += yao
                    player_details[bitee] -= yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class sanliuAnYaoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'An Yao', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        biter_label = tk.Label(self, text= 'Choose Biter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        biter_label.place(relx= 0.2, rely = 0.3, anchor= 'center')

        bitee_label = tk.Label(self, text= 'Choose Bitten', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        bitee_label.place(relx= 0.2, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            biter_droplist['values'] = players

        biter_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 50)
        biter_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        def updateBitee():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != biter]
            bitee_droplist['values'] = new_list
        
        bitee_droplist = ttk.Combobox(self, postcommand= updateBitee, width= 50)
        bitee_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        def next():
            biter = tk.StringVar()
            biter = biter_droplist.get()
            bitee = tk.StringVar()
            bitee = bitee_droplist.get()
            players = self.controller.shared_data['player_list']
            an_yao = self.controller.shared_data['anyao_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if biter and bitee in players:
                if bitee == 'ALL':
                    player_details[biter] += 3*an_yao
                    for player in player_details:
                        if player != biter:
                            player_details[player] -= an_yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                else:
                    player_details[biter] += an_yao
                    player_details[bitee] -= an_yao
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class sanliuGangPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Gang', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        ganger_label = tk.Label(self, text= 'Choose Who Gang', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        ganger_label.place(relx= 0.3, rely = 0.3, anchor= 'center')

        gangee_label = tk.Label(self, text= 'Choose Shooter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        gangee_label.place(relx= 0.3, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            ganger_droplist['values'] = players

        ganger_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 40)
        ganger_droplist.place(relx= 0.75, rely= 0.3, anchor= 'center')

        def updateGangee():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            new_list = self.controller.shared_data['player_list']
            new_list = [i for i in new_list if i != ganger]
            gangee_droplist['values'] = new_list
        
        gangee_droplist = ttk.Combobox(self, postcommand= updateGangee, width= 40)
        gangee_droplist.place(relx= 0.75, rely= 0.5, anchor= 'center')

        def next():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            gangee = tk.StringVar()
            gangee = gangee_droplist.get()
            players = self.controller.shared_data['player_list']
            gang = self.controller.shared_data['gang_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if ganger and gangee in players:
                if gangee == 'ALL':
                    player_details[ganger] += 3*gang
                    for player in player_details:
                        if player != ganger:
                            player_details[player] -= gang
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                else:
                    player_details[ganger] += 3*gang
                    player_details[gangee] -= 3*gang
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class sanliuAnGangPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'An Gang', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        ganger_label = tk.Label(self, text= 'Choose Who Gang', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        ganger_label.place(relx= 0.3, rely = 0.3, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            ganger_droplist['values'] = players

        ganger_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width = 40)
        ganger_droplist.place(relx= 0.75, rely= 0.3, anchor= 'center')

        def next():
            ganger = tk.StringVar()
            ganger = ganger_droplist.get()
            players = self.controller.shared_data['player_list']
            an_gang = self.controller.shared_data['angang_amt']
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if ganger in players:
                player_details[ganger] += 3*an_gang
                for player in player_details:
                    if player != ganger:
                        player_details[player] -= an_gang
                #Event Logging
                p1_profit = controller.shared_data['player_info'][p1_name]
                p2_profit = controller.shared_data['player_info'][p2_name]
                p3_profit = controller.shared_data['player_info'][p3_name]
                p4_profit = controller.shared_data['player_info'][p4_name]

                self.controller.shared_data['event_count'] += 1
                self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                self.controller.shared_data['p1_events'].append(p1_profit)
                self.controller.shared_data['p2_events'].append(p2_profit)
                self.controller.shared_data['p3_events'].append(p3_profit)
                self.controller.shared_data['p4_events'].append(p4_profit)
                self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Player Does Not Exist')

        #Buttons 
        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

class sanliuHuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Hu', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        winner_label = tk.Label(self, text= 'Select Winner', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        winner_label.place(relx= 0.25, rely= 0.2, anchor= 'center')

        shooter_label = tk.Label(self, text= 'Select Shooter', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        shooter_label.place(relx= 0.25, rely= 0.4, anchor= 'center')

        tai_label = tk.Label(self, text= 'Tai', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        tai_label.place(relx= 0.25, rely= 0.6, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            winner_droplist['values'] = players

        winner_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width= 40)
        winner_droplist.place(relx= 0.7, rely= 0.2, anchor= 'center')

        def updateShooter():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            new_list = list(self.controller.shared_data['player_info'].keys())
            new_list = [i for i in new_list if i != winner]
            shooter_droplist['values'] = new_list 

        shooter_droplist = ttk.Combobox(self, postcommand= updateShooter, width= 40)
        shooter_droplist.place(relx= 0.7, rely= 0.4, anchor= 'center')

        tai_droplist = ttk.Combobox(self, values= [1, 2, 3, 4, 5], width= 40)
        tai_droplist.place(relx= 0.7, rely= 0.6, anchor= 'center')

        #Buttons
        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

        def next():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            shooter = tk.StringVar()
            shooter = shooter_droplist.get()
            tai = int(tai_droplist.get())
            possible_tai = [1, 2, 3, 4, 5]
            players = list(self.controller.shared_data['player_info'].keys())
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if (winner and shooter in players) and (tai in possible_tai):
                if tai == 1:
                    player_details[winner] += 4
                    player_details[shooter] -= 4
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 2:
                    player_details[winner] += 7
                    player_details[shooter] -= 7
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 3:
                    player_details[winner] += 11
                    player_details[shooter] -= 11
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 4:
                    player_details[winner] += 20
                    player_details[shooter] -= 20
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
                else:
                    player_details[winner] += 40
                    player_details[shooter] -= 40
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)
                    self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Invalid input in one or more fields')

        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

class sanliuZimoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Zi Mo', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        winner_label = tk.Label(self, text= 'Select Winner', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        winner_label.place(relx= 0.25, rely= 0.3, anchor= 'center')

        tai_label = tk.Label(self, text= 'Tai', font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
        tai_label.place(relx= 0.25, rely= 0.5, anchor= 'center')

        #DropDown List
        def updatedPlayers():
            players = list(self.controller.shared_data['player_info'].keys())
            winner_droplist['values'] = players

        winner_droplist = ttk.Combobox(self, postcommand= updatedPlayers, width= 40)
        winner_droplist.place(relx= 0.7, rely= 0.3, anchor= 'center')

        tai_droplist = ttk.Combobox(self, values= [1, 2, 3, 4, 5], width= 40)
        tai_droplist.place(relx= 0.7, rely= 0.5, anchor= 'center')

        #Buttons
        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.3, rely= 0.8, anchor= 'center')

        def next():
            winner = tk.StringVar()
            winner = winner_droplist.get()
            tai = int(tai_droplist.get())
            possible_tai = [1, 2, 3, 4, 5]
            zimoBonus_amt = self.controller.shared_data['zimoBonus_amt']
            players = list(self.controller.shared_data['player_info'].keys())
            player_details = self.controller.shared_data['player_info']

            #Event Logging
            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            if (winner in players) and (tai in possible_tai):
                if tai == 1:
                    player_details[winner] += 3*(2 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (2 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 2:
                    player_details[winner] += 3*(3 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (3 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 3:
                    player_details[winner] += 3*(5 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (5 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 4:
                    player_details[winner] += 3*(10 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (10 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(sanliuMainPage)
                elif tai == 5:
                    player_details[winner] += 3*(20 + zimoBonus_amt)
                    for losers in player_details:
                        if losers != winner:
                            player_details[losers] -= (20 + zimoBonus_amt)
                    #Event Logging
                    p1_profit = controller.shared_data['player_info'][p1_name]
                    p2_profit = controller.shared_data['player_info'][p2_name]
                    p3_profit = controller.shared_data['player_info'][p3_name]
                    p4_profit = controller.shared_data['player_info'][p4_name]

                    self.controller.shared_data['event_count'] += 1
                    self.controller.shared_data['event_number'].append(self.controller.shared_data['event_count'])
                    self.controller.shared_data['p1_events'].append(p1_profit)
                    self.controller.shared_data['p2_events'].append(p2_profit)
                    self.controller.shared_data['p3_events'].append(p3_profit)
                    self.controller.shared_data['p4_events'].append(p4_profit)   
                    self.controller.show_frame(sanliuMainPage)
            else:
                tk.messagebox.showerror(title= 'Error', message= 'Invalid input in one or more fields')

        next_button = tk.Button(self, text= 'Next', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= next)
        next_button.place(relx= 0.7, rely= 0.8, anchor= 'center')

class endPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'End Game', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        #Button 
        def results():
            results_button.destroy()    
            back_button.destroy()

            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            p1_profit = controller.shared_data['player_info'][p1_name]
            p2_profit = controller.shared_data['player_info'][p2_name]
            p3_profit = controller.shared_data['player_info'][p3_name]
            p4_profit = controller.shared_data['player_info'][p4_name]

            #Create Labels 
            p1_label = tk.Label(self, text= p1_name, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p1_label.place(relx= 0.2, rely= 0.3, anchor= 'center')

            p2_label = tk.Label(self, text= p2_name, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p2_label.place(relx= 0.2, rely= 0.4, anchor= 'center')

            p3_label = tk.Label(self, text= p3_name, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p3_label.place(relx= 0.2, rely= 0.5, anchor= 'center')

            p4_label = tk.Label(self, text= p4_name, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p4_label.place(relx= 0.2, rely= 0.6, anchor= 'center')

            #Result Labels
            p1_res = tk.Label(self, text= p1_profit, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p1_res.place(relx= 0.7, rely= 0.3, anchor= 'center')
            
            p2_res = tk.Label(self, text= p2_profit, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p2_res.place(relx= 0.7, rely= 0.4, anchor= 'center')

            p3_res = tk.Label(self, text= p3_profit, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p3_res.place(relx= 0.7, rely= 0.5, anchor= 'center')

            p4_res = tk.Label(self, text= p4_profit, font= ('MS Sans Serif', 28, 'bold'), bg= 'papaya whip')
            p4_res.place(relx= 0.7, rely= 0.6, anchor= 'center')

            stats_button = tk.Button(self, text= 'See Statistics', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(statsPage))
            stats_button.place(relx= 0.5, rely= 0.8, anchor= 'center')

        results_button = tk.Button(self, text= 'See Results', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= results)
        results_button.place(relx= 0.5, rely= 0.3, anchor= 'center')

        back_button = tk.Button(self, text= 'Back', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= lambda: controller.show_frame(sanliuMainPage))
        back_button.place(relx= 0.5, rely= 0.5, anchor= 'center')

class statsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg= 'papaya whip')

        #Labels
        header_label = tk.Label(self, text= 'Statistics', font= ('MS Sans Serif', 48, 'bold'), bg= 'papaya whip')
        header_label.place(relx= 0.5, rely= 0.1, anchor= 'center')

        #Plotting
        def plot():
            print_stats.destroy()

            p1_name = controller.shared_data['player_list'][0]
            p2_name = controller.shared_data['player_list'][1]
            p3_name = controller.shared_data['player_list'][2]
            p4_name = controller.shared_data['player_list'][3]

            event_num = controller.shared_data['event_number']
            p1_eventlog = controller.shared_data['p1_events']
            p2_eventlog = controller.shared_data['p2_events']
            p3_eventlog = controller.shared_data['p3_events']
            p4_eventlog = controller.shared_data['p4_events']

            f = Figure(figsize= (8,4), dpi= 100)
            a = f.add_subplot(111)
            a.plot(event_num, p1_eventlog, color= 'r', label= p1_name)
            a.plot(event_num, p2_eventlog, color= 'b', label= p2_name)
            a.plot(event_num, p3_eventlog, color= 'g', label= p3_name)
            a.plot(event_num, p4_eventlog, color= 'y', label= p4_name)
            a.axhline(y= 0, color= 'k')
            a.legend()

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().place(relx= 0.5, rely= 0.5, anchor= 'center')

            #Button
            exit_button = tk.Button(self, text= 'Exit', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= app.destroy)
            exit_button.place(relx= 0.5, rely= 0.9, anchor= 'center')  

        #Button
        print_stats = tk.Button(self, text= 'Print Graph', font= ('MS Sans Serif', 20, 'bold'), bd= 5, command= plot)
        print_stats.place(relx= 0.5, rely= 0.3, anchor= 'center')
      
if __name__ == '__main__':
    app = Application()
    app.mainloop()

#test