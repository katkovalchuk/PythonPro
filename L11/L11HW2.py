# Task 34
import re
# 1.
re.match(r"^[HBMP][HBMP]\d{7}$", "HB1234567")

# 2.
re.match(r"^(Hello|Good morning|Salut)\sdear user$", "Hello dear user")

# 3.
re.match(r"^\d\s(\+|\*|/|-)\s\d$", "4 + 5")