import re
import sys

ignore = ['', 'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is', 'am', 'are', 'was', 'were', 'being', 'been', 'has', 'have', 'had', 'do', 'does', 'did', 'shall', 'will', 'should', 'would', 'may', 'might', 'must', 'can', 'could']

def remove_puncuation(text):
    return re.sub('[\"\'\[\]@#\$%\^&\*\(\)\-_=\+,\.\?<>{}\|]', '', text.lower())

def get_words(text):
    refined = ''
    sentences = get_sentences(text)
    for sentence in sentences:
        refined += sentence[1] + ' '
    raw_words = re.split(' ', remove_puncuation(refined))
    word_list = [word for word in raw_words if word not in ignore]
    return word_list

def get_sentences(text):
    sentence_list = []
    start = 0
    for i, char in enumerate(text):
        if i == len(text) - 1:
            sentence_list.append([text[start:], text[start:]])
        elif char == '.' and text[i+1].upper() not in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for j, nextchar in enumerate(text[i+1:]):
                if nextchar == ' ':
                    end = i + 1 + j
                    sentence_list.append([text[start:end], text[start:i+1]])
                    start = end + 1
                    break
    return sentence_list

def get_word_score(text):
    word_score = {}
    for word in get_words(text):
        if word in word_score:
            word_score[word] += 1
        else:
            word_score[word] = 0
    return word_score

def get_sentence_score(text):
    sentence_score = {}
    for sentence in get_sentences(text):
        for word in get_words(sentence[1]):
            if sentence[0] in sentence_score:
                sentence_score[sentence[0]] += get_word_score(text)[word]
            else:
                sentence_score[sentence[0]] = 0
    return sentence_score

def summarize(text, length=1):
    sentence_score = get_sentence_score(text)
    max = []
    for sentence in sentence_score:
        if len(max) < length:
            max.append([sentence, sentence_score[sentence]])
        else:
            min = ['', sys.maxint]
            for i, sent in enumerate(max):
                if sent[1] < min[1]:
                    min = [i, sent[1]]
            if sentence_score[sentence] > min[1]:
                max[min[0]] = [sentence, sentence_score[sentence]]
    summary = ''
    for sentence in get_sentences(text):
        if [sentence[0], sentence_score[sentence[0]]] in max:
            summary += sentence[0] + ' '
    return summary
