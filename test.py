import Overlay,time

a = Overlay.Overlay()
a.labeler("TEST",300,300)
a.win.after(1000,a.stop)
a.start()
