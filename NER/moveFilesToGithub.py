#the purpose of this code is to move the dataset from the folder it's in
# to another folder that is connected to a github repository

with open("WebScraping/CyberText/sentenceSources.txt","r",encoding ="utf-8") as sourceFile:
        SentenceSources = []

        for line in sourceFile:

            text = ""
            source = line.strip()

            with open("WebScraping/"+source,encoding="utf-8") as file:
                for line in file:
                    text += line
            
            source = source.split("CyberText\\Sentences\\")[1]
            SentenceSources.append(source)
            
            with open("CyberBlogDataset/Sentences/" + source, "w", encoding="utf-8",newline='\n') as file:
                file.write(text)

        with open("CyberBlogDataSet/SentenceFileNames.txt", "w", encoding="utf-8",newline='\n') as file:
            for line in SentenceSources:
                file.write(line)
                file.write("\n")

with open("WebScraping/CyberText/paragraphFileNames.txt","r",encoding ="utf-8") as sourceFile:
        paragraphSources = []

        for line in sourceFile:

            text = ""
            source = line.strip()

            with open("WebScraping/CyberText/Paragraphs/"+source,encoding="utf-8") as file:
                for line in file:
                    text += line
            
            paragraphSources.append(source)
            
            with open("CyberBlogDataset/Paragraphs/" + source, "w", encoding="utf-8",newline='\n') as file:
                file.write(text)

        with open("CyberBlogDataSet/ParagraphFileNames.txt", "w", encoding="utf-8",newline='\n') as file:
            for line in SentenceSources:
                file.write(line)
                file.write("\n")