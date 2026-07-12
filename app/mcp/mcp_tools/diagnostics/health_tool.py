HEALTH = {
    "VPN Gateway": "Healthy",
    "LDAP Server": "Warning",
    "Authentication Server": "Critical",
    "Database": "Healthy",
}


def service_health(service: str) -> str:
    """
    Return simulated service health.
    """

    return HEALTH.get(
        service,
        "Unknown"
    )