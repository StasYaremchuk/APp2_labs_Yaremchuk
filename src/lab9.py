def counting_sort(words):
    if not words:
        return []
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    count = [[] for _ in range(max_len + 1)]

    for word in words:
        count[len(word)].append(word)

    sorted_words = []
    for bucket in count:
        sorted_words.extend(bucket)

    return sorted_words


def get_max(values):
    max_value = 0
    for v in values:
        if v > max_value:
            max_value = v
    return max_value


with open("wchain.in") as f:
    n = int(f.readline())
    words = []
    word_set = set()

    for _ in range(n):
        word = f.readline().strip()
        words.append(word)
        word_set.add(word)

words = counting_sort(words)

dp = {}

for word in words:
    dp[word] = 1
    wl = len(word)
    for i in range(wl):
        shorter = word[:i] + word[i + 1:]
        if shorter in word_set:
            val = dp[shorter] + 1
            if val > dp[word]:
                dp[word] = val

max_chain = get_max(dp.values())

with open("wchain.out", "w") as f:
    f.write(str(max_chain) + "\n")
