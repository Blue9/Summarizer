# Summarizer
An automatic paraphraser/summarizer/information extractor built using Python.
## Usage
### Summarizing a paragraph of text
This is most likely what you're looking for. To summarize text, simply use `Summarizer`'s `summarize()` function:

    summarizer.summarize('insert text here', n)
where n = number of sentences to condense text down to.  
**Note:** The second argument can be omitted and will default to 1.
