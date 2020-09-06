# TREBA UPDATE DA SE URADI
# NECE DA OTVORI OUTPUT SECTION KAD SE KLIKNE NA SEE BALANCE

# BALANCE

from tkinter import *
import tkinter as tk
import sqlite3
import Query

def balance(old):
    
    c.execute('SELECT * FROM Balance')
    expences = c.fetchall()
    
    incomes           = old[0]+expences[1]
    food              = old[1]+expences[2]
    food_left         = old[2]-expences[2]
    clothes           = old[3]+expences[3]
    clothes_left      = old[4]-expences[3]
    bills             = old[5]+expences[4]
    bills_left        = old[6]-expences[4]
    direct_debts      = old[7]+expences[5]
    direct_debts_left = old[8]-expences[5]
    other             = old[9]+expences[6]
    other_left        = old[10]-expences[6]
    total             = food+clothes+bills+direct_debts+other 
    left              = old[12]-expences[0]-expences[1]-expences[2]-expences[3]-expences[4]-expences[5]-expences[6]
    
    new=[incomes, food, food_left, clothes, clothes_left, bills, bills_left, direct_debts, direct_debts_left, other, other_left, total, left]
    
    #UPDATE BALANCE
    

# Output section after clicking on button
def output_section(master, list_box, indexes_list):

     s = Query.get_row("Balance",list_box,indexes_list)
     if(s != []):
       # Set column index and its relative weight to distributeadditional space between
       master.grid_columnconfigure(2, weight=1)
       # Make labels and position them
       l1  = tk.Label(master, text="Incomes:"+s[1], width=20, height=2).grid(row=1, column=2)
       l2  = tk.Label(master, text="Food:"+s[2], width=20, height=2).grid(row=2, column=2)
       l3  = tk.Label(master, text="Food Left:"+s[3], width=20, height=2).grid(row=3, column=2)
       l4  = tk.Label(master, text="Clothes:"+s[4], width=20, height=2).grid(row=4, column=2)
       l5  = tk.Label(master, text="Clothes Left:"+s[5], width=20, height=2).grid(row=5, column=2)
       l6  = tk.Label(master, text="Bills:"+s[6], width=20, height=2).grid(row=6, column=2)
       l7  = tk.Label(master, text="Bills Left:"+s[7], width=20, height=2).grid(row=7, column=2)
       l8  = tk.Label(master, text="Direct Debts:"+s[8], width=20, height=2).grid(row=8, column=2)
       l9  = tk.Label(master, text="Direct Debts Left:"+s[9], width=20, height=2).grid(row=9, column=2)
       l10 = tk.Label(master, text="Other:"+s[10], width=20, height=2).grid(row=10, column=2)
       l11 = tk.Label(master, text="Other Left:"+s[11], width=20, height=2).grid(row=11, column=2)
       l12 = tk.Label(master, text="Total:"+s[12], width=20, height=2).grid(row=12, column=2)
       l13 = tk.Label(master, text="Left:"+s[13], width=20, height=2).grid(row=13, column=2)
