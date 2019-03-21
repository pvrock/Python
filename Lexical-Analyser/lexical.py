# if u guys have any queries either mail me at prateekvashist88@gmail.com or comment below.........Happy to help!!
#*****importing modules*****
import texttable as tt
import os
import re
import sys
from Tkinter import *

stack=[]
st={}
l=[]

#*****creating node*****

class node(object):
    def __init__(self):
        self.data_type=None
    def add(self,d):
        self.data_type=d
        
#*****creating symbol table*****
        
class symbol_table:
    def add1(self,x,v):    
        n=node()
        n.add(x)
        st[v]=n
        l.append(v)
    
    def display(self):
        j=len(l)
        for m in range(0,j):
            k=l[m]
            ob=st[k]
            print "Identifier: %s\t\t\tType: %s"%(k,ob.data_type)
            

    def lookup(self,ln):
            if len(stack)==0:
                return
            else:
                e1.error_invalid(ln)

#*****lexeme errors*****
                
class error:
    def error_multiple(self,ln):
        print "Error: Multiple declaration\tline no.: %d"%ln
        getch=raw_input()
        sys.exit(0)
    def error_invalid(self,ln):
        print "Error: Can't use keyword as identifier\tline no.: %d"%ln
        getch=raw_input()
        sys.exit(0)
    def error_declaration(self,ln):
        print "Error: Invalid declaration\tLine no.: %d"%ln
        getch=raw_input()
        sys.exit(0)
    def invalid_expression(self,data1):
        self.init='q0'
        for tt in range(len(data1)):
             if self.init=='q0':
                if data1[tt]=='i':
                    self.init='q1'
                elif data1[tt]=='w':
                    self.init='q4'
                elif data1[tt]=='f':
                    self.init='q10'

             elif self.init=='q1':
                if data1[tt]=='f':
                    self.init='q2'
            
             elif self.init=='q2':
                if data1[tt]=='f':
                    self.init='q3'

             elif self.init=='q10':
                if data1[tt]=='o':
                    self.init='q11'
                    
             elif self.init=='q11':
                if data1[tt]=='r':
                    self.init='q12'

             elif self.init=='q12':
                if data1[tt]=='r':
                    self.init='q13'

             elif self.init=='q4':
                if data1[tt]=='h':
                    self.init='q5'
            
             elif self.init=='q5':
                if data1[tt]=='i':
                    self.init='q6'

             elif self.init=='q6':
                if data1[tt]=='l':
                    self.init='q7'
                    
             elif self.init=='q7':
                if data1[tt]=='e':
                    self.init='q8'

             elif self.init=='q8':
                if data1[tt]=='e':
                    self.init='q9'
        if self.init=='q9':
            print "\n******Suggestion:Use while keyword*******"
        elif self.init=='q3':
            print "\n******Suggestion:Use if keyword******"
        elif self.init=='q13':
            print "\n******Suggestion:Use for keyword******"
            
                    
class nfa:
    def __init__(self):
        self.states=['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                     'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20']
        self.alphabets=['a','b','c','e','h','k','n','o','r','s','t','u'];
        self.delta=None;
        self.initial='q0';
        self.final=['q4','q9','q16','q20'];
    def defdelta(self,data):
        self.init='q0';
        for tt in range(len(data)):

            if self.init=='q0':
                if data[tt]=='a':
                    self.init='q1'
                elif data[tt]=='b':
                    self.init='q5'
                elif data[tt]=='c':
                    self.init='q10'

            elif self.init=='q1':
                if data[tt]=='u':
                    self.init='q2'
            
            elif self.init=='q2':
                if data[tt]=='t':
                    self.init='q3'

            elif self.init=='q3':
                if data[tt]=='o':
                    self.init='q4'

            elif self.init=='q5':
                if data[tt]=='r':
                    self.init='q6'

            elif self.init=='q6':
                if data[tt]=='e':
                    self.init='q7'

            elif self.init=='q7':
                if data[tt]=='a':
                    self.init='q8'

            elif self.init=='q8':
                if data[tt]=='k':
                    self.init='q9'

            elif self.init=='q10':
                if data[tt]=='a':
                    self.init='q11'
                elif data[tt]=='h':
                    self.init='q14'
                elif data[tt]=='o':
                    self.init='q17'

            elif self.init=='q14':
                if data[tt]=='a':
                    self.init='q5'

            elif self.init=='q15':
                if data[tt]=='r':
                    self.init='q16'

            elif self.init=='q17':
                if data[tt]=='n':
                    self.init='q18'

            elif self.init=='q18':
                if data[tt]=='s':
                    self.init='q19'

            elif self.init=='q19':
                if data[tt]=='t':
                    self.init='q20'

    def result(self):
        if self.init=='q4':
            print "Nfa Working"
        elif self.init=='q6':
            print "Nfa Working"
        elif self.init=='q14':
            print "Nfa Working"
        elif self.init=='q20':
            print "Nfa Working"
 
           
            
            
            
n=nfa()              

#*****File dialog*****

import tkFileDialog
def openfile():
    file_path=tkFileDialog.askopenfilename()
    if os.path.exists(file_path):
        f=open(file_path,'r')
        content=f.read()
        app.text.insert(0.0,content)

s1=symbol_table()
e1=error()

def lexical():
    pattern=re.compile("(#(.)*)|(\d{1,3})|(\d+(\w)+)|(\w*_*\w+)|(\"(.*)\")|(<+=+)|(>+=+)|(==+)|(!+=+)|(<+)|(>+)|op|(//(.)*)|(.)|(\s+)|((/\*)+(.)*)")
    scan=pattern.scanner(app.text.get(0.0,END))
    
    keywords=('auto','break','case','char','const','continue','default','do','double','else','enum','extern',
          'float','for','goto','if','int','long','register','return','short','signed','sizeof','static',
          'struct','switch','typedef','union','unsigned','void','volatile','while')
    data=('char','double','float','int','short','void')
    op=('+','-','*','/','%','++','--','?:')
    if_var=None;
    while_var=None;
    for_var=None;
    if_opr=-1;
    while_opr=-1
    for_opr=-1
    logical=('&&','||','!','&','|','^')
    rel=('==','!=','>','<','>=','<=')
    assi=('+=','=','-=','*=','/=','%=','&=','|=','^=')
    line=1
    flag=0
    
    i=0
    p=0

    temp=None

    while 1:
        m=scan.match()
        if not m:
            break
        lexeme=m.group(m.lastindex)
        if lexeme=='\n':
            line=line+1
            if if_opr==0:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)
            elif if_opr==1:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)

            if while_opr==0:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)
            elif while_opr==1:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)

            if for_opr==0:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)
            elif for_opr==1:
                print "Syntax error.....line no. %d "%line
                getch=raw_input()
                sys.exit(0)

            
            del stack[:]
            if i==1:
                e1.error_invalid(line)
                i=0;
            
        if m.lastindex==1:
            print lexeme + "\t\t//Header files"

    #*****operators*****
    
        elif m.lastindex==17:
            if if_var=="if":
                
                if lexeme=='(':
                    if_opr=1
                elif lexeme==')' and if_opr==1:
                    if_opr=2
                    if_var=None

            if while_var=="while":
                
                if lexeme=='(':
                    while_opr=1
                elif lexeme==')' and while_opr==1:
                    while_opr=2
                    while_var=None

            if for_var=="for":
                
                if lexeme=='(':
                    for_opr=1
                elif lexeme==')' and for_opr==1:
                    for_opr=2
                    for_var=None
                
            for word in op:
                if word==lexeme:
                    print lexeme + "\t\t//operator"
                    break
            for word in logical:
                if word==lexeme:
                    print lexeme + "\t\t//Logical operator"
                    break
            for word in rel:
                if word==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    break
            for word in assi:
                if word==lexeme:
                    print lexeme + "\t\t//Assignment operator"
                    break
            if lexeme==';':
                i=0
                p=0
                temp=None
                del stack[:]
            if lexeme==',':
                if temp!=None:
                    i=1

    #*****Keyword/Identifiers*****    

        elif m.lastindex==6:
            e1.invalid_expression(lexeme)
            
            for word in keywords:
                if lexeme=="if":
                    if_var="if"
                    if_opr=0
                if lexeme=="for":
                    for_var="for"
                    for_opr=0
                if lexeme=="while":
                    while_var="while"
                    while_opr=0
                if word==lexeme:
                    s1.lookup(line)
                    n.defdelta(word)
                    n.result()
                    for xyz in data:
                        if xyz==lexeme:
                            temp=lexeme
                        #i=1 when the comiler sees a data type
                            i=1
                            stack.append(lexeme)
                            break
                    flag=1
                    break
                elif i==1:
                    s1.add1(temp,lexeme)
                    i=0
                    p=0
            if flag:
                print lexeme + "\t\t//keyword"
                flag=0
            else:
                print lexeme + "\t\t//identifier"

    #*****numbers*****

        elif m.lastindex==3:
            print lexeme + "\t\t//number"

    #*****Literals*****

        elif m.lastindex==7:
            print lexeme + "\t\t//Literals"

    #*****Comments*****
        
        elif m.lastindex==7:
            print lexeme + "\t\t//comment"

        elif m.lastindex==3:
            e1.error_declaration(line)
        
        elif m.lastindex==9:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)

        elif m.lastindex==10:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)


        elif m.lastindex==11:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)


        elif m.lastindex==12:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)


        elif m.lastindex==13:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)


        elif m.lastindex==14:
            relation=True
            for ch in rel:
                if ch==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    relation=False
            if(relation):
                print lexeme+"\t\t//Invalid operator"
                getch=raw_input()
                sys.exit(0)


#*****Total lines*****
    
    print "\n\nTotal lines: %d"%line

#*****Displaying symbol table*****

    print "\n\n\n*****Symbol table*****\n"
    print s1.display()
                
def close():
    exit()

class application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.widget()
    def widget(self):
        self.label=Label(self,text="Lexical Analyser" ,fg="white",bg="black",font=("@Adobe Fan Heiti Std B", 44))
        self.label.grid(row=0)
        self.text=Text(self,width=70,height=25,bg="seashell")
        self.text.grid(row=1)
        self.text.grid(padx=70,pady=20)
        self.button=Button(self,text="Analyse",command=lexical,fg="red",bg="lavender")
        self.button.grid(row=2,pady=5)
        self.label=Label(self,text="Team members :-\n\t\t\t\tPrateek Vashist\n\t\t\t\t   Ritesh Kumar Singh\n\t\t\t\tRahul Malhotra",fg="white", bg="black",font=("Courier", 8))
        self.label.grid(row=3)
#Creating Window
        
root=Tk()

#Modifying Window

root.title("Lexical analyser")
root.geometry("700x630")
root.configure(background='black')

#putting image in root window
#path = "secure.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel =Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="close",command=close)

menubar.add_cascade(label="File",menu=filemenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About")
helpmenu.add_command(label="Developers")

menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)


#Creating Frame
app=application(root)
app.configure(background="black",height=600)

root.mainloop()
def f2():
    tab = tt.Texttable()
    alphabets=['','a','b','c','e','h','k','n','o','r','s','t','u'];
    x = [[]] # The empty row will have the header

    x.append(['q0','q1','q5','q10','-','-','-','-','-','-','-','-','-'])
    x.append(['q1','-','-','-','-','-','-','-','-','-','-','-','q2'])
    x.append(['q2','-','-','-','-','-','-','-','-','-','-','q3','-'])
    x.append(['q3','-','-','-','-','-','-','-','q4','-','-','-','-'])
    x.append(['(q4)','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q5','-','-','-','-','-','-','-','-','q6','-','-','-'])
    x.append(['q6','-','-','-','-','q7','-','-','-','-','-','-','-'])
    x.append(['q7','q8','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q8','-','-','-','-','-','q9','-','-','-','-','-','-'])
    x.append(['(q9)','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q10','q11','-','-','-','q14','-','-','q17','-','-','-','-'])
    x.append(['q11','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q12','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q13','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q14','q15','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q15','-','-','-','-','-','-','-','-','q16','-','-','-'])
    x.append(['(q16)','-','-','-','-','-','-','-','-','-','-','-','-'])
    x.append(['q17','-','-','-','-','-','-','q18','-','-','-','-','-'])
    x.append(['q18','-','-','-','-','-','-','-','-','-','q19','-','-'])
    x.append(['q19','-','-','-','-','-','-','-','-','-','-','q20','-'])
    x.append(['(q20)','-','-','-','-','-','-','-','-','-','-','-','-'])

    tab.add_rows(x)
    tab.set_cols_align(['r','r','r','r','r','r','r','r','r','r','r','r','r'])
    tab.header(alphabets)
    print "\n\n******Transition Table******\n"
    print tab.draw()

f2();

