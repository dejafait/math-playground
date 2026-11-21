# Independent centred-moment audit — step136 (unfinished)

Target and ready coverage: exact target in
`drafts/literature/2026-11-10-centred-moment-independent-audit-135.md`
(SPECIALIZE, saved before invocation). Reproduction, not new mathematics.

The main gap remains L030–L032/C032a. The bounded target would pay only
L960’s complete-support M32<81/4 premise. Continue only on all closed
cases and directed leaf upper bounds; no midpoint maximum is sufficient.

Source checker at commit18dbc01ea36bf9a24d8f79822b5ce06b545e4ace and
Theorem3.3 proof were inspected. Shell download failed DNS. Default
Python3.15 and Python3.12/3.13/3.14 lack flint. An isolated Python3.12
venv in /private/tmp/riemann-moment-136-venv was created; pip installation
of python-flint0.9.0 failed DNS. Narrow pip-wheel and uv-cache searches
found no flint package. No source hash, Arb execution or bound verified.

The analytic reduction audit is now preserved canonically in L960 under
“Partial independent audit of the moment premise (step136)”: coefficient
normalization, closed walls, complete-support comparison, convex derivative
control, strict sum/integral comparison and erfi differentiation. These are
source reproductions conditional on the unexecuted finite inequalities.
No new moment theorem or new lemma is claimed.

The exact-integer portion of
`scripts/centred-moment/independent_audit_136.py` ran successfully:
151 adjacent leaves, terminal3100000,914 named gates. Its certificate
`scripts/centred-moment/independent-audit-136.json` is INCOMPLETE:
5 exact global gates passed,0 failed,909 unexecuted, actual moment
upper bound null. The complete selected integer-check, gate-count and
failure fields were inspected with the JSON inspector’s --full option.
The Arb branch is unexecuted/unvalidated and must not be presented as
an independent reproduction of the bound. The 192-bit attempt ended at
ModuleNotFoundError before numerical work; no 256-bit rerun is justified.

No mathematical defect in the inspected analytic reduction was found.
This does not validate the paper’s numerical inputs, release or global
claims. A working Arb runtime is a prerequisite for another replay;
repeating source searches or the same failing installation is not a
new mathematical test. This was one incomplete mathematical attempt,
outcome EXPLORATION, classification REPRODUCTION, not an advance or
informative refutation. All independent L960/RH gaps remain.
