import FireeyeTextSoup
import FortinetTextSoup
import IBMTextSoup
import JuniperTextSoup
import KaperskyTextSoup
import McAfeeTextSoup
import RecordedFutureTextSoup

def GetArticles():
    FortinetTextSoup.Main()
    KaperskyTextSoup.Main()
    McAfeeTextSoup.Main()
    RecordedFutureTextSoup.Main()
    FireeyeTextSoup.Main()
    IBMTextSoup.Main()
    JuniperTextSoup.Main()

if __name__ == "__main__":
    GetArticles()