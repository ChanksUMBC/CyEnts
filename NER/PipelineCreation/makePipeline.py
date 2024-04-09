import spacy
from spacy import displacy


def loadAttackTypeList():
    """
    This function will load the list of attack types from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/attack_type.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"Attack_Type"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list


def loadFileExtList():
    """
    This function will load the list of file extensions from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/file_ext.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"File_Extension"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list

def loadProgLangList():
    """
    This function will load the list of programming languages from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/languages.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"Programming_Language"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list


def loadMalwareTypesList():
    """
    This function will load the list of malware types from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/malware_types.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"Malware_Type"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list


def loadOSList():
    """
    This function will load the list of operating Systems from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/os_short.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"Operating_System"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list


def loadProtocolList():
    """
    This function will load the list of protocols from the file and return
    it in the format used for patterns in the entitiy ruler
    RETURN :: List of dictionaries in the format that spacy expects patterns in
            which is 
    {'label':'LABEL_NAME', 'pattern': [{'LOWER':'Some_text'},{'TEXT':'Text2'}]}
    where lower matches the lowercase of token's text to our pattern text
    """
    final_list = []
    with open("EntityLists/protocols.txt", "r") as file:

        for line in file:
            line_pattern = {"label":"Protocol"}

            words = line.strip("\n\r").split()
            pattern_list = []
            for word in words:
                pattern_list.append({"LOWER":word.lower()})

            line_pattern["pattern"] = pattern_list
            final_list.append(line_pattern)

    return final_list



if __name__ == "__main__":
    nlp = spacy.load("../CyEnts/model-best")

    ruler = nlp.add_pipe("entity_ruler", before="ner")

    """
    ============================================================================
    add pattern based recognition based on lists of items for various types
    ============================================================================
    """

    #attack type list
    attack_type = loadAttackTypeList()
    ruler.add_patterns(attack_type)

    #file extension list
    file_ext = loadFileExtList()
    ruler.add_patterns(file_ext)

    #programming languages list
    lang = loadProgLangList()
    ruler.add_patterns(lang)

    #Malware Types list
    mal_type = loadMalwareTypesList()
    ruler.add_patterns(mal_type)

    #Operating Systems list
    os_list = loadOSList()
    ruler.add_patterns(os_list)

    #protocols list
    prot = loadProtocolList()
    ruler.add_patterns(prot)


    """
    ============================================================================
    add in regex support for various types
    ============================================================================
    """

    #add in regex for URLS and EMAIL (built into spacy)
    patterns = [{"label": "Email", "pattern": [{'LIKE_EMAIL':True}]},
                {"label": "URL", "pattern": [{'LIKE_URL':True}]}]         
    ruler.add_patterns(patterns)

    #add support for emails with "." replaced by "[.]" found commonly in some texts (namely Mandiant)
    email_rx_brackets = r"[\w-]+@([\w-]+\[\.\])+[\w-]+"
    email_rx= [ {"TEXT": {"REGEX": email_rx_brackets}}]
    ruler.add_patterns([{"label":"Email", "pattern":email_rx}])

    #add support for URLs with "." replaced by "[.]" found commonly in some texts
    url_rx_brackets = r"(http(s)?:\/\/.)?(www\[\.\])?[-a-zA-Z0-9@:%._\+~#=]{2,256}\[\.\][a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    url_rx= [ {"TEXT": {"REGEX": url_rx_brackets}}]
    ruler.add_patterns([{"label":"URL", "pattern":url_rx}])

    #regex for IP addresses
    octet_rx = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    ip_rx= [ {"TEXT": {"REGEX": r"(^{0}(?:\.{0}){{3}}$)".format(octet_rx)}}]
    ruler.add_patterns([{"label":"IP_Address", "pattern":ip_rx}])

    #add support for IP addesses with "." replaced by "[.]" found commonly in some texts
    ip_rx_brackets= [ {"TEXT": {"REGEX": r"(^{0}(?:\[\.\]{0}){{3}}$)".format(octet_rx)}}]
    ruler.add_patterns([{"label":"IP_Address", "pattern":ip_rx_brackets}])

    #regex for hash values
    md5_rx = [{"TEXT": {"REGEX": r"^[0-9a-fA-F]{32}$"}}]
    ruler.add_patterns([{"label":"Hash", "pattern":md5_rx}])

    sha256_rx = [{"TEXT": {"REGEX": r"^[A-Fa-f0-9]{64}$"}}]
    ruler.add_patterns([{"label":"Hash", "pattern":sha256_rx}])

    sha512_rx = [{"TEXT": {"REGEX": r"^[A-Fa-f0-9]{128}$"}}]
    ruler.add_patterns([{"label":"Hash", "pattern":sha512_rx}])

    sha1_rx = [{"TEXT": {"REGEX": r"^[a-fA-F0-9]{40}$"}}]
    ruler.add_patterns([{"label":"Hash", "pattern":sha1_rx}])

    #regex for ports
    port_number_rx = {"TEXT": {"REGEX": r"^\d{1,5}$"}}
    ruler.add_patterns([{"label":"Port", "pattern": [{'LOWER':'port'}, port_number_rx ]}])

    #regex for CVE vulnerabilities
    cve_pat = [{"LOWER": {"REGEX": r"cve-\d{4}"}}, {"TEXT": "-"}, {"TEXT": {"REGEX": r"\d{4,7}"}}]
    ruler.add_patterns([{"label":"Vulnerability", "pattern": cve_pat}])



    """
    ============================================================================
    save the created pipeline
    ============================================================================
    """

    save_pipeline = True
    pipeline_directory = "./CyEnts_with_gazeteers"
    if save_pipeline:
        print("Saving pipeline")
        nlp.to_disk(pipeline_directory)
        print(f"Pipeline saved to {pipeline_directory}")



    """
    ============================================================================
    test the function and output an html file
    ============================================================================
    """



    text = """Many of the phishing emails appeared legitimate – they referenced a specific job opportunity and salary, provided a link to the spoofed company’s employment website, and even included the spoofed company’s Equal Opportunity hiring statement.
However, in a few cases, APT33 operators left in the default values of the shell’s phishing module.
These appear to be mistakes, as minutes after sending the emails with the default values, APT33 sent emails to the same recipients with the default values removed.
As shown in Figure 3, the “fake mail” phishing module in the ALFA Shell contains default values, including the sender email address (solevisible@gmail[.]com), subject line (“your site hacked by me”), and email body (“Hi Dear Admin”).
Figure 3:
ALFA TEaM Shell v2-Fake Mail (Default) Figure 4 shows an example email containing the default values the shell.
Figure 4:
Example Email Generated by the ALFA Shell with Default Values Domain Masquerading APT33 registered multiple domains that masquerade as Saudi Arabian aviation companies and Western organizations that together have partnerships to provide training, maintenance and support for Saudi’s military and commercial fleet.
Based on observed targeting patterns, APT33 likely used these domains in spear phishing emails to target victim organizations.
The following domains masquerade as these organizations: Boeing, Alsalam Aircraft Company, Northrop Grumman Aviation Arabia (NGAAKSA), and Vinnell Arabia.
boeing.servehttp[.]com
alsalam.ddns[.]net ngaaksa.ddns[.]net ngaaksa.sytes[.]net vinnellarabia.myftp[.]org Boeing, Alsalam Aircraft company, and Saudia Aerospace Engineering Industries entered into a joint venture to create the Saudi Rotorcraft Support Center in Saudi Arabia in 2015 with the goal of servicing Saudi Arabia’s rotorcraft fleet and building a self-sustaining workforce in the Saudi aerospace supply base.
Alsalam Aircraft Company also offers military and commercial maintenance, technical support, and interior design and refurbishment services.
Two of the domains appeared to mimic Northrop Grumman joint ventures."""

    doc = nlp(text)
    print("done!")

    #colors = {'URL': "#85C1E9", "EMAIL": "red", "MALWARE_NAME":"orange", "vulnerability":"#CAFF70", \
    #       "IP_ADDRESS":"#EE82EE", 'threat_actor':"#FFB90F", 'port':'#E0FFFF', 'hash':'#FFFF00', \
    #        'MALWARE_TYPE':'#3CB371',"THREAT_ACTOR":"blue"}

    html = displacy.render(doc, style="ent", page = True)

    with open("test.html", "w") as file:
        file.write(html)