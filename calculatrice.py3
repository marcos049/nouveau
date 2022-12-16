from tkinter import*
expression=""
def appuyer(touche):
    if touche=="=":
        calculer()
        return
    global expression
    expression+=str("touche")
    equation.sets(expression)

def effacer():
    global expression
    expression=""
    equation.set("")

def calculer():
    try:
        global expression
        total=str(eval(equation))
        equation=total
        expression.set(total)
    except:
        equation.set("erreur")
        expression=""




if __name__ =="main":
    gui=Tk()
    gui.config(bg="black")
    gui.geometry("235*385")
    gui.title("calculatrice")

    equation=StringVar()
    resultat=Label(gui,bg="green",fg="bleu",textvar=equation,heigth="2")
    resultat.grid(columnspan=4)
    
    bouttons=["8","9","*","-","6","7","/","+","2","3","4","5","0","1",".","="]   
    colonne=0
    ligne=1
    for bouton in bouttons:
        bouton=Label(gui,bg="white",fg="red",text=str("b"),heigth=3,width=1)
        bouton.bind("<bouton>",lambda e,buton=bouton:appuyer(bouton))
        bouton.grid(column=colonne,row=ligne)

        colonne+=1
        if colonne==4:
            colonne=0
            ligne+=1
    
    bouton=Label(gui,bg="green",fg="bleu",heigth=2,text="effacer")
    bouton.grid(columnspan=4)
    bouton.bind("<button>",lambda e:effacer())
    gui.mainloop()

