import DifferentSites.FireeyeTextSoup as Fireeye
import DifferentSites.FortinetTextSoup as Fortinet
import DifferentSites.IBMTextSoup as IBM
import DifferentSites.JuniperTextSoup as Juniper
import DifferentSites.KasperskyTextSoup as Kaspersky
import DifferentSites.McAfeeTextSoup as McAfee
import DifferentSites.RecordedFutureTextSoup as RecordedFuture
import SegmentData.paragraphMaker as paragraphMaker
import SegmentData.SentenceMaker as sentenceMaker

def GetArticles():
    Fortinet.Main()
    Kaspersky.Main()
    McAfee.Main()
    RecordedFuture.Main()
    Fireeye.Main()
    IBM.Main()
    Juniper.Main()
    
    sentenceMaker.makeSentences()
    paragraphMaker.makeParagraphs()

if __name__ == "__main__":
    GetArticles()