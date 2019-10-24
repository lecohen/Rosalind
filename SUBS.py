s = "GATATATGCATATACTT"
t = "ATAT"

def location_substring(s, t):
    output = []
    for a in range(len(s) - len(t)):
        if s[a:a + len(t)] == t:
            output.append(a)
    return output

print(location_substring(s, t))
