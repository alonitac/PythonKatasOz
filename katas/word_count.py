"""Count the words in a sentence."""


def word_count(sentence):
    """
    Counts how many words are in a sentence.

    Words are separated by whitespace. Repeated spaces, tabs, and newlines
    count as a single break. 

    Args:
        sentence: the text to count

    Returns:
        the number of words. An empty or whitespace-only sentence returns 0.
    """

    wlist = []
    left = 0
    right = 0

    while left < len(sentence):
        right = left
        while right < len(sentence) and is_letter(sentence[right]):
            right = right + 1
        if right != left:
            wlist.append(sentence[left:right])
        left = go_to_next_letter(sentence,right)
       
        
    
            
    return len(wlist)    
    





def go_to_next_letter(sentence: str, index: int) -> int:
    temp = index
    while temp < len(sentence) and sentence[temp].isspace():
        temp = temp + 1
    return temp

def is_letter(chr: str) -> bool:
    return not chr.isspace()


if __name__ == '__main__':
    print(word_count("hello world"))          # 2
    print(word_count("  one   two three "))   # 3
