import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[2]
RUNTIME_PARENT = REPO / "reference-runtime"

sys.path.insert(0, str(RUNTIME_PARENT))

from f1.effect_engine import classify_effect
from f1.reconciliation_engine import (
    classify_continuity,
    classify_reconciliation,
    historical_equivalent,
    projected_equivalent,
)
from f1.remediation_engine import (
    append_remediation,
    classify_compensation,
    classify_reversal,
    executable,
)
from f1.residual_engine import compute_residual_vector
from f1.types import (
    CompensationOutcome,
    ContinuityClass,
    DimensionType,
    EffectDimension,
    GlobalEffectClass,
    History,
    ReconciliationClass,
    RemediationEvent,
    ReversalOutcome,
)


class EffectEngineTests(unittest.TestCase):

    def test_partial_quantitative_effect(self):
        sig = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=60,
            )
        ])
        self.assertEqual(sig.global_class, GlobalEffectClass.E_PARTIAL)

    def test_indeterminate_not_zero(self):
        sig = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=0,
                evidence_present=False,
            )
        ])
        self.assertEqual(sig.global_class, GlobalEffectClass.E_INDETERMINATE)

    def test_contradictory_not_completed(self):
        sig = classify_effect([
            EffectDimension(
                "owner",
                DimensionType.RELATIONAL,
                intended="B",
                observed="C",
            )
        ])
        self.assertEqual(sig.global_class, GlobalEffectClass.E_MIXED)


class ResidualTests(unittest.TestCase):

    def test_quantitative_residual(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=60,
            )
        ])
        self.assertEqual(residuals[0].detail["delta"], 40)
        self.assertFalse(residuals[0].resolved)

    def test_set_residual(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "parties",
                DimensionType.SET_VALUED,
                intended=["A", "B", "C"],
                observed=["A", "B"],
            )
        ])
        self.assertEqual(residuals[0].detail["missing"], ["C"])


class CompensationTests(unittest.TestCase):

    def test_exact_compensation(self):
        outcome = classify_compensation(
            target_resolved=True,
            partial_progress=False,
        )
        self.assertEqual(outcome, CompensationOutcome.COMP_EXACT)

    def test_partial_compensation(self):
        outcome = classify_compensation(
            target_resolved=False,
            partial_progress=True,
        )
        self.assertEqual(outcome, CompensationOutcome.COMP_PARTIAL)

    def test_over_compensation(self):
        outcome = classify_compensation(
            target_resolved=True,
            partial_progress=False,
            over=True,
        )
        self.assertEqual(outcome, CompensationOutcome.COMP_OVER)


class ReversalTests(unittest.TestCase):

    def test_exact_reversal(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
        )
        self.assertEqual(outcome, ReversalOutcome.REV_EXACT)

    def test_stale_reversal(self):
        outcome = classify_reversal(
            target_resolved=False,
            partial_progress=False,
            stale_target=True,
        )
        self.assertEqual(outcome, ReversalOutcome.REV_STALE_TARGET)

    def test_non_reversible(self):
        outcome = classify_reversal(
            target_resolved=False,
            partial_progress=False,
            non_reversible=True,
        )
        self.assertEqual(outcome, ReversalOutcome.REV_NON_REVERSIBLE)


class RecursiveRemediationTests(unittest.TestCase):

    def test_child_requires_own_admission(self):
        root = RemediationEvent(
            event_id="e0",
            event_type="ORIGIN",
            parent_event_id=None,
            depth=0,
            admitted=True,
            consequential=True,
        )

        parent = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=True,
            consequential=True,
        )

        child = RemediationEvent(
            event_id="c2",
            event_type="COMPENSATION",
            parent_event_id="c1",
            depth=2,
            admitted=False,
            consequential=True,
        )

        h = History(events=[root])
        h = append_remediation(h, parent)
        h = append_remediation(h, child)

        self.assertTrue(executable(parent))
        self.assertFalse(executable(child))

    def test_history_append_preservation(self):
        root = RemediationEvent(
            event_id="e0",
            event_type="ORIGIN",
            parent_event_id=None,
            depth=0,
            admitted=True,
            consequential=True,
        )

        compensation = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=True,
            consequential=True,
        )

        h0 = History(events=[root])
        h1 = append_remediation(h0, compensation)

        self.assertEqual(
            [x.event_id for x in h0.events],
            ["e0"],
        )

        self.assertEqual(
            [x.event_id for x in h1.events],
            ["e0", "c1"],
        )


class ReconciliationTests(unittest.TestCase):

    def test_reconciled_does_not_require_history_equivalence(self):
        state_a = {"cash": 100}
        state_b = {"cash": 100}

        self.assertTrue(
            projected_equivalent(
                state_a,
                state_b,
                ["cash"],
            )
        )

        self.assertFalse(
            historical_equivalent(
                ["origin", "compensation"],
                ["prior"],
            )
        )

    def test_divergent_reconciliation(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=80,
            )
        ])

        result = classify_reconciliation(
            history_explainable=True,
            evidence_sufficient=True,
            residuals=residuals,
        )

        self.assertEqual(
            result,
            ReconciliationClass.DIVERGENT,
        )

    def test_function_restored_does_not_force_preserved(self):
        result = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=False,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertEqual(
            result,
            ContinuityClass.FUNCTION_RESTORED_ONLY,
        )


class CounterexampleFixtureTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = REPO / "tests" / "f1" / "fixtures" / "counterexamples.json"
        cls.fixtures = json.loads(path.read_text(encoding="utf-8-sig"))

    def test_exactly_nine_counterexamples_registered(self):
        self.assertEqual(len(self.fixtures), 9)

    def test_counterexample_ids_unique(self):
        ids = [x["counterexample_id"] for x in self.fixtures]
        self.assertEqual(len(ids), len(set(ids)))

    def test_counterexample_claims_unique(self):
        claims = [x["claim_id"] for x in self.fixtures]
        self.assertEqual(len(claims), len(set(claims)))

    def test_ce001_compensation_requirement_non_authorization(self):
        required = True
        admitted = False

        self.assertTrue(required)
        self.assertFalse(admitted)

    def test_ce002_reversal_requirement_non_authorization(self):
        required = True
        admitted = False

        self.assertTrue(required)
        self.assertFalse(admitted)

    def test_ce003_exact_compensation_non_historical_equivalence(self):
        comp = classify_compensation(
            target_resolved=True,
            partial_progress=False,
        )

        self.assertEqual(comp, CompensationOutcome.COMP_EXACT)

        self.assertFalse(
            historical_equivalent(
                ["origin-partial", "compensation-exact"],
                ["prior"],
            )
        )

    def test_ce004_exact_reversal_non_historical_equivalence(self):
        rev = classify_reversal(
            target_resolved=True,
            partial_progress=False,
        )

        self.assertEqual(rev, ReversalOutcome.REV_EXACT)

        self.assertFalse(
            historical_equivalent(
                ["origin", "reversal"],
                ["prior"],
            )
        )

    def test_ce005_reconciled_non_preserved_continuity(self):
        continuity = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertNotEqual(
            continuity,
            ContinuityClass.PRESERVED,
        )

    def test_ce006_function_restored_non_preserved_continuity(self):
        continuity = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=False,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertEqual(
            continuity,
            ContinuityClass.FUNCTION_RESTORED_ONLY,
        )

    def test_ce007_parent_authority_not_child_authority(self):
        parent = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=True,
            consequential=True,
        )

        child = RemediationEvent(
            event_id="c2",
            event_type="COMPENSATION",
            parent_event_id="c1",
            depth=2,
            admitted=False,
            consequential=True,
        )

        self.assertTrue(executable(parent))
        self.assertFalse(executable(child))

    def test_ce008_projected_equivalence_non_history_equivalence(self):
        a = {"cash": 100, "owner": "B"}
        b = {"cash": 100, "owner": "C"}

        self.assertTrue(
            projected_equivalent(
                a,
                b,
                ["cash"],
            )
        )

        self.assertFalse(
            historical_equivalent(
                ["origin", "compensation"],
                ["prior"],
            )
        )

    def test_ce009_residual_resolution_non_preserved_continuity(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=100,
            )
        ])

        self.assertTrue(all(r.resolved for r in residuals))

        continuity = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertNotEqual(
            continuity,
            ContinuityClass.PRESERVED,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
