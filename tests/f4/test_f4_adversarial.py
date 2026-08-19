import importlib.util
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[2] / '07-ledger' / 'runtime' / 'f4_runtime' / 'runtime.py'
spec = importlib.util.spec_from_file_location('f4_runtime_adv', RUNTIME)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

F4State = mod.F4State
decide = mod.decide
transition = mod.transition
classify_reconstruction = mod.classify_reconstruction
custody_authorized = mod.custody_authorized
ledger_matches_underlying = mod.ledger_matches_underlying
ledger_representation_is_financial_truth = mod.ledger_representation_is_financial_truth

def test_adv_001_committed_like_record_does_not_override_authority_block():
    s = F4State(record_value='COMMITTED-A')
    d = decide('WRITE', authority_ok=False, evidence_ok=True)
    assert d == 'F4-BLOCK'
    assert transition(s, d, new_value='COMMITTED-B') is None

def test_adv_002_matching_state_does_not_convert_block_to_admit():
    s = F4State(record_value='100', underlying_financial_state='100')
    assert ledger_matches_underlying(s) is True
    assert decide('WRITE', authority_ok=False) == 'F4-BLOCK'

def test_adv_003_recorded_custody_cannot_self_authorize():
    s = F4State(recorded_custody='A', custody_authority=None)
    assert custody_authorized(s) is False

def test_adv_004_reconstruction_content_equality_does_not_force_identity():
    r, identity, continuity = classify_reconstruction(reconstructed=True, identity_preserved=False, continuity_preserved=True)
    assert r == 'RECONSTRUCTED'
    assert identity == 'NOT_ESTABLISHED'
    assert continuity == 'PRESERVED'

def test_adv_005_reconstruction_does_not_force_continuity():
    r, identity, continuity = classify_reconstruction(reconstructed=True, identity_preserved=True, continuity_preserved=False)
    assert r == 'RECONSTRUCTED'
    assert identity == 'PRESERVED'
    assert continuity == 'NOT_ESTABLISHED'

def test_adv_006_revalidation_cannot_be_used_as_reopen():
    s = F4State(record_value='A', historical_value='H', reopening_status='CLOSED')
    out = transition(s, decide('REVALIDATE'))
    assert out.reopening_status == 'CLOSED'
    assert out.historical_value == 'H'

def test_adv_007_reopen_preserves_existing_history():
    s = F4State(record_value='CURRENT', historical_value='ORIGINAL')
    out = transition(s, decide('REOPEN'))
    assert out.reopening_status == 'REOPENED'
    assert out.historical_value == 'ORIGINAL'

def test_adv_008_reopen_captures_history_if_missing():
    s = F4State(record_value='FINAL')
    out = transition(s, decide('REOPEN'))
    assert out.historical_value == 'FINAL'

def test_adv_009_block_dominates_valid_evidence():
    assert decide('WRITE', authority_ok=False, evidence_ok=True) == 'F4-BLOCK'

def test_adv_010_defer_when_authority_valid_but_evidence_missing():
    assert decide('WRITE', authority_ok=True, evidence_ok=False) == 'F4-DEFER'

def test_adv_011_authority_failure_dominates_evidence_failure():
    assert decide('WRITE', authority_ok=False, evidence_ok=False) == 'F4-BLOCK'

def test_adv_012_admit_without_transition_is_possible():
    s = F4State(record_value='A')
    d = decide('WRITE')
    assert d == 'F4-ADMIT'
    assert transition(s, d, new_value=None) is None

def test_adv_013_admit_with_transition_does_not_establish_truth():
    s = F4State(record_value='A', underlying_financial_state='REAL')
    out = transition(s, decide('WRITE'), new_value='FALSE')
    assert out.record_value == 'FALSE'
    assert ledger_matches_underlying(out) is False
    assert ledger_representation_is_financial_truth(out) is False

def test_adv_014_unknown_decision_fails_closed():
    s = F4State(record_value='A')
    try:
        transition(s, 'F4-UNKNOWN', new_value='B')
        assert False, 'unknown decision must fail'
    except ValueError:
        pass

def test_adv_015_block_does_not_erase_existing_record():
    s = F4State(record_value='HISTORICAL-A')
    assert transition(s, 'F4-BLOCK', new_value='B') is None
    assert s.record_value == 'HISTORICAL-A'

def test_adv_016_defer_does_not_mutate_existing_record():
    s = F4State(record_value='A')
    assert transition(s, 'F4-DEFER', new_value='B') is None
    assert s.record_value == 'A'

def test_adv_017_ledger_truth_function_never_promotes_representation():
    s1 = F4State(record_value='100', underlying_financial_state='100')
    s2 = F4State(record_value='100', underlying_financial_state='80')
    assert ledger_representation_is_financial_truth(s1) is False
    assert ledger_representation_is_financial_truth(s2) is False

def test_adv_018_reopen_does_not_change_current_record_value():
    s = F4State(record_value='FINAL-A')
    out = transition(s, decide('REOPEN'))
    assert out.record_value == 'FINAL-A'

def test_adv_019_revalidation_is_idempotent_for_record_state():
    s = F4State(record_value='A', historical_value='H', reopening_status='CLOSED')
    out1 = transition(s, decide('REVALIDATE'))
    out2 = transition(out1, decide('REVALIDATE'))
    assert out1 == out2

def test_adv_020_financial_state_can_diverge_after_valid_record_transition():
    s = F4State(record_value='A', underlying_financial_state='REAL')
    out = transition(s, decide('WRITE'), new_value='B')
    assert out.record_value == 'B'
    assert out.underlying_financial_state == 'REAL'
    assert ledger_matches_underlying(out) is False
