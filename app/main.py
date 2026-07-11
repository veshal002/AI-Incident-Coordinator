from app.agents.incident_classifier import IncidentClassifier
from app.retrievers.hybrid_retriever import HybridRetriever

def main():


    classifier=IncidentClassifier()
    retriever= HybridRetriever()

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


    docs=retriever.retrieve("LADAP replication delay")
    for doc in docs:
        print("-"*50)
        print(doc.page_content)



if __name__ == "__main__":
    main()
