# Summarizer
An automatic paraphraser/summarizer/information extractor built using Python.
## Usage
### Summarizing a paragraph of text
This is most likely what you're looking for. To summarize text, simply use `Summarizer`'s `summarize()` function:

    summarizer.summarize("insert text here", length=1)
where `length` equals the number of sentences to condense the text down to.

**Note:** The second argument can be omitted and will default to `1`. In other words, if you omit the `length` argument, the function will return one sentence.

### Functions
`remove_punctuation(text)`: Removes punctuation and converts all letters to lowercase.

`get_words(text)`: Returns a list of all the words found in `text`.

`get_sentences(text)`: Returns a list of all the sentences found in `text`.

`get_word_score(text)`: Counts the number of times a word appears in `text` an returns this data in a dictionary in the format: `{ "word": # of times in text, ...}`

`get_sentence_score(text)`: Adds the score of each word in the sentences of `text` and returns this data in a dictionary in the format: `{ "sentence": score, ...}`

`summarize(text)`: Described [here](https://github.com/Blue9/Summarizer#summarizing-a-paragraph-of-text).
