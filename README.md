# CyEnts Code
CyEnts is a system that recognizes instances of cybersecurity relevant entities in text.

# Setup
Install Python version >= 3.5.3

Run the following command:
    `pip install -r requirements.txt`

# Directories Included
(as of 11/28/2022)
-NER

    Holds the code relevant to the project

    -AnnotationFolder

        An example directory of what an annotator would use to annotate cybersecurity text.
        Includes onramp_nlp, which is the NLP model used to recognize entities,
        a command line command to activate the Prodigy annotation tool,
        a text file with the text to be annotated, 
        a jsonl file which is the output of the annotations,
        and the list of labels for entity types.

    -AnnotationSets

        Randomly generated sets of text for annotators to annotate.

    -PipelineCreation

        Code involved in created the NLP model.
        Includes makePipeline.py which creates the base model that uses rule based recognition such as regular expressions and Gazeteers.
        Includes the spaCy experimental coref project, to be intergrated with the model.

    -TrainingData

        Various sets of training data for the ML parts of the NLP model.

    -WebScraping

        Includes code that gathers articles from various cyber security companies and blogs to create our dataset.
        Also includes code to segment that data into sentences and paragraphs.
        The main interface for all of those parts is GetArticles.py

    There are also various other files of python code that deal with the annotation process present in this directory.

-Unused

    Holds code that is no longer used but may be useful to reference at a later date.
