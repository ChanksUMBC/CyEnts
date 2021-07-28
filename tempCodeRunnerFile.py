    sent = str(sent)
            sent = sent[:-1]

            words = sent.split(" ")
            finalWords = []
            
            for word in words:

                if word:
                    if word.lower() not in stopWords:    
                        finalWords.append(word)