"""
FIN-F2 reference runtime.

This package is a deterministic reference implementation of the locked
F2 semantics. Runtime conformance is distinct from formal proof.
"""

from .models import (
    RequirementState,
    ConsensusState,
    AdmissibilityState,
    AtomicityState,
    FinalityState,
    ReconciliationState,
    ContinuityState,
)

from .engine import (
    authority_complete,
    classify_consensus,
    classify_admissibility,
    classify_atomicity,
    classify_finality,
    classify_reconciliation,
    classify_continuity,
)
