RiskAssure: Digital Insurance Suite
A Python-based medical insurance management mini project developed using Python libraries and automation tools.
This project simulates a real-world insurance system with login authentication, OTP verification, insurance application, QR code payment, WhatsApp automation, and insurance card generation

Steps Implemented (20)
1.	Welcome logo +10 sec welcome music (Pygame)
2.	Welcome banner with stars
3.	Register – name, age, gender, Email, password, mobile number
4.	Login form - User authentication, Password verification (recursive, retries until correct)
5.	OTP Verification – WhatsApp OTP via – must be entered to proceed (Random, PyWhatkit)
6.	Select members you to Insurance – (Self, Family, Father, Mother, Wife, Brother, Sister,)
7.	Insurance Selection (1 Apply / 2 Claim) 
8.	Apply - Insurance Selection – (1 Private Insurance Company / 2 Government Insurance)
9.	1 Private Insurance Company
1.  Select Company (1 Schemes select Star Health Insurance / 2 Niva Bupa  / 3 Care    Health              Insurance / 4 ICICI Lombard / 5 TATA AIG) 
2. Insurance Company Logo +10 sec music
3. Schemes select (Top 5 Scheme show (1, 2, 3, 4, 5)) 
4. View the profile – show the scheme Details (Premium details / Hospital coverage / Room rent benefits / Ambulance coverage / Cashless hospitals / Daycare treatment)
5. OTP Verification – WhatsApp OTP via – must be entered to proceed
6. Insurance Apply Form (Address, Blood, Aadhar, Pancard, Family No, Income Certificate No)
7. Payment System - UPI QR code generation , Payment amount calculation , Monthly & yearly premium options (QRCode, PIL) 
8. Insurance Dome card Photo (3 sec)
9. Send the WhatsApp Message in Insurance details
10.	Government Insurance (1 India Insurance / 2 Tamil Nadu Insurance )
1. Insurance Company Logo +10 sec music
2. Schemes select (Top 5 Scheme show (1, 2, 3, 4, 5)) 
3. View the profile – show the scheme Details (Premium details / Hospital coverage /     Room rent benefits / Ambulance coverage / Cashless hospitals / Daycare treatment)
4. OTP Verification – WhatsApp OTP via – must be entered to proceed
5. Insurance Apply Form (Address, Blood, Aadhar, Pancard, Family No, Income Certificate No)
6. Send the WhatsApp Message in Insurance details

11.	Insurance Claim
12.	Insurance Selection – (1 Private Insurance Company / 2 Government Insurance)
13.	Insurance login-(mobile no, name, Insurance NO, OTP)
14.	OTP Verification – WhatsApp OTP via – must be entered to proceed
15.	Show the insurance Person Details(Name, Insurance company, Policy Type, Insurance Sum Amount)
16.	Patient Details (Name,  Hospital Name, Dc.Name, Reason, Reason summary, Admission Date, Discharge Data )
17.	 Hospital Bill – ( Room, Doctor Fess, Surgery Charges, Medical Fess, Lap Test, Consumables)(pandas)
18.	Validation – Payment
19.	Insurance Approved Hospital Bill (Pandas)
20.	Send the WhatsApp Message in Insurance claim hospital bill and approved amount . 
 Libraries Installation
Install all required libraries before running the project.
pip install pygame
pip install pywhatkit
pip install pyautogui
pip install pandas
pip install qrcode
pip install pillow


NOTES
•	Internet connection is required for WhatsApp OTP sending. 
•	WhatsApp Web must be logged in for PyWhatKit automation. 
•	Keep image and music files in correct folders. 
•	QR code images are generated automatically. 
•	This project is for educational purposes only



