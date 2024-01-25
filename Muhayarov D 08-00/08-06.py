max_length = int(input())
n = int(input())

headlines = []

for _ in range(n):
    headline = input()
    headlines.append(headline)

for headline in headlines:
    if len(headline) <= max_length:
        print(headline)
    else:
        truncated_headline = headline[:max_length-3] + "..."
        print(truncated_headline)