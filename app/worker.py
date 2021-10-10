import subprocess, time


# it should be {'id': 'address'}
rec_list = {'recordings': {}}

def stop_rec_by_id(id):
    global rec_list
    address = rec_list['recordings'][id]

    subprocess.run(['sh', 'app/scripts/stop_rec.sh', '{}'.format(id)])

    del rec_list['recordings'][id]

    # address of the video
    # i can't give real address - i need a web drive
    return 'https://www.youtube.com/watch?v=-mZICVd-Oek'


def start_rec_with_address(address):
    global rec_list

    command = ['sh', 'app/scripts/start_rec.sh', address, '{}'.format(time.time().__str__())]
    process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
    id = process.pid

    rec_list['recordings'][id] = address
    
    return id
