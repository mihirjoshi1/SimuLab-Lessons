# coding=utf-8

madlib_template = """I enjoy long, {0} walks on the beach, getting {1} in the rain and serendipitous encounters with {2}.
I really like pina coladas mixed with {3}, and romantic, candle-lit {4}.
I am looking for {5} and beauty in the form of a {6} goddess.
I would prefer if she knew how to cook, clean, and wash my {7}."""

# Pre calculation of One Eighth we can use later, written in shorthand
oe = 1.0/8.0*100.0

progress = input("Would you like a progress report? (y/n) ")

adjective1 = input("Adjective: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*1))

verbed = input("Verb Ending in 'ed': ")
if progress == 'y':
	print("You are {}% complete!".format(oe*2))

pluralNoun1 = input("Plural Noun: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*3))

liquid = input("Liquid: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*4))

pluralNoun2 = input("Plural Noun: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*5))

noun = input("Noun: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*6))

nationality = input("Nationality: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*7))

pluralNoun3 = input("Plural Noun: ")
if progress == 'y':
	print("You are {}% complete!".format(oe*8))

print(madlib_template.format(adjective1, verbed, pluralNoun1, liquid, pluralNoun2, noun, nationality, pluralNoun3))

