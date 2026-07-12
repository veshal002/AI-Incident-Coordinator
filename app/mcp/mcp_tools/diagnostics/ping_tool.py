SERVICES = {
    "VPN Gateway": "Reachable",
    "LDAP Server": "Reachable",
    "Authentication Server": "Unreachable",
    "Database": "Reachable",
}


def ping_service(service: str) -> str:
    """
    Simulate a network connectivity check.
    """

    return SERVICES.get(
        service,
        "Unknown Service"
    )