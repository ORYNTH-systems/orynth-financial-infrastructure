from dataclasses import dataclass, replace
from typing import Optional

@dataclass(frozen=True)
class F4State:
    record_value: Optional[str] = None
    historical_value: Optional[str] = None
    reopening_status: str = 'CLOSED'
    reconstruction_status: str = 'NOT_REQUIRED'
    historical_identity: str = 'NOT_ESTABLISHED'
    continuity: str = 'UNCLASSIFIED'
    recorded_custody: Optional[str] = None
    custody_authority: Optional[str] = None
    underlying_financial_state: Optional[str] = None

def decide(action: str, *, authority_ok: bool = True, evidence_ok: bool = True) -> str:
    if not authority_ok:
        return 'F4-BLOCK'
    if not evidence_ok:
        return 'F4-DEFER'
    if action == 'REVALIDATE':
        return 'F4-REVALIDATE'
    if action == 'REOPEN':
        return 'F4-REOPEN'
    return 'F4-ADMIT'

def transition(state: F4State, decision: str, *, new_value: Optional[str] = None) -> Optional[F4State]:
    if decision in {'F4-BLOCK', 'F4-DEFER'}:
        return None
    if decision == 'F4-REVALIDATE':
        return replace(state)
    if decision == 'F4-REOPEN':
        historical = state.historical_value
        if historical is None:
            historical = state.record_value
        return replace(state, historical_value=historical, reopening_status='REOPENED')
    if decision == 'F4-ADMIT':
        if new_value is None:
            return None
        return replace(state, record_value=new_value)
    raise ValueError(f'Unknown decision: {decision}')

def classify_reconstruction(*, reconstructed: bool, identity_preserved: bool, continuity_preserved: bool):
    reconstruction_status = 'RECONSTRUCTED' if reconstructed else 'NOT_REQUIRED'
    historical_identity = 'PRESERVED' if identity_preserved else 'NOT_ESTABLISHED'
    continuity = 'PRESERVED' if continuity_preserved else 'NOT_ESTABLISHED'
    return reconstruction_status, historical_identity, continuity

def custody_authorized(state: F4State) -> bool:
    return state.custody_authority is not None

def ledger_matches_underlying(state: F4State) -> bool:
    return state.record_value == state.underlying_financial_state

def ledger_representation_is_financial_truth(state: F4State) -> bool:
    return False
