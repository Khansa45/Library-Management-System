
class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"Your name is {self.name} and your ID is {self.id}")
    
class Student(Person):
    def __init__(self,id,name,password):
         super().__init__(id, name)      # Initialize id and name from Person
         self.password = password
         self.borrowed_books = []  
    

    def borrow_book(self,book):
        self.borrowed_books.append(book)

    def return_book(self,book):
        if book in self.borrowed_books:
          self.borrowed_books.remove(book)
          print("Book returned successfully.")
        else:
            print("You didn't borrow this book.")

    def login(self):
       enter_id=input("Enter your Id : ")
       enter_psword = input("Enter your password: ")
       if(enter_id==self.id and enter_psword==self.password):
           print("Login sucessfull")
           return True
       else:
           print("Login not sucessfull")
           return False    

class Book:
    def __init__(self,book_id,title,author,copies):
        self.title=title
        self.book_id=book_id
        self.author=author
        self.copies=copies

    def display(self):
        print("---------------------------")
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Copies  : {self.copies}")

    def is_available(self):
          return self.copies>=1
           
class Library:
    def __init__(self):
      self.books=[]
      self.students=[]

    def add_book(self, book):
     self.books.append(book)
     print("Book added successfully")

    def remove_book(self,book_id):
     book = self.search_book(book_id)
     if book:
        self.books.remove(book)
        print("Book removed successfully.")
     else:
        print("Book not found.")

    def search_book(self,book_id):
        for book in self.books:
            if(book.book_id==book_id):
              return book
        return None

    def display_books(self):
     for book in self.books:
        book.display()

    def add_student(self, student):
      self.students.append(student)
      print("Student added successfully.")

    def search_student(self, student_id):
      for student in self.students:
         if student.id == student_id:
             return student
      return None

    def issue_book(self, student_id, book_id):
     student = self.search_student(student_id)
     book = self.search_book(book_id)
     if student and book:
        if book.is_available():
            student.borrow_book(book)
            book.copies -= 1
            print("Book issued successfully.")
        else:
            print("Book is not available.")
     else:
        print("Invalid Student ID or Book ID.")
    

    def return_book(self, student_id, book_id):
      student = self.search_student(student_id)
      book = self.search_book(book_id)
      if student and book:
          if book in student.borrowed_books:
           student.return_book(book)
           book.copies += 1
           print("Book returned successfully.")
          else:
           print("Student never borrowed this book.")
        

class Admin(Person):
     def __init__(self,id,name,password):
         super().__init__(id,name)
         self.password=password
       
     def Login(self):
        enter_id=input("Enter admin id: ")
        enter_pass=input("Enter admin password :")
        if(enter_id == self.id and enter_pass==self.password):
           print("Admin Login sucessful")
           return True
        else:
            print("Invalid Admin ID or Password")
            return False
        
     def add_Book(self,library,book):
         library.add_book(book)
         print("Book added successfully")

     def remove_Book(self,library,book_id):
        library.remove_book(book_id)
                 


library = Library()
admin = Admin("A101", "Khansa", "admin123")
student1 = Student("S101", "Ali", "1234")
book1 = Book("B101", "Python", "Eric", 5)
book2 = Book("B102", "C++", "Bjarne", 3)
library.add_book(book1)
library.add_book(book2)
library.add_student(student1)

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        if admin.Login():

            while True:

                print("\n===== ADMIN MENU =====")
                print("1. Add Book")
                print("2. Remove Book")
                print("3. Display Books")
                print("4. Search Book")
                print("5. Logout")

                admin_choice = int(input("Enter choice: "))
                if admin_choice == 1:
                   bk_id=input('Enter book id:')
                   bk_title=input('Enter book title:')
                   bk_author=input('Enter book author:')
                   book1 = Book(bk_id, bk_title, bk_author,1)
                   library.add_book(book1)

                elif admin_choice == 2:
                   bk_id=input('Enter book id to remove:')
                   library.remove_book(bk_id)

                elif admin_choice == 3:
                   library.display_books()

                elif admin_choice == 4:
                   bk_id = input("Enter book id to search: ")
                   book = library.search_book(bk_id)
                   if book:
                     book.display()
                   else:
                    print("Book not found.")

                elif admin_choice == 5:
                    break

    elif choice == 2:

        if student1.login():

            while True:

                print("\n===== STUDENT MENU =====")
                print("1. Display Books")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Logout")

                student_choice = int(input("Enter choice: "))

                if student_choice == 1:
                    library.display_books()

                elif student_choice == 2:
                   bk_id = input("Enter Book ID: ")
                   library.issue_book(student1.id, bk_id)

                elif student_choice == 3:
                    st_id=input('Enter your id:')
                    bk_id=input('Enter book id:')
                    library.return_book(st_id,bk_id)

                elif student_choice == 4:
                    break

    elif choice == 3:
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid Choice")
