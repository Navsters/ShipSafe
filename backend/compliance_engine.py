from .schemas import ReleaseRequestBase


def evaluate_release(payload: ReleaseRequestBase) -> tuple[str,str]:

    high_version = payload.software_version.endswith(".0")
    vuln_in_name = "vuln" in payload.software_name.lower()

    if high_version or vuln_in_name:
        return "high", "High risk release detected"
    else:
        return "low", "Low risk release detected"

