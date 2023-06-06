import moviepy.editor

video = moviepy.editor.VideoFileClip('NGGYU.mp4')
audio = video.audio
audio.write_audiofile("NGGYU.mp3")

























