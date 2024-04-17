from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
from datetime import date



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")


        #variables
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.cust_id=StringVar()
        z=random.randint(1000,9999)
        self.cust_id.set(z)
        self.datetimes=StringVar()
        


        ####product category list
        self.Category=["Select Option","Cloths","Cosmatics","Mobiles"]


        #SUBCATCLOTHS
        self.subcatclothes=["Pant", "T-Shirt", "Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=8000

        self.t_shirt=["Polo","Roadstar","Jack&Jones"]
        self.price_polo=1500
        self.price_roadstar=1700
        self.price_jackjones=1800

        self.shirt=["Peter England","Lovis Phillipe","Park Avenue"]
        self.price_peter=2100
        self.price_lovis=2700
        self.price_park=1800
         

         #subcatcosmatics
        self.subcatcosmatics=["Bath Soap", "Face Cream", "Hair Oil"]
        self.bath_soap=["Lux","Santoor","Pears","Dove"]
        self.price_lux=50
        self.price_santoor=70
        self.price_pears=80
        self.price_dove=60

        self.face_cream=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=50
        self.price_ponds=30
        self.price_olay=40
        self.price_garnier=60

        self.hair_oil=["Parachute","Jashmin","Bajaj"]
        self.price_parachute=40
        self.price_jashmin=30
        self.price_bajaj=60
        

        #subcatmobile
        self.subcatmobiles=["Iphone","Samsung","Xiome", "Real Me", "One+"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_ix=50000
        self.price_i11=70000
        self.price_i12=80000

        self.Samsung=["Samsung M16","Samsung M12","Samsung M121"]
        self.price_sm16=15000
        self.price_sm12=17000
        self.price_sm21=18000

        self.Xiome=["Red11","Redme-12","RedmePro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_rel12=52000
        self.price_rel13=27000
        self.price_relpro=28000

        self.OnePlus=["OnePlus1","OnePlus2","OnePlus3"]
        self.price_one1=45000
        self.price_one2=47000
        self.price_one3=48000
        



    


        #image1
        img1=Image.open(r"gol.jpg")
        img1=img1.resize((500,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img=Label(self.root,image=self.photoimg1)
        lbl_img.place(x=0,y=0,width=500,height=50)


         #image2
        img2=Image.open(r"gol.jpg")
        img2=img2.resize((500,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img=Label(self.root,image=self.photoimg2)
        lbl_img.place(x=500,y=0,width=500,height=50)


         #image3
        img3=Image.open(r"gol.jpg")
        img3=img3.resize((520,50),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_img=Label(self.root,image=self.photoimg3)
        lbl_img.place(x=1000,y=0,width=520,height=50)


        ######label
        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("TIMES NEW ROMAN",22,"bold"),bg="white",fg="red")
        lbl_title.place(x=3,y=30,width=1530,height=42)



        #main frame
        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=70,width=1530,height=600)




        #customer label frame
        Cust_frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_frame.place(x=10,y=0,width=310,height=120)

        def time():
            string = strftime('%m-%d-%Y     %H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font=("times new roman",16,"bold"),bg="white",fg="orangered")
        lbl.place(x=960,y=(-7),width=320,height=50)
        time()


         
         #mobile
        self.lbl_mob=Label(Cust_frame,text="Mobile no.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

              #name
       
        self.lblcustname=Label(Cust_frame,text="Customer name",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblcustname.grid(row=1,column=0,sticky=W,pady=2,padx=5)

        self.textcustname=ttk.Entry(Cust_frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=24)
        self.textcustname.grid(row=1,column=1,sticky=W,pady=2,padx=5)

              #email
        self.lblemail=Label(Cust_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        self.lblemail.grid(row=2,column=0,sticky=W,pady=2,padx=5)

        self.textemail=ttk.Entry(Cust_frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=24)
        self.textemail.grid(row=2,column=1,sticky=W,pady=2,padx=5)




               #product label frame
        Product_frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_frame.place(x=320,y=0,width=530,height=120)
        



        #category
        self.lblCategory=Label(Product_frame,font=("times new roman",12,"bold"),bg="white",text="Select Category",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(Product_frame,value=self.Category,font=('arial',9,'bold'),width=24,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)


              #subcategory
        self.lblSubCategory=Label(Product_frame,font=("times new roman",12,"bold"),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.comboSubcategory=ttk.Combobox(Product_frame,value=[""],font=('arial',9,'bold'),width=24,state="readonly")
        self.comboSubcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.comboSubcategory.bind("<<ComboboxSelected>>",self.product_add)


              #product name
        self.lblproduct=Label(Product_frame,font=("times new roman",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.comboproduct=ttk.Combobox(Product_frame,textvariable=self.product,font=('arial',9,'bold'),width=24,state="readonly")
        self.comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.comboproduct.bind("<<ComboboxSelected>>",self.pricce)


              #price
        self.lblprice=Label(Product_frame,font=("times new roman",12,"bold"),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.comboprice=ttk.Combobox(Product_frame,textvariable=self.prices,font=('arial',9,'bold'),width=15,state="readonly")
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)



              #qty
        self.lblqty=Label(Product_frame,font=("times new roman",12,"bold"),bg="white",text="QTY",bd=4)
        self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.comboqty=ttk.Entry(Product_frame,textvariable=self.qty,font=('arial',9,'bold'),width=15)
        self.comboqty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        #middle image frame
        middleframe=Frame(Main_frame,bd=4)
        middleframe.place(x=10,y=130,width=830,height=340)


            #image4
        img4=Image.open(r"nat.jpg")
        img4=img4.resize((360,340),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl_img=Label(middleframe,image=self.photoimg4)
        lbl_img.place(x=0,y=30,width=360,height=340)


         #image5
        img5=Image.open(r"girl.jpg")
        img5=img5.resize((550,340),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbl_img=Label(middleframe,image=self.photoimg5)
        lbl_img.place(x=370,y=0,width=470,height=340)

          #id
        self.lbl_mob=Label(middleframe,text="Customer Id",font=("times new roman",12,"bold"))
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(middleframe,textvariable=self.cust_id,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.entry_mob.grid(row=0,column=1)





        #search
        search_frame=Frame(Main_frame,bd=2,bg="white")
        search_frame.place(x=860,y=0,width=500,height=40)

        self.lblbill=Label(search_frame,font=("times new roman",12,"bold"),bg="red",fg="white",text="Bill No.")
        self.lblbill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_entry=ttk.Entry(search_frame,textvariable=self.search_bill,font=('arial',9,'bold'),width=24)
        self.txt_entry.grid(row=0,column=1,sticky=W,padx=2)

        self.btnsearch=Button(search_frame,text="Search",command=self.find_bill,font=("times new roman",13,"bold"),fg="white",bg="orangered",width=13,cursor="hand2")
        self.btnsearch.grid(row=0,column=2)

        



        #bill area
        rightlabelframe=LabelFrame(Main_frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        rightlabelframe.place(x=855,y=30,width=405,height=410)


        scroll_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("arial",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        #bill counter
        button_frame=LabelFrame(Main_frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        button_frame.place(x=0,y=435,width=1530,height=130)


        #subtotal
        self.lblsubtotal=Label(button_frame,font=("times new roman",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entrysubtotal=ttk.Entry(button_frame,textvariable=self.sub_total,font=('arial',9,'bold'),width=15,state="readonly")
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        


                #gov tax
        self.lbl_tax=Label(button_frame,font=("times new roman",12,"bold"),bg="white",text="Gov. Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(button_frame,textvariable=self.tax_input,font=('arial',9,'bold'),width=15,state="readonly")
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)


                #total
        self.lblamounttotal=Label(button_frame,font=("times new roman",12,"bold"),bg="white",text="Total",bd=4)
        self.lblamounttotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtamounttotal=ttk.Entry(button_frame,textvariable=self.total,font=('arial',9,'bold'),width=15,state="readonly")
        self.txtamounttotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)



        ##########buttons frame
        btn_frame=Frame(button_frame,bd=2,bg="white")
        btn_frame.place(x=320,y=0)

        self.btnaddtocart=Button(btn_frame,command=self.AddItem,height=2,text="Add to cart",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=15)
        self.btnaddtocart.grid(row=0,column=0)

        self.btngenerate=Button(btn_frame,height=2,command=self.gen_bill,text="Generate Bill",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=15)
        self.btngenerate.grid(row=0,column=1)

        self.btnsave=Button(btn_frame,height=2,command=self.save_bill,text="Save Bill",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=15)
        self.btnsave.grid(row=0,column=2)

        self.btnprint=Button(btn_frame,height=2,command=self.iprint,text="Print",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=15)
        self.btnprint.grid(row=0,column=3)

        self.btnclear=Button(btn_frame,height=2,command=self.clear,text="Clear",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=15)
        self.btnclear.grid(row=0,column=4)

        self.btnexit=Button(btn_frame,command=self.root.destroy,height=2,text="Exit",font=('arial',13,"bold"),bg="orangered",fg="white",relief=GROOVE,cursor="hand2",width=13)
        self.btnexit.grid(row=0,column=5)

        self.welcome()
        self.l=[]



        #function decalaration
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select Products")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n********************************")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n********************************")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill??")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            F1=open("bills/"+str(self.bill_no.get())+".txt","w")
            F1.write(self.bill_data)
            F1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} Successfull")
        else:
            return

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                F1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in F1:
                    self.textarea.insert(END,d)
                F1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")



    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        X=random.randint(1000,9999)
        self.bill_no.set(str(X))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        

    




 

            
            




 
         

            






        


        

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome Our Shop ")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Customer Id:{self.cust_id.get()}")
        
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Email:{self.c_email.get()}")

        
        self.textarea.insert(END,"\n")
        self.textarea.insert(END,f"\n Products\t\tQTY\tPrice")
        self.textarea.insert(END,"\n")











    ### select category  combo

    def Categories(self,event=""):
        if self.combo_category.get()=="Cloths":
            self.comboSubcategory.config(value=self.subcatclothes) 
            self.comboSubcategory.current(0)


        if self.combo_category.get()=="Cosmatics":
            self.comboSubcategory.config(value=self.subcatcosmatics) 
            self.comboSubcategory.current(0)


        if self.combo_category.get()=="Mobiles":
            self.comboSubcategory.config(value=self.subcatmobiles) 
            self.comboSubcategory.current(0)


    def product_add(self, event=""):

        #cloths
        if self.comboSubcategory.get()=="Pant":
            self.comboproduct.config(value=self.pant)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="T-Shirt":
            self.comboproduct.config(value=self.t_shirt)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Shirt":
            self.comboproduct.config(value=self.shirt)
            self.comboproduct.current(0)


            #cosmatics
        if self.comboSubcategory.get()=="Bath Soap":
            self.comboproduct.config(value=self.bath_soap)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Face Cream":
            self.comboproduct.config(value=self.face_cream)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Hair Oil":
            self.comboproduct.config(value=self.hair_oil)
            self.comboproduct.current(0)


            #mobiles
        if self.comboSubcategory.get()=="Iphone":
            self.comboproduct.config(value=self.Iphone)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Samsung":
            self.comboproduct.config(value=self.Samsung)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Xiome":
            self.comboproduct.config(value=self.Xiome)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="Real Me":
            self.comboproduct.config(value=self.RealMe)
            self.comboproduct.current(0)

        if self.comboSubcategory.get()=="One+":
            self.comboproduct.config(value=self.OnePlus)
            self.comboproduct.current(0)

    #####prices
    def pricce(self,event=""):
        #pant
        if self.comboproduct.get()=="Levis":
            self.comboprice.config(value=self.price_levis)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Mufti":
            self.comboprice.config(value=self.price_mufti)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Spykar":
            self.comboprice.config(value=self.price_spykar)
            self.comboprice.current(0)
            self.qty.set(1)



         #tshirt
        if self.comboproduct.get()=="Polo":
            self.comboprice.config(value=self.price_polo)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Roadstar":
            self.comboprice.config(value=self.price_roadstar)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Jack&Jones":
            self.comboprice.config(value=self.price_jackjones)
            self.comboprice.current(0)
            self.qty.set(1)


         #shirt
        if self.comboproduct.get()=="Peter England":
            self.comboprice.config(value=self.price_peter)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Lovis Phillipe":
            self.comboprice.config(value=self.price_lovis)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Park Avenue":
            self.comboprice.config(value=self.price_park)
            self.comboprice.current(0)
            self.qty.set(1)



          #bathsoap
        if self.comboproduct.get()=="Lux":
            self.comboprice.config(value=self.price_lux)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Santoor":
            self.comboprice.config(value=self.price_santoor)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Pears":
            self.comboprice.config(value=self.price_pears)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Dove":
            self.comboprice.config(value=self.price_dove)
            self.comboprice.current(0)
            self.qty.set(1)



          #face cream
        if self.comboproduct.get()=="Fair&Lovely":
            self.comboprice.config(value=self.price_fair)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Ponds":
            self.comboprice.config(value=self.price_ponds)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Olay":
            self.comboprice.config(value=self.price_olay)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Garnier":
            self.comboprice.config(value=self.price_garnier)
            self.comboprice.current(0)
            self.qty.set(1)



          #hair oil
        if self.comboproduct.get()=="Parachute":
            self.comboprice.config(value=self.price_parachute)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Jashmin":
            self.comboprice.config(value=self.price_jashmin)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Bajaj":
            self.comboprice.config(value=self.price_bajaj)
            self.comboprice.current(0)
            self.qty.set(1)


        
          #iphone
        if self.comboproduct.get()=="Iphone_X":
            self.comboprice.config(value=self.price_ix)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Iphone_11":
            self.comboprice.config(value=self.price_i11)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Iphone_12":
            self.comboprice.config(value=self.price_i12)
            self.comboprice.current(0)
            self.qty.set(1)



         #samsung
        if self.comboproduct.get()=="Samsung M16":
            self.comboprice.config(value=self.price_sm16)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Samsung M12":
            self.comboprice.config(value=self.price_sm12)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="Samsung M121":
            self.comboprice.config(value=self.price_sm21)
            self.comboprice.current(0)
            self.qty.set(1)


        
         #xiomi
        if self.comboproduct.get()=="Red11":
            self.comboprice.config(value=self.price_r11)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="Redme-12":
            self.comboprice.config(value=self.price_r12)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="RedmePro":
            self.comboprice.config(value=self.price_rpro)
            self.comboprice.current(0)
            self.qty.set(1)


        
         #red me
        if self.comboproduct.get()=="RealMe 12":
            self.comboprice.config(value=self.price_rel12)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="RealMe 13":
            self.comboprice.config(value=self.price_rel13)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="RealMe Pro":
            self.comboprice.config(value=self.price_relpro)
            self.comboprice.current(0)
            self.qty.set(1)


        
        #one+
        if self.comboproduct.get()=="OnePlus1":
            self.comboprice.config(value=self.price_one1)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.comboproduct.get()=="OnePlus2":
            self.comboprice.config(value=self.price_one2)
            self.comboprice.current(0)
            self.qty.set(1)


        if self.comboproduct.get()=="OnePlus3":
            self.comboprice.config(value=self.price_one3)
            self.comboprice.current(0)
            self.qty.set(1)


































if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()

#========================================================================================================================================================================================#
#========================================================================================================================================================================================#



