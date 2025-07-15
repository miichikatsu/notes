# Escape Sequences

## Definitions
An *escape sequence* is a sequence of characters that starts with `\` and has a special semantic meaning. List of escape characters with their meanings:
|Escape character|Meaning|
|---|----------------------|
|`\\`|Backslash.|
|`\'`|Single quote.|
|`\"`|Double quote.|
|`\n`|ASCII Line Feed (LF).|
|`\f`|ASCII Form Feed (FF).|
|`\r`|ASCII Carriage Return (CR).|
|`\v`|ASCII Vertical Tab (VT).|
|`\t`|ASCII Horizontal Tab (HT).|
|`\b`|ASCII Backspace (BS).|
|`\a`|ASCII Bell (BEL).|
|`\xhh`|Unicode 0-FF.|
|`\ooo`|Unicode 0-512.|

Only for string literals:
|Escape character|Meaning|
|---------|----------------------|
|`\N{name}`|Unicode character by name.|
|`\uxxxx'`|Unicode 0-FFFF.|
|`\Uxxxxxx'`|Unicode.|

## Examples
[Escape Sequences](src/escape_sequences.py)

## References
[1] [Wikipedia: Escape Sequence](https://en.wikipedia.org/wiki/Escape_sequence)

[2] [ASCII Code: Table](https://www.ascii-code.com/)

[3] [Python Language Tutorial: Escape Sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences)