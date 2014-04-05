def ngrams(input, n):
    """Returns n-gram of a string"""
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
