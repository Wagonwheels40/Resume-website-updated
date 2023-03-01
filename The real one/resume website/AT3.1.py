import json # Imported to enable json file to work.
filename = "patients_1111.json"
 
__author__ = 'Daniel Wagner'
__version__ = 'Python 3'
__date__ = '25/11/22'

def Choices():
   print("S I T")
   print("Patient Management Portal")
   print("(1) View Patient")
   print("(2) Add Patient")
   print("(3) Delete Patient")
   print("(4) Exit")
 
def view_patient():
   '''Function used to list details of all clients at SIT.  All of them come from the patient_1111.json file'''
   with open (filename, "r") as f:
       temp = json.load(f)
       i = 0
       for entry in temp:
           print(entry)
           i=i+1
 
def add_patient():
   patient_data = {}
   with open (filename, "r") as f:
       temp = json.load(f)
   patient_data = input("Name of patient: ")
   temp.append(patient_data)
   with open (filename, "w") as f:
       json.dump(temp, f, indent=4)  
 
def delete_patient():
   '''Function used to delete a clients' details SIT. '''
   view_patient()
   new_patient = []
   with open (filename, "r") as f:
       temp = json.load(f)
       data_length = len(temp)-1
   print ("Which index number would you like to delete?")
   delete_option = input(f"Select a number 0-{data_length}")
   i=0
   for entry in sorted(temp):
       if i == int(delete_option):
           pass
           i=i+1
       else:
           new_patient.append(entry)
           i=i+1
   with open (filename, "w") as f:
       json.dump(new_patient, f, indent=4)
 
while True:
   Choices()
   choice = input("\nEnter Number: ")
   if choice == "1":
       view_patient()
   elif choice == "2":
       add_patient()
   elif choice == "3":
       delete_patient()
   elif choice == "4":
       break
   else:
       print ("You need to select a number")
