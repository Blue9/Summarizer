# Summarizer
An automatic paraphraser/summarizer/information extractor built using Python.
## Usage
### Summarizing a paragraph of text
This is most likely what you're looking for. To summarize text, simply use `Summarizer`'s `summarize()` function:

    summarizer.summarize('insert text here', length=1)
where `length` equals the number of sentences to condense the text down to.

**Note:** The second argument can be omitted and will default to `1`. In other words, if you omit the `length` argument, the function will return one sentence.
