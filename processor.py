def sanitize_string(data):
    """
    Removes special characters and trims the input.
    Defensive handling for None and non-strings.
    """
    if not isinstance(data, str):
        return ""
    data = data.strip()
    for ch in ['!', '@', '#', '$', '%']:
        data = data.replace(ch, '')
    return data


def parse_int_list(csv_string):
    """
    Parses a CSV string of integers into a list of ints.
    Defensive handling:
    - None or empty -> return []
    - Skip empty tokens
    - Skip non-integer values safely
    """
    if not isinstance(csv_string, str) or not csv_string.strip():
        return []
    
    parts = csv_string.split(',')
    nums = []
    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            nums.append(int(p))
        except ValueError:
            # skip values like "a" or "three"
            continue
    return nums


def reverse_words(sentence):
    """
    Reverses each word in a sentence.
    Defensive handling for None or non-string.
    """
    if not isinstance(sentence, str):
        return ""
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g., 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)


if __name__ == "__main__":
    main()
