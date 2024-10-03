from transformers import pipeline

classifier = pipeline("fill-mask")
classifier("Paris is the <mask> of France.")

'''If a model name is not provided, the pipeline will be initialized with distilroberta-base. You can provide masked text and it will return a list of possible mask values ​​ranked according to the score.'''
