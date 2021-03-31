import os, json
import collections
from collections import defaultdict
import math


# Meeting scheduler

# Calendar application
# Functionalities:
# Scheduler
# - Book a room with a set of ppl -> Meeting object
# - notify ppl for that meeting
# - give the list of rooms available for that time.


class Meeting:
    def __init__(self, room_id, invitees, start_time, end_time):
        self.room_id = room_id
        self.invitees = invitees
        self.start_time = start_time
        self.end_time = end_time


class User:
    def __init__(self, name):
        self.name = name

    def notify(self, start, end, meeting_room):
        print(f"Hello {self.name} You have a meeting scheduled at {meeting_room} from {start} to {end}")


# time as just numbers
# 5 meeting rooms
class Scheduler:
    def __init__(self):
        # mapping between a meeting room object and the start_end and end_time
        # 1 -> [1, 3]
        self.meeting_rooms = {rid: [] for rid in (1, 2, 3, 4, 5)}

    def book(self, start_time, end_time, meeting_room, invitees):
        if self.is_room_available(start_time, end_time, meeting_room):
            m = Meeting(meeting_room, invitees, start_time, end_time)
            self.meeting_rooms[meeting_room].append(m)
            self.notify(m)
        else:
            print('Room not available')

    def is_room_available(self, start_time, end_time, meeting_room):
        overlapping = False
        meetings = self.meeting_rooms[meeting_room]
        for meeting in meetings:
            start = meeting.start_time
            end = meeting.end_time

            max_start = max(start, start_time)
            min_end = min(end, end_time)
            if max_start < min_end:
                overlapping = True
                break
        return not overlapping

    # gives a list of available meeting rooms
    def check(self, start_time, end_time):
        output = []
        for mr_id, meetings in self.meeting_rooms.items():
            if self.is_room_available(start_time, end_time, mr_id):
                output.append(mr_id)

        return output

    def notify(self, meeting):
        for invitee in meeting.invitees:
            invitee.notify(meeting.start_time, meeting.end_time, meeting.room_id)


def main():
    u1 = User("Deepu")
    u2 = User("Doofu")
    u3 = User("Noob")
    u4 = User("Tourist")
    u5 = User("Lboard")

    s = Scheduler()
    print(s.check(1, 3))
    s.book(1, 4, 1, [u1, u2])
    s.book(2, 3, 1, [u1, u3])
    print(s.check(1, 5))
    s.book(14, 18, 2, [u3, u4, u1, u5])
    print(s.check(2, 15))


if __name__ == "__main__":
    main()
