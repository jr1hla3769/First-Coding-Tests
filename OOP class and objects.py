import locale
# Set place value to compute with
sample_amount = 1234567.89
# Next, set local to FR
locale.setlocale(locale.LC_ALL, "fr_FR")
# USE locale.currency() to show sample amount in locale format
print(locale.currency(sample_amount, grouping=True))

