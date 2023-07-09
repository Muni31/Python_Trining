# Write a python program to convert XML string to dictionary. (Regex) 
#         ========================== 
#  Input: 
#     <abc>123</abc>       
#    <pqr>456</pqr> 
#    <xyz>789</xyz> 
#   Output: 
#         { 
#    "abc":"123", 
#     "pqr":"456", 
#     "xyz":"789" 
#         } 

import xmltodict

def xyz(xml_string):
    try:
        data_xml = xmltodict.parse(xml_string)
        return data_xml
    except Exception as e:
        print(f"Error converting XML to dictionary: {str(e)}")
        return None

def abc():
    xml_string = '''<data>
        <abc>123</abc>
        <pqr>456</pqr>
        <xyz>789</xyz>
    </data>'''

    data_xml = xyz(xml_string)
    if data_xml:
        print(data_xml)

abc()

