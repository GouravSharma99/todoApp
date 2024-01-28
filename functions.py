File_Path = "todos.txt"

def get_todos(filepath=File_Path):
    
    """Take a file and return list of to-do items"""
    
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
            return todos_local
        
        
def write_todos(todo_arg, filepath=File_Path):
    
    """Write the to-do items list in file"""
    
    with open(filepath, 'w') as todo_file:
        todo_file.writelines(todo_arg)
        
    
print("hello")
if __name__ == "__main__":
    demo = "lololol"
    print("Jai ho")
