from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import json

# Load the config keys
with open('configs.json', 'r') as data_file:
        config = json.load(data_file)
        
key_var_name = config["azure_key"]
endpoint_var_name = config["azure_endpoint"]

credentials = CognitiveServicesCredentials(key_var_name)

text_analytics = TextAnalyticsClient(endpoint=endpoint_var_name, credentials=credentials)

documents = [
    {
        "id": "1",
        "language": "en",
        "text": "Sharks are a group of elasmobranch fish characterized by a cartilaginous skeleton, five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head. Modern sharks are classified within the clade Selachimorpha (or Selachii) and are the sister group to the rays. However, the term shark has also been used for extinct members of the subclass Elasmobranchii outside the Selachimorpha, such as Cladoselache and Xenacanthus, as well as other Chondrichthyes such as the holocephalid eugenedontidans. Under this broader definition, the earliest known sharks date back to more than 420 million years ago.[2] Acanthodians are often referred to as spiny sharks; though they are not part of Chondrichthyes proper, they are a paraphyletic assemblage leading to cartilaginous fish as a whole. Since then, sharks have diversified into over 500 species. They range in size from the small dwarf lanternshark (Etmopterus perryi), a deep sea species of only 17 centimetres (6.7 in) in length, to the whale shark (Rhincodon typus), the largest fish in the world, which reaches approximately 12 metres (40 ft) in length.[3] Sharks are found in all seas and are common to depths of 2,000 metres (6,600 ft). They generally do not live in freshwater although there are a few known exceptions, such as the bull shark and the river shark, which can be found in both seawater and freshwater.[4] Sharks have a covering of dermal denticles that protects their skin from damage and parasites in addition to improving their fluid dynamics. They have numerous sets of replaceable teeth.[5] Well-known species such as the tiger shark, blue shark, mako shark, thresher shark, and hammerhead shark are apex predators—organisms at the top of their underwater food chain. Many shark populations are threatened by human activities."
    }
]
response = text_analytics.key_phrases(documents=documents)

for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Phrases:")
    for phrase in document.key_phrases:
        print("\t\t", phrase)