import os

for i in range(1, 61):
    current_folder_path = "Ghibli/validation/" + str(i)
    new_folder_path = "Ghibli/validation/" + str(i+140)

    try:
        os.rename(current_folder_path, new_folder_path)
        print(f"Folder renamed from '{current_folder_path}' to '{new_folder_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: The source folder '{current_folder_path}' was not found.")
    except FileExistsError:
        print(f"Error: The destination folder '{new_folder_path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")