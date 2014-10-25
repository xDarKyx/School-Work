
def generate(pairs):
    i=3
    t="Transport"
    c="Clothing"
    ti="Telephone"
    o="Others"
    f="Food"
    h="House keeping"
    
    while(i<=31):
        d=str(i)
        pairs.append((t+d,0))
        pairs.append((c+d,0))
        pairs.append((ti+d,0))
        pairs.append((o+d,0))
        pairs.append((f+d,0))
        pairs.append((h+d,0))
        i+=1