import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[3]
RUNTIME_PARENT = REPO / "reference-runtime"

sys.path.insert(0, str(RUNTIME_PARENT))

from f1.effect_engine import classify_effect
from f1.residual_engine import compute_residual_vector
from f1.remediation_engine import (
    append_remediation,
    classify_compensation,
    classify_reversal,
    executable,
)
from f1.reconciliation_engine import (
    classify_continuity,
    classify_reconciliation,
    full_current_state_equivalent,
    historical_equivalent,
    projected_equivalent,
)
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


class MissingEvidenceAttacks(unittest.TestCase):

    def test_missing_evidence_cannot_be_no_effect(self):
        signature = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=0,
                evidence_present=False,
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_INDETERMINATE,
        )

        self.assertNotEqual(
            signature.global_class,
            GlobalEffectClass.E_NO_EFFECT,
        )

    def test_missing_relational_evidence_cannot_be_zero_by_default(self):
        signature = classify_effect([
            EffectDimension(
                "ownership",
                DimensionType.RELATIONAL,
                intended="B",
                observed=None,
                evidence_present=False,
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_INDETERMINATE,
        )


class PartialEffectCollapseAttacks(unittest.TestCase):

    def test_partial_quantity_not_completed(self):
        signature = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=60,
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_PARTIAL,
        )

        self.assertNotEqual(
            signature.global_class,
            GlobalEffectClass.E_COMPLETED,
        )

    def test_partial_party_coverage_not_completed(self):
        signature = classify_effect([
            EffectDimension(
                "parties",
                DimensionType.SET_VALUED,
                intended=["A", "B", "C"],
                observed=["A", "B"],
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_PARTIAL,
        )

    def test_partial_graph_propagation_not_completed(self):
        signature = classify_effect([
            EffectDimension(
                "propagation",
                DimensionType.GRAPH_STATE,
                intended={
                    "nodes": ["A", "B", "C"],
                    "edges": [["A", "B"], ["B", "C"]],
                },
                observed={
                    "nodes": ["A", "B"],
                    "edges": [["A", "B"]],
                },
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_PARTIAL,
        )


class ContradictionAndOverEffectAttacks(unittest.TestCase):

    def test_wrong_owner_not_partial_or_complete(self):
        signature = classify_effect([
            EffectDimension(
                "owner",
                DimensionType.RELATIONAL,
                intended="B",
                observed="C",
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_MIXED,
        )

    def test_over_effect_not_completed(self):
        signature = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=120,
            )
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_MIXED,
        )

    def test_mixed_full_and_contradictory_not_completed(self):
        signature = classify_effect([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=100,
            ),
            EffectDimension(
                "owner",
                DimensionType.RELATIONAL,
                intended="B",
                observed="C",
            ),
        ])

        self.assertEqual(
            signature.global_class,
            GlobalEffectClass.E_MIXED,
        )


class CompensationAttacks(unittest.TestCase):

    def test_wrong_dimension_compensation(self):
        outcome = classify_compensation(
            target_resolved=False,
            partial_progress=False,
            wrong_dimension=True,
        )

        self.assertEqual(
            outcome,
            CompensationOutcome.COMP_WRONG_DIMENSION,
        )

    def test_over_compensation_not_exact(self):
        outcome = classify_compensation(
            target_resolved=True,
            partial_progress=False,
            over=True,
        )

        self.assertEqual(
            outcome,
            CompensationOutcome.COMP_OVER,
        )

        self.assertNotEqual(
            outcome,
            CompensationOutcome.COMP_EXACT,
        )

    def test_new_divergence_not_exact(self):
        outcome = classify_compensation(
            target_resolved=True,
            partial_progress=False,
            new_divergence=True,
        )

        self.assertEqual(
            outcome,
            CompensationOutcome.COMP_NEW_DIVERGENCE,
        )

    def test_contradictory_compensation_not_partial_success(self):
        outcome = classify_compensation(
            target_resolved=False,
            partial_progress=True,
            contradictory=True,
        )

        self.assertEqual(
            outcome,
            CompensationOutcome.COMP_CONTRADICTORY,
        )


class CompensationAuthorityAttacks(unittest.TestCase):

    def test_compensation_required_does_not_create_executability(self):
        remediation = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=False,
            consequential=True,
        )

        self.assertFalse(executable(remediation))

    def test_parent_admission_cannot_authorize_child(self):
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


class ReversalAttacks(unittest.TestCase):

    def test_stale_target_does_not_become_exact(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
            stale_target=True,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_STALE_TARGET,
        )

    def test_non_reversible_dimension_does_not_become_exact(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
            non_reversible=True,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_NON_REVERSIBLE,
        )

    def test_intervening_conflict_does_not_become_exact(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
            intervening_conflict=True,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_INTERVENING_CONFLICT,
        )

    def test_wrong_object_reversal(self):
        outcome = classify_reversal(
            target_resolved=False,
            partial_progress=False,
            wrong_object=True,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_WRONG_OBJECT,
        )

    def test_over_reversal_not_exact(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
            over=True,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_OVER,
        )


class ReversalAuthorityAttacks(unittest.TestCase):

    def test_reversal_required_does_not_create_executability(self):
        reversal = RemediationEvent(
            event_id="r1",
            event_type="REVERSAL",
            parent_event_id="e0",
            depth=1,
            admitted=False,
            consequential=True,
        )

        self.assertFalse(executable(reversal))


class RemediationDepthAttacks(unittest.TestCase):

    def test_invalid_depth_rejected(self):
        root = RemediationEvent(
            event_id="e0",
            event_type="ORIGIN",
            parent_event_id=None,
            depth=0,
            admitted=True,
            consequential=True,
        )

        malformed = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=5,
            admitted=True,
            consequential=True,
        )

        history = History(events=[root])

        with self.assertRaises(ValueError):
            append_remediation(history, malformed)

    def test_missing_parent_rejected(self):
        root = RemediationEvent(
            event_id="e0",
            event_type="ORIGIN",
            parent_event_id=None,
            depth=0,
            admitted=True,
            consequential=True,
        )

        malformed = RemediationEvent(
            event_id="c2",
            event_type="COMPENSATION",
            parent_event_id="missing",
            depth=1,
            admitted=True,
            consequential=True,
        )

        history = History(events=[root])

        with self.assertRaises(ValueError):
            append_remediation(history, malformed)


class HistoryReplacementAttacks(unittest.TestCase):

    def test_append_does_not_replace_origin(self):
        root = RemediationEvent(
            event_id="e0",
            event_type="ORIGIN",
            parent_event_id=None,
            depth=0,
            admitted=True,
            consequential=True,
        )

        comp = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=True,
            consequential=True,
        )

        before = History(events=[root])
        after = append_remediation(before, comp)

        self.assertEqual(
            [x.event_id for x in before.events],
            ["e0"],
        )

        self.assertEqual(
            [x.event_id for x in after.events],
            ["e0", "c1"],
        )

    def test_exact_compensation_cannot_make_histories_equal(self):
        self.assertFalse(
            historical_equivalent(
                ["origin-partial", "compensation-exact"],
                ["prior"],
            )
        )

    def test_exact_reversal_cannot_make_histories_equal(self):
        self.assertFalse(
            historical_equivalent(
                ["origin", "reversal"],
                ["prior"],
            )
        )


class ReconciliationCollapseAttacks(unittest.TestCase):

    def test_unresolved_residual_prevents_reconciled_class(self):
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

    def test_missing_evidence_prevents_reconciliation(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=100,
            )
        ])

        result = classify_reconciliation(
            history_explainable=True,
            evidence_sufficient=False,
            residuals=residuals,
        )

        self.assertEqual(
            result,
            ReconciliationClass.INDETERMINATE,
        )

    def test_unexplainable_history_prevents_reconciliation(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=100,
            )
        ])

        result = classify_reconciliation(
            history_explainable=False,
            evidence_sufficient=True,
            residuals=residuals,
        )

        self.assertEqual(
            result,
            ReconciliationClass.INDETERMINATE,
        )


class EquivalenceCollapseAttacks(unittest.TestCase):

    def test_projected_equality_not_full_state_equality(self):
        a = {
            "cash": 100,
            "owner": "B",
        }

        b = {
            "cash": 100,
            "owner": "C",
        }

        self.assertTrue(
            projected_equivalent(a, b, ["cash"])
        )

        self.assertFalse(
            full_current_state_equivalent(a, b)
        )

    def test_full_current_equality_not_historical_equality(self):
        a = {
            "cash": 100,
            "owner": "B",
        }

        b = {
            "cash": 100,
            "owner": "B",
        }

        self.assertTrue(
            full_current_state_equivalent(a, b)
        )

        self.assertFalse(
            historical_equivalent(
                ["origin", "compensation"],
                ["prior"],
            )
        )


class ContinuityCollapseAttacks(unittest.TestCase):

    def test_function_restored_not_preserved(self):
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

        self.assertNotEqual(
            result,
            ContinuityClass.PRESERVED,
        )

    def test_reconstructed_not_preserved(self):
        result = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertEqual(
            result,
            ContinuityClass.RECONSTRUCTED,
        )

        self.assertNotEqual(
            result,
            ContinuityClass.PRESERVED,
        )

    def test_break_survives_later_state_equivalence(self):
        prior = {
            "cash": 100,
            "owner": "B",
        }

        after = {
            "cash": 100,
            "owner": "B",
        }

        self.assertTrue(
            full_current_state_equivalent(prior, after)
        )

        result = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertNotEqual(
            result,
            ContinuityClass.PRESERVED,
        )

    def test_missing_continuity_evidence_is_indeterminate(self):
        result = classify_continuity(
            continuity_break_demonstrated=False,
            history_reconstructable=False,
            function_available=True,
            evidence_sufficient=False,
        )

        self.assertEqual(
            result,
            ContinuityClass.INDETERMINATE,
        )


class CountermodelObligationAttacks(unittest.TestCase):

    def test_ce001(self):
        required = True

        event = RemediationEvent(
            event_id="c1",
            event_type="COMPENSATION",
            parent_event_id="e0",
            depth=1,
            admitted=False,
            consequential=True,
        )

        self.assertTrue(required)
        self.assertFalse(executable(event))

    def test_ce002(self):
        required = True

        event = RemediationEvent(
            event_id="r1",
            event_type="REVERSAL",
            parent_event_id="e0",
            depth=1,
            admitted=False,
            consequential=True,
        )

        self.assertTrue(required)
        self.assertFalse(executable(event))

    def test_ce003(self):
        outcome = classify_compensation(
            target_resolved=True,
            partial_progress=False,
        )

        self.assertEqual(
            outcome,
            CompensationOutcome.COMP_EXACT,
        )

        self.assertFalse(
            historical_equivalent(
                ["origin-partial", "compensation-exact"],
                ["prior"],
            )
        )

    def test_ce004(self):
        outcome = classify_reversal(
            target_resolved=True,
            partial_progress=False,
        )

        self.assertEqual(
            outcome,
            ReversalOutcome.REV_EXACT,
        )

        self.assertFalse(
            historical_equivalent(
                ["origin", "reversal-exact"],
                ["prior"],
            )
        )

    def test_ce005(self):
        result = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertNotEqual(
            result,
            ContinuityClass.PRESERVED,
        )

    def test_ce006(self):
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

    def test_ce007(self):
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

    def test_ce008(self):
        a = {
            "cash": 100,
            "owner": "B",
        }

        b = {
            "cash": 100,
            "owner": "C",
        }

        self.assertTrue(
            projected_equivalent(a, b, ["cash"])
        )

        self.assertFalse(
            historical_equivalent(
                ["origin", "compensation"],
                ["prior"],
            )
        )

    def test_ce009(self):
        residuals = compute_residual_vector([
            EffectDimension(
                "cash",
                DimensionType.QUANTITATIVE,
                intended=100,
                observed=100,
            )
        ])

        self.assertTrue(
            all(r.resolved for r in residuals)
        )

        result = classify_continuity(
            continuity_break_demonstrated=True,
            history_reconstructable=True,
            function_available=True,
            evidence_sufficient=True,
        )

        self.assertNotEqual(
            result,
            ContinuityClass.PRESERVED,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
