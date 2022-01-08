# laat kalender zien van gegeven jaar en maand

# importeren van calender module
import calendar

jj = int(input("Enter jaar: "))
mm = int(input("Enter maand: "))

# laat de kalender zien
print(calendar.month(jj, mm))
