from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import filedialog
from tkinter import *

#playlist_url = "https://www.youtube.com/playlist?list=PLwNv9Hhd8gZjeee8SBwokNf2JhqBvYqeB"
#start_downloading_in_video_number = start_downloading_in_video_number_field_value.get()
#total_videos_in_playlist = 99


def downloadPlaylist():
    playlist_url = playlist_url_field_value.get()                                                              #Get the Input value by User from the playlist field in UI and assign it to a variable.
    print(playlist_url)                                                                                         #Print the url obtained in console.
    start_downloading_in_video_number = start_downloading_in_video_number_field_value.get()                     #Get the Input value by User from the playlist field in UI and assign it to a variable.
    start_downloading_in_video_number_iterator = int(start_downloading_in_video_number)                         #Converts the Input Data Type from str to int.
    print("Configured to start in Video #: "+start_downloading_in_video_number)
    total_videos_in_playlist = total_videos_in_playlist_field_value.get()
    total_videos_in_playlist_iterator = int(total_videos_in_playlist)
    print("Configured total " + total_videos_in_playlist + " videos in playlist")
    #int(total_videos_in_playlist)
    
    for start_downloading_in_video_number_iterator in range(total_videos_in_playlist_iterator):
        start_downloading_in_video_number_iterator = start_downloading_in_video_number_iterator+1
        #print(start_downloading_in_video_number_iterator)
        #print(total_videos_in_playlist_iterator)
        firefox_browser = webdriver.Firefox()
        firefox_browser.get(playlist_url)
        print("Opening Playlist ")
        firefox_browser.implicitly_wait(16)
        #video_index_in_string = str(start_downloading_in_video_number)
        #start_downloading_in_video_number = start_downloading_in_video_number-2
        print("Searching video #: "+ start_downloading_in_video_number)
        start_downloading_in_video_number_iterator = str(start_downloading_in_video_number_iterator)
        firefox_browser.find_element(By.CSS_SELECTOR, "a[href*='index="+start_downloading_in_video_number_iterator+"']").click()
        print("Opening video in Playlist")
        firefox_browser.implicitly_wait(13)
        video_url = firefox_browser.current_url

        download_url = video_url[:19] + 'pp' + video_url[19:]
        firefox_browser.get(download_url)
        firefox_browser.implicitly_wait(66)
        print("Opening downloader")
        download_url = firefox_browser.current_url
        if "uto" in download_url:
            firefox_browser.implicitly_wait(33)
            firefox_browser.find_element(By.ID, "btn-start-convert").click()
            print("Converting video")
            firefox_browser.implicitly_wait(33)
            firefox_browser.find_element(By.ID, "asuccess").click()
            print("Downloading video")
        else:
            print("normal-flow")
            firefox_browser.implicitly_wait(33)
            firefox_browser.find_element(By.CLASS_NAME, "btn-success").click()
            firefox_browser.implicitly_wait(33)
            print("Preparing video to Dowwnload")
            firefox_browser.find_element(By.CLASS_NAME, "btn-file").click()
            print("Downloading video")
            
# Crear la ventana principal
window = tk.Tk()
window.title("YouTube Keeper Py")
window.geometry("633x133")
window.configure(bg="#222222")

#Entries
#playlist_url_field = Label(window, text = "Playlist url: ",)
#playlist_url_field.pack()
playlist_url_field_value = tk.Entry(window,text="Playlist url:",width=60,bg="gray")
playlist_url_field_value.pack()
start_downloading_in_video_number_field_value = tk.Entry(window,text="Video #",width=3,bg="gray")
start_downloading_in_video_number_field_value.pack()
total_videos_in_playlist_field_value = tk.Entry(window, text = "Total Videos",width=3,bg='gray')
total_videos_in_playlist_field_value.pack()

#Button
search_url_button = tk.Button(window, text="Download",command=downloadPlaylist)
search_url_button.pack()

#Value GETs from


window.mainloop()


