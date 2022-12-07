#!/usr/bin/env python

def mainloop():
  found_entries = dict()
  with open('events.log', 'r') as file:
    while line := file.readline():
      event_ugly_datetime, event_ugly_text = line.split('] ', 1)
      event_text = event_ugly_text.strip()
      event_dtm = event_ugly_datetime[1:].strip().replace("  ", "")[:-3]
      if event_text == 'NOK':
        try:
          found_entries[event_dtm] = found_entries[event_dtm]+1
        except KeyError:
          found_entries[event_dtm] = 1
  
    if found_entries:
      for key in found_entries:
        print(f'{key} – {found_entries[key]}')
  

if __name__ == '__main__':
  mainloop()
