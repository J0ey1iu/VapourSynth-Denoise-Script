preview:
	python vapoursynth-preview/run.py denoise.py

denoise:
	vspipe -y --arg filename=noisy.MP4 denoise.py test.raw
	# ffmpeg -i pipe: -i noisy.MP4 -map 0:v:0 -map 1:a:0 -c:v libx264 -crf 23.5 output.mp4