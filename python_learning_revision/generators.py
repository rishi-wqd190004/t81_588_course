guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    new_guest = (yield name)
    if new_guest:
      n_name, n_age = new_guest.split(',')
      guests[n_name.strip()] = int(n_age.strip())
      yield n_name.strip()

def table_1():
  for i in range(1,6):
    yield (f"Chicken", "Table X", f"Seat {i}")

def table_2():
  for i in range(1,6):
    yield (f"Beef", "Table Y", f"Seat {i}")

def table_3():
  for i in range(1,6):
    yield (f"Fish", "Table Z", f"Seat {i}")

def combined_tbs():
  yield from table_1()
  yield from table_2()
  yield from table_3()

def sitting(guests, tb_gen):
  table_gen = tb_gen()
  for guest in guests:
      try:
          yield (guest, next(table_gen))
      except StopIteration:
          break

guest = read_guestlist('guest_list.txt')
for idx, val in enumerate(guest):
  if idx <= 10:
    print(val)
    guest.send("Jane, 35")
  else:
    break
#guest.send("Jane, 35")
print("*******")
print(next(guest))

over_21 = (name for name, ov_21 in guests.items() if ov_21 > 21)
print(list(over_21))

seating_gen = sitting(guests, combined_tbs)
for assignment in seating_gen:
    print(assignment)