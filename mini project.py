import random as rd
import time as t
import pywhatkit as pk
import pyautogui as pg
import datetime as dt
import pandas as pd
import pygame as p
import qrcode
from PIL import Image,ImageDraw,ImageFont
from pyautogui import getPointOnLine
import os
FILE_NAME = "Insurance_Details.txt"
# Create file if not exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

#----------------Welcome Logo--------------------------------#
p.init()
p.mixer.init()
# set up display Name
p.display.set_caption("PY INSURANCE KOMPANY")
# set up display
ps1 = p.display.set_mode((554, 554))
# load background Image
ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\company logo.jpeg")
ps = p.transform.scale(ps, (554, 554))
ps1.blit(ps, (0, 0))
# update display
p.display.update()
# load background music
p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\welcome song.mpeg")
p.mixer.music.play(-1)
# wait for image and music
t.sleep(10)
p.mixer.music.stop()
p.quit()

#-------------------------START PROGRAM-------------------------#
def intro_page():
    global City,mobile,Age
    t.sleep(3)
    print()
    print("*********** Select Members You Want To Insurance *****************")
    l = ["1.Self", "2.family", "3.Father", "4.Mother", "5.Brother", "6.sister", "7.Others"]
    for i in l:
        print(i)
    select_insurance = input("Enter your choice: ")
    if select_insurance=="2":
        name_1=input("Enter the Family Name: ")
        n=input("Enter the Family No: ")
    else:
        Name=input("Enter your Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        current_year = dt.datetime.now().year
        Age = current_year - birth_year
        print("Age: ", Age)
    City = input("Enter your City: ")
    pincode="Enter the Pincode: "
    #Mobile Number Validation
    mobile = int(input("Enter your mobile number: "))
    if mobile_1.isdigit() and len(mobile_1) == 10 and mobile_1.startswith(("6", "7", "8", "9")):
        print("Your Details Upload...")
    else:
        print("check the number")
        intro_page()

#---------------------------------login page----------------------------#
def login():
    #wait for Loing Page
    t.sleep(3)
    print()
    print("************************ LOGIN PAGE ***********************")
    print()
    user = input("Enter the Username* :").lower()
    if user == name_1:
        password2 = input("Enter the Password* :")
        if password_1 == password2:
            #Generate OTP
            OTP = rd.randrange(1234,5678)
            print("OTP:",OTP)
            print("Sending OTP to WhatsApp....")
            pk.sendwhatmsg_instantly(f"+91 {mobile_1}",
                                     f":Your OTP for Medical Insurance Login is: {OTP}",
                                     wait_time=15,
                                     tab_close=True,
                                     close_time=3)
            #wait for WhatsApp web to load
            t.sleep(5)
            #press Enter Automatically
            pg.press("enter")
            # #OTP Verification
            OTP1 = int(input("Enter the OTP* :"))
            if OTP1 == OTP:
                print("Login Successful")
                print()
                t.sleep(1)
                print("Welcome",name_1)
                t.sleep(2)
                intro_page()
            else:
                print("Check the OTP")
                login()
        else:
            print("wrong password..")
            login()
    else:
        print("check the username...")

        login()

#-------------------------------welcome page---------------------------------------#
def welcome():
    global name_1,password_1,mobile_1,Age,gender,Email_1
    print()
    print("************ RiskAssure: Digital Insurance Suite *************")
    print("********************* Sing Up **************************")
    name_1= input("Enter the Name: ").lower()
    birth_year = int(input("Enter the Birth year: "))
    current_year = dt.datetime.now().year
    Age = current_year - birth_year
    print("Age: ", Age)
    gender = input("Enter the Gender(Male/Female): ")
    Email_1= input("Enter the Email: ").lower()
    #Email Id Validation
    if "@" in Email_1 and ".com" in Email_1:
        password_1 = input("Enter the Password: ")
        mobile_1 = input("Enter the Mobile Number: ")
        # Mobile Number Validation
        if mobile_1.isdigit() and len(mobile_1) == 10 and mobile_1.startswith(("6", "7", "8", "9")):
            print("Signup Successful...")
            login()
        else:
            print("check the number")
            welcome()
    else:
        print("Wrong Email...")
        welcome()
welcome()

#-----------------------Government Insurance documents delivery page------------------------------------------#
def address2():
    print("**********documents Delivery page**********")
    print(f"name :{name2}")
    print(f"Mobile No :  {mobile8}")
    Address=input("change your address(yes or no): ").lower()
    if Address == "yes":
        a=input("Enter the Address: ")
        t.sleep(2)
        print("30 days later Your Insurance card and documents delivery in your address ")
    elif Address == "no":
        print(f"Address: {Address1}")
        t.sleep(2)
        print("30 days later Your Insurance card and documents delivery in your address ")

#----------Private insurance document delivery page-------------------#
def address1():
    print("**********documents Delivery page**********")
    print(f"Name: {name1}")
    print(f"Mobile No : {mobile4}")
    Address=input("change your address(yes or no): ").lower()
    if Address == "yes":
        a=input("Enter the Address: ")
        t.sleep(2)
        print("30 days Your Insurance card and documents delivery in your address ")
    elif Address == "no":
        print(f"Address: {Address2}")
        t.sleep(2)
        print("30 days Your Insurance card and documents delivery in your address ")

#--------------- government insurance profile save --------------------#
def profile_save2():
    insurance_no=f"{st2}{a_1}"
    name=f"{name2}"
    family=f"{family_no}"
    schemes=f"{schemes1}"
    insurance_amount=f"{ policy_amount}"
    Ration=f"{Ration_card}"
    with open(FILE_NAME, "a") as file:
        file.write(f"{insurance_no},{name},{family},{schemes},{insurance_amount},{Ration}\n")
    t.sleep(3)
    print("Insurance Registered Successfully.....✔\n")
    address2()

#----------------- private insurance profile save ---------------------#
def profile_save1():
    insurance_no=f"{st1}{a}"
    name=f"{name1}"
    family_no=f"{family_no1}"
    policy=f"{policy6}"
    insurance_company_name=f"{company_name}"
    insurance_amount=f"{ policy_amount}"
    with open(FILE_NAME, "a") as file:
        file.write(f"{insurance_no},{name},{family_no},{policy},{insurance_company_name},{insurance_amount}\n")
    t.sleep(3)
    print("Insurance Registered Successfully.....✔\n")
    address1()

#-------------Government Insurance apply login page-------------------#
def login2():
    global Address1,a_1,policy_amount,family_no,Ration_card
    t.sleep(1)
    OTP = rd.randrange(1234, 5678)
    print("OTP:",OTP)
    pk.sendwhatmsg_instantly(f"+91 {mobile8}", f"{OTP}")
    pg.doubleClick()
    OTP1 = int(input("Enter the OTP* :"))
    if OTP1 == OTP:
        t.sleep(3)
        print("Login Successful")
        t.sleep(2)
        Blood = input("Enter the blood group: ")
        Aadhar_number = input("Enter The Aadhar Number: ")
        Ration_card = input("your Ration card No: ")
        family_no = input("Enter The Family Numbers: ")
        Pancard = input("Enter The Pancard :")
        Address1 = input("Enter The Address : ")
        income_no = input("Enter the income certificate number: ")
        t.sleep(2)
        print()
        l = [f"Name: {name2}", f"Gender : {genders2}", f"Mobile Number: {mobile8}",
             f"Email ID: {Email_1}", f"Address: {Address1}", f"Ration card: {Ration_card}",f"Blood: {Blood}", f"Aadhaar Number: {Aadhar_number}",
             f"Family No: {family_no}", f"Income Certificate Number: {income_no}",f"Pancard: {Pancard}"]
        for i in l:
            print(i)
        t.sleep(4)
        print()
        policy_amount = rd.randint(500000, 1000000)
        print("policy amount ₹", policy_amount)
        t.sleep(1)
        a_1= rd.randint(987654321, 1234567890)
        print("Insurance number", a_1)
        print("sending Insurance copy to WhatsApp")
        t.sleep(5)
        card = """
        ******************************
        schemes     : {}
        Name        : {}
        Address     : {}
        Blood       : {}
        Family NO   : {}
        Insurance   : {}{}
        ******************************
        """
        sms = card.format(schemes1,name2,Address1 , Blood, family_no,st2,a_1)
        pk.sendwhatmsg_instantly(f"+91{mobile8}", sms)
        t.sleep(5)
        pg.doubleClick()
        profile_save2()
    else:
        print("Check the  OTP")
        login2()


#--------------------Sending whatsapp messages-------------------------#
def messages():
    t.sleep(5)
    card = """
                ********************************
                Name      : {}                 Insurance company : {}  
                Age       : {}                 
                Address   : {}
                Family no : {}
                Blood     : {}
                Policy    : {}
                insurance number  :{}{}
                ********************************

                *****************************************************************************
                Toll Free Customer Helpline No. : {}                        
                Ple
                ase quote your UHID No. for assistance
                    * l This card is invalid if the policy is cancelled.
                    * l Immediate intimation to RCare Health is a must in case of 
                      hospitalization.
                    * l To avail cashless facility at the Network Hospitals, please produce
                      your Health Card & Photo ID proof at the Helpdesk.
                    * l Updated list of Network Hospitals available on.

                ------------------------------------------------------------------------------
                {}
                Address : {}
                24 Hours Toll Free Fax No : {}
                Email : {}
                Pls refer claims FAQ& updatedhospital list in our wedsite
                *****************************************************************************
                """
    sms = card.format(name1, company_name, Age1, Address2, family_no1, Blood, policy6, st1, a, Call, company_name, Add1,Call, Email)
    pk.sendwhatmsg_instantly(f"+91{mobile1}", sms)
    t.sleep(5)
    pg.doubleClick()
    print("Thank you....!")
    profile_save1()
# ----------private insurance company apply login page----------------#
def login1():
    global Address2,Blood,family_no1,a,policy_amount
    print("Sending OTP to WhatsApp")
    t.sleep(1)
    OTP = rd.randrange(1234, 5678)
    print("OTP",OTP)
    pk.sendwhatmsg_instantly(f"+91 {mobile1}", f"{company_name} apply OTP: {OTP}")
    pg.doubleClick()
    OTP1 = int(input("Enter the OTP* :"))
    if OTP1 == OTP:
        t.sleep(3)
        print("Login Successful")
        t.sleep(2)
        Blood = input("Enter the blood group: ")
        Aadhar_number = input("Enter The Aadhar Number: ")
        Pancard = input("Enter The Pancard :").upper()
        Address2 = input("Enter The Aaddress : ")
        family_no1 = input("Enter The Family Numbers: ")
        income_no = input("Enter the income certificate number: ")
        t.sleep(2)
        print()
        l=[f"Name: {name1}",f"Age: {Age1}",f"Gender : {genders1}",f"Mobile Number: {mobile1}",f"Email ID: {Email_1}",f"Address: {Address2}",f"Blood: {Blood}",f"Aadhaar Number: {Aadhar_number}",
           f"Family No: {family_no1}",f"Income Certificate Number: {income_no}",f"Pancard: {Pancard}"]
        for i in l:
            print(i)
        t.sleep(4)
        print()
        policy_amount = rd.randint(500000, 1000000)
        print("policy amount ₹", policy_amount)
        amount = rd.randrange(350, 750, 25)
        print("premium", amount)
        month = input("Your premium payment Method (month or year): ").upper()
        if month=="MONTH":
            print("Monthly Payment ₹",amount)
        elif month=="YEAR":
            amount=amount*12
            print("yearly Payment ₹",amount)
        else:
            print("Payment Method Not define")
            login1()
        pay = input("Enter the UPI/Debit card: ").upper()
        if pay=="UPI":
            upi_id = "yourname@bank"
            name = Name
            amount = amount
            currency = "INR"
            pay_id = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(pay_id)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
            canvas = Image.new("RGB", (img.size[0], img.size[1] + 80), "white")
            canvas.paste(img, (0, 80))
            draw = ImageDraw.Draw(canvas)
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            draw.text((canvas.size[0] // 2 - 80, 20), "PY-Pay", fill="green", font=font)
            canvas.save("py_pay_qr.png")
            p.init()
            p.display.set_caption("PY-Pay - SCAN TO PAY")
            ps1 = p.display.set_mode(canvas.size)
            ps1.blit(p.image.load("py_pay_qr.png"), (0, 0))
            p.display.update()
            t.sleep(10)
            p.quit()
            t.sleep(10)
            print("Payment Successful...✔")
        elif pay=="DEBIT CARD":
            print("DEBIT CARD NO: ")
            print("Payment Successful...✔")
        else:
            print("Payment Method Not Define")
            login1()
        t.sleep(3)
        l=["1.Salaried","2.Doctor","3.Businessman/Businesswoman","4.Homemaker"]
        for i in l:
            print(i)
        oc=input("Enter the Occupation: ")
        a = rd.randint(987654321, 1234567890)
        print("Insurance number",st1,a)
        x=company_name
        #-------------------------Insurance card------------------------#
        if x=="Start Health And Allied Insurance":
            #-----------Start Health And Allied Insurance Card------------#
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("Start Health And Allied Insurance Card")
            # set up display
            ps1 = p.display.set_mode((850, 500))
            # load background Image
            ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\start insurance card.jpeg")
            ps = p.transform.scale(ps, (850, 500))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\insurance card.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            t.sleep(3)
            p.mixer.music.stop()
            p.quit()
            messages()
        elif x=="NIVA BUPA HEALTH INSURANCE":
            #----------------niva bupa health insurance card------------------#
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("NIVA BUPA HEALTH INSURANCE ")
            # set up display
            ps1 = p.display.set_mode((850, 500))
            # load background Image
            ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\navi buba insurance card.jpeg")
            ps = p.transform.scale(ps, (850, 500))
            ps1.blit(ps, (0, 0))
            # Update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\insurance card.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            time.sleep(3)
            p.mixer.music.stop()
            p.quit()
            messages()
        elif x=="care Health Insurance":
            #---------------------health care insurance card----------------#
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("HEALTH CARE ")
            # set up display
            ps1 = p.display.set_mode((850, 500))
            # load background Image
            ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\health care logo.jpeg")
            ps = p.transform.scale(ps, (850, 500))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\insurance card.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            time.sleep(3)
            p.mixer.music.stop()
            p.quit()
            messages()
        elif x=="ICICICI Lombard Health Insurance":
            #-------------icicici health insurance card------------------#
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("P.L.I (PY LIFE INSURANCE)")
            # set up display
            ps1 = p.display.set_mode((850, 500))
            # load background Image
            ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\icici insurance card.jpeg")
            ps = p.transform.scale(ps, (850, 500))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\insurance card.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            time.sleep(3)
            p.mixer.music.stop()
            p.quit()
            messages()
        elif x=="TATA AIG":
            #----------------tata aig insurance card-------------------#
            p.init()
            p.mixer.init()
            #set up display Name
            p.display.set_caption("TATA AIG INSURANCE ")
            #set up display
            ps1 = p.display.set_mode((850, 500))
            #load background Image
            ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tata aig insurance card.jpeg")
            ps = p.transform.scale(ps, (850, 500))
            ps1.blit(ps, (0, 0))
            #update display
            p.display.update()
            #load background music
            p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\insurance card.mpeg")
            p.mixer.music.play(-1)
            #wait for image and music
            time.sleep(3)
            p.mixer.music.stop()
            p.quit()
            messages()
    else:
        print("Check the  OTP")
        login1()

#--------------private insurance company  Apply Form-------------------#
def apply1():
    t.sleep(3)
    global Name,mobile1,Age
    print()
    print("********************* Apply Form ***************************")
    Name=name1
    print(f"Name: {name1}")
    Age=Age1
    print(f"Age : {Age1}")
    print( f"gender : {genders1}")
    print(f"Email ID: {Email_1}")
    City = input("Enter the city: ")
    pincode=input("Enter the pincode: ")
    mobile1 = f"{mobile4}"
    print("mobile no: ", mobile1)
    annual_income = input("Enter the Annual Income: ")
    if annual_income < "100000000":
        t.sleep(3)
        print("You Are Eligible ")
        login1()
    elif annual_income > "100000":
        print("You Are Not Eligible")
        insurance_company()

#-------------------Government Insurance Apply Form---------------------#
def apply2():
    global  mobile8
    t.sleep(3)
    print()
    print("********************** Apply Form *************************")
    print(f"Name: {name2}")
    print(f"Gender: {genders2}")
    print(f"Email: {Email_1}")
    mobile8 = input("Enter the mobile Number:")
    print("Mobile no: ",mobile8)
    City = input("Enter the city: ")
    pincode = int(input("Enter the pin code: "))
    print("Sending OTP to WhatsApp....")
    login2()

#Start Health And Allied Insurance
def Insurance_Type1():
    print("********************* Insurance Type ************************")
    g=["1.Super Star Value","2.Supar Star","3.Super Star Essential","4.Super Star Preferred","5.Super Star Secure","6.Back"]
    for i in g:
        print(i)
    choose5=input("Enter the Choice: ")
    #------------------------Super Star Value-------------------------#
    if choose5=="1":
        t.sleep(2)
        l = [">Room rent limit(single private AC Room)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (5 lakh Unlimited times in a year, for both related and unrelated)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 2.5 lakh per year and up to maximum of Rs 5 lakh for each claim free year)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (85% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Up to Rs 1 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to actual expenses)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (14256 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type1()
    #---------------------------Supar Star----------------------------#
    elif choose5=="2":
        t.sleep(2)
        l = [">Room rent limit(Any Category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (5lakh Unlimited times in a year, for both related and unrelated)",
             "f you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 2.5 lakh per year and up to maximum of Rs 5 lakh for each claim free year)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Up to Rs 5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to actual expenses)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (14256 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type1()
    #-----------------------------Super Star Essential-----------------#
    elif choose5=="3":
        t.sleep(2)
        l = [">Room rent limit(single private AC Room)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (5 lakh Unlimited times in a year, for both related and unrelated)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 2.5 lakh per year and up to maximum of Rs 5 lakh for each claim free year)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (85% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Up to Rs 1 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to actual expenses)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (14256 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type1()
    #------------------------Super Star Preferred--------------------#
    elif choose5=="4":
        t.sleep(2)
        l = [">Room rent limit( Any Category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (7.5 lakh Unlimited times in a year, for both related and unrelated)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 3.75 lakh per year and up to maximum of Rs 5 lakh for each claim free year)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Up to Rs 7.5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to actual expenses)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (14256 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        print()
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type1()
    #--------------------------Super Star Secure------------------------#
    elif choose5=="5":
        t.sleep(2)
        l = [">Room rent limit( Any Category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (7.5 lakh Unlimited times in a year, for both related and unrelated)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 3.75 lakh per year and up to maximum of Rs 5 lakh for each claim free year)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Up to Rs 7.5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to actual expenses)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (14256 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
             Insurance_Type1()
    elif choose5=="6":
        l=["1.insurance company","2.Insurance Type"]
        for i in l:
            print(i)
        c=input("Enter the Back: ")
        if c=="1":
            insurance_company()
        elif c=="2":
            Insurance_Type1()
        else:
            print("Check the policy")
            Insurance_Type1()
def Start_Health_And_Allied_Insurance():
    global company_name,Email,Call,Add1,name1,Age1,mobile4,genders1,st1
    # start insuranc logoSTART HEALTH AND ALLIED INSURANCE logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("START HEALTH AND ALLIED INSURANCE ")
    # set up the display
    ps1 = p.display.set_mode((554, 554))
    #load and scale Background Images
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\Start insurance logo.jpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    #login
    t.sleep(1)
    print()
    print("***************Start Health And Allied Insurance**************")
    company_name="Start Health And Allied Insurance"
    Email="support@starhealth.in"
    Call="1800 425 2255"
    Add1="No. 1, New Tank Street,Valluvar Kottam High Road,Nungambakkam,Chennai – 600034India"
    st1="SHAAI"
    l = [
        "Star Health Insurance is a preferred option for individuals and families It is one of the first standalone health insurance companies india. It has earned its reputation through customer-first policies and fast claims processing.",
        ">>>Claim Settlement Ratio (CSR): 99.81% (FY 2024-25).",
        ">>>Highlights: The company offers a wide network of over 14,000 hospitals, disease-specific health insurance policies, and special health insurance plans for seniors.",

        ">>>Popular For: reliable claim settlement and a wide range of health insurance products catering to individuals of all ages."]
    for i in l:
        print(i)
        print()
    print(">>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    t.sleep(2)
    name1 = name_1
    Age1 = Age
    genders1 = gender
    mobile4 = mobile
    l = [f"Name: {name1}", f"Age: {Age1}", f"Gender: {genders1}", f"Mobile No:{mobile4}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name1 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age1 = cy - birth_year
        print(f"Age: {Age1}")
        genders1 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile4 = input("Enter the Mobile Number: ")
        if mobile4.isdigit() and len(mobile4) == 10 and mobile4.startswith(("6", "7", "8", "9")):
            print()
            Insurance_Type1()
        else:
            print("check the number")
            Start_Health_And_Allied_Insurance()
    elif c == "no":
        print()
        Insurance_Type1()
    else:
        Start_Health_And_Allied_Insurance()

#-------------------NIVA BUPA HEALTH INSURANCE-----------------------#
def Insurance_Type2():
    print("****************** Insurance Type **************************")
    l=["1.ReAssure 3.0 Elite","2.Aspire Gold+value (Direct)","3.Max saver 2.0","4.ReAssure 2.0 Bronze+","5.Aspire God+como","6.Back"]
    for i in l:
        print(i)
    choose6=input("Enter the Choice: ")
    #------------------------ReAssure 3.0 Elite------------------------#
    if choose6=="1":
        t.sleep(2)
        l = [">Room rent limit( Single AC Room)",
                          "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
                          "",
                          "* Restoration of cover (5 lakh Unlimited times in a year, for both related and unrelated, This will be carried forward at every renewal maximum up to 100%)",
                          "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
                          "",
                          "* Renewal Bonus(Rs 5 lac per year and up to maximum of Rs 50 lac for . remaining unutilized illness. This will be carried forward maximum upto 50lac under booster+benefit)",
                          "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
                          "",
                          "* Co-pay (Full claim paid by insurer)",
                          "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
                          "",
                          "* Pre-hospitalization coverage ( 60 days)",
                          "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
                          "",
                          "* Post-hospitalization coverage(180 days)",
                          "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
                          "",
                          "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
                          "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
                          "",
                          "*Hospitalization at home (covered upto sumlnsured) ",
                          "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
                          "",
                          "* Ambulance charges (Up to actual )",
                          "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
                          "",
                          "* Cashless hospitals (11053 cashless hospitals in India)",
                          "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
           Insurance_Type2()
    #---------------------------Aspire Gold+value (Direct)---------------------#
    elif choose6=="2":
        t.sleep(2)
        l = [">Room rent limit( Single AC Room)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of Sum Insured once in a policy year for related and unrelated illnesses.)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 5 lac per year and up to maximum of Rs 50 lac for . remaining unutilized illness. This will be carried forward maximum upto 50lac under booster+benefit)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (80% claim paid by Insurer outside tiered network. 100% claim paid for maternity)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs 5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh )",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (8997 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type2()
    #-----------------------Max saver 2.0---------------------#
    elif choose6=="3":
        t.sleep(2)
        l = [">Room rent limit(Any category up to Rs 10 lakh; Single Private Room (up to SI) for next 90 lacs)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs 1 cr) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11053 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type2()
    #-------------------------ReAssure 2.0 Bronze+-----------------#
    elif choose6=="4":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11053 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type2()
    #---------------------------Aspire God+como------------------------#
    elif choose6=="5":
        t.sleep(2)
        l = [">Room rent limit(Any category up to Rs 10 lakh; Single Private Room (up to SI) for next 90 lacs)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs l cr) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11053 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type2()
    elif choose6=="6":
        insurance_company()
    else:
        print("Check the policy")
        Insurance_Type2()

def Niva_Bupa_Health_Insurance():
    global company_name, Email, Call, Add1,name1,Age1,mobile4,genders1,st1
    #-------------niva bupa health insurance logo----------------#
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("NIVA BUPA HEALTH INSURANCE")
    # set up the display
    ps1 = p.display.set_mode((735, 517))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\niva bupa insurance logo.jpeg")
    ps = p.transform.scale(ps, (735, 517))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    #-------------------------------login----------------------------#
    t.sleep(1)
    print()
    print("*************** NIVA BUPA HEALTH INSURANCE ******************")
    print()
    company_name = "NIVA BUPA HEALTH INSURANCE"
    Email = "customercare@nivabupa.com"
    Call = "1860-500-8888"
    Add1= "C-98, 1st Floor,Lajpat Nagar, Part 1,South Delhi,New Delhi – 110024, India"
    st1="NBHI"
    l = [
        ">>>Niva Bupa (previously known as Max Bupa) is preferred by customers due to its 'no room rent capping' feature. This offers greater freedom to the policyholders during hospitalization.",
        ">>>CSR: 100% (FY 2024-25).", ">>>Highlights: over 9,000 network hospitals, worldwide coverage, and OPD cove.",
        ">>>Popular For: simple and straightforward policy terms and clear policy benefits that are easy to understand."]
    for i in l:
        print(i)
        print()
    print(">>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    t.sleep(2)
    name1 = name_1
    Age1 = Age
    genders1 = gender
    mobile4 = mobile
    l = [f"Name: {name1}", f"Age: {Age1}", f"Gender: {genders1}", f"Mobile No:{mobile4}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name1 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age1 = cy - birth_year
        print(f"Age: {Age1}")
        genders1 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile4 = input("Enter the Mobile Number: ")
        if mobile4.isdigit() and len(mobile4) == 10 and mobile4.startswith(("6", "7", "8", "9")):
            print()
            Insurance_Type2()
        else:
            print("check the number")
            Niva_Bupa_Health_Insurance()
    elif c == "no":
        print()
        Insurance_Type2()
    else:
        Niva_Bupa_Health_Insurance()

#----------------------care Health Insurance--------------------------#
def Insurance_Type3():
    print("*********************** Insurance Type **********************")
    l = ["1.Ultimate care (Direct)", "2.Care supreme Direct", "3.Care supreme Combo", "4.Care Plus ",
         "5.Care supreme","6.Back"]
    for i in l:
        print(i)
    choose7= input("Enter the Choice: ")
    #------------------------Ultimate care (Direct)-------------------#
    if choose7=="1":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",

             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11909 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type3()
    #--------------------------Care supreme Direct---------------------#
    elif choose7=="2":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10,000)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11909 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type3()
    #----------------------------Care supreme Combo--------------------#
    elif choose7=="3":
        t.sleep(2)
        l = [">Room rent limit(Any category up to Rs 10 lakh; Single Private Room (up to SI) for next 90 lacs)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Available as an optional cover)",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet( All day care treatments, no need to meet the 24 hour minimum requirement)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs   1 cr) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11909 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type3()
    #-----------------------------Care Plus---------------------------#
    elif choose7=="4":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 20,000)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11909 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type3()
    #-------------------------Care supreme--------------------#
    elif choose7=="5":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Rs 10 lakh unlimited times in a year; both related and unrelated illness. This will be carried forward at every renewal maximum up to 100%)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus(Rs 10 lakh will be added per year maximum up to Rs 30 lakh if you don’t claim. Even if you make a claim, balance sum insured for base plan (ReAssure Bronze) will be carried forward )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 30 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(60 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10,000)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11909 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type3()
    elif choose7=="6":
        t.sleep(2)
        insurance_company()
    else:
        print("Check the policy")
        Insurance_Type3()

def Care_Health_Insurance():
    global company_name, Email, Call, Add1,name1,Age1,mobile4,genders1,st1
    #--------Health care insurance logo-----------#
    p.init()
    p.mixer.init()
    # set up the display Name
    p.display.set_caption("HEALTH CARE INSURANCE ")
    # set up the display
    ps1 = p.display.set_mode((800, 600))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\health care logo.jpeg")
    ps = p.transform.scale(ps, (800, 600))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    #login
    t.sleep(1)
    print()
    print("****************** Care Health Insurance ********************")
    print()
    company_name="care Health Insurance"
    Email="customerfirst@careinsurance.com"
    Call="1800-102-6655"
    Add1="5th Floor, Chawla House,19, Nehru Place,New Delhi – 110019, India"
    st1="CHI"
    l = [
        ">>>Care Health (previously known as Religare Health) has seen a steady rise of late due to offering affordable premium rates while providing comprehensive coverage.",
        ">>>CSR: 99.95% (FY 2024-25).", ">>>Highlights: large network of 21,000+ hospitals (and counting!), wellness benefits and maternity cover in certain insurance policies.",
        ">>>Popular For: Competitive pricing, broad span of network hospitals.."]
    for i in l:
        print(i)
        print()
    print(">>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    t.sleep(2)
    name1 = name_1
    Age1 = Age
    genders1 = gender
    mobile4 = mobile
    l = [f"Name: {name1}", f"Age: {Age1}", f"Gender: {genders1}", f"Mobile No:{mobile4}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name1 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age1 = cy - birth_year
        print(f"Age: {Age1}")
        genders1 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile4 = input("Enter the Mobile Number: ")
        if mobile4.isdigit() and len(mobile4) == 10 and mobile4.startswith(("6", "7", "8", "9")):
            print()
            Insurance_Type3()
        else:
            print("check the number")
            Care_Health_Insurance()
    elif c == "no":
        print()
        Insurance_Type3()
    else:
        Care_Health_Insurance()

#----------------------ICICI Lombard Health Insurance-----------------#
def Insurance_Type4():
    print()
    print("******************** Insurance Type ***********************")
    l = ["1.Elevate", "2.Elevate OPD", "3.Elevate Value", "4.Elevate Combo",
         "5.Health AdvantEdge","6.Back"]
    for i in l:
        print(i)
    choose8= input("Enter the Choice: ")
#--------------------------------Elevate-------------------------------#
    if choose8=="1":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11445 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type4()
    #-----------------------------Elevate OPD----------------------------#
    elif choose8=="2":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  10 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11445 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type4()
    #------------------------------Elevate Value---------------------#
    elif choose8=="3":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  10 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 10 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (8652 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type4()
    #-----------------------------Elevate Combo-------------------------#
    elif choose8=="4":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  1 cr) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 1 cr)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11445 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type4()
    #---------------------------Health AdvantEdge------------------------#
    elif choose8=="5":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (7.5 lakh restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1.5 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 60 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  7.5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 7,500 maximum up to 10,000)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (11445 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type4()
    elif choose8=="6":
        insurance_company()
    else:
        print("Check the policy")
        Insurance_Type()
def ICICI_Lombard_Health_Insurance():
    global company_name, Email, Call, Add1,name1,Age1,mobile4,genders1,st1
    #----------ICICICI PRUDENTIAL LIFE INSURANCE logo----------#
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("ICICICI PRUDENTIAL LIFE INSURANCE")
    # set up the display
    ps1 = p.display.set_mode((800, 600))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\icici insurance logo.jpeg")
    ps = p.transform.scale(ps, (800, 600))
    ps1.blit(ps, (0, 0))
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # update display
    p.display.update()
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    #login
    t.sleep(1)
    print()
    print("*************** ICICICI Lombard Health Insurance ***************")
    print()
    company_name="ICICICI Lombard Health Insurance"
    Email="customersupport@icicilombard.com"
    Call=" 1800 2666"
    Add1="ICICI Lombard Health Care,ICICI Bank Tower, Plot No. 12,Financial District, Nanakram Guda, Gachibowli,Hyderabad – 500032, India"
    st1="ICICI"
    l = [
        ">>>India's most trusted health insurance companies india, especially for families and corporate groups."
        ">>>CSR: 97.16%. (FY 2024-25).",
        ">>>Highlights: no pre-medical check-ups for young buyers, a number of add-ons available, and emergency ambulance services",
        ">>>Popular For: Strong financial strength, backed by the ICICI group and wide hospital network."]
    for i in l:
        print(i)
        print()
    print(">>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    t.sleep(2)
    name1 = name_1
    Age1 = Age
    genders1 = gender
    mobile4 = mobile
    l = [f"Name: {name1}", f"Age: {Age1}", f"Gender: {genders1}", f"Mobile No:{mobile4}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name1 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age1 = cy - birth_year
        print(f"Age: {Age1}")
        genders1 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile4 = input("Enter the Mobile Number: ")
        if mobile4.isdigit() and len(mobile4) == 10 and mobile4.startswith(("6", "7", "8", "9")):
            print()
            Insurance_Type4()
        else:
            print("check the number")
            ICICI_Lombard_Health_Insurance()
    elif c == "no":
        print()
        Insurance_Type4()
    else:
        ICICI_Lombard_Health_Insurance()

#=----------------------------TATA AIG--------------------------------#
def Insurance_Type5():
    print()
    print("*********************** Insurance Type ************************")
    l = ["1.Medicare select", "2.Medicare Premier ", "3.Medicare Plus","4.Back"]
    for i in l:
        print(i)
    choose9= input("Enter the Choice: ")
    #---------------------------Medicare select----------------------#
    if choose9=="1":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (13741 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type5()
    #------------------------Medicare Premier-------------------------#
    elif choose9=="2":
        t.sleep(2)

        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (Not Available in the plan)","",
             "* Renewal Bonus( Rs 2.5 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 3,000)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (13741 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type5()
    #-----------------------------Medicare Plus------------------------#
    if choose9=="3":
        t.sleep(2)
        l = [">Room rent limit(Any category)",
             "This means the cost of the hospital room you stay in during treatment. Your insurance pays for the room up to a certain amount or type (like a shared room, private room or any room)",
             "",
             "* Restoration of cover (100% restoration of the Annual Sum Insured, unlimited times in a policy year for related and unrelated illnesses)",
             "If you use up your entire insurance amount in one claim, the insurance company can refill the same amount again within the same year for the same or another illness",
             "",
             "* Renewal Bonus( Rs 1 lakh every claim free year up to maximum of Rs 5 lakh. In case of claim, renewal bonus will not be reduced )",
             "If you do not make any claim during the year, the insurance company rewards you by increasing your coverage amount at renewal without any increase in the premium",
             "",
             "* Co-pay (100% paid by the insurer)",
             "This means you and the insurance company share the hospital bill. For example, if the bill is Rs. 1,00,000 and your co-pay is 10%, you pay Rs. 10,000, and the insurance company pays the remaining Rs. 90,000.",
             "",
             "* Pre-hospitalization coverage ( 90 days)",
             "These are medical expenses incurred before you are admitted to the hospital, such as doctor visits, tests, or medications related to the illness",
             "",
             "* Post-hospitalization coverage(180 days)",
             "These are expenses after you are discharged, such as follow-up doctor visits, medicines, or tests needed for recovery",
             "",
             "* Day care treatmentGet covered even for short hospital stays of just 2 hours. Ideal for quick treatments or minor procedures that don’t need an overnight stay. (Not applicable for OPD, diagnostic, or AYUSH treatments.)",
             "some treatments or surgeries do not need a full 24-hour hospital stay. These short procedures, done in a few hours, are called day care treatments.",
             "",
             "*Hospitalization at home (Upto Rs  5 lakh) ",
             "Sometimes treatment can be safely done at home rather than in a hospital because hospital beds are unavailable or the patient cannot move. Insurance may still cover the cost of treatment at home.",
             "",
             "* Ambulance charges (Up to Rs 5 lakh)",
             "If you need an ambulance to reach the hospital during a medical emergency, the insurance can pay for the ambulance charges",
             "",
             "* Cashless hospitals (13741 cashless hospitals in India)",
             "At certain hospitals connected to your insurance company, you do not have to pay the hospital bill upfront. The insurance company directly settles the bill with the hospital"]
        for i in l:
            print(i)
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply1()
        elif apply == "no":
            Insurance_Type5()
    elif choose9=="4":
        insurance_company()
    else:
        print("Check the policy")
        Insurance_Type5()
def TATA_AIG():
    global company_name, Email, Call, Add1,name1,mobile4,Age1,genders1,st1
    # tata aig insurance logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("TATA AIG LIFE INSURANCE CARD")
    # set up the display name
    ps1 = p.display.set_mode((670, 500))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tata aig logo.jpeg")
    ps = p.transform.scale(ps, (670, 500))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    #login
    t.sleep(1)
    print()
    print("************************ TATA AIG *************************")
    print()
    company_name=" TATA AIG"
    Email="customersupport@tataaig.com"
    Call="1800 266 7780"
    Add1="Peninsula Business Park, Tower A, 15th Floor,G.K. Marg, Lower Parel,Mumbai – 400013, India"
    st1="TATA"
    l = [
        ">>>India's most trusted health insurance companies india, especially for families and corporate groups."
        ">>>CSR: 97.16%. (FY 2024-25).",
        ">>>Highlights: no pre-medical check-ups for young buyers, a number of add-ons available, and emergency ambulance services",
        ">>>Popular For: Strong financial strength, backed by the ICICI group and wide hospital network."]
    for i in l:
        print(i)
        print()
    print(">>>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    t.sleep(2)
    name1 = name_1
    Age1 = Age
    genders1 = gender
    mobile4= mobile
    l = [f"Name: {name1}", f"Age: {Age1}", f"Gender: {genders1}", f"Mobile No:{mobile4}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name1 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age1 = cy - birth_year
        print(f"Age: {Age1}")
        genders1 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile4 = input("Enter the Mobile Number: ")
        if mobile4.isdigit() and len(mobile4) == 10 and mobile4.startswith(("6", "7", "8", "9")):
            print()
            Insurance_Type5()
        else:
            print("check the number")
            TATA_AIG()
    elif c == "no":
        print()
        Insurance_Type5()
    else:
        TATA_AIG()
#-----------------------Medical Insurance company-----------------------#
def insurance_company():
    global policy6
    print()
    print("******************* Insurance Policy ********************")
    e=["1.Health Insurance","2.Family Insurance","3.personal Accident cover Insurance"]
    for i in e:
        print(i)
    print()
    policy6=input("Choose your policy: ").title()
    print()
    print("***************Health Insurance company(top-5)y***************")
    f=["1.Start Health & Allied Insurance","2.Niva Bupa Health Insurance","3.Care Health Insurance","4.ICICI Lombard Health Insurance","5.TATA AIG"]
    for i in f:
        print(i)
    print()
    choose4=input("Choose your choice: ")
    if choose4=="1":
        Start_Health_And_Allied_Insurance()
    elif choose4=="2":
        Niva_Bupa_Health_Insurance()
    elif choose4=="3":
        Care_Health_Insurance()
    elif choose4=="4":
        ICICI_Lombard_Health_Insurance()
    elif choose4=="5":
        TATA_AIG()
    elif choose4=="6":
        insurance_apply()

#1. Ayushm
# an Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)
def ABPMJAYPJ():
    global name2,mobile2,Age2,genders2,st2,schemes1
    # Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY) logo
    p.init()
    p.mixer.init()
    # set up the display Name
    p.display.set_caption("Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)")
    # set up the display
    ps1 = p.display.set_mode((670, 500))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india-1.jpeg")
    ps = p.transform.scale(ps, (670, 500))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    print("Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)")
    print(">>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="ABPMJAYPJ"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            ABPMJAYPJ()
    elif c == "no":
        print()
    else:
        ABPMJAYPJ()
    schemes1 = "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)"
    print(schemes1)
    l = [">>>Coverage: Up to 5 lakh per family/year",
         ">>>For: Poor & vulnerable families (10+ crore beneficiaries)",
         ">>>Cashless treatment in government & private hospitals",
         ">>>Best overall government health scheme in India"]
    for i in l:
        print(i)
    print("********************* DETAILS ************************")
    l = [">>>Coverage: Up to ₹5 lakh per family per year for secondary and tertiary hospitalization.",
         ">>>Target Beneficiaries: Poor and vulnerable families identified through the Socio-Economic Caste Census (SECC).",
         ">>>Cashless Treatment: Available at empaneled public and private hospitals across India.",
         ">>>No Family Size Limit: Covers all members of the family, regardless of age or number.",
         ">>>Portability: Beneficiaries can avail treatment anywhere in India.", "",
         "*COVER", ">>>Hospitalization expenses (surgery, medicines, diagnostics, etc.)",
         ">>>Pre- and post-hospitalization costs", ">>>Day-care procedures", "", "*ELIGIBILITY",
         ">>>Based on deprivation and occupational criteria in rural and urban areas.",
         ">>>No need for prior enrollment—eligible families are automatically included", ]
    for i in l:
        print(i)
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        India_Medical_Insurance()

#----------------Central Government Health Scheme (CGHS)---------------#
def CGHS():
    global name2,Age2,mobile2,genders2,st2,schemes1
    # (CGHS) logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("Central Government Health Scheme (CGHS)")
    # set up the display
    ps1 = p.display.set_mode((500, 500))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india-2.jpeg")
    ps = p.transform.scale(ps, (500, 500))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    print("******* Central Government Health Scheme (CGHS) ********")
    print(">>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<")
    st2="CGHS"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            CGHS()
    elif c == "no":
        print()
    schemes1 = "Central Government Health Scheme (CGHS)"
    print(schemes1)
    l = [">>>For: Central govt employees, pensioners, MPs", ">>>Covers OPD + hospitalization + medicines + tests",
         ">>>Available in major cities like Delhi, Mumbai, Kolkata", ">>>Best for government employees"]
    for i in l:
        print(i)
    print("************************ DETAILS ***********************")
    l = ["*ELIGIBLE :", "CGHS offers a wide range of healthcare services:",
         ">>>OPD treatment at CGHS Wellness Centres", ">>>Free or subsidized medicines",
         ">>>Specialist consultations (through referral)",
         ">>>Hospitalization(including cashless treatment in empanelled hospitals)",
         "Diagnostic tests (labs, X-rays, scans)", ">>>Emergency services", "",
         "*mainly for:", ">>>Central Government employees", ">>>Central Government pensioners",
         ">>>Members of Parliament", ">>>Judges of the Supreme Court and High Courts",
         ">>>Freedom fighters and certain other notified categorie", "", "*it works",
         ">>>Apply and receive a CGHS card", ">>>Visit a CGHS Wellness Centre for primary care",
         ">>>Get referral for specialists/hospitals if required",
         ">>>Avail treatment at empanelled hospitals (often cashless)", "",
         "*Key features:", ">>>Cashless treatment at CGHS-approved hospitals",
         ">>>Fixed package rates for procedures", "Lifelong coverage for pensioners (with contribution)",
         "Network of wellness centres and hospitals in major cities", "",
         "*Availability:", "CGHS is mainly operational in urban areas such:", ">Delhi", ">Chennai", "Mumbai",
         "Kolkata", "Bengaluru", "Hyderabad"]
    for i in l:
        print(i)
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        India_Medical_Insurance()

#--------------Employees' State Insurance Scheme (ESIC)----------------#
def ESIC():
    global name2, Age2, mobile2,genders2,st2,schemes1
    # Employees' State Insurance Scheme (ESIC) logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("Employees' State Insurance Scheme (ESIC)")
    # set up the display
    ps1 = p.display.set_mode((670, 500))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india-3.jpeg")
    ps = p.transform.scale(ps, (670, 500))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    print("******* Employees' State Insurance Scheme (ESIC) ***********")
    print(">>>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="ESIC"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2= mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            ESIC()
    elif c == "no":
        print()
    schemes1 = "Employees' State Insurance Scheme (ESIC)"
    print(schemes1)
    l = ["For: Workers in organized sector (salary-based eligibility)",
         "Covers medical care + maternity + disability benefits",
         "Includes hospitals, dispensaries & cash benefits", "Best for salaried workers in factories/companies"]
    for i in l:
        print(i)
    print("************************ DETAILS ************************")
    l = ["*Medical benefits", ">>>Free treatment for insured workers and their families",
         ">>>OPD and hospitalization services", ">>>OPD and hospitalization services",
         "Medicines and emergency treatment", "",
         "*Cash benefits", ">>>Sickness benefit: Income support during illness",
         ">>>Maternity benefit: Paid leave for pregnant women",
         ">>>Disablement benefit: Compensation for work-related injury or disability",
         "Dependents’ benefit: Financial support to family in case of death due to employment injury",
         "Dependents’ benefit: Financial support to family in case of death due to employment injury",
         ">>>Funeral expenses: Lump sum support", "",
         "*COVERED", ">>>Employees working in factories and establishments covered under the ESI Act",
         ">>>Typically applies to workers earning below a certain wage threshold (revised periodically)",
         "Employer must be registered under ESIC",
         ">>>Typically applies to workers earning below a certain wage threshold (revised periodically)",
         "Employer must be registered under ESIC", "",
         "*works", ">>>Both employer and employee contribute a percentage of wages",
         ">>>Employee gets an ESI card (Pehchan Card)", ">>>Can access services at ESIC hospitals and dispensaries",
         "*Key features", ">>>Covers both healthcare and wage loss", ">>>Family coverage included",
         ">>>Nationwide network of ESIC hospitals and dispensaries", ">>>Mandatory for eligible establishments",
         "*Difference from CGHS",
         ">>>Employees' State Insurance Scheme (ESIC): For private"
         "/organized sector workers (low to mid income)",
         ">>>Central Government Health Scheme (CGHS): For central government employees and pensioners"]
    for i in l:
        print(i)
        # You Are Apply This Scheme
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        India_Medical_Insurance()

#--------------Pradhan Mantri Suraksha Bima Yojana (PMSBY)---------------#
def PMSBY():
    global name2, Age2, mobile2,genders2,st2,schemes1
    # Pradhan Mantri Suraksha Bima Yojana (PMSBY) logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("Pradhan Mantri Suraksha Bima Yojana (PMSBY)")
    # set up the display
    ps1 = p.display.set_mode((500, 502))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india-4.jpg")
    ps = p.transform.scale(ps, (500, 502))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    print("******* Pradhan Mantri Suraksha Bima Yojana (PMSBY) *******")
    print(">>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="PMSBY"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************* Change the profile **********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            PMSBY()
    elif c=="no":
        print()
        schemes1="Pradhan Mantri Suraksha Bima Yojana (PMSBY)"
        print(schemes1)
        l = [">>>Very low premium (~20/year)", ">>>Covers accidental death/disability (2 lakh)", ">>>Age: 18-70 years",
             ">>>Good as basic accident + medical support plan"]
        for i in l:
            print(i)
        print("********************** DETAILS ***********************")
        l = ["*Key features:", ">>>Premium: ₹20 per year (auto-debited from bank account)",
             ">>>Coverage period: 1 year (June 1 to May 31, renewable annually)", "",
             "*Benefits", ">>>₹2 lakh for accidental death or total disability", ">>>₹1 lakh for partial disability",
             "",
             "*Can Enroll", ">>>Individuals aged 18 to 70 years", ">>>Must have a savings bank account",
             ">>>Consent to auto-debit of premium", "",
             "*covers", ">>>Death due to accident",
             ">>>Loss of both eyes, both hands/feet, or one eye + one limb (full disability)",
             ">>>Loss of one eye or one limb (partial disability)", "",
             "*Enroll", "You can join through:", ">>>Banks (public or private)",
             ">>>Internet banking or mobile banking", ">>>Some insurance providers and government portals", "",
             "*Important points", ">>>It is purely accident insurance (does not cover illness or natural death)",
             ">>>Very affordable and suitable for broad sections of the population",
             ">>>Can be linked with other schemes like:",
             "     *Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY) – life insurance",
             "     *Atal Pension Yojana (APY) – pension scheme"]
        for i in l:
            print(i)
        # You Are Apply This Insurance
        apply = input("your are apply this scheme(Yes/no)?: ")
        if apply == "yes":
            apply2()
        elif apply == "no":
            India_Medical_Insurance()
    else:
        print("check the number")
        PMSBY()

#----------------Aam Aadmi Bima Yojana (AABY)---------------------#
def AABY():
    global name2, Age2, mobile2,genders2,st2,schemes1
    # Aam Aadmi Bima Yojana (AABY) logo
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("Aam Aadmi Bima Yojana (AABY)")
    # set up the display
    ps1 = p.display.set_mode((500, 502))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india-5.jpeg")
    ps = p.transform.scale(ps, (500, 502))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    print("************* Aam Aadmi Bima Yojana (AABY) *****************")
    print(">>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="AABY"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************** Change the Profile *********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            AABY()
    elif c=="no":
        print()
    schemes1 = "Aam Aadmi Bima Yojana (AABY)"
    print(schemes1)
    l = ["For: Rural Landless & Low-income families", "Covers death & disability (natural + accidental)",
         "Includes scholarship benefits for children", "Best for rural/Low-income households"]
    for i in l:
        print(i)
    print("********************** DETAILS ***********************")
    l = ["*Key features", ">>>Administered by the Life Insurance Corporation of India (LIC)",
         ">>>Designed for poor and vulnerable families", ">>>Covers the head of the household or earning member",
         "",
         "*Eligibility", ">>>Age: 18 to 59 years",
         ">>>Belongs to a below poverty line (BPL) household or certain identified occupational groups",
         ">>>Typically one member per family is covered", "",
         "*Premium", ">>>Around ₹200 per year",
         ">>>Shared between the Central Government and State Government (beneficiary pays little or nothing in many cases)",
         "",
         "*Benefits", ">>>₹30,000 for natural death",
         ">>>₹75,000 for accidental death or permanent total disability", ">>>₹37,500 for partial disability", "",
         "*Additional benefit", "Scholarship for children:",
         "   >>>Up to two children of the insured (studying in classes 9–12)", "   >>>₹100 per month per child", "",
         "*Important note", "AABY has largely been merged or replaced by newer schemes like:",
         "   >>>Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
         "   >>>Pradhan Mantri Suraksha Bima Yojana (PMSBY)"]
    for i in l:
        print(i)
    # You Are Apply This Insurance
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        India_Medical_Insurance()

#-----------------TamilNadu Medical Insurance--------------------#
#Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)
def CMCHIS():
    global name2, Age2, mobile2,genders2,schemes1,st2
    # Tamil Nadu Insurance Scheme Logo
    p.init()
    p.mixer.init()
    # set up display name
    p.display.set_caption("TAMIL NADU INSURANCE SCHEMES  ")
    # set up display
    ps1 = p.display.set_mode((554, 554))
    # load and scale Background image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tamilnadu insurance logo.jpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    print()
    print("Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)")
    print(">>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="CMCHIS"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile2 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************* Change the Profile ********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            CMCHIS()
    elif c=="no":
        print()
    schemes1 = "Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)"
    print(schemes1)
    l = [
        "*The Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS) is a flagship health insurance program run by the Government of Tamil Nadu to provide free medical treatment to eligible low- and middle-income families.",
        "*Launched by the Tamil Nadu government, CMCHIS aims to reduce the financial burden of major illnesses by offering cashless treatment in both government and empanelled private hospitals.",
        "", "Main state government insurance", ">>>Coverage: up to 5 lakh per family/year", "Schemes Seva",
        "Cashless treatment in govt + private hospitals", "Covers surgeries, hospitalization, diagnostics",
        "Best for: low-income families in Tamil Nadu"]
    for i in l:
        print(i)
    print("*********************** DETAILS ************************")
    l = ["*Features", ">>>Coverage: Up to ₹5 lakh per family per year (for certain procedures/packages)",
         ">>>Cashless treatment: Available at network hospitals",
         ">>>Family-based scheme: Covers the entire family", "",
         "*Eligibility", ">>>Residents of Tamil Nadu",
         ">>>Annual family income generally up to ₹1.2 lakh (may vary based on updates)",
         ">>>Must have a valid ration card", "",
         "*Covers", ">>>Major surgeries (cardiac, cancer, neuro, etc.)", ">>>Hospitalization expenses",
         ">>>Diagnostic tests", ">>>Follow-up treatments (for certain conditions)", "",
         "*Hospitals covered", ">>>Government hospitals across Tamil Nadu",
         ">>>Empanelled private hospitals under the scheme", "",
         ""]
    for i in l:
        print(i)
    # You Are Apply This Insurance
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        Tamil_Nadu_Medical_Insurance()

#------------------Kalaignar Kaappittu Thittam-------------------------#
def KKT():
    global name2, Age2, mobile2,genders2,st2,schemes1
    # Tamil Nadu Insurance Scheme Logo
    p.init()
    p.mixer.init()
    # set up display name
    p.display.set_caption("TAMIL NADU INSURANCE SCHEMES  ")
    # set up display
    ps1 = p.display.set_mode((554, 554))
    # load and scale Background image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    print()
    print("************** Kalaignar Kaappittu Thittam *****************")
    print(">>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="KKT"
    name2=name_1
    Age2=Age
    genders2=gender
    mobile2=mobile
    l=[f"Name: {name2}",f"Age: {Age2}", f"Gender: {genders2}",f"Mobile No:{mobile2}"]
    for i in l:
        print(i)
    c=input("Change the Profile(yes/no): ")
    if c=="yes":
        print("******************* Change the Profile ***********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            KKT()
    elif c=="no":
        print()
    schemes1 = "Kalaignar Kaappittu Thittam"
    print(schemes1)
    l = [
        "*The Kalaignar Kaappittu Thittam was a major health insurance scheme launched by the Tamil Nadu government to provide free medical treatment for poor families, especially for life-saving surgeries.",
        "*Introduced in 2009 under the leadership of M. Karunanidhi,Aimed at low-income families in Tamil Nadu,Focused mainly on high-cost treatments and surgeries",
        "Earlier version of CMCHIS (still referred in records)", "Now merged/improved into CMCHIS",
        "Provided free medical insurance for poor family"]
    for i in l:
        print(i)
    print("********************* DETAILS ***************************")
    l = ["*Features", ">>>Cashless treatment in empanelled hospitals",
         ">>>Coverage for major surgeries (cardiac, cancer, renal, etc.)",
         ">>>Financial protection against expensive medical procedures", "",
         "*Eligibility", ">>>Families with low annual income", ">>>Must possess a valid ration card", "",
         "*Hospitals covered", ">>>Government hospitals",
         ">>>Selected private hospitals empanelled under the scheme"]
    for i in l:
        print(i)
    # You Are Apply This Insurance
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        Tamil_Nadu_Medical_Insurance()


#--------------------Amma Kaappittu Thittam----------------------------#
def AKT():
    global name2, Age2, mobile3,genders2,st2,schemes1
    # Tamil Nadu Insurance Scheme Logo
    p.init()
    p.mixer.init()
    # set up display name
    p.display.set_caption("TAMIL NADU INSURANCE SCHEMES  ")
    # set up display
    ps1 = p.display.set_mode((554, 554))
    # load and scale Background image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tamilnadu insurance logo.jpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    print()
    print("************** Amma Kaappittu Thittam ***************")
    print(">>>>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="AKT"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile3 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile3}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ")
    if c == "yes":
        print("******************* Change the Profile ***********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile3 = input("Enter the Mobile Number: ")
        if mobile3.isdigit() and len(mobile3) == 10 and mobile3.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            AKT()
    elif c=="no":
        print()
    schemes1 = "Amma Kaappittu Thittam"
    print(schemes1)
    l = [
        "*The Amma Kaappittu Thittam was a health insurance scheme launched by the Government of Tamil Nadu to provide financial protection for medical treatments to economically weaker families.",
        "*Introduced during the period of J. Jayalalithaa",
        "*Aimed at expanding access to cashless hospitalization for poor and middle-income families",
        "Functioned as an upgraded continuation of earlier state health insurance initiatives"]
    for i in l:
        print(i)
    print("************************ DETAILS ************************")
    l = ["*Features", ">>>Cashless treatment in empanelled private and government hospitals",
         ">>>Coverage for major surgeries and serious illnesses",
         ">>>Family-based coverage for eligible households", ">>>Focus on reducing out-of-pocket medical expenses",
         "",
         "*Eligibility", ">>>Low and middle-income families in Tamil Nadu",
         ">>>Valid ration card or income-based eligibility criteria"]
    for i in l:
        print(i)
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        Tamil_Nadu_Medical_Insurance()

#------------New Health Insurance Scheme (NHIS) Tamil Nadu--------------#
def NHIS():
    global name2, Age2, mobile3,genders2,st2,schemes1
    # Tamil Nadu Insurance Scheme Logo
    p.init()
    p.mixer.init()
    # set up display name
    p.display.set_caption("TAMIL NADU INSURANCE SCHEMES  ")
    # set up display
    ps1 = p.display.set_mode((554, 554))
    # load and scale Background image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tamilnadu insurance logo.jpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    print()
    print("****** New Health Insurance Scheme (NHIS) Tamil Nadu *******")
    print(">>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="NHIS"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile3 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile3}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ").lower()
    if c == "yes":
        print("******************* Change the Profile ***********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile3 = input("Enter the Mobile Number: ")
        if mobile3.isdigit() and len(mobile3) == 10 and mobile3.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            NHIS()
    elif c=="no":
        print()
    schemes1 = "New Health Insurance Scheme (NHIS) Tamil Nadu"
    print(schemes1)
    l = [
        "The New Health Insurance Scheme (NHIS) in Tamil Nadu is a state-sponsored health insurance program mainly for government employees and pensioners.",
        "The New Health Insurance Scheme (NHIS) in Tamil Nadu is a state-sponsored health insurance program mainly for government employees and pensioners.",
        ">State government employees", ">Pensioners and family pensioners",
        ">Certain public sector and board employees (depending on eligibility rules)",
        "It is implemented through an insurance company and works as a cashless hospitalisation cover system in empanelled hospitals",
        ">>>For Tamil Nadu government employees & pensioners", ">>>Coverage: approx ₹5-10 lakh",
        ">>>Premium deducted from salary", ">>>Cashless treatment in approved hospitals"]
    for i in l:
        print(i)
    print("**************************** DETAILS ************************")
    l = ["*Features", ">>>Coverage: Around ₹5 lakh per family (per policy block period)",
         ">>>Higher coverage: Up to ₹10 lakh for specified serious treatments/surgeries",
         ">>>Cashless treatment in network hospitals", ">>>for Covers employee + eligible dependents",
         ">>>Policy works in multi-year blocks (typically 4 years)", "",
         "*Eligibility", ">>>Government department employees", ">>>State public sector undertakings (PSUs)",
         ">>>Local bodies and statutory boards", ">>>State government universities",
         ">>>Pensioners receiving pension from Tamil Nadu government systems", "",
         "*Covers", ">>>Hospitalisation expenses", ">>>Surgeries (cardiac, cancer, neurological, kidney, etc.)",
         ">>>Emergency treatments", ">>>Listed medical procedures under policy package rates",
         ">>>Pre-defined hospital networks for cashless care",
         "*Works", ">>>Employee/pensioner is automatically enrolled through department",
         ">>>Insurance premium is usually deducted from salary/pension", ">>>Beneficiary gets NHIS ID card",
         ">>>Treatment taken in empanelled hospital", ">>>Treatment taken in empanelled hospital"]
    for i in l:
        print(i)
    # You Are Apply This Insurance
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        Tamil_Nadu_Medical_Insurance()

#------Chief Minister's Health Insurance Scheme for Pensioners---------#
def CMCHISP():
    global name2, Age2, mobile3,genders2,st2, schemes1
    # Tamil Nadu Insurance Scheme Logo
    p.init()
    p.mixer.init()
    # set up display name
    p.display.set_caption("TAMIL NADU INSURANCE SCHEMES  ")
    # set up display
    ps1 = p.display.set_mode((554, 554))
    # load and scale Background image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\tamilnadu insurance logo.jpeg")
    ps = p.transform.scale(ps, (554, 554))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    print()
    print("**** Chief Minister's Health Insurance Scheme for Pensioners ****")
    print(">>>>>>>>>>>>>>>>>>>>>> LONG PAGE <<<<<<<<<<<<<<<<<<<<<<<<<<")
    st2="CMCHISP"
    name2 = name_1
    Age2 = Age
    genders2 = gender
    mobile3 = mobile
    l = [f"Name: {name2}", f"Age: {Age2}", f"Gender: {genders2}", f"Mobile No:{mobile3}"]
    for i in l:
        print(i)
    c = input("Change the Profile(yes/no): ").lower()
    if c == "yes":
        print("******************* Change the Profile ***********************")
        name2 = input("Enter the Name: ").lower()
        birth_year = int(input("Enter the Birth year: "))
        cy = dt.datetime.now().year
        Age2 = cy - birth_year
        print(f"Age: {Age2}")
        genders2 = input("Enter the Gender(Male/Female): ")
        # mobile Number Validation
        mobile3 = input("Enter the Mobile Number: ")
        if mobile3.isdigit() and len(mobile3) == 10 and mobile3.startswith(("6", "7", "8", "9")):
            print()
        else:
            print("check the number")
            CMCHISP()
    elif c=="no":
        print()
    schemes1 = "Chief Minister's Health Insurance Scheme for Pensioners"
    print(schemes1)
    l = [
        "The “Chief Minister’s Health Insurance Scheme for Pensioners” in Tamil Nadu generally refers to the pensioner coverage provided under the state’s group insurance program, namely.",
        "This scheme is meant for:", " *Retired Tamil Nadu government employees", " *Family pensioners",
        "It ensures they continue to receive cashless hospital treatment after retirement.", "",
        "*Features", ">>>Coverage: About ₹5 lakh per family (per policy block)",
        ">>>Up to ~₹10 lakh for select high-end procedures", ">>>Cashless treatment in empanelled hospitals",
        ">>>Covers pensioner and eligible family members",
        ">>>Runs in fixed multi-year policy periods (e.g., 4 years)", "",
        "*Eligibility", ">>>Tamil Nadu government pensioners",
        ">>>Family pensioners drawing pension from the state", ">>>Must be enrolled under NHIS", "",
        "*covers", ">>>Hospitalization expenses", ">>>Major surgeries (cardiac, cancer, neuro, renal, etc.)",
        ">>>Emergency treatments", ">>>Pre-approved procedures under package rates", "",
        "*Works", ">>>Enrollment through pension disbursing authority",
        ">>>Premium (if applicable) deducted from pension", ">>>NHIS card issued", ">>>Visit empanelled hospital",
        ">>>Get cashless treatment after authorization"]
    for i in l:
        print(i)
    # You Are Apply This Insurance
    apply = input("your are apply this scheme(Yes/no)?: ")
    if apply == "yes":
        apply2()
    elif apply == "no":
        Tamil_Nadu_Medical_Insurance()

#-----------------TAMIL NADU MEDICAL INSURANCE------------------------#
def Tamil_Nadu_Medical_Insurance():
    #----Tamil Nadu Government logo-----#
    p.init()
    p.mixer.init()
    # set up the display name
    p.display.set_caption("Tamil Nadu Government")
    # set up the display
    ps1 = p.display.set_mode((650, 500))
    # load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\TamilNadu logo.jpeg")
    ps = p.transform.scale(ps, (650, 500))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    # wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    #Tamil Nadu Top 5 Insurance
    print(">>>>>>>>>>>>>>>>>>>>> Top 5 Insurance <<<<<<<<<<<<<<<<<<<<<<")
    l=["1.Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)","2.Kalaignar Kaappittu Thittam","3.Amma Kaappittu Thittam","4.New Health Insurance Scheme (NHIS) Tamil Nadu","5.Chief Minister's Health Insurance Scheme for Pensioners","6.Back"]
    for i in l:
        print(i)
    choose=input("choose the choice: ")
    if choose=="1":
        CMCHIS()
    elif choose=="2":
        KKT()
    elif choose=="3":
        AKT()
    elif choose=="4":
        NHIS()
    elif choose=="5":
        CMCHISP()
    elif choose=="6":
        Government_Insurance()
    else:
        print("Check The Insurance...!")
        Tamil_Nadu_Medical_Insurance()

#--------------------INDIA MEDICAL INSURANCE-------------------------#
def India_Medical_Insurance():
    #-----India Government logo-----#
    p.init()
    p.mixer.init()
    #set up the display name
    p.display.set_caption("India Government")
    #set up the display
    ps1 = p.display.set_mode((550, 650))
    #load and scale Background Image
    ps = p.image.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\india logo .jpeg")
    ps = p.transform.scale(ps, (550, 650))
    ps1.blit(ps, (0, 0))
    #update display
    p.display.update()
    # load and scale Background Music
    p.mixer.music.load(r"C:\Users\Naveen M\PycharmProjects\Mini Project\.venv\Scripts\PIK\logos music\logo song.mpeg")
    p.mixer.music.play(-1)
    #wait for  Image and Music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(1)
    print()
    #India TOp 5 nsurance
    print(">>>>>>>>>>>>>>>>>>> Top 5 Insurance <<<<<<<<<<<<<<<<<<<<<<<<<<")
    l=["1.Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)","2.Central Government Health Scheme (CGHS)","3.Employees' State Insurance Scheme (ESIC)","4.Pradhan Mantri Suraksha Bima Yojana (PMSBY)","5.Aam Aadmi Bima Yojana (AABY)","6.Back"]
    for i in l:
        print(i)
    choose=input("Choose your choice: ")
    if choose=="1":
        ABPMJAYPJ()
    elif choose=="2":
        CGHS()
    elif choose=="3":
        ESIC()
    elif choose=="4":
        PMSBY()
    elif choose=="5":
        AABY()
    elif choose=="6":
        Government_Insurance()
    else:
        print("Check The Insurance...!")
        India_Medical_Insurance()

#--------------------Government Medical Insurance-----------------------#
def Government_Insurance():
    print()
    print("************** Government Medical insurance ****************")
    l = ["1.INDIA MEDICAL INSURANCE ", "2.TAMIL NADU INSURANCE","3.Back"]
    for i in l:
        print(i)
    choose=input("Choose your choice: ")
    if choose=="1":
        #INDIA MEDICAL INSURANCE
        India_Medical_Insurance()
    elif choose=="2":
        #TAMIL NADU INSURANCE
        Tamil_Nadu_Medical_Insurance()
    elif choose=="3":
        insurance_apply()
    else:
        print("Check The Insurance...!")
        Government_Insurance()

#--------------------claim Details Final payment------------------------#
def Final_payment():
    t.sleep(5)
    #Final Amount Calculation
    pay=total-Total
    print()
    print(">>>>>>>>>>>>>>>>>>>>> Final payment <<<<<<<<<<<<<<<<<<<<<<<<")
    print()
    x=f"*Total Bill: ₹{total}"
    print(x)
    y=f"Insurance payment: ₹{Total}"
    print(y)
    z=f"*Patient payment: ₹{pay}"
    print(z)
    #Patient Details Document Post a Email Id
    print(f"send a documents in Email Id ")
    print("Sending claim Details to WhatsApp")
    t.sleep(5)
    #All Details Send aWhatsApp Message
    w="""
    "Hospital name" :{}
    ========================================================
    "Final Approved Amount(Approx)" :{}
    ========================================================
    "Total Approved=₹" : {}
    "Total Bill" : {}
    "Insurance payment" : {}
    "Patient payment"  :{} 
    """
    q=w.format(hospital,V,Total,total,Total,pay)
    pk.sendwhatmsg_instantly(f"+91 {mobile2}",  f"{q}")
    pg.doubleClick()


#--------------------Final Approved Amount(Approx)---------------------#
def Final_approved_amount():
    global Total,V
    # wait Final Approved page load
    t.sleep(5)
    print()
    print("~~~~~~~~~~~~~~ Final Approved Amount(Approx) ~~~~~~~~~~~~~~~~")
    print()
    # wait for Final Approved Amount page load
    t.sleep(3)
    #Approvel Amount calculation
    f=(10/100)*R
    r=R-f
    f = (10 / 100) * D
    d = D - f
    f = (10 / 100) * S
    s = S - f
    f = (10 / 100) * I
    i = I - f
    f = (10 / 100) * M
    m = M - f
    f = (10 / 100) * LT
    lt = LT - f
    f = (10 / 100) * C
    c = C - f
    Total=r+d+s+i+m+lt+c
    bill1= {
        "Expense Type": ["Room Rent", "Doctor Fees", "Surgery Charges", "ICU Charges", "Medicines", "Lab Tests",
                         "Consumables"],
        "Claimed": [R, D, S, I, M, LT, C],
        "Approved":[r,d,s,i,m,lt,c]
    }
    V=pd.DataFrame(bill1)
    print(V)
    t.sleep(5)
    #Approvel Total Amount
    print(f"Total Approved= ₹{Total}")
    Final_payment()

#-----------------------0Hospital Bill Breakdown------------------------#
def hospital_bill():
    global R,D,S,I,M,LT,C,total
    t.sleep(1)
    print()
    print("*************** Hospital Bill Breakdown *******************")
    R=int(input("Patient Room Rent:₹"))
    D=int(input("Surgery Doctor Fees:₹"))
    S=int(input("Patient Surgery charges:₹"))
    I=int(input("Patient ICU charges:₹"))
    M=int(input("Patient Medicines charges:₹"))
    LT=int(input("Lab Tests charges:₹"))
    C=int(input("Patient consumables charges:₹"))
    total=R+D+S+I+M+LT+C

    bill={
        "Expense Type" :["Room Rent","Doctor Fees","Surgery Charges","ICU Charges","Medicines","Lab Tests","Consumables","Total Bill"],
        "Amount(₹)"    :[R,D,S,I,M,LT,C,total]
    }
    print(pd.DataFrame(bill))
    Final_approved_amount()

#-----------------------Hospitalization Details-------------------------#
def hospital_details():
    global hospital
    t.sleep(2)
    print()
    print("--------------- Hospitalization Details --------------------")
    hospital=input("1.Hospital Name: ")
    Reason=input("2.Enter the Reason: ")
    Reason_summary=input("3.Reason Summary: ")
    Doctor_name=input("Enter the Doctor Name: ")
    Admission_Date=input("4.Enter the Admission date: ")
    Discharge_date=input("5.Enter the Discharge date: ")
    hospital_bill()

#------------------------ Government Insurance Details -----------------------------#
def search_insurance2():
    roll_search = input("Enter Insurance  Number to Search: ").upper()
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            insurance_no, name, family,schemes,insurance_amount,Ration = line.strip().split(",")

            if insurance_no == roll_search:
                print("\nInsurance Details")
                print("----------------")
                print("Insurance No :", insurance_no)
                print("Name    :", name)
                print("Family No  :", family)
                print("Schemes  :", schemes)
                print("insurance Amount   :", insurance_amount)
                print("Ration No   :", Ration)
                found = True
                hospital_details()
                break
    if not found:
        print("Insurance Id Not Found!\n")

#------------------------private Insurance Details-----------------------------#
def search_insurance1():
    roll_search = input("Enter Insurance  Number to Search: ").upper()
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            insurance_no, name, family_no, policy, insurance_company_name, insurance_amount = line.strip().split(",")

            if insurance_no == roll_search:
                print("\nInsurance Details")
                print("----------------")
                print("Insurance No :", insurance_no)
                print("Name    :", name)
                print("Family No  :", family_no)
                print("Policy   :",  policy)
                print("insurance company   :", insurance_company_name)
                print("insurance Amount   :", insurance_amount)
                found = True
                hospital_details()
                break
    if not found:
        print("Insurance Id Not Found!\n")

#-----------------Private Insurance Company Claim-----------------------#
def private_Insurance_company():
    global name1,mobile2
    # wait for Insurance page load
    t.sleep(2)
    print()
    print("**************** private Insurance company claim ****************")
    name1 = input("Enter the Name: ")
    # Mobile Number Validation
    mobile2 = input("Enter the Mobile Number: ")
    print("Sending OTP to WhatsApp...")
    t.sleep(1)
    if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
        OTP = rd.randrange(1234, 5678)
        print("OTP",OTP)
        # Send WhatsApp Message
        pk.sendwhatmsg_instantly(f"+91 {mobile2}", f" Claim insurance OTP: {OTP}")
        pg.doubleClick()
        #OTP Verification
        OTP1 = int(input("Enter the OTP* :"))
        if OTP1 == OTP:
            #Insurance Details
            print(f"Name: {name1}")
            search_insurance1()
        else:
            print("chek the OTP...!")
            private_Insurance_company()
    else:
        print("check the number...!")
        private_Insurance_company()

#------------------- Government Insurance claim ------------------------#
def Government_Medical_Insurance():
    global name1, mobile2
    #wait for Government Insurance Claim Page
    t.sleep(2)
    print()
    print("**************** Government Insurance claim ****************")
    l = ["1.Indian Insurance Schemes", "2.Tamil Nadu Insurance Schemes"]
    for i in l:
        print(i)
    sm = input("Select Tha Insurance Scheme: ")
    if sm == "1":
        # Indian Insurance Schemes Claim
        print()
        print("*************** Indian Insurance Schemes ****************")
        name1 = input("Enter the Name: ")
        mobile2 = input("Enter the Mobile Number: ")
        t.sleep(1)
        #mobile Number Validation
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            OTP = rd.randrange(1234, 5678)
            print("Sending OTP to WhatsApp...")
            print(OTP)
            # Send WhatsApp Message
            pk.sendwhatmsg_instantly(f"+91 {mobile2}",
                                     f" Indian Insurance Schemes Claim Loging OTP: {OTP}",
                                     wait_time=15,
                                     tab_close=True,
                                     close_time=3)
            t.sleep(2)
            #press Enter Automatically
            pg.press("enter")
            # OTP Verification
            OTP1 = int(input("Enter the OTP* :"))
            if OTP1 == OTP:
                #INsurance Details
                print(f"Name: {name1}")
                Ration_card = input("your Ration card No: ")
                search_insurance2()
            else:
                print("chek the OTP...!")
                Government_Medical_Insurance()
        else:
            print("check the number...!")
            Government_Medical_Insurance()
    elif sm == "2":
        #Tmail Nadu Government Insurance Schemes Claim
        print()
        print("**************** Tamil Nadu Insurance Schemes ****************")
        name1 = input("Enter the Name: ")
        # mobile Number Validation
        mobile2 = input("Enter the Mobile Number: ")
        print("Sending OTP to WhatsApp...")
        t.sleep(1)
        if mobile2.isdigit() and len(mobile2) == 10 and mobile2.startswith(("6", "7", "8", "9")):
            OTP = rd.randrange(1234, 5678)
            # Send WhatsApp Message
            # pk.sendwhatmsg_instantly(f"+91 {mobile2}", f" Claim insurance OTP: {OTP}")
            # pg.doubleClick()
            pk.sendwhatmsg_instantly(f"+91 {mobile2}",
                                     f" Tamil Nadu Government Insurance Schemes Claim Loging OTP: {OTP}",
                                     wait_time=15,
                                     tab_close=True,
                                     close_time=3)
            t.sleep(2)
            # press Enter Automatically
            pg.press("enter")
            # OTP Verification
            OTP1 = int(input("Enter the OTP* :"))
            if OTP1 == OTP:
                #Insurance Details
                print(f"Name: {name1}")
                Ration_card = input("your Ration card No: ")
                search_insurance2()
            else:
                print("chek the OTP...!")
                Government_Medical_Insurance()
        else:
            print("check the number...!")
            Government_Medical_Insurance()

#---- Private Company Insurance claim or Government Insurance Claim ----#
def insurance_claim():
    print()
    print("******************** Insurance Claim ***********************")
    d=["1.private Insurance company","2.Government Medical Insurance"]
    for i in d:
        print(i)
    choose3=input("Choose your choice: ")
    if choose3=="1":
        # Private Insurance Company Claim
        private_Insurance_company()
    elif choose3=="2":
        # Government Insurance Calim
        Government_Medical_Insurance()
    elif choose3=="3":
        choose()
    else:
        insurance_claim()

#-----Private Insurance Company or Government Insurance-------------------#
def insurance_apply():
    print()
    print("***************** Insurance Apply **************************")
    print("Enter your Insurance:")
    c = ["1.private Insurance company", "2.Government Insurance","3.Back"]
    for i in c:
        print(i)
    choose1=input("Enter the Insurance type: ")
    if choose1=="1":
        # Private Insurance Company
        insurance_company()
    elif choose1=="2":
        # Government Insurance
        Government_Insurance()
    elif choose1=="3":
        choose()
    else:
        insurance_apply()

#--------------------Insurance Apply or Claim Page--------------------#
def choose():
    print()
    print(">>>>>>>>>>>>>>>>>>>> Apply and Claim >>>>>>>>>>>>>>>>>>>>>>>")
    b = ["1.Insurance apply", "2.Insurance claim"]
    for i in b:
        print(i)
    choose1=input("Choose your choice: ")
    if choose1=="1":
        insurance_apply()
    elif choose1=="2":
        insurance_claim()
choose()
