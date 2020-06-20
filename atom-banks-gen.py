#!/usr/bin/python3

start = 0x24
end = 0x84

notes_in_bank = 16

def print_bank(start_note, notes_in_bank, to_ch, to_start):
	to = to_start

	for i in range(start_note, start_note + notes_in_bank):
		print('XX {0:02X} = X{1:X} {2:02X}'.format(i, to_ch, to))
		to += 1

channel = 0
for bank in range(start, end, notes_in_bank):
	print("# {:X} to channel {}".format(bank, channel + 1))
	print_bank(bank, notes_in_bank, channel, start)
	channel += 1

# NOTE: channel 6 is special, because of overflow, must be fixed manually!

# channel 7 and 8
for bank in range(0x04, 0x04 + 16*2, notes_in_bank):
	print("# {:X} to channel {}".format(bank, channel + 1))
	print_bank(bank, notes_in_bank, channel, start)
	channel += 1
