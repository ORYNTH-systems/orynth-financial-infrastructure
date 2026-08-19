import importlib.util
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[2] / '07-ledger' / 'runtime' / 'f4_runtime' / 'runtime.py'
spec = importlib.util.spec_from_file_location('f4_runtime', RUNTIME)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

F4State = mod.F4State
decide = mod.decide
transition = mod.transition
classify_reconstruction = mod.classify_reconstruction
custody_authorized = mod.custody_authorized
ledger_matches_underlying = mod.ledger_matches_underlying
ledger_representation_is_financial_truth = mod.ledger_representation_is_financial_truth

def test_po_033_block_prevents_target_mutation():
    s = F4State(record_value='A')
    d = decide('WRITE', authority_ok=False)
    assert d == 'F4-BLOCK'
    assert transition(s, d, new_value='B') is None

def test_po_034_defer_prevents_target_mutation():
    s = F4State(record_value='A')
    d = decide('WRITE', evidence_ok=False)
    assert d == 'F4-DEFER'
    assert transition(s, d, new_value='B') is None

def test_po_035_revalidation_is_not_reopening():
    s = F4State(record_value='A', reopening_status='CLOSED')
    d = decide('REVALIDATE')
    out = transition(s, d)
    assert d == 'F4-REVALIDATE'
    assert out.reopening_status == 'CLOSED'

def test_po_036_reopening_preserves_historical_record():
    s = F4State(record_value='FINAL-A')
    d = decide('REOPEN')
    out = transition(s, d)
    assert out.reopening_status == 'REOPENED'
    assert out.historical_value == 'FINAL-A'

def test_po_037_reconstruction_not_historical_identity():
    r, identity, continuity = classify_reconstruction(reconstructed=True, identity_preserved=False, continuity_preserved=False)
    assert r == 'RECONSTRUCTED'
    assert identity == 'NOT_ESTABLISHED'

def test_po_038_reconstruction_not_continuity_preservation():
    r, identity, continuity = classify_reconstruction(reconstructed=True, identity_preserved=True, continuity_preserved=False)
    assert r == 'RECONSTRUCTED'
    assert continuity == 'NOT_ESTABLISHED'

def test_po_039_recorded_custody_does_not_create_authority():
    s = F4State(recorded_custody='PARTY-A', custody_authority=None)
    assert s.recorded_custody == 'PARTY-A'
    assert custody_authorized(s) is False

def test_po_040_ledger_representation_not_underlying_truth():
    s = F4State(record_value='100', underlying_financial_state='80')
    assert ledger_matches_underlying(s) is False
    assert ledger_representation_is_financial_truth(s) is False

def test_admit_without_transition_when_value_absent():
    s = F4State(record_value='A')
    d = decide('WRITE')
    assert d == 'F4-ADMIT'
    assert transition(s, d, new_value=None) is None

def test_matching_record_does_not_create_authority():
    s = F4State(record_value='100', underlying_financial_state='100', recorded_custody='PARTY-A', custody_authority=None)
    assert ledger_matches_underlying(s) is True
    assert custody_authorized(s) is False
