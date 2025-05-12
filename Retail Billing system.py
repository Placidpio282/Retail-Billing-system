from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

#==============================================================================================!
                                                                                          #FUNCTIONALITY PART:
#==============================================================================================!
#-----------------------------------------------------------------!
                              #CLEAR BUTTON:
#-----------------------------------------------------------------!

def clear():
      bathsoapEntry.delete(0,END)
      facecreamEntry.delete(0,END)
      facewashEntry.delete(0,END)
      hairsprayEntry.delete(0,END)
      hairgelEntry.delete(0,END)
      bodylotionEntry.delete(0,END)

      riceEntry.delete(0,END)
      oilEntry.delete(0,END)
      daalEntry.delete(0,END)
      wheatEntry.delete(0,END)
      sugarEntry.delete(0,END)
      teaEntry.delete(0,END)

      maazaEntry.delete(0,END)
      pepsiEntry.delete(0,END)
      spriteEntry.delete(0,END)
      bovontoEntry.delete(0,END)
      frootiEntry.delete(0,END)
      cocacolaEntry.delete(0,END)

      cosmeticpriceEntry.delete(0,END)
      grocerypriceEntry.delete(0,END)
      colddrinkspriceEntry.delete(0,END)

      cosmetictaxEntry.delete(0,END)
      grocerytaxEntry.delete(0,END)
      colddrinkstaxEntry.delete(0, END)

      nameEntry.delete(0,END)
      phonenumberEntry.delete(0,END)
      billnumberEntry.delete(0,END)
      
      textarea.delete(1.0,END)

#-----------------------------------------------------------------!
                            #EMAIL BUTTON:
#-----------------------------------------------------------------!

def send_email(): 
    def send_gmail():
        try:
              ob=smtplib.SMTP('smtp.gmail.com',587)
              ob.starttls()
              ob.login(senderEntry.get(),passwordEntry.get())
              message=email_textarea.get(1.0,END)
              ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
              ob.quit()
              messagebox.showinfo('Success',' Bill is Successfully sent',parent=root1)
        except:
            messagebox.showerror('Error','Something went wrong, Please try again', parent=root1)
          
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
            root1=Toplevel()
            root1.title('send gmail')
            root1.config(bg='gray20')
            root1.resizable(0,0)
            
            senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
            senderFrame.grid(row=0,column=0,padx=40,pady=20)
            
            senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
            senderLabel.grid(row=0,column=0,padx=10,pady=8)

            senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            senderEntry.grid(row=0,column=1,padx=10,pady=8)

            passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
            passwordLabel.grid(row=1,column=0,padx=10,pady=8)

            passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
            passwordEntry.grid(row=1,column=1,padx=10,pady=8)


            recipientFrame=LabelFrame(root1,text='RECIPENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
            recipientFrame.grid(row=1,column=0,padx=40,pady=20)


            recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
            recieverLabel.grid(row=0,column=0,padx=10,pady=8)

            recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
            recieverEntry.grid(row=0,column=1,padx=10,pady=8)

            messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
            messageLabel.grid(row=1,column=0,padx=10,pady=8)

            email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                                width=42,height=11)
            email_textarea.grid(row=2,column=0,columnspan=2)
            email_textarea.delete(1.0,END)
            email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t         ').replace('\t\t','\t\t   '))

            sendButton=Button(root1,text='send',font=('arial',16,'bold'),width=15,command=send_gmail)
            sendButton.grid(row=2,column=0,pady=20)      
            
            root1.mainloop()

#-----------------------------------------------------------------!
                              #BILL BUTTON:
#-----------------------------------------------------------------!            

def print_bill():
    if textarea.get(1.0,END)=='\n':
         messagebox.showerror('Error','Bill is empty')
    else:
          file=tempfile.mktemp('.txt')
          open(file,'w').write(textarea.get(1.0,END))
          os.startfile(file,'print')
#-----------------------------------------------------------------!
                              #SEARCH BUTTON:
#-----------------------------------------------------------------!          
    
def search_bill():
    for i in os.listdir('C:\\Users\\picasso\\Desktop\\python\\PROJECT.PY\\bills/'):
          if i.split('.')[0]==billnumberEntry.get():
               f=open(f'C:\\Users\\picasso\\Desktop\\python\\PROJECT.PY\\bills/{i}','r')
               textarea.delete(1.0,END)
               for data in f:
                      textarea.insert(END,data)
               f.close()
               break
    else:
        messagebox.showerror('Error','Invaild Bill Number')
        
if not os.path.exists('C:\\Users\\picasso\\Desktop\\python\\PROJECT.PY\\bills'):
    os.mkdir('C:\\Users\\picasso\\Desktop\\python\\PROJECT.PY\\bills')

#-----------------------------------------------------------------!
                             #SAVE BILL
#-----------------------------------------------------------------!

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
         bill_content=textarea.get(1.0,END)
         file=open(f'C:\\Users\\picasso\\Desktop\\python\\PROJECT.PY\\bills/{billnumber}.txt','w')
         file.write(bill_content)
         file.close()
         messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
         billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

#-----------------------------------------------------------------!
                             #BILL AREA:
#-----------------------------------------------------------------!

def bill_area():
      if nameEntry.get()=='' or phonenumberEntry.get()=='':
          messagebox.showerror('Error','Customer Details Are Required')
      elif cosmeticpriceEntry.get()=='' and  grocerypriceEntry.get()=='' and colddrinkspriceEntry.get()=='':
         messagebox.showerror('Error', 'No Products are selected')
      elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and colddrinkspriceEntry.get()=='0 Rs' :
          messagebox.showerror('Error', 'No Products are selected')
      else:
              textarea.delete(1.0,END)
                     
              textarea.insert(END,'\t\t**Welcome Customer**\n')
              textarea.insert(END,f'\nBill number: {billnumber}')
              textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
              textarea.insert(END,f'\nCustomer Phone Number: {phonenumberEntry.get()}')
              textarea.insert(END,'\n================================================')
              textarea.insert(END,'\nProduct\t\t    Quantity\t\t        Price')
              textarea.insert(END,'\n================================================')

#-----------------------------------------------------------------!
#BILL AREA: cosmetics Items            
#-----------------------------------------------------------------!
              if bathsoapEntry.get()!='0':
                          textarea.insert(END,f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t{soapprice} Rs')
              if facecreamEntry.get()!='0':
                          textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t{facecreamprice} Rs')
              if facewashEntry.get()!='0':
                          textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t{facewashprice} Rs')
              if hairsprayEntry.get()!='0':
                          textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t{hairsparyprice} Rs')
              if hairgelEntry.get()!='0':
                          textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t{hairgelprice} Rs')
              if bodylotionEntry.get()!='0':
                          textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t{bodylotionprice} Rs')
#-----------------------------------------------------------------!
#BILL AREA: grocery Items
#-----------------------------------------------------------------!
              if riceEntry.get()!='0':
                          textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t{riceprice} Rs')
              if oilEntry.get()!='0':
                          textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t{oilprice} Rs')
              if daalEntry.get()!='0':
                          textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t{daalprice} Rs')
              if wheatEntry.get()!='0':
                          textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t{wheatprice} Rs')
              if sugarEntry.get()!='0':
                          textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t{sugarprice} Rs')
              if teaEntry.get()!='0':
                          textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t{teaprice} Rs')
#-----------------------------------------------------------------!
#BILL AREA: cooldrinks Items
#-----------------------------------------------------------------!
              if maazaEntry.get()!='0':
                          textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t{maazaprice} Rs')
              if pepsiEntry.get()!='0':
                          textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t{pepsiprice} Rs')
              if spriteEntry.get()!='0':
                          textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t{spriteprice} Rs')
              if bovontoEntry.get()!='0':
                          textarea.insert(END,f'\nBovonto\t\t\t{bovontoEntry.get()}\t\t{bovontoprice} Rs')
              if frootiEntry.get()!='0':
                          textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t{frootiprice} Rs')
              if cocacolaEntry.get()!='0':
                          textarea.insert(END,f'\nCocacola\t\t\t{cocacolaEntry.get()}\t\t{cocacolaprice} Rs')
              textarea.insert(END,'\n------------------------------------------------')

              if cosmetictaxEntry.get()!='0.0 Rs':
                          textarea.insert(END,f'\nComestic Tax\t\t\t{cosmetictaxEntry.get()}')
              if grocerytaxEntry.get()!='0.0 Rs':
                          textarea.insert(END,f'\nGrocery Tax\t\t\t{grocerytaxEntry.get()}')
              if colddrinkstaxEntry.get()!='0.0 Rs':
                          textarea.insert(END,f'\nCool Drinks Tax\t\t\t{colddrinkstaxEntry.get()}')
              textarea.insert(END,f'\nTotal bill \t\t\t{totalbill}')
              textarea.insert(END,'\n------------------------------------------------')
              save_bill()

#==============================================================================================!

#-----------------------------------------------------------------!
                        #TOTAL BUTTON:
#-----------------------------------------------------------------!

def total ():
    global soapprice,facecreamprice,facewashprice,hairsparyprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global maazaprice,pepsiprice,spriteprice,bovontoprice,frootiprice,cocacolaprice
    global totalbill
   
#-----------------------------------------------------------------!     
#Cosmetics price calculation PART:
#-----------------------------------------------------------------!    
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsparyprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facewashprice+facecreamprice+hairsparyprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0, f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END) 
    cosmetictaxEntry.insert(0,str(cosmetictax) +'Rs' )
   
#-----------------------------------------------------------------!    
    #grocery price calculation PART:
#-----------------------------------------------------------------!
    
    riceprice=int(riceEntry.get())* 20  
    oilprice=int(oilEntry.get())*20
    daalprice=int(daalEntry.get())*20
    wheatprice=int(wheatEntry.get())*20
    sugarprice=int(sugarEntry.get())*20
    teaprice=int(teaEntry.get())*20

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+' Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END) 
    grocerytaxEntry.insert(0,str(grocerytax) +'Rs' )

#-----------------------------------------------------------------!    
    #colddrinks price calculation PART:
#-----------------------------------------------------------------!
    maazaprice=int(maazaEntry.get())*10
    pepsiprice=int(pepsiEntry.get())*10
    spriteprice=int(spriteEntry.get())*10
    bovontoprice=int(bovontoEntry.get())*10
    frootiprice=int(frootiEntry.get())*10
    cocacolaprice=int(cocacolaEntry.get())*10
    
    totalcolddrinksprice=maazaprice+pepsiprice+spriteprice+bovontoprice+frootiprice+cocacolaprice
    colddrinkspriceEntry.delete(0,END)
    colddrinkspriceEntry.insert(0, str(totalcolddrinksprice)+' Rs ')
    colddrinkstax=totalcolddrinksprice*0.08
    colddrinkstaxEntry.delete(0, END) 
    colddrinkstaxEntry.insert(0, str(colddrinkstax) + ' Rs' )

    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddrinkstax

#==============================================================================================!
                                                                                                      #GUI PART:
#==============================================================================================!   
        
root= Tk()
root.title('Retail Billng System' )
root.geometry('1270x685')
root.iconbitmap('icon-icon.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='firebrick3',
                   fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#==============================================================================================!
Customer_details_frame=LabelFrame(root,text='Cusmoter Details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='firebrick3')
Customer_details_frame.pack(fill=X)
#==============================================================================================!
nameLabel=Label(Customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
nameLabel.grid(row=0,column=0,padx=55,pady=2)

nameEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=1)
#==============================================================================================!
phonenumberLabel=Label(Customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
phonenumberLabel.grid(row=0,column=2,padx=40,pady=2)

phonenumberEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
phonenumberEntry.grid(row=0,column=3,padx=0)
#==============================================================================================!
billnumberLabel=Label(Customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(Customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=6,padx=0)
#==============================================================================================!

searchButton=Button(Customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,bg='red3',fg='gold',
                    width=10,command=search_bill)
searchButton.grid(row=0,column=10,padx=35,pady=8 )

#==============================================================================================!

productsFrame=Frame(root)
productsFrame.pack()

#==============================================================================================!
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),
                                  fg='red4',bd=8,relief=GROOVE,bg='ghost white',pady=20)
cosmeticsFrame.grid(row=0,column=0,padx=5)
#==============================================================================================!

bathsoapLabel=Label(cosmeticsFrame,text='Bath soap',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
bathsoapEntry.grid(row=0,column=1,padx=20)
bathsoapEntry.insert(0,0)

#==============================================================================================!
facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
facecreamEntry.grid(row=1,column=1,padx=20)
facecreamEntry.insert(0,0)
#==============================================================================================!
facewashLabel=Label(cosmeticsFrame,text='Face Wish',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
facewashEntry.grid(row=2,column=1,padx=20)
facewashEntry.insert(0,0)
#==============================================================================================!
hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=20)
hairsprayEntry.insert(0,0)
#==============================================================================================!
hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
hairgelEntry.grid(row=4,column=1,padx=20)
hairgelEntry.insert(0,0)
#==============================================================================================!
bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=9,bd=5)
bodylotionEntry.grid(row=5,column=1,padx=20)
bodylotionEntry.insert(0,0)
#==============================================================================================!
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),
                                  fg='red4',bd=8,relief=GROOVE,bg='ghost white',pady=20)
groceryFrame.grid(row=0,column=1)
#==============================================================================================!
riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
riceLabel.grid(row=0,column=0,pady=9,padx=20,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
riceEntry.grid(row=0,column=1,padx=35)
riceEntry.insert(0,0)
#==============================================================================================!
oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
oilLabel.grid(row=1,column=0,pady=9,padx=20,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
oilEntry.grid(row=1,column=1,padx=35)
oilEntry.insert(0,0)
#==============================================================================================!
daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
daalLabel.grid(row=2,column=0,pady=9,padx=20,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
daalEntry.grid(row=2,column=1,padx=35)
daalEntry.insert(0,0)
#==============================================================================================!
wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
wheatLabel.grid(row=3,column=0,pady=9,padx=20,sticky='w')
 
wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
wheatEntry.grid(row=3,column=1,padx=35)
wheatEntry.insert(0,0)
#==============================================================================================!
sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
sugarLabel.grid(row=4,column=0,pady=9,padx=20,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
sugarEntry.grid(row=4,column=1,padx=35)
sugarEntry.insert(0,0)
#==============================================================================================!
teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
teaLabel.grid(row=5,column=0,pady=9,padx=20,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=9,bd=5)
teaEntry.grid(row=5,column=1,padx=35)
teaEntry.insert(0,0)
#==============================================================================================!
colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),
                                  fg='red4',bd=8,relief=GROOVE,bg='ghost white',pady=20)
colddrinksFrame.grid(row=0,column=2,padx=5)
#==============================================================================================!

maazaLabel=Label(colddrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
maazaLabel.grid(row=0,column=0,pady=9,padx=20,sticky='w')

maazaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
maazaEntry.grid(row=0,column=3,padx=40)
maazaEntry.insert(0,0)
#==============================================================================================!
pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
pepsiLabel.grid(row=1,column=0,pady=9,padx=20,sticky='w')

pepsiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
pepsiEntry.grid(row=1,column=3,padx=40)
pepsiEntry.insert(0,0)
#==============================================================================================!
spriteLabel=Label(colddrinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
spriteLabel.grid(row=2,column=0,pady=9,padx=20,sticky='w')

spriteEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
spriteEntry.grid(row=2,column=3,padx=40)
spriteEntry.insert(0,0)
#==============================================================================================!
bovontoLabel=Label(colddrinksFrame,text='Bovonto',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
bovontoLabel.grid(row=3,column=0,pady=9,padx=20,sticky='w')

bovontoEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
bovontoEntry.grid(row=3,column=3,padx=40)
bovontoEntry.insert(0,0)
#==============================================================================================!
frootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
frootiLabel.grid(row=4,column=0,pady=9,padx=20,sticky='w')

frootiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
frootiEntry.grid(row=4,column=3,padx=40)
frootiEntry.insert(0,0)
#==============================================================================================!
cocacolaLabel=Label(colddrinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='ghost white',fg='gray20')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=20,sticky='w')

cocacolaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=9,bd=5)
cocacolaEntry.grid(row=5,column=3,padx=40)
cocacolaEntry.insert(0,0)
#==============================================================================================!
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=8)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=19, width=48,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)
#==============================================================================================!
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),
                         fg='gold',bd=8,relief=GROOVE,bg='firebrick3')
billmenuFrame.pack(pady=1)
#==============================================================================================!
cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,padx=9)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,padx=9)

colddrinkspriceLabel=Label(billmenuFrame,text='Colddrinks Price',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
colddrinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

colddrinkspriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
colddrinkspriceEntry.grid(row=2,column=1,padx=9)

#==============================================================================================!

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,padx=9)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,padx=9)

colddrinkstaxLabel=Label(billmenuFrame,text='Colddrinks Tax',font=('times new roman',15,'bold'),bg='firebrick3',fg='white')
colddrinkstaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

colddrinkstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
colddrinkstaxEntry.grid(row=2,column=3,padx=9)

#==============================================================================================!

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='red3',fg='gold',
                   bd=5,width=8,padx=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='red3',fg='gold',
                   bd=5,width=8,padx=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='red3',fg='gold',
                   bd=5,width=8,padx=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='red3',fg='gold',
                   bd=5,width=8,padx=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='red3',fg='gold',
                   bd=5,width=8,padx=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

#==============================================================================================!

