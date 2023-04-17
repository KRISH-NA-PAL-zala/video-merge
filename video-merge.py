import moviepy.editor as mp

video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]

video_clips = [mp.VideoFileClip(video_file) for video_file in video_files]

final_video = mp.concatenate_videoclips(video_clips)

final_video.write_videofile("merged_video.mp4", codec="libx264")
