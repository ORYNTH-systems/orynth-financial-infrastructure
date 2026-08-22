# F1 Compensation Evidence Requirements

Every compensation chain must preserve evidence linking:

originating execution
-> originating effect
-> compensation requirement determination
-> compensation proposal
-> compensation authority
-> compensation admission
-> compensation execution
-> compensation effect
-> resulting state
-> later reconciliation where applicable.

Required properties:

1. Originating and compensating event IDs remain distinct.

2. The original event remains present in historical lineage.

3. Compensation authority must be attributable independently.

4. Reuse of an originating authorization artifact must be detectable.

5. Compensation scope must be separately evidenced.

6. Compensation effect classification must use the F1 effect-state algebra.

7. A completed compensation must not overwrite prior effect evidence.

8. Recursive compensation chains must remain ordered and reconstructable.

The evidence model must support:

e_0 -> e_c1 -> e_c2 -> ... -> e_cn

without reducing the chain to only the final economic balance.
