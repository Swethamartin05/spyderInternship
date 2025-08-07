class student:
    def __init__(self,name,roll_no,marks):
        self.n= name
        self.r= roll_no
        self.m= marks

    def display_info(self):
        print(f"name:{self.n} roll_no:{self.r} marks:{self.m}")

s=student("Nilav",24,98)
s.display_info() 
