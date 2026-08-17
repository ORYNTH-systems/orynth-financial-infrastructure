from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PARENT = ROOT / "06-f3-discovery" / "runtime"
sys.path.insert(0, str(RUNTIME_PARENT))

from f3_runtime import (
    FinalityRequest,
    evaluate_finality,
    reopen_finality,
    apply_post_finality_contradiction,
)


def fully_valid_request(**overrides):
    values = dict(
        execution_complete=True,
        effect_occurred=True,
        obligation_satisfied=True,
        residual_exists=False,
        custody_possession=True,
        custody_authority_valid=True,
        custody_state_valid=True,
        atomic_complete=True,
        consensus_complete=True,
        reconciliation_complete=True,
        authority_valid=True,
        scope_valid=True,
        temporal_valid=True,
        evidence_sufficient=True,
        finality_conflict=False,
        blocking_contradiction=False,
        transition_valid=True,
        requirement_set_non_vacuous=True,
    )
    values.update(overrides)
    return FinalityRequest(**values)


def test_valid_full_request_is_final():
    result = evaluate_finality(fully_valid_request())
    assert result.eligible is True
    assert result.classification == "FINALITY_DOMAIN_COMPLETE"


def test_execution_only_does_not_create_finality():
    result = evaluate_finality(
        FinalityRequest(
            execution_complete=True,
            requirement_set_non_vacuous=True,
        )
    )
    assert result.eligible is False
    assert result.classification == "FINALITY_INELIGIBLE"


def test_consensus_only_does_not_create_finality():
    result = evaluate_finality(
        FinalityRequest(
            consensus_complete=True,
            requirement_set_non_vacuous=True,
        )
    )
    assert result.eligible is False


def test_custody_possession_does_not_create_custody_authority():
    result = evaluate_finality(
        fully_valid_request(
            custody_possession=True,
            custody_authority_valid=False,
        )
    )
    assert result.eligible is False
    assert "CUSTODY_AUTHORITY" in result.blockers


def test_unresolved_finality_conflict_blocks_finality():
    result = evaluate_finality(
        fully_valid_request(finality_conflict=True)
    )
    assert result.eligible is False
    assert "FINALITY_CONFLICT" in result.blockers


def test_reopening_preserves_historical_finality():
    final = evaluate_finality(fully_valid_request())
    reopened = reopen_finality(final)

    assert reopened.classification == "FINALITY_REOPENED"
    assert reopened.historical_finality_preserved is True


def test_post_finality_contradiction_is_explicit():
    final = evaluate_finality(fully_valid_request())
    invalidated = apply_post_finality_contradiction(final)

    assert invalidated.classification == "FINALITY_INVALIDATED"
    assert invalidated.post_finality_contradiction is True
    assert invalidated.historical_finality_preserved is True


def test_atomic_completion_alone_is_not_finality():
    result = evaluate_finality(
        FinalityRequest(
            atomic_complete=True,
            requirement_set_non_vacuous=True,
        )
    )
    assert result.eligible is False


def test_reconciliation_alone_is_not_finality():
    result = evaluate_finality(
        FinalityRequest(
            reconciliation_complete=True,
            requirement_set_non_vacuous=True,
        )
    )
    assert result.eligible is False


def test_residual_blocks_finality():
    result = evaluate_finality(
        fully_valid_request(
            obligation_satisfied=True,
            residual_exists=True,
        )
    )
    assert result.eligible is False
    assert "OBLIGATION" in result.blockers


def test_invalid_scope_blocks_finality():
    result = evaluate_finality(
        fully_valid_request(scope_valid=False)
    )
    assert result.eligible is False
    assert "SCOPE" in result.blockers


def test_vacuous_requirement_set_blocks_finality():
    result = evaluate_finality(
        fully_valid_request(requirement_set_non_vacuous=False)
    )
    assert result.eligible is False
    assert "VACUOUS_REQUIREMENTS" in result.blockers
