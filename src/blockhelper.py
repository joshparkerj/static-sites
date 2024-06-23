from re import fullmatch, finditer

def block_to_block_type(block):
    if fullmatch(r'(?s)#{1,6} \w.*', block):
        return 'heading'
    if fullmatch(r'(?s)```.*```', block):
        return 'code'
    if fullmatch(r'>.*(\n>.*)*', block):
        return 'quote'
    if fullmatch(r'[-\*] .*(\n[-\*] .*)*', block):
        return 'unordered_list'
    if fullmatch(r'\d+\. .*(\n\d+\. .*)*', block) and all(m.group(0) == str(i + 1) for i, m in enumerate(finditer(r'(?m)^\d+', block))):
        return 'ordered_list'
    return 'paragraph'

    
