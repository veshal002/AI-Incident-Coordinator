from app.agents.coordinator_agent import CoordinatorAgent

def main():

    incident = """
VPN authentication is failing for users in Singapore.
Several employees are unable to connect remotely.
Authentication timeout observed after credential validation.
"""

    coordinator = CoordinatorAgent()

    result = coordinator.handle_incident(
        incident
    )

    print(result.model_dump_json(indent=2))

if __name__ == "__main__":
    main()