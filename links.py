import webbrowser

#teste

links = [
    "https://get.adobe.com/br/reader/",
    "https://www.ccleaner.com/defraggler/download",
    "https://www.ccleaner.com/pt-br/ccleaner/download",
    "https://www.google.com/intl/pt-BR/chrome/",
    "https://www.nvidia.com/Download/index.aspx",
    "https://www.videolan.org/vlc/index.pt-BR.html",
    "https://www.win-rar.com/predownload.html?&L=9",
    "https://www.qbittorrent.org/download.php",
    "https://code.visualstudio.com/",
    "https://www.python.org/downloads/release/python-380/",
    "https://www.oo-software.com/en/ooappbuster"
    ]

for link in links:
    webbrowser.open(link)
