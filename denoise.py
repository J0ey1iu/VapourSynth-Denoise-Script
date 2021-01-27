import vapoursynth as vs

core = vs.core

video = core.ffms2.Source(filename)
orig = video
core.std.LoadPlugin("./vapoursynth-mvtools/build/libmvtools.dylib")

blksize = 32
if preset == "low":
    blksize = 16
elif preset == "medium":
    blksize = 32
elif preset == "high":
    blksize = 64
elif preset == "extreme":
    blksize = 128

video = core.std.AddBorders(video, blksize/2, blksize/2, blksize/2, blksize/2)
sup = core.mv.Super(video, pel=2, sharp=1)
backward_vec1 = core.mv.Analyse(sup, isb = True, delta = 1, overlap=blksize/4, blksize=blksize)
forward_vec1 = core.mv.Analyse(sup, isb = False, delta = 1, overlap=blksize/4, blksize=blksize)
backward_vec2 = core.mv.Analyse(sup, isb = True, delta = 2, overlap=blksize/4, blksize=blksize)
forward_vec2 = core.mv.Analyse(sup, isb = False, delta = 2, overlap=blksize/4, blksize=blksize)
backward_vec3 = core.mv.Analyse(sup, isb = True, delta = 3, overlap=blksize/4, blksize=blksize)
forward_vec3 = core.mv.Analyse(sup, isb = False, delta = 3, overlap=blksize/4, blksize=blksize)
video = core.mv.Degrain3(video,sup,backward_vec1,forward_vec1,backward_vec2,forward_vec2,backward_vec3,forward_vec3,thsad=400)
video = core.std.Crop(video, blksize/2, blksize/2, blksize/2, blksize/2)

# fnl = core.std.StackVertical([orig, video])
# fnl.set_output()

video.set_output()