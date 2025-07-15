# Backslash
print("Path: C:\\Users\\File.txt")  # Output: Path: C:\Users\File.txt

# Single quote
print('Don\'t stop believin\'')     # Output: Don't stop believin'

# Double quote
print("She said: \"Hello world!\"") # Output: She said, "Hello world!"

# Line Feed
print("First line\nSecond line")     # Output: First line
                                     #         Second line

# Form Feed (clears terminal screen in some environments)
print("Above form feed\fBelow form feed")

# Carriage Return
print("Old text\rNew")               # Output: New text

# Vertical Tab
print("Top\vMiddle\vBottom")         # Output: Top
                                     #             Middle
                                     #                 Bottom

# Horizontal Tab
print("Name:\tJohn\tAge:\t30")       # Output: Name:    John    Age:    30

# Backspace
print("123\b\bXY")                   # Output: 1XY

# Bell
print("Alert!\a")                    # Makes a beep sound

# Byte hex value
print("Hex: \x48\x65\x6C\x6C\x6F")   # Output: Hex: Hello

# Byte octal value
print("Octal: \110\145\154\154\157") # Output: Octal: Hello

# Unicode by name
print("Snowman: \N{SNOWMAN}")        # Output: Snowman: ☃

# 4-digit hex Unicode
print("Euro: \u20AC")                # Output: Euro: €

# 8-digit hex Unicode
print("Smile: \U0001F600")            # Output: Smile: 😀