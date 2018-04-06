import tixelbox as tb
import tixelbox.object_detection as objdet
import os

with tb.sample_video() as video:
    frames = list(range(0, video.num_frames(), 3))
    bboxes = objdet.detect_objects(video, frames)
    objdet.draw_bboxes(video, bboxes, frames, path='sample_objects.mp4')
    print('Wrote video with objects drawn to {}'.format(os.path.abspath('sample_objects.mp4')))