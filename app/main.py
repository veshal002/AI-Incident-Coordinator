from app.agents.incident_classifier import IncidentClassifier
from app.retrievers.semantic_retriver import SemanticRetriever


def main():


    classifier=IncidentClassifier()
    retriever=SemanticRetriever()

    incident = """
VPN authentication is failing for users in Singapore.
Several employees are unable to connect remotely.
Authentication timeout observed after credential validation.
"""
    classification=classifier.classify(incident)
    print("=" * 60)
    print("AI Incident Intelligence Platform")
    print("=" * 60)

    print("\nIncident:\n")
    print(incident)

    print("\nclassification:\n")
    print(f'Classification type: {classification.category}')
    print(f'Confidence score: {classification.confidence}')
    print(f'Reason: {classification.reasoning}')


    docs=retriever.retrieve("VPN authentication timeout singapore")
    for i, doc in enumerate(docs, start=1):
        print("\n",'-'*50)
        print(f"Document: {i}")



if __name__ == "__main__":
    main()
