# Given an input of a string like "Hello {{a}} world. How {{b}} {{c}}" and substitution replacements like "a" is "{{c}}", "b" is "{{a}}", "c" is "{{b}}", return the filled string:
# "Hello happy world. How happy happy".


# sdfsd {{sdfds}}

replace_dict = {
    "a": "happy",
    "b": "{{a}}",
    "c": "{{b}}"
}

seen = set()


def replace_string(input_str, replace_dict):
    if not replace_dict:
        return input_str

    idx = 0
    output = ""

    while idx < len(input_str):

        if idx < len(input_str) - 1 and input_str[idx] == '{' and input_str[idx + 1] == '{':
            idx += 2
            curr = ""
            while idx < len(input_str) and input_str[idx].isalpha():
                curr += input_str[idx]
                idx += 1

            # closing double braces
            if idx < len(input_str) - 1 and input_str[idx] == '}' and input_str[idx + 1] == '}':
                if curr in replace_dict and curr not in seen:
                    seen.add(curr)
                    output += replace_string(replace_dict[curr], replace_dict)
                    seen.remove(curr)
                else:
                    raise "bad input"

            else:
                output += "{{" + curr

            idx += 1
        else:
            output += input_str[idx]

        idx += 1

    return output


print(replace_string("Hello {{a}} world. How {{b}} {{c}}", replace_dict))


