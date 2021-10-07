import subprocess, signal, os, time, sys


command = 'gst-launch-1.0 -ev rtspsrc location=rtsp://172.18.191.95:554/Streaming/Channels/1 ! queue ! rtph264depay ! h264parse ! matroskamux ! filesink location=aboba.mkv'

process = subprocess.Popen(args=command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

input('proc is working')

#print(process.pid)
process.send_signal(signal.CTRL_C_EVENT)
process.communicate()#'^C\n'.encode('utf-8'))
input('proc has been terminated')
#os.send_signal(signal.CTRL_BREAK_EVENT)
#os.kill(process.pid, signal.CTRL_BREAK_EVENT)
#input()