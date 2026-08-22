from .model import AdmissionResult, Decision, FinancialExecutionEvent


def evaluate_admission(event: FinancialExecutionEvent) -> AdmissionResult:
    authority = event.authority

    if authority is None:
        return AdmissionResult(
            Decision.BLOCK,
            "NO_AUTHORITY_CONTEXT",
        )

    if not authority.current:
        return AdmissionResult(
            Decision.BLOCK,
            "AUTHORITY_NOT_CURRENT",
        )

    if not authority.authorized:
        return AdmissionResult(
            Decision.BLOCK,
            "NOT_AUTHORIZED",
        )

    if not authority.scope_valid:
        return AdmissionResult(
            Decision.BLOCK,
            "SCOPE_INVALID",
        )

    return AdmissionResult(
        Decision.ADMIT,
        "CURRENT_AUTHORITY_AND_SCOPE_VALID",
    )
