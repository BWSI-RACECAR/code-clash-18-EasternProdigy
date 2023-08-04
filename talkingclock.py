"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
        
        num_to_word = {
            "00": "twelve", "01": "one", "02": "two", "03": "three", "04": "four", "05": "five",
            "06": "six", "07": "seven", "08": "eight", "09": "nine", "10": "ten",
            "11": "eleven", "12": "twelve", "13": "one", "14": "two", "15": "three",
            "16": "four", "17": "five", "18": "six", "19": "seven", "20": "eight",
            "21": "nine", "22": "ten", "23": "eleven",
            "30": "thirty", "40": "forty", "50": "fifty",
        }

        hours, minutes = input_time.split(":")
        if int(hours) < 12: am_pm = "am"
        else: am_pm = "pm"

        if hours in num_to_word: hours_in_words = num_to_word[hours]
        else: hours_in_words = ""

        if minutes in num_to_word: minutes_in_words = num_to_word[minutes]
        else:
            if minutes[0] + "0" in num_to_word and minutes[1] in num_to_word:
                minutes_in_words = num_to_word[minutes[0] + "0"] + " " + num_to_word[minutes[1]]
            elif minutes[0] + "0" in num_to_word:
                minutes_in_words = num_to_word[minutes[0] + "0"]
            elif minutes[1] in num_to_word:
                minutes_in_words = "oh " + num_to_word[minutes[1]]

        return f"It's {hours_in_words} {minutes_in_words} {am_pm}"

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        