# it should be {'id': 'address'}
rec_list = {'recordings': {}}
last_id = 0

def stop_rec_by_id(id):
    global spisochek
    # blablabla
    # work...
    address = rec_list['recordings'][id]
    del rec_list['recordings'][id]

    # address of the video
    return 'https://www.youtube.com/watch?v=-mZICVd-Oek'


def start_rec_with_address(address):
    global rec_list, last_id
    # blablabla
    # work...
    last_id += 1
    rec_list['recordings'][last_id] = address
    
    return last_id
