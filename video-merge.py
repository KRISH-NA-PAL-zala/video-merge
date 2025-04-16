import moviepy
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def open_file_dialog():
    file_paths = filedialog.askopenfilenames(title="Select video files", filetypes=[("MP4 files", "*.mp4")])
    for file_path in file_paths:
        listbox.insert(tk.END, file_path)


def remove_selected_files():
    selected_indices = listbox.curselection()
    listbox.delete(*selected_indices)


def merge_videos():
    file_paths = listbox.get(0, tk.END)

    video_clips = [moviepy.VideoFileClip(video_file) for video_file in file_paths]
    final_video = moviepy.concatenate_videoclips(video_clips)
    final_video.write_videofile("merged_video.mp4", codec="libx264")

    messagebox.showinfo("Success", "Videos merged successfully!")


root = tk.Tk()
root.title("Video Merger")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=80)
listbox.pack(pady=10)

open_button = tk.Button(root, text="Add Videos", command=open_file_dialog)
open_button.pack(pady=5)
remove_button = tk.Button(root, text="Remove Selected", command=remove_selected_files)
remove_button.pack(pady=5)
merge_button = tk.Button(root, text="Merge Videos", command=merge_videos)
merge_button.pack(pady=5)

root.mainloop()
