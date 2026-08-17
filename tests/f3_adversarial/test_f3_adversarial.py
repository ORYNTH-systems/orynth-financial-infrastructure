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


def valid_request(**overrides):
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


def test_execution_completion_cannot_bypass_authority():
    result = evaluate_finality(
        valid_request(
            execution_complete=True,
            authority_valid=False,
        )
    )
    assert result.eligible is False
    assert "AUTHORITY" in result.blockers


def test_consensus_cannot_bypass_scope():
    result = evaluate_finality(
        valid_request(
            consensus_complete=True,
            scope_valid=False,
        )
    )
    assert result.eligible is False
    assert "SCOPE" in result.blockers


def test_atomic_completion_cannot_bypass_conflict():
    result = evaluate_finality(
        valid_request(
            atomic_complete=True,
            finality_conflict=True,
        )
    )
    assert result.eligible is False
    assert "FINALITY_CONFLICT" in result.blockers


def test_reconciliation_cannot_bypass_custody_authority():
    result = evaluate_finality(
        valid_request(
            reconciliation_complete=True,
            custody_authority_valid=False,
        )
    )
    assert result.eligible is False
    assert "CUSTODY_AUTHORITY" in result.blockers


def test_custody_possession_without_valid_custody_state_is_blocked():
    result = evaluate_finality(
        valid_request(
            custody_possession=True,
            custody_state_valid=False,
        )
    )
    assert result.eligible is False
    assert "CUSTODY_STATE" in result.blockers


def test_full_execution_with_residual_is_blocked():
    result = evaluate_finality(
        valid_request(
            execution_complete=True,
            residual_exists=True,
        )
    )
    assert result.eligible is False
    assert "OBLIGATION" in result.blockers


def test_stale_temporal_authority_context_is_blocked():
    result = evaluate_finality(
        valid_request(
            temporal_valid=False,
        )
    )
    assert result.eligible is False
    assert "TEMPORAL" in result.blockers


def test_insufficient_evidence_cannot_be_compensated_by_consensus():
    result = evaluate_finality(
        valid_request(
            consensus_complete=True,
            evidence_sufficient=False,
        )
    )
    assert result.eligible is False
    assert "EVIDENCE" in result.blockers


def test_invalid_transition_cannot_be_compensated_by_all_other_valid_factors():
    result = evaluate_finality(
        valid_request(
            transition_valid=False,
        )
    )
    assert result.eligible is False
    assert "TRANSITION" in result.blockers


def test_vacuous_requirements_never_self_create_finality():
    result = evaluate_finality(
        valid_request(
            requirement_set_non_vacuous=False,
        )
    )
    assert result.eligible is False
    assert "VACUOUS_REQUIREMENTS" in result.blockers


def test_post_finality_contradiction_preserves_history_but_invalidates_current_finality():
    final = evaluate_finality(valid_request())
    assert final.classification == "FINALITY_DOMAIN_COMPLETE"

    invalidated = apply_post_finality_contradiction(final)

    assert invalidated.classification == "FINALITY_INVALIDATED"
    assert invalidated.historical_finality_preserved is True
    assert invalidated.post_finality_contradiction is True
    assert invalidated.eligible is False


def test_reopening_does_not_erase_historical_finality():
    final = evaluate_finality(valid_request())
    reopened = reopen_finality(final)

    assert reopened.classification == "FINALITY_REOPENED"
    assert reopened.historical_finality_preserved is True


def test_non_final_state_cannot_be_reopened_as_if_previously_final():
    nonfinal = evaluate_finality(
        valid_request(authority_valid=False)
    )

    try:
        reopen_finality(nonfinal)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_post_finality_contradiction_requires_previous_finality():
    nonfinal = evaluate_finality(
        valid_request(scope_valid=False)
    )

    try:
        apply_post_finality_contradiction(nonfinal)
        assert False, "Expected ValueError"
    except ValueError:
        pass
