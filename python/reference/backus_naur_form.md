# Backus-Naur Form (BNF)

### Definitions
*Backus-Naur form* is a notation system for defining the syntax of formal languages. Key notations:

- `*` - Zero or more.
- `+` - One or more.
- `::=` - Definition.
- `[]` - Optional.
- `|` - Alternative.
- `""` - Literal string.
- `<>` - Rule name.
- `...` - Ellipsis.

### Features
Extended BNF (EBNF) is used to describe Python syntax.

### Examples
```
<letter> = "a" | "b" | ... | "z"
<string> ::= <letter>*
<non_empty_string> ::= <letter>+
<choice> = "Lose." | "Win."
<first_name> ::= "Johan"
<last_name> ::= "Liebert"
<full_name> ::= <first_name> [<last_name>]
```

### References
[1] [Python Language Reference: BNF](https://docs.python.org/3/reference/introduction.html#notation)

[2] [Wikipedia: BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)