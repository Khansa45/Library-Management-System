class Library:
    def __init__(self):
        self.books=[]
        self.students=[]

class Student:
    def __init__(self,name,student_id,dept):
        self.name=name
        self.student_id=student_id
        self.dept=dept
        self.issued_books=[]
    def issue_book(self,book_id):
       self.issued_books.append(book_id)
    def return_book(self,book_id):
        self.issued_books.remove(book_id)
    def display(self):
        print("-----STUDENT INFO-----"
              "\nName : ",self.name,
              "\nStudent_ID : ",self.student_id,
              "\nDepartment : ",self.dept,
              "\nIssued_Books : ",self.issued_books)
        
class Book:
    def __init__(self,book_id,title,author,genre,year,quantity,available):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.genre=genre
        self.year=year
        self.quantity=quantity
        self.available=available
    def display(self):
        print("------BOOK INFO-------" 
              "\nBook id  : ",self.book_id,
              "\nTitle    : " ,self.title,
              "\nAuthor   : ",self.author,
              "\nGenre    : ",self.genre,
              "\nYear     : ",self.year,
              "\nTotal Quantity     : ",self.quantity,
              "\nAvailable Quantity : ",self.available)
    def is_available(self):
        return self.available>=1 


class Admin:
    def __init__(self,Library):
        self.name="Admin"
        self.password="A1234"
        self.library=Library
    def login(self,name,password):
        if name=="Admin" and password=="A1234":
           return True
        else:
           return False
    def add_book(self):
        bk_id=int(input("Enter book ID : "))
        bk_title=input("Enter book Title : ")
        bk_author=input("Enter book author : ")
        bk_genre=input("Enter book genre : ")
        bk_year=int(input("Enter year of Publication : "))
        bk_quantity=int(input("Enter total Quantity : "))
        bk_available= bk_quantity
        book=Book(bk_id,bk_title,bk_author,bk_genre,bk_year,bk_quantity,bk_available)
        self.library.books.append(book)
        print("Book added successfully.")
    def remove_book(self):
        bookToRemove=int(input("Enter book ID to remove : "))
        for bk in self.library.books:
            if(bookToRemove==bk.book_id):
              self.library.books.remove(bk)
              print("Book removed successfully.")
              return 
        else:
            print("This book doesn't exist")
    def search_book(self):
        bk_title=input("Enter book title : ")
        for book in self.library.books:
          if(book.title==bk_title):
           print("Book is available,Here are details")
           book.display()
           return True
        else:
           print("Book not found")
           return False
    def issued_books(self):
        student_found = False
        std_id=int(input("Enter student ID : "))
        for std in self.library.students:
            if std.student_id==std_id:
              student_found = True
              bk_id=int(input("Enter book id : "))
              for bk in self.library.books:
               if bk.is_available() and bk.book_id==bk_id:
                std.issue_book(bk.book_id)
                print("Book issued sucessfully")
                bk.available-=1
                return 
        else:
            if student_found == False:
               print("Student is not found")
            else:
               print("Book is not available")
            return 
    def return_book(self):
        student_found = False
        std_id=int(input("Enter student ID : "))
        for std in self.library.students:
            if std.student_id==std_id:
              student_found = True
              bk_id=int(input("Enter book id : "))
              for bk in self.library.books:
               if bk.book_id==bk_id:
                 if bk_id in std.issued_books:
                  std.return_book(bk.book_id)
                  print("Book returned sucessfully")
                  bk.available+=1
                  return 
                 else:
                    print("Student doesnot borrow this book")
                    return
        else:
             if student_found == False:
               print("Student is not found")
             else:
               print("Book is not available")
             return 
    def add_student(self):
        std_id=int(input("Enter Student ID : "))
        std_name=input("Enter Student Name : ")
        std_dept=input("Enter Student Department : ")
        newStudent=Student(std_name,std_id,std_dept)
        for std in self.library.students:
           if std.student_id ==std_id:
              print("Student already exist")
              return 
        else:
              self.library.students.append(newStudent)
              print("Student added successfully")
              return
    def remove_student(self):
        std_id=int(input("Enter Student ID : "))
        for std in self.library.students:
           if std.student_id ==std_id:
            self.library.students.remove(std)
            print("Student removed successfully")
            return
        else:
            print("Student not found")
            return
    
    def display_all(self):
        if not self.library.books:
         print("No books available in the library.")
         return
        for book in self.library.books:
          book.display()
    
def main():
   while(True):
    print("===== WELCOME TO LIBRARY MANAGEMENT SYSTEM =====")
    try:
     ch=int(input("1-Admin Login\n2-Student Login\n3-Exit\nEnter your choice : "))
    except ValueError:
       print("Please enter a number")
       continue
    match ch:
     case 1:
      admin_dashboard()
     case 2:
      student_dashboard()
     case 3:
       print('Exit sucessfully')
       return
     case _:
       print("Invalid")

def admin_dashboard():
    ad_id=input("Enter admin name : ")
    ad_pass=input("Enter Admin password : ")
    if admin.login(ad_id,ad_pass):
       print("---Welcome to Admin dashboard---")
       while(True):
         print("""What you want to do?
               1-Add book
               2-Remove book
               3-Search book
               4-Issued Books
               5-Returned Books
               6-Add Student
               7-Remove Student
               8-Display all books
               9-Logout""") 
         try:
          ch_A=int(input("Enter your choice : "))
         except ValueError:
            print("Invalid choice")
            continue
         if ch_A==1:
             admin.add_book()
         elif ch_A==2:
             admin.remove_book()
         elif ch_A==3:
             admin.search_book()
         elif ch_A==4:
             admin.issued_books()
         elif ch_A==5:
             admin.return_book()
         elif ch_A==6:
             admin.add_student()
         elif ch_A==7:
             admin.remove_student()
         elif ch_A==8:
             admin.display_all()
         elif ch_A==9:
             return
         else:
            print("Invalid choice")
    else:
       print("Invalid id or password")
       return              
        

def student_dashboard():
     student_found=False
     st_id=int(input("Enter student id : "))
     for st in library.students:
           if st.student_id ==st_id:
               student=st
               student_found=True
               print("---Welcome to Student dashboard---")
               while(True):
                  print("What you want to do?\n1-Issue book\n2-Return book\n3-Display books\n4-Logout")
                  try:
                   ch_S=int(input("Enter your choice : "))
                  except ValueError:
                     print("Please enter a number")
                     continue
                  if ch_S == 1:
                    bktoIssue = int(input("Enter book ID you want to issue: "))
                    book_found = False
                    for bk in library.books: 
                     if bk.book_id == bktoIssue:
                      book_found = True
                      if bk.is_available():
                       student.issue_book(bk.book_id)
                       bk.available -= 1
                       print("Book issued successfully")
                      else:
                       print("Book is not available")
                      break
                    if not book_found: 
                      print("Book not found")
                  elif ch_S==2:
                   bktoReturn=int(input("Enter book ID to return : "))
                   student.return_book(bktoReturn)
                  elif ch_S==3:
                   admin.display_all();
                  elif ch_S==4:
                    break
                  else:
                    print("Invalid choice")
               break
     if student_found==False:
        print("Student not found")
        return   
library=Library()
admin=Admin(library)
main()
