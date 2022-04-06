import os.path
import random
import json

sources = []

with open("WebScraping/CyberText/sentenceSources.txt", "r") as sourceList:
    for line in sourceList:
        sources.append(line.replace("CyberText\\Sentences\\","").replace(".txt", "").strip())

pairings = [["Kate", "Michael"], ["Leyton", "Casey"], ["Priyanka", "Mike"]]
articles = []

with open("AnnotationSets/usedArticles.json","r", encoding = "utf-8") as file:
    articles = json.load(file)

for pair in pairings:
    
    annoSet = ""

    for i in range(10):
        num = random.randint(0,len(sources) - 1)

        while(num in articles):
            num = random.randint(0,len(sources) - 1)

        articles.append(num)
        
        for j in range(1, 11):
            
            filePath = "WebScraping\\CyberText\\Paragraphs\\" + sources[num] + "!!PART" + str(j) + ".txt"
            if(os.path.exists(filePath)):
                with open(filePath, "r", encoding = "utf-8") as paragraph:
                    newParagraph = "".join(paragraph.readlines())
                    annoSet += newParagraph
                
                for name in pair:

                    with open("AnnotationSets/" + name + "AnnotationSet.txt", "w", encoding = "utf-8") as file:
                        
                        file.write(annoSet)

with open("AnnotationSets/usedArticles.json", "w", encoding = "utf-8") as file:
    json.dump(articles, file)
