import datetime
import mysql.connector

mydb=mysql.connector.connect (host="localhost",user="root",passwd="s@meer2004",database="doctor")
mycursor = mydb.cursor()

currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
    a = ("LOGIN SUCCESSFUL. GOOD MORNING ")
elif 12 <= currentTime.hour < 18:
    a = ("LOGIN SUCCESSFUL. GOOD AFTERNOON ")
else:
    a = ("LOGIN SUCCESSFUL. GOOD EVENING ")

#function to enter the name       
def name():
    name = str(input('Enter the name: '))
    return name

#function to enter the password
def password():
    password = str(input('Enter the password: '))
    return password

#function to display patient's information
def info():
    name3 = input("Enter the patient's name (IN BLOCK LETTERS): ")
    print("")
    print("----------PATIENT'S INFO---------")
    mycursor.execute('SELECT NAME,DISEASE,YEAR FROM history;')
    data2 = mycursor.fetchall()
    for i in range(len(data2)):
        if data2[i][0] == name3:
            print("Name",data2[i][0],"Previous Medical History",data2[i][1],"Year",data2[i][2])
            accident()
        break
    
#function during accident 
def accident():
    print("What is the patient suffering from??")
    print("")
    print("--------PROBLEM--------")
    print("|    CARDIAC ARREST   |")
    print("|       ACCIDENT      |")
    print("|    GUNSHOT WOUND    |") 
    print("| ATTACK WITH A KNIFE |")
    print("|      HEATSTROKE     |")
    print("|         BURNS       |")
    print("")
    problem = input('Enter the problem: ')
    print("")
    mycursor.execute('SELECT * FROM accident')
    data3 = mycursor.fetchall()
    for i in range (len(data3)):
        if data3[i][0] == problem:
            print("DO AS WRITTEN")
            print(data3[i][0],data3[i][1])
        break

#function to login
def login():
    print (" ----------- LOGIN -----------")
    print("")
    print("Please enter all information in BLOCK letters")
    print("")
    n = name() #function call
    p = password() #function call
    mycursor.execute('SELECT NAME,PASSWORD FROM login;')
    data = mycursor.fetchall()
    for i in range(len(data)):
        if data[i][0] == n and data[i][1] == p:
            print("")
            print(a,n)
            break
            
        if data[i][0] == n and data[i][1] != p:
            print("")
            print ("!INCORRECT PASSWORD, PLEASE ENTER AGAIN!")
            p1 = password() #function call
            if data[i][0] == n and data[i][1] == p1:
                print("")
                print(a,n)
                break
                
        if data[i][0] != n and data[i][1] == p:
            print("")
            print ("!INCORRECT NAME, PLEASE ENTER AGAIN!")
            n1 = name() #function call
            if data[i][0] == n1 and data[i][1] == p:
                print("")
                print(a,n1)
                break
    else:
        print("!BOTH PASSWORD AND NAME ARE INCORRECT!")
        login() #function call
    
print("")  

#function to create a new account
def new_acc():
    print (" ----------- NEW ACCOUNT -----------")
    print ("")
    print("Please enter all information in BLOCK letters")
    name1 = str(input('Enter your name: '))
    age1 = str(input('Enter the age: '))
    gender1 = str(input('Enter the gender (MALE/FEMALE): '))
    password1 = str(input('Enter the password: '))
    password2 = str(input('Re-enter the password: '))
    print("")
    if password1 == password2:
        mycursor.execute("INSERT INTO LOGIN (NAME,PASSWORD,AGE,GENDER) VALUES ('{}','{}','{}','{}')".format(name1,password1,age1,gender1))
        mydb.commit()
        print ("ACCOUNT CREATED SUCCESSFULLY")
        print("")
        login()

    else:
        print("PASSWORD DOES NOT MATCH")
        new_acc()
        print("")

#function to detect the disease
symplist = []
dislist = []
def diagnosis():
    for i in range (len(symplist)):
        mycursor.execute("SELECT SYMPTOMS,Diseases FROM SYMPTOMS;")
        data = mycursor.fetchall() #fetching values from SQL table
        for j in data:
            if symplist[i] == j[0]:
                if j[1] not in dislist:
                    dislist.append(j[1])
                else:
                    continue

    for a in range(len(dislist)):
        if dislist[a] == "ALLERGIES":
            choice = input('Do you have rashes on your skin?? (Y/N): ')
            choice1 = input('Do you have a swelling on any part of your body?? (Y/N): ')
            if choice == 'Y' or choice1 == 'Y':
                 print(" ")
                 print("-----------------------------------------------------------------------------")
                 print ("You're suffering from ALLERGIES, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'ALLERGIES';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue

        elif dislist[a] == "COLD AND FLU":
            choice = input('Are you having a sore throat?? (Y/N): ')
            choice1 = input('Are you having a fever?? (Y/N): ')
            if choice == 'Y' or choice1 == 'Y':
                 choice3 = input('Are you having a difficulty in breathing?? (Y/N): ')
                 if choice3 == 'Y':
                         print(" ")
                         print("----------------------------------------------------------------------------")
                         print ("You're suffering from ASTHAMA, Please use the medication recommended below ")
                         print("")
                         mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'ASTHAMA';")
                         data1 = mycursor.fetchall() #fetching values from SQL table
                         for j in data1:
                             print(str(j[0]))
                             print("")
                             print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                             print("")
                             print("--------------------------------------------------------------------------")
                             print("")
                             print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                             print("")
                             print("==========================================================================")
                         break
                 elif choice3 == 'N':
                     print(" ")
                     print("---------------------------------------------------------------------------------")
                     print ("You're suffering from COLD AND FLU, Please use the medication recommended below ")
                     print("")
                     mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'COLD AND FLU';")
                     data1 = mycursor.fetchall() #fetching values from SQL table
                     for j in data1:
                         print(str(j[0]))
                         print("")
                         print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                         print("")
                         print("--------------------------------------------------------------------------")
                         print("")
                         print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                         print("")
                         print("==========================================================================")
                         
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue
                 
        elif dislist[a] == "CONJUNCTIVITIS":
            choice = input('Do you have a reddiness in your eye?? (Y/N): ')
            if choice == 'Y':
                 print(" ")
                 print("----------------------------------------------------------------------------------")
                 print ("You're suffering from CONJUNCTIVITIS, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'CONJUNCTIVITIS';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue

        elif dislist[a] == "DIARRHEA":
            choice = input('Are you having Frequent Bowel Movements?? (Y/N): ')
            choice1 = input('Are you also experiencing Nausea?? (Y/N): ')
            if choice == 'Y' or choice1 == 'Y':
                 print(" ")
                 print("----------------------------------------------------------------------------")
                 print ("You're suffering from DIARRHEA, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'DIARRHEA';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue

        elif dislist[a] == "HEADACHE":
            choice = input('Are you experiencing migraine?? (Y/N): ')
            if choice == 'Y':
                 print(" ")
                 print("----------------------------------------------------------------------------")
                 print ("You're suffering from HEADACHE, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'HEADACHE';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue
            
            break

        elif dislist[a] == "INTESTINAL GAS":
            choice = input('Are you experiencing Flatulence (Gas in the abdomen)?? (Y/N): ')
            choice1 = input('Are you also expericing Pain in the Abdomen?? (Y/N): ')
            if choice == 'Y' or choice1 =='Y':
                 print(" ")
                 print("----------------------------------------------------------------------------------")
                 print ("You're suffering from INTESTINAL GAS, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'INTESTINAL GAS';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue
         
        elif dislist[a] == "ASTHAMA":
            choice = input('Do you feel tightness in your chest?? (Y/N): ')
            choice1 = input('Are you having cough in your throat?? (Y/N): ')
            if choice == 'Y' or choice1 == 'Y':
                 choice3 = input('Are you spitting yellow-grey mucous(cough)?? (Y/N): ')
                 if choice3 == 'Y':
                     print(" ")
                     print("----------------------------------------------------------")
                     print ("You're suffering from BRONCHITIS, Please use the medication recommended below")
                     print("")
                     mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'BRONCITIS';")
                     data1 = mycursor.fetchall() #fetching values from SQL table
                     for j in data1:
                         print(str(j[0]))
                         print("")
                         print("PRECAUTIONS -:")
                         print("1. Don't smoke")
                         print("2. Stay away from or try to reduce your time around things that irritate your airway")
                         print("3. If you catch a cold, get plenty of rest")
                         print("")
                         print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                         print("GET A X-RAY DONE")
                         print("")
                         print("--------------------------------------------------------------------------")
                         print("")
                         print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                         print("")
                         print("==========================================================================")
                     break
                 elif choice3 == 'N':
                     choice2 = input('Are you having a difficulty in breathing?? (Y/N): ')
                     if choice2 == 'Y':
                         print(" ")
                         print("----------------------------------------------------------------------------")
                         print ("You're suffering from ASTHAMA, Please use the medication recommended below ")
                         print("")
                         mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'ASTHAMA';")
                         data1 = mycursor.fetchall() #fetching values from SQL table
                         for j in data1:
                             print(str(j[0]))
                             print("")
                             print("PRECAUTIONS -:")
                             print("1. Don't smoke")
                             print("2. Stay away from or try to reduce your time around things that irritate your airway")
                             print("3. If you catch a cold, get plenty of rest")
                             print("")
                             print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                             print("GET A X-RAY DONE")
                             print("")
                             print("--------------------------------------------------------------------------")
                             print("")
                             print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                             print("")
                             print("==========================================================================")
                         break
                     elif choice2 == 'N':
                         continue
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue

        elif dislist[a] == "BRONCHITIS":
            choice = input('Are you having cough in your throat?? (Y/N): ')
            choice1 = input('Are you spitting yellow-grey mucous(cough)?? (Y/N): ')
            if choice == 'Y' and choice1 =='Y':
                 print(" ")
                 print("----------------------------------------------------------")
                 print ("You're suffering from BRONCHITIS, Please use the medication recommended below")
                 print("")
                 mycursor.execute("SELECT MEDICINE FROM MEDICINE WHERE DISEASE = 'BRONCHITIS';")
                 data1 = mycursor.fetchall() #fetching values from SQL table
                 for j in data1:
                     print(str(j[0]))
                     print("")
                     print("PRECAUTIONS -:")
                     print("1. Don't smoke")
                     print("2. Stay away from or try to reduce your time around things that irritate your airway")
                     print("3. If you catch a cold, get plenty of rest")
                     print("")
                     print("IF THE CONDITION WORSENS, CONSULT A DOCTOR")
                     print("GET A X-RAY DONE")
                     print("")
                     print("--------------------------------------------------------------------------")
                     print("")
                     print("THANK YOU FOR USING! WISH YOU A SPEEDY RECOVERY")
                     print("")
                     print("==========================================================================")
                 break
            elif choice == 'N':
                print(" ")
                print ("Please wait")
                continue

print("")                

#function for nose related symptoms
def nose():
    print ("---SYMPTOMS---")
    print("| SNEEZING    |")
    print("| RUNNY NOSE  |")
    print("| ITCHY NOSE  |") 
    print("| STUFFY NOSE |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #function call
            break

#function for eye related symptoms
def eyes():
    print ("-------- SYMPTOMS ---------")
    print("| PUFFY EYES               |") 
    print("| EYE IRRITATION           |") 
    print("| EYE INFECTION            |")
    print("| REDNESS IN EYE           |") 
    print("| ITCHING IN EYE           |")
    print("| BURNING SENSATION IN EYE |")
    print("| PUS IN EYE               |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #function call
            break

#function for throat related symptoms
def throat():
    print ("---- SYMPTOMS -----")
    print ("| INFLAMED THROAT |")
    print ("| SORE THROAT     |")
    print ("| COUGH           |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #fucntion call
            break

#function for chest related symptoms
def chest():
    print ("--------- SYMPTOMS --------")
    print ("| DIFFICULTY IN BREATHING |") 
    print ("| WHEEZING                |")
    print ("| TIGHTNESS IN CHEST      |")
    print ("| INFLAMATION IN LUNGS    |")
    print ("| YELLOW-GREY MUCOUS      |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #fucntion call
            break
#function for skin related symptoms
def skin():
    print ("--- SYMPTOMS ---")
    print ("| SKIN RASHES  |") 
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #function call
            break
    
#function for abdomen related symptoms
def abdomen():
    print ("--------- SYMPTOMS ---------")
    print ("| VOMITING                 |") 
    print ("| INDIGESTION              |") 
    print ("| EXCESSING GAS            |")
    print ("| WATERY STOOLS            |") 
    print ("| LOOSE STOOLS             |") 
    print ("| NAUSEA                   |")
    print ("| BLOATING                 |") 
    print ("| FREQUENT BOWEL MOVEMENTS |")
    print ("| PAIN IN ABDOMEN          |")
    print ("| FLATULENCE               |")
    print ("| CRAMPS IN ABDOMEN        |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #function call
            break
#function for head related symptoms
def head():
    print ("----- SYMPTOMS -----")
    print("| NAUSEA            |")
    print("| PAIN IN FOREHEAD  |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #fucntion call
            break

#function for body related symptoms
def body():
    print ("--- SYMPTOMS ---")
    print("| TINGLING      |")
    print("| FEVER         |") 
    print("| FATIGUE       |")
    print("| INTENSE PAIN  |") 
    print("| SWELLING      |")
    print("")
    symp = str(input("Enter the symptom experienced by you: "))
    print("")
    symplist.append(symp)
    while True:
        print ("Do you want to enter any other symptoms?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            symp1 = input('Enter the symptom experienced by you: ')
            symplist.append(symp1)
            print("")
            continue
        else:
            print("----------------------------------")
            othersymp() #function call
            break

#function to re-enter the problem areas
def othersymp():
    while True:
        print("")
        print ("Do you want to enter any other problematic areas?? (Y/N): ")
        choice1 = input('Enter the choice: ')
        print("")
        if choice1 == 'Y':
            print("NOSE, EYES, THROAT, CHEST, SKIN, ABDOMEN, HEAD, BODY")
            prb_area1 = input('Enter the problem area: ')
            if prb_area1 == "NOSE":
                nose() #function call
                break
            elif prb_area1 == "EYES":
                eyes() #function call
                break
            elif prb_area1 == "THROAT":
                throat() #function call
                break
            elif prb_area1 == "CHEST":
                chest() #function call
                break
            elif prb_area1 == "SKIN":
                skin() #function call
                break
            elif prb_area1 == "ABDOMEN":
                abdomen() #function call
                break
            elif prb_area1 == "HEAD":
                head() #function call
                break
            elif prb_area1 == "BODY":
                body() #function call
                break
        elif choice1 == 'N':
            diagnosis() #fucntion call
            break
        else:
            print("!! INVALID CHOICE !!")

print ("================ MyMedibuddy ================")
print("")
print ("Enter 1 to login")
print ("Enter 2 to create a new account")
print ("Enter 3 for emergency")
print("")
#asks user whether they want to login or create a new account
choice = int(input('Enter the choice: '))
print("")
while True:
    if choice == 1:
        login() #function call
        print("----------PATIENT'S INFO---------")
        mycursor.execute('SELECT NAME,PASSWORD FROM login;')
        data2 = mycursor.fetchall()
        break
        
    elif choice == 2:
        new_acc() #function call
        break

    elif choice == 3:
        info() #function call

        break


print("")        
print("----------- DIAGNOSIS -----------")
print("")
prb_list = []
print("NOSE, EYES, THROAT, CHEST, SKIN, ABDOMEN, HEAD, BODY")
prb_area = str(input('Enter the problem area: '))
print("")
if prb_area == "NOSE":
    nose() #fucntion call
elif prb_area == "EYES":
    eyes() #function call
elif prb_area == "THROAT":
    throat() #function call
elif prb_area == "CHEST":
    chest()  #function call
elif prb_area == "SKIN":
    skin() #fucntion call
elif prb_area == "ABDOMEN":
    abdomen() #fucntion call
elif prb_area == "HEAD":
    head() #fucntion call
elif prb_area == "BODY":
    body() #fucntion call

mydb.close()
