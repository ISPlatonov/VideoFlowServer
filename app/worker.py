# it should be {'id': 'address'}
spisochek = {'recordings': {}}
last_id = 0

def stop_rec_by_id(id):
    global spisochek
    # blablabla
    # work...
    address = spisochek['recordings'][id]
    del spisochek['recordings'][id]

    # address of the video
    return 'https://www.youtube.com/watch?v=-mZICVd-Oek'


def start_rec_with_address(address):
    global spisochek, last_id
    # blablabla
    # work...
    last_id += 1
    spisochek['recordings'][last_id] = address
    
    return last_id
