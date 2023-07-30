import os
import webbrowser

def open_html_file(file_path):
    try:
        # Get the absolute path of the file
        abs_file_path = os.path.abspath(file_path)

        # Open the file in the default web browser
        webbrowser.open("file://" + abs_file_path, new=2, autoraise=True)
    except Exception as e:
        print("Error opening the file:", e)

if __name__ == "__main__":
    # Replace "index.html" with the path to your HTML file
    html_file_path = "D:\Enigma Quest\index.html"

    open_html_file(html_file_path)
