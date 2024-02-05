#some variables
EXIT = "no"
User = "LeeMan12"
Pass = "MrMan@1"

#inputs for logging in
username = input("input username: ")
password = input("input password: ")

#checking if username/password matches
if username == User:

    if password == Pass:
        #loops program
        while EXIT.lower() != "yes":

            #gets input for what user wants to do and opens the file
            option = input("do you want to: input, read, or log out? ")
            file = open("tutorInfo.txt","r")

            #if the user wants to add a new student
            if option.lower() == "input":
                #takes the number of lines in the file (number of students)
                StudentNum = len(file.readlines())
                #if the number of students is 25 or greater, doesnt allow any more to be added
                if (StudentNum - 2) > 25:
                    print("maximun number of students in tutor reached")
                    EXIT = input("do you want to exit: yes or no? ")
                    print("\n")

                else:
                    file.close()
                    #opens file in append mode and creates an empty list
                    file = open("tutorInfo.txt","a")
                    StudentInf = []

                    #inputs for student data
                    ForeName = input("input student forename: ")
                    SurName = input("input student surname: ")
                    DoB = input("input student date of birth (dd/mm/yyyy format): ")
                    Gender = input("input student gender: ")
                    ID = input("input student ID number: ")
                    Address = input("input student address: ")
                    Phone = input("input student phone number: ")

                    #validity checks for student data
                    if ForeName.isalpha() == True:
                        if SurName.isalpha() == True:
                            if DoB.isalpha() == False:
                                if Gender.isalpha() == True:
                                    if ID.isdigit() == True:
                                        if Phone.isdigit() == True:

                                            #concatenats descriptors onto the student data and appends them to the list
                                            StudentInf.append("Forename: " +ForeName)
                                            StudentInf.append("Surname: " +SurName)
                                            StudentInf.append("Date of birth: " +DoB)
                                            StudentInf.append("Gender: " +Gender)
                                            StudentInf.append(" Student ID: " +ID)
                                            StudentInf.append("Address: " +Address)
                                            StudentInf.append("Phone number: " +Phone + "\n")

                                            #appends the list to the file and closes it
                                            x = 0
                                            for i in range(len(StudentInf)):
                                                file.write(StudentInf[x])
                                                file.write(' ')
                                                x += 1

                                            file.close()




                    #messages for invalid data types
                                        else:
                                            print("phone number is not only numbers, invalid")
                                            EXIT = input("do you want to exit: yes or no? ")
                                            print("\n")


                                    else:
                                        print("ID number is not only numbers, invalid")
                                        EXIT = input("do you want to exit: yes or no? ")
                                        print("\n")


                                else:
                                    print("gender contains numbers or symbols, invalid")
                                    EXIT = input("do you want to exit: yes or no? ")
                                    print("\n")


                            else:
                                print("date of birth contains letters, invalid")
                                EXIT = input("do you want to exit: yes or no? ")
                                print("\n")

                        else:
                            print("surname contains numbers or symbols, invalid")
                            EXIT = input("do you want to exit: yes or no? ")
                            print("\n")

                    else:
                        print("forename contains numbers or symbols, invalid")
                        EXIT = input("do you want to exit: yes or no? ")
                        print("\n")




            #if the user wants to read the student data stored in the file
            elif option.lower() == "read":
                #opens the file in read mode and prints each line to the screen
                file = open("tutorInfo.txt","r")
                LINE = file.readlines()
                Line = 0
                for line in LINE:
                   Line += 1
                   print(line)

                #closes the file and asks the user if they want to exit
                file.close()
                EXIT = input("do you want to exit: yes or no? ")
                print("\n")

            #if the user wants to log out (end the program)
            elif option.lower() == "log out":
                #closes the file and kills the program
                file.close()
                quit()

#error messages for inccorect inputs
            else:
                print("chosen option does not exist")

    else:
        print("incorrect username or password")

else:
    print("incorrect username or password")
