
def all_variants(n):
    for start in range(len(n)):
        for end in range(start+1, len(n)+1):
            yield n[start:end]

a = all_variants("abc")
for i in a:
    print(i)
