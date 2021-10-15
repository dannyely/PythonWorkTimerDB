#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dely
"""
from datetime import datetime
import time
import PyDB
from pydub import AudioSegment
from pydub.playback import play


def timer_exec():
    timerData = {}
    # Adjust time in minutes here
    timeAmount = 0
    
    #Giving an input begins the timer
    nullIgnore = input('Press enter to begin {} \n'.format(timeAmount))
    
    #Timer is running, it will print out each second that passes for reference
    startTime = datetime.now()
    while True:
        currentTime = datetime.now()
        duration = currentTime - startTime
        time.sleep(1)
        print('Time elapsed:', duration.seconds//60, ':', duration.seconds%60)
        if duration.seconds >= timeAmount*60:
            break
        
        
    #Timer has ended, alarm has played
    endTime = datetime.now().strftime('%H:%M')
    #Select an mp3 alarm, and adjust its volume
    #Change the mp3 path
    song = AudioSegment.from_file(file = '/path/to/mp3/file', fromat = 'mp3')
    song -= 12
    play(song)
    
    #Enter input to save this record, or 'q' to discard it
    comments = input('Comments: or press any key to continue, enter q to discount \n MOVE AROUND \n')
    if comments != 'q':
        #If user accepts the record, put together all of the record's metadata
        timerData['Date'] = startTime.strftime('%b-%d-%Y')
        timerData['startTime'] = startTime.strftime('%H:%M')
        timerData['endTime'] = endTime
        if len(comments) > 1:
            timerData['comments'] = comments
        else:
            timerData['comments'] = ''

        print(timerData)
        return timerData['Date'], timerData['startTime'], timerData['endTime'], timerData['comments']


if __name__ == "__main__":
    #Creates the table if it needs to (the first iteration)
    PyDB.create_table()
    
    #If no data was returned, then the insert_data() will fail and nothing happens
    try:
        PyDB.insert_data(timer_exec())
    except:
        print('NO DATA RECORDED')