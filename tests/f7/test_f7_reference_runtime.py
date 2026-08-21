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
    evidence_implies_authority,
    technical_reach_implies_authority,
)

def test_absent_authority_requires_reauthorization_even_with_reach():
    req = F7Request(technical_reach=True, jurisdictions=(JurisdictionBoundary(authority_active=False),))
    assert decide(req) == Decision.REAUTHORIZE

def test_authority_in_one_jurisdiction_does_not_cover_second():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(authority_active=False),
    ))
    assert complete_coverage(req) is False
    assert partial_coverage(req) is True
    assert decide(req) == Decision.REAUTHORIZE

def test_blocking_restriction_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(blocking_restriction=True),))
    assert decide(req) == Decision.BLOCK

def test_blocking_conflict_blocks():
    req = F7Request(jurisdictions=(JurisdictionBoundary(blocking_conflict=True),))
    assert decide(req) == Decision.BLOCK

def test_nonattenuated_delegation_blocks():
    req = F7Request(delegation_used=True, delegation_attenuated=False)
    assert decide(req) == Decision.BLOCK

def test_defer_keeps_transition_undefined():
    req = F7Request(evidence_resolved=False)
    assert decide(req) == Decision.DEFER
    assert transition_exists(req) is False

def test_revalidate_keeps_transition_undefined():
    req = F7Request(revalidation_required=True)
    assert decide(req) == Decision.REVALIDATE
    assert transition_exists(req) is False

def test_evidence_and_reach_do_not_constitute_authority():
    assert evidence_implies_authority() is False
    assert technical_reach_implies_authority() is False

def test_admit_requires_operation_preconditions_for_transition():
    req = F7Request(operation_preconditions_satisfied=False)
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is False

def test_complete_multijurisdiction_coverage_admits():
    req = F7Request(jurisdictions=(
        JurisdictionBoundary(),
        JurisdictionBoundary(),
    ))
    assert complete_coverage(req) is True
    assert partial_coverage(req) is False
    assert decide(req) == Decision.ADMIT
    assert transition_exists(req) is True
