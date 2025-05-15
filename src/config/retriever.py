
#from typing import Literal
#from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
# class RetrieverConfig():
#     knowledge_base_id: str
#     number_of_results: int
#     overrideSearchType: Literal["HYBRID", "SEMANTIC"]
#     filter: dict

#     def __init__(self, 
#                  knowledge_base_id: str,
#                  number_of_results: int,
#                  overrideSearchType: Literal["HYBRID", "SEMANTIC"],
#                  filter: dict):
#         self.knowledge_base_id = knowledge_base_id
#         self.number_of_results = number_of_results
#         self.overrideSearchType = overrideSearchType
#         self.filter = filter

#     def get_config(self):
#         #TODO: add filter to config
#         return {
#             "knowledge_base_id": self.knowledge_base_id,
#             "retrieval_config": {"vectorSearchConfiguration": {"numberOfResults": self.number_of_results,
#                                                               "overrideSearchType": self.overrideSearchType}}
#         }

# retriever_config = RetrieverConfig(
#     knowledge_base_id="K5AQF6GLSG",
#     number_of_results=4,
#     overrideSearchType="SEMANTIC",
#     filter={}
# )

# retriever = AmazonKnowledgeBasesRetriever(knowledge_base_id=retriever_config.knowledge_base_id)

# result = retriever.client.retrieve(
#     retrievalQuery={"text": query},
#     knowledgeBaseId=retriever_config.knowledge_base_id,
#     retrievalConfiguration=retriever_config.get_config()["retrieval_config"]
# )
# print(result)

from langchain_community.vectorstores import OpenSearchVectorSearch
from langchain_aws.embeddings import BedrockEmbeddings
import boto3
from opensearchpy import RequestsHttpConnection
from requests_aws4auth import AWS4Auth

region = 'us-east-1'
model_id = "amazon.titan-embed-text-v2:0"
opensearch_url = "https://gt9iwx52nfcp60iedxa5.us-east-1.aoss.amazonaws.com/"
index_name = "bedrock-knowledge-base-default-index"
engine = "faiss"
vector_field = "bedrock-knowledge-base-default-vector"
text_field = "AMAZON_BEDROCK_TEXT"
metadata_field = "AMAZON_BEDROCK_METADATA"
search_type = "approximate_search" #script_scoring, or painless_scripting

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, 'aoss', session_token=credentials.token)


embeddings = BedrockEmbeddings(
    model_id=model_id
)

vector_store = OpenSearchVectorSearch(
    opensearch_url=opensearch_url,
    embedding_function=embeddings,
    index_name=index_name,
    http_auth=awsauth,
    timeout=300,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    engine=engine
)


if __name__ == "__main__":
    query = "¿Desde cuándo está vigente el Programa ueno+?"

    docs = vector_store.similarity_search(
        query=query,
        k=4,
        vector_field=vector_field,
        text_field=text_field,
        metadata_field=metadata_field,
        search_type=search_type
    )
 
    print(docs)



