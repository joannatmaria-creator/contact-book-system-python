class contacts():
    def __init__(self):
        self.file="contac.txt"
    def add_contact(self):
        contact_id=input("enter contact id:")
        contact_name=input("enter contact name:")
        ph_no=input("enter phone number:")
        try:
            with open (self.file,"r") as f:
                contacts=f.readlines()
        except:
            contacts=[]
        for contact in contacts:
            if contact.strip()=="":
                continue
            i,n,p=contact.strip().split(",")
            if p==ph_no:
                print("PHONE NIUMBER ALREADY EXIST")
                return
        with open(self.file,"a") as f:
            f.write(contact_id+","+contact_name+","+ph_no+"\n")
        print("CONTACT ADDED")
    def view_contact(self):
        with open (self.file,"r") as f:
            contacts=f.readlines()
        if not contacts:
            print("NO CONTACT FOUND")
            return
        print("CONTACT LIST")
        for contact in contacts:
            if contact.strip()=="":
                continue
            i,n,p=contact.strip().split(",")
            print("\ncontact id:",i,
                  "\ncontact name:",n,
                  "\nphone number:" ,p,"\n")
    def search_contact(self):
        contact_id=input("enter contact id:")
        with open (self.file,"r") as f:
            contacts=f.readlines()
        found=False
        for contact in contacts:
            if contact.strip()=="":
                continue
            i,n,p=contact.strip().split(",")
            if i==contact_id:
                print("\ncontact id:",i,
                  "\ncontact name:",n,
                  "\nphone number:",p,"\n")
                found=True
        if not found:
            print("INVALID CONTACT ID")
    def update_contact(self):
        contact_id=input("enter contact id:")
        new_num=input("enter number:")
        with open (self.file,"r") as f:
            contacts=f.readlines()
        update=[]
        found=False
        for contact in contacts:
            if contact.strip()=="":
                continue
            i,n,p=contact.strip().split(",")
            if i==contact_id:
                update.append(str(i)+","+n+","+str(new_num)+"\n")
                found=True

            else:
                update.append(contact)
        with open (self.file,"w") as f:
            f.writelines(update)
        if found:
            print("CONTACT UPDATED")
        else:
            print("INVALID CONTACT ID :(")
    def delete_contact(self):
        contact_id=input("enter contact id:")
        with open(self.file,"r") as f:
            contacts=f.readlines()
        delete=[]
        found=False
        for contact in contacts:
            if contact.strip()=="":
                continue
            i,n,p=contact.strip().split(",")
            if i==contact_id:
                found=True
            else:
                delete.append(contact)
        with open(self.file,"w") as f:
            f.writelines(delete)
        if found:
            print("CONTACT DELETED")
        else:
            print("INVALID CONTACT ID")
system=contacts()
while True:
    print("\nCONTACT BOOK SYSTEM")
    print("1.add contact")
    print("2.view contact")
    print("3.search contact")
    print("4.update contact number")
    print("5.delete contact")
    print("6.EXIT")
    choice=int(input("enter your choice:"))
    if choice==1:
        system.add_contact()
    elif choice==2:
        system.view_contact()
    elif choice==3:
        system.search_contact()
    elif choice==4:
        system.update_contact()
    elif choice==5:
        system.delete_contact()
    elif choice==6:
        print("--------------------EXITING CONTACT BOOK SYSTEM---------")
        break
    else:
        print("INVALID CHOICE")
        
            
                
        
                
            
        
        
