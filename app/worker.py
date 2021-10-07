import subprocess, signal, time, os, psutil


# it should be {'id': 'address'}
rec_list = {'recordings': {}}
#last_id = 0

def stop_rec_by_id(id):
    global spisochek
    address = rec_list['recordings'][id]

    #process.send_signal(signal.CTRL_BREAK_EVENT)
    #os.kill(id, signal.CTRL_BREAK_EVENT)
    process = psutil.Process(id)
    process.send_signal(signal.SIGINT)

    del rec_list['recordings'][id]

    # address of the video
    # i can't give real address - i need a web drive
    return 'https://www.youtube.com/watch?v=-mZICVd-Oek'


def start_rec_with_address(address):
    global rec_list#, last_id

    command = 'gst-launch-1.0 -ev  rtspsrc location={location} ! queue ! rtph264depay ! h264parse ! matroskamux ! filesink location=recordings/rec_{time_since_epoch}.mkv'.format(location=address, time_since_epoch=time.time_ns())
    process = subprocess.Popen(args=command, stdout=subprocess.PIPE, shell=True)
    id = process.pid

    #last_id += 1
    rec_list['recordings'][id] = address
    
    return id
