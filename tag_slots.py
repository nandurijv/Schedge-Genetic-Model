import json
import math

file = open('tag_slots.py')
data2 = json.loads(file)

def add_slots(data, data2):
    
    slot_dur = int(data["slot_dur"])
    start = int(data["interval_start"])

    tags = data2
    
    for i in range(len(tags)):
        tags[i]["slots"] = [math.ceil(j/slot_dur) for j in range(int(tags[i]['start_time'])-start, int(tags[i]['end_time'])-start,slot_dur)]
    return tags