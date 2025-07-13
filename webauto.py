import webbrowser as wb

def webauto():
    fox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    URLs = ( 
        "google.com",
        "youtube.com",
        "gmail.com"
    )

    for url in URLs:
        print("Opening: " + url)
        wb.get(fox_path).open(url)

if __name__ == "__main__":
    webauto()