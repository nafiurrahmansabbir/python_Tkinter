from tkinter import *
root=Tk()
root.geometry("544x333")
root.title("My GUI....!")

# importance label option
# text - adds the text
# bd - background
# fg - foreground
# font=("comicsansms 19 bold")
# font - sets the font
# padx - x padding
# pady - y padding
# relief- border styling- SUNKEN, RAISED, GROOVE,RIDGE

title_label=Label(text="In publishing and graphic design, Lorem "
                       "\nipsum is a placeholder text "
                       "\ncommonly used to demonstrate the visual"
                       "\n form of a documenl copy"
                       "\n is available.",bg='green',padx=20,pady=20,font=("comicsansms",19,"bold"),borderwidth=3
                  )
title_label.pack()


# importance pack option
# side=top,bottom,left,right
# title_label.pack(side=TOP,anchor="se") #est west north south
title_label.pack(side=TOP,fill=X) #est west north south
# title_label.pack(side=LEFT,fill=Y) #est west north south


root.mainloop()