import threading
import tkinter as tk
from tkinter import ttk
import subprocess

print("Hello")

# Create a dialog with a progress bar and an ok button
# The progress bar will be updated by the worker thread
# The ok button will be disabled while the worker thread is running
# The dialog will close when the worker thread is done
# The dialog will be created in the main thread
# The worker thread will be created in the main thread
# The worker thread will be started in the main thread
# The worker thread will be joined in the main thread
# The dialog will be closed in the main thread

def pipe_to_server():
    def worker():
        process = subprocess.Popen(['server'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            while True:
                # Simulate sending data to the server
                process.stdin.write("10\n")
                process.stdin.flush()
                
                # Read the response from the server
                response = process.stdout.readline()
                if response.strip().isdigit():
                    progress_value = int(response.strip())
                    progress['value'] = progress_value
                    root.update_idletasks()
                if response:
                    print(f"Server response: {response.strip()}")
                else:
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            process.stdin.close()
            process.stdout.close()
            process.stderr.close()
            process.wait()

    thread = threading.Thread(target=worker)
    thread.start()
    return thread

# Start the worker thread
pipe_to_server()

def advance_progress():
    progress.step(10)

root = tk.Tk()
root.title("Progress Dialog")
root.geometry("300x150")
root.resizable(False, False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = ttk.Frame(root, padding=60)
frame.grid(row=0, column=0, sticky="nsew")

progress = ttk.Progressbar(frame, orient="horizontal", mode="determinate", length=200)
progress.grid(row=0, column=0, pady=10)

ok_button = ttk.Button(frame, text="OK", state="enabled")
ok_button.grid(row=1, column=0, pady=10)
ok_button.config(command=advance_progress)

root.mainloop()



