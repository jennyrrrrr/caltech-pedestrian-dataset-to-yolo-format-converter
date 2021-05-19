# adapted from https://github.com/mitmul/caltech-pedestrian-dataset-converter/blob/master/scripts/convert_seqs.py

import os
import glob
import cv2 as cv


def save_img(dname, fn, i, frame):
	cv.imwrite('{}/{}_{}_{}.png'.format(
		out_dir, os.path.basename(dname),
		os.path.basename(fn).split('.')[0], i), frame)

out_dir = 'images'
if not os.path.exists(out_dir):
	os.makedirs(out_dir)

def convert(dir):
	# print(os.getcwd())
	for dname in sorted(glob.glob(dir)):
		for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
			cap = cv.VideoCapture(fn)
			# # i = 0
			# count = 0
			# while True:
			# 	ret, frame = cap.read()
			# 	if not ret:
			# 		break
			# 	else :
			# 		save_img(dname, fn, i, frame)
			# 	# i += 1
			count = 0
			while cap.isOpened():
				ret, frame = cap.read()

				if ret:
					frameId = cap.get(count)
					save_img(dname, fn, frameId, frame)
					count += 500
				else:
					cap.release()
					break
			print(fn)


convert('../caltech/train*')
convert('../caltech/test*')