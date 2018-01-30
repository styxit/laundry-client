
class TimeConverter:

    def toSeconds(self, digits):
        # Quit when something unexpected was found.
        # In Some cases weird characters are detected which can not be parsed.
        if (len(digits) > 4):
            return None

        # See if the timer ended.
        if self.__isEndState(digits):
            return 0

        # Sum and return remaining hours and minutes as seconds.
        return self.__getHoursAsSeconds(digits) + self.__getMinutesAsSeconds(digits)

    def __isEndState(self, digits):
        # Detect end status, the Display shows "End".
        # The "n" character can not be detected by ssocr, an "a" is detected instead.
        # Look for "ead" and consider the job to be complete.
        if digits == "end" or digits == "ead":
            return True

    def __getMinutesAsSeconds(self, digits):
        # Get remaining minutes.
        # The final two characters are the remaining minutes.
        if (digits[-2] == "0"):
            # If the first minute-character is a zero, ignore it and just use the last character.
            # (string) "08" becomes (int) 8.
            minutesRemaining = int(digits[-1])
        else:
            # Join both minute-characters and convert to int.
            # (string) "12" becomes (int) 12.
            minutesRemaining = int(digits[-2] + digits[-1])

        # Minutes in seconds.
        return minutesRemaining * 60

    def __getHoursAsSeconds(self, digits):
        # The first character is the hours remaining.
        # Convert hours to seconds.
        return int(digits[0]) * 60 * 60
