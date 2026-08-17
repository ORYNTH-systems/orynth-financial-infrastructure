from .models import FinalityRequest, FinalityResult


def evaluate_finality(request: FinalityRequest) -> FinalityResult:
    blockers = []

    if not request.obligation_satisfied or request.residual_exists:
        blockers.append("OBLIGATION")

    if not request.custody_state_valid:
        blockers.append("CUSTODY_STATE")

    if not request.custody_authority_valid:
        blockers.append("CUSTODY_AUTHORITY")

    if not request.authority_valid:
        blockers.append("AUTHORITY")

    if not request.scope_valid:
        blockers.append("SCOPE")

    if not request.temporal_valid:
        blockers.append("TEMPORAL")

    if not request.evidence_sufficient:
        blockers.append("EVIDENCE")

    if request.finality_conflict:
        blockers.append("FINALITY_CONFLICT")

    if request.blocking_contradiction:
        blockers.append("CONTRADICTION")

    if not request.transition_valid:
        blockers.append("TRANSITION")

    if not request.requirement_set_non_vacuous:
        blockers.append("VACUOUS_REQUIREMENTS")

    eligible = len(blockers) == 0

    return FinalityResult(
        eligible=eligible,
        classification="FINALITY_DOMAIN_COMPLETE" if eligible else "FINALITY_INELIGIBLE",
        blockers=blockers,
    )


def reopen_finality(previous: FinalityResult) -> FinalityResult:
    if previous.classification != "FINALITY_DOMAIN_COMPLETE":
        raise ValueError("Only a currently final state may be reopened.")

    return FinalityResult(
        eligible=False,
        classification="FINALITY_REOPENED",
        blockers=[],
        historical_finality_preserved=True,
    )


def apply_post_finality_contradiction(previous: FinalityResult) -> FinalityResult:
    if previous.classification != "FINALITY_DOMAIN_COMPLETE":
        raise ValueError("Post-finality contradiction requires a previously final state.")

    return FinalityResult(
        eligible=False,
        classification="FINALITY_INVALIDATED",
        blockers=["CONTRADICTION"],
        historical_finality_preserved=True,
        post_finality_contradiction=True,
    )
