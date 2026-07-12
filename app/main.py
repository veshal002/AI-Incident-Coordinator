from app.agents.coordinator_agent import CoordinatorAgent


def main():

    incident = """
VPN authentication is failing for users in Singapore.
Several employees are unable to connect remotely.
Authentication timeout observed after credential validation.
"""

    coordinator = CoordinatorAgent()

    result = coordinator.handle_incident(incident)

    print("=" * 80)
    print("AI INCIDENT INTELLIGENCE PLATFORM")
    print("=" * 80)

    print("\nINCIDENT\n")
    print(incident.strip())

    print("\n" + "=" * 80)
    print("CLASSIFICATION")
    print("=" * 80)
    print(f"Category   : {result.classification.category}")
    print(f"Confidence : {result.classification.confidence}")
    print(f"Reason     : {result.classification.reason}")

    print("\n" + "=" * 80)
    print("ROOT CAUSE ANALYSIS")
    print("=" * 80)
    print(result.root_cause)

    print("\n" + "=" * 80)
    print("TROUBLESHOOTING")
    print("=" * 80)
    print(result.troubleshooting)

    print("\n" + "=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)
    print(result.recommendation)

    print("\n" + "=" * 80)
    print("WORKFLOW COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()