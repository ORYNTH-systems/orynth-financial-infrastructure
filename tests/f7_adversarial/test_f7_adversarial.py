import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "10-cross-jurisdiction" / "runtime"))

from f7_reference_runtime import (
    Decision,
    F7Request,
    JurisdictionBoundary,
    complete_coverage,
    partial_coverage,
    decide,
    transition_exists,
)

def test_reach_without_authority_never_admits():
    req = F7Request(technical_reach=True, jurisdictions=(JurisdictionBoundary(authority_active=False),))
    assert decide(req) != Decision.ADMIT

def test_one_valid_jurisdiction_cannot_universalize_authority():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(authority_active=False),
    ))
    assert complete_coverage(req) is False
    assert decide(req) != Decision.ADMIT

def test_partial_coverage_is_detected():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(scope_valid=False),
    ))
    assert partial_coverage(req) is True
    assert complete_coverage(req) is False

def test_inapplicable_jurisdiction_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(applicable=False),))
    assert decide(req) == Decision.BLOCK

def test_expired_temporal_authority_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(temporal_valid=False),))
    assert decide(req) == Decision.BLOCK

def test_scope_overreach_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(scope_valid=False),))
    assert decide(req) == Decision.BLOCK

def test_unsupported_authority_source_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(authority_source_supported=False),))
    assert decide(req) == Decision.BLOCK

def test_blocking_restriction_cannot_be_bypassed_by_reach():
    req = F7Request(technical_reach=True, jurisdictions=(JurisdictionBoundary(blocking_restriction=True),))
    assert decide(req) == Decision.BLOCK

def test_blocking_conflict_cannot_be_bypassed_by_reach():
    req = F7Request(technical_reach=True, jurisdictions=(JurisdictionBoundary(blocking_conflict=True),))
    assert decide(req) == Decision.BLOCK

def test_nonattenuated_delegation_blocks_even_with_valid_authority():
    req = F7Request(delegation_used=True, delegation_source_valid=True, delegation_attenuated=False)
    assert decide(req) == Decision.BLOCK

def test_invalid_delegation_source_blocks():
    req = F7Request(delegation_used=True, delegation_source_valid=False, delegation_attenuated=True)
    assert decide(req) == Decision.BLOCK

def test_missing_global_evidence_defers():
    req = F7Request(evidence_resolved=False)
    assert decide(req) == Decision.DEFER
    assert transition_exists(req) is False

def test_missing_jurisdiction_evidence_defers():
    req = F7Request(jurisdictions=(JurisdictionBoundary(evidence_sufficient=False),))
    assert decide(req) == Decision.DEFER
    assert transition_exists(req) is False

def test_revalidation_preempts_admission():
    req = F7Request(revalidation_required=True)
    assert decide(req) == Decision.REVALIDATE
    assert transition_exists(req) is False

def test_absent_authority_requires_reauthorization():
    req = F7Request(jurisdictions=(JurisdictionBoundary(authority_active=False),))
    assert decide(req) == Decision.REAUTHORIZE
    assert transition_exists(req) is False

def test_no_jurisdiction_set_cannot_admit():
    req = F7Request(jurisdictions=())
    assert decide(req) == Decision.DEFER
    assert transition_exists(req) is False

def test_admit_without_operation_preconditions_does_not_transition():
    req = F7Request(operation_preconditions_satisfied=False)
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is False

def test_two_valid_jurisdictions_and_preconditions_transition():
    req = F7Request(jurisdictions=(JurisdictionBoundary(), JurisdictionBoundary()))
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is True

def test_three_jurisdictions_one_blocking_conflict_blocks_all():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(blocking_conflict=True),
        JurisdictionBoundary(),
    ))
    assert decide(req) == Decision.BLOCK

def test_three_jurisdictions_one_blocking_restriction_blocks_all():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(),
        JurisdictionBoundary(blocking_restriction=True),
    ))
    assert decide(req) == Decision.BLOCK
