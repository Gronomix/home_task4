'''Требуется реализовать программу, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).'''


def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

longest_words('article.txt')
print(longest_words('article.txt'))

