from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="your-keys",
    api_version="2023-05-15",
    azure_endpoint="your-azure-openai-endpoint",
)

response = client.embeddings.create(
    input=["鯊魚寶寶 doo doo doo doo doo doo, 鯊魚寶寶"],
    model="ada-002"
)

dimensions=len(response.model_dump()["data"][0]["embedding"])
print("Dimesion: ", dimensions)
#print(response.model_dump_json(indent=2))
