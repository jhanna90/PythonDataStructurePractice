def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiouAEIOU"
    frequency_map = {}
    
    for char in phrase:
        if char in vowels:
            frequency_map[char.lower()] = frequency_map.get(char.lower(), 0) + 1
            
    return frequency_map