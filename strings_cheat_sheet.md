# 🐍 Python for DevOps: Strings Cheat Sheet

## 🔑 Minimum to Know by Heart
Frequently used in logs, configs, parsing, and automation.

```python
s.split(sep)         # Split string into a list by separator
sep.join(list)       # Join list into a string using separator
s.strip()            # Remove whitespace/newlines (or specified characters)
s.replace(a, b)      # Replace substring a with b
s.find(substr)       # Find substring (returns -1 if not found)
s.startswith(x)      # Check if string starts with x
s.endswith(x)        # Check if string ends with x
s[a:b]               # Slice string (from index a to b)
```


## ⚙️ Useful to Know
Sometimes used when working with data, templates, or text normalization.

```python
s.count(substr)      # Count how many times substring occurs
s.upper()            # Convert to uppercase
s.lower()            # Convert to lowercase
f"{var}"             # f-strings, formatting (preferred way)
s.format(...)        # Alternative string formatting method
```

## ❌ Rarely Needed
Uncommon in DevOps scripting — good to know they exist, but you can look them up when needed.

```python
s.zfill(5)           # Pad string on the left with zeros
s.rjust(10)          # Right-align string with spaces
s.ljust(10)          # Left-align string with spaces
s.swapcase()         # Swap case (upper <-> lower)
s.title()            # Capitalize first letter of each word
s.capitalize()       # Capitalize only the first character
s.partition(x)       # Split into 3 parts: before, x, after
s.rpartition(x)      # Like partition, but from the right
s.rsplit(sep, n)     # Split string from the right, max n times
s.isalpha()          # Check if string has only letters
s.isdigit()          # Check if string has only digits
s.isalnum()          # Check if string has only letters or digits
s.isupper()          # Check if all chars are uppercase
s.islower()          # Check if all chars are lowercase
s.isspace()          # Check if string has only whitespace  
```

