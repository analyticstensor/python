#!/usr/bin/env python


def is_empty(text):
    """Check empty string. Return True if empty else False."""
    if not text.strip():
        return True
    else:
        return False     


def word_count(sentence):
    import pandas as pd
    if not is_empty(sentence):        
        string_token = sentence.split(" ")
        total_words = len(string_token)
        print("Input String:%s" % sentence)        
        print("=================\n   Statistics\n=================")
        df_string = pd.Series(string_token)
        print("Total words: %d." % total_words)
        df_count = df_string.value_counts()
        return df_count
    else:
        print("Input sentence is empty. Please provide valid input.")
