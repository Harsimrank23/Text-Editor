#real software 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,colorchooser,font,filedialog
import os

main_application=tk.Tk()
main_application.geometry('1200x800') #it is used to set the dimensions of tkinter window and is used to set the position the main window on the user's desktop geometry (dimensions+alignment along x axis + lignment along y axis)
main_application.title('My Text Editor')
main_application.wm_iconbitmap('icon.ico') #for icon on text editor

######################### main menu ###############################

main_menu=tk.Menu()

#file icons
#for image icon we have PhotoImage class
#initially store images in variable using photoimage claa
new_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\new.png')
open_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\open.png')
save_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\save.png')
save_as_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\save_as.png')
exit_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\exit.png')

file=tk.Menu(main_menu,tearoff=0)
#we will add_commands in functionality because they might need some functions so they should be declared in last

#edit icons
copy_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\copy.png')
cut_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\cut.png')
paste_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\paste.png')
clear_all_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\clear_all.png')
find_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\find.png')

edit=tk.Menu(main_menu,tearoff=0)

#view icons
tool_bar_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\tool_bar.png')
status_bar_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\status_bar.png')

view=tk.Menu(main_menu,tearoff=0)

#color themes
#adding color theme icons
light_default_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\light_default.png')
light_plus_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\light_plus.png')
monokai_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\monokai.png')
red_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\red.png')
night_blue_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\night_blue.png')
dark_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\dark.png')

color_theme=tk.Menu(main_menu,tearoff=0)

theme_choice=tk.StringVar() #it is to store the selected color option
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
#we need dictionary when we add functionality 
#first key value represents text color
#second key value represents background color
color_dict={
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)

#------------------------End main menu----------------------------


######################### toolbar ###############################

##font box
#tk module has font class which has font method which will return tuple of fonts
# print(tk.font.families())
#making label for combobox
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar() #this will store user selected font
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuples #setting values for combobox
font_box.current(font_tuples.index('Arial')) #setting current value as arial
font_box.grid(row=0,column=0,padx=5)

##size box
size_var=tk.IntVar() #store selected user size
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81,2)) #sizes
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

##bold button
bold_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon) #making button for icon
bold_btn.grid(row=0,column=2,padx=5)

##italic button
italic_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon) #making button for icon
italic_btn.grid(row=0,column=3,padx=5)

##underlinne button
underline_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon) #making button for icon
underline_btn.grid(row=0,column=4,padx=5)

##font color button
font_color_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

##align left
align_left_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

##align center
align_center_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=8,padx=5)

##align right
align_right_icon=tk.PhotoImage(file=r'C:\Users\ASUS\Desktop\python\240_project\icons\align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=7,padx=5)

#------------------------End toolbar----------------------------


######################### text editor ###############################

#tk has text class
text_editor=tk.Text(main_application)
# wrap means when we enter into new line whole word will move on in next line not characters thst is why wrap=words
#relief refers to certain simulated 3D effects around outside of the widget- FLAT,RAISED,SUNKEN,GROOVE,RIDGE
text_editor.config(wrap='word',relief=tk.FLAT)

#scrollbar in text editor:
#tk has scrollbar class
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set() #for setting cursor in text editor
#positioning scroll bar
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
#here pack is good option as we want to expand in both the sides
text_editor.pack(expand=True,fill=tk.BOTH)
#how will scroll bar recognize that it is for text editor??
scroll_bar.config(command=text_editor.yview) #command for vertical scrollbar in text editor
text_editor.config(yscrollcommand=scroll_bar.set) #setting scroll bar in vertical direction

#********font family and font size functionality
current_font_family='Arial'
current_font_size=12

#here we had to pass main_application because of bind function here we can pass anything like event=None
def change_font(main_application):
    global current_font_family #because we are globally changing it
    current_font_family=font_family.get() #gettng selected font from storing variable
    #now changing font of text editor
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size #because we are globally changing it
    current_font_size=size_var.get() 
    text_editor.configure(font=(current_font_family,current_font_size))

#binding combobox with the function:
#combobox_name("<<ComboboxSelected>>",function_name)
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)


#************buttons functionality***************

##bold button functionality
#we imported tk.font which has Font class which has method actual() which return default properties
#print(tk.font.Font(font=text_editor['font']).actual())
#in output we get dictionary of properties
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    #if weight is normal change into bold if it is bold change into normal
    if text_property.actual()['weight']=='normal':
        #weight is a propety returned by actual method
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

#giving bold button command
bold_btn.configure(command=change_bold)

##Italic button functionality
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    #if slant is roman change into italic if it is italic change into roman
    if text_property.actual()['slant']=='roman':
        #slant is a propety returned by actual method
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

#giving italic button command
italic_btn.configure(command=change_italic)

##underline button functionality
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    #if slant is roman change into italic if it is italic change into roman
    if text_property.actual()['underline']==0:
        #slant is a propety returned by actual method
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)

##font color functionality
def change_font_color():
    #colorchooser module has askcolor method which makes complete color window to choose from and selected color will be stored in the variable
    color_var=tk.colorchooser.askcolor()
    #print(color_var) -->gives two indexed tuple index 1 is hexagonal color which is easy to use so we will work with 1 index
    text_editor.configure(fg=color_var[1]) #fg is for foreground color which is for text

font_color_btn.configure(command=change_font_color)

##align functionality

#left
def align_left():
    #first we will store all the text content in the variable from 1 to end
    text_content=text_editor.get(1.0,'end')
    #capture content and left is for left alignment
    text_editor.tag_config('left',justify=tk.LEFT)
    #and delete everything from text editor
    text_editor.delete(1.0,tk.END)
    #then we will insert in text editor-->text_editor.insert(tk.Insert,content,position)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

#center
def align_center():
    #first we will store all the text content in the variable from 1 to end
    text_content=text_editor.get(1.0,'end')
    #capture content and left is for left alignment
    text_editor.tag_config('center',justify=tk.CENTER)
    #and delete everything from text editor
    text_editor.delete(1.0,tk.END)
    #then we will insert in text editor-->text_editor.insert(tk.Insert,content,position)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

#right
def align_right():
    #first we will store all the text content in the variable from 1 to end
    text_content=text_editor.get(1.0,'end')
    #capture content and left is for left alignment
    text_editor.tag_config('right',justify=tk.RIGHT)
    #and delete everything from text editor
    text_editor.delete(1.0,tk.END)
    #then we will insert in text editor-->text_editor.insert(tk.Insert,content,position)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

#suppose if u want to start type initialy in editor in ARIAL and with font size=12:
text_editor.configure(font=('Arial',12))

#------------------------End text editor----------------------------


######################## status bar ###############################

#status bar for giving info of char and no of words
status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False #will be useful while making exit functionality

def changed(event=None):
    global text_changed
    #text_editor has method edit_modified which tells weather text has been modified or not if it is modified then we want to count the words
    if text_editor.edit_modified():
        text_changed=True
        #counting words again
        words=len(text_editor.get(1.0,'end-1c').split()) #end-1c means read till end but last newline is not counted unnecessarily and split is used to count different words
        #counting char again
        characters=len(text_editor.get(1.0,'end-1c')) #spaces are also counted as characters
        #status bar written content
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False) #to update everytime we modify our text because when we call edit_modified its value will remain true so we need to false everytime

#binding function with text editor
text_editor.bind('<<Modified>>',changed)


#------------------------End status bar----------------------------


######################### main menu functionality ###############################

#variable:
url=''  #bestway to tell if file is present or not by seeing its url if it is empty then file already exists

#new functionaliy:

def new_file(event=None):
    global url
    #creating new file and deleting old ones
    url=''
    text_editor.delete(1.0,tk.END)

#file_commands

#add labels in file menu and pass image for icon and compound=tk.Left means icon should stick to the left side so that they do not overlap each other
#like for mentioning shortcut key we can write in label too but best method is using accelarator='text'
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

#open functionaliy:

def open_file(event=None):
    global url
    #will ask user to which file open for this we have filedialog module which has askopenfilename function in this we will pass initial dirctory which will be cwd and title ,filetype etc
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    #i user didnt select any file there will be error so we will handel it
    try:
        with open(url,'r') as fr:
            #now we had to open that file read from that and write 
            text_editor.delete(1.0,tk.END) #if something is written on editor delete it and read from opened file and insert on text editor
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url)) #title will be selected file

file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

#save functionality

def save_file(event=None):
    global url
    try:
        if url: #that is if file already exists
            #now we had to read that file and convert into string
            content=str(text_editor.get(1.0,tk.END)) 
            #after reading open that file in write mode
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content) #just reading from the stored variable and writing into the file 
        else: #if url doesnt exist 
            #same as askopenfilename method
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

#save as functionality

def save_as(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        content=str(text_editor.get(1.0,tk.END))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)

#exit functionality

def exit_func(event=None):
    global url,text_changed #text_changed defined above will tell if file is modified or not
    try:
        if text_changed: #if modified
            mbox=messagebox.askyesnocancel('warning','Do you want to save the file ?') #warning messagebox
            if mbox is True: #same save_file function
                if url:
                    content=str(text_editor.get(1.0,tk.END)) 
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content) 
                        main_application.destroy() #for exit
                else: 
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy() #simply destroy
        else: #if not modified
            main_application.destroy() #if not modified simply destroy
    except:
        return

file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

#edit commands
#adding commands/labels in edit menu
#functionality using lambda function
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Clear all',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))

##find functionality :bit different from above
def find_func(event=None):
    
    def find():
        word=find_input.get() #get the input word/char to find
        text_editor.tag_remove('match','1.0',tk.END) #remove tag initially
        matches=0 #initialize with 0
        if word:#if user has input some word
            start_pos='1.0'
            while True: #run till word will be finded
                #change start pos accordingly 
                #text_editor has search function which will search for the word
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos: #that is when word is not found
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                #adding tag where searched word is there and changing is foreground(text) and background color
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                #used to configure tag properties
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word=find_input.get() #get the input word/char to replace
        replace_text=replace_input.get() #get the word to be replaced with
        #store all the content in a variable
        content=text_editor.get(1.0,tk.END)
        #store new content in a variable by using replace method
        new_content=content.replace(word,replace_text)
        #now delete all the old content
        text_editor.delete(1.0,tk.END)
        #insert the new content
        text_editor.insert(1.0,new_content)
    
    #creating pop up window to find
    #there is toplevel class in tk:
    find_dialogue=tk.Toplevel()
    #setting its geometry
    find_dialogue.geometry('450x250+500+200')#geometry(size,left,right)
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0) #we cannot resize it with this parameter

    ##creating frame on find_dialogue
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    ##labels on frame
    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_replace_label=ttk.Label(find_frame,text='Replace : ')

    ##entry boxes on frame
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    ##button on frame
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    
    ##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    ##entry boxes grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    ##button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop() #we dont want to close filedialogue box automatically


edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

#view button
#in view we are adding checkbuttons to view checked bar

show_statusbar=tk.BooleanVar() #to store true and false value
show_statusbar.set(True) #initially set there values to true
show_toolbar=tk.BooleanVar() #to store true and false value
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar #for changing its values
    if show_toolbar: #if value is true
        #then hide it
        #pack_forget function hides the toolbar
        tool_bar.pack_forget()
        show_toolbar=False
    else:#if toolbar is already hidden then we will show it
        #to make arrangement as previous we need to forget text editor and status bar then pack them in sequence
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar #for changing its values
    if show_statusbar: #if value is true
        #then hide it
        #pack_forget function hides the statusar
        status_bar.pack_forget()
        show_statusbar=False
    else:#if statusbar is already hidden then we will show it
        #here we can directly hide/unhide status bar as it is in bottom
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


#in this we will add onvalue=True and offvalue=False because initialyy we want toolbar and status bar to show 
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=status_bar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

##color theme

#color theme functionality

def change_theme():
    chosen_theme=theme_choice.get() #defined in the beggining
    color_tuple=color_dict.get(chosen_theme) #getting color tuple fg and bg  from the dictionary defined above
    fg_color,bg_color=color_tuple[0],color_tuple[1] #extracting fg and bg from the tuple
    text_editor.config(background=bg_color,foreground=fg_color)

count=0 #to iterate the index in dictionary
for i in color_dict: #i will give key
    #addinf radiobuttons for choosing colors
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme) #image can be extracted from tuple and for storing color value we are doing variable=theme_choice
    count+=1

#------------------------End main menu functionality----------------------------

main_application.config(menu=main_menu)


##binding shortcut keys
main_application.bind("<Control-n>",new_file) #new key bind
main_application.bind("<Control-o>",open_file) #open key bind
main_application.bind("<Control-s>",save_file) #save key bind
main_application.bind("<Control-Alt-s>",save_as) #nsave as key bind
main_application.bind("<Control-q>",exit_func) #exit key bind
main_application.bind("<Control-f>",find_func) #find key bind



main_application.mainloop()