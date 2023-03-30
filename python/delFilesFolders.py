import os, shutil, datetime

fh = open("filesDeleted.txt", "a")
now = datetime.datetime.now()
fh.write(str(now))
fh.write("\n**********************************************************\n")

def delStudentFiles():
    student_profile_path = "C:\\Users\student\\"
    folders = ["Desktop", "Downloads", "Documents", "Music", "Pictures", "Videos"]

    for folder in folders:
        current_path = student_profile_path + folder    
        os.chdir(current_path)
        print(current_path)
        print("**********************")
        files = os.listdir()            
        
        for file in files:
            path = current_path + "\\" + file
            if os.path.isfile(path):
                print("It's file -", file)
                os.remove(file)
                fh.write(path)
                fh.write("\n")
            else:
                print("it's folder -", file)
                shutil.rmtree(path, ignore_errors=True, onerror=None)
                fh.write(path)
                fh.write("\n")

delStudentFiles()                

fh.close()            
    