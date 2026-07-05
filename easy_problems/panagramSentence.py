def checkIfPangram(self, sentence: str) -> bool:
    seen_letters = set(sentence)
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in seen_letters:
            return False  
                
    return True