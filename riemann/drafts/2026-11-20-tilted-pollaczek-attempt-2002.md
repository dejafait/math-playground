# Degree24 inertia attempt2002

20 November 2026. RESEARCH / REPRODUCTION under the pre-existing
SPECIALIZE assessment2000. Main gap: actual-Xi all-degree mixed
positivity (L030-L032/C032a). The sole intermediate target is the saved
degree24 negative-index diagnostic. Its possible downstream use is a
uniform finite-exception mechanism, followed by independently justified
weighted compact convergence and Xi symmetry. Those steps and
multiplicity/height payment remain open. Index at most one retains this
investigation; index at least two stops the proposed uniform one-pair
bound. A zero-containing enclosure is unresolved; a finite pass is not RH.

The supplied assessment and full source-review2001 were used, together
with discovery2000's source comparison. The scoped October30 and
step111 attempt records were read: their generic L530/L955 obstructions
do not decide this actual-family calculation. No detailed lemma input
is needed for this finite reproduction; C028b/d/f and C029j are context,
not premises. Existing unfinished work is preserved.

## Saved implementation and unfinished work

`scripts/pollaczek/tilted_degree24_inertia_2002.py` implements only the
approved Kuznetsov (2)/(4)/(13) and Coste Newton/Jacobi protocol. It
retains all beta_0,...,beta_24, u_0,...,u_26, B_2,...,B_54, all 25
weights, and exact rational basis coefficients. It normalizes to monic
only after separating the leading coefficient. Newton sums through
s_46 feed all 24 leading Hermite determinants. Sign changes are counted
only when every determinant has separated from zero; a successful
full determinant would also establish nullity zero and simplicity.
Negative index would count distinct conjugate pairs, by Coste
Theorem1.14/Plaumann Theorem1.1, not a general multiplicity census.

The fixed precision ladder is 256,512,1024,2048 bits. Each actual run
would retain complete ball strings and raw representations for inputs,
coefficients, Newton sums and determinants, version data and failures.
Decimal ball strings retain radii; no midpoint conversion or floating
root calculation is used. Incremental writes preserve incomplete runs.
The mathematical branch has **not executed or been verified**.

For implementation API details only, rechecked the already cited
[python-flint0.9 arb manual](https://python-flint.readthedocs.io/en/latest/arb.html)
(`bernoulli`, `str`, `repr`, constructor) and
[arb_mat.det](https://python-flint.readthedocs.io/en/latest/arb_mat.html#flint.arb_mat.det).
This is not new literature coverage or a changed mathematical method.
Full mathematical citations/hypotheses remain in source-review2001;
no result is installed in lemmas, and Mathlib coverage is unchecked.

## Runtime failure and evidence

Read-only import checks found no flint in Homebrew Python3.12,3.13,
3.14,3.15 or default Python3 (3.15). No binding was found at the
checked notebook/parent or temporary virtualenv paths, Homebrew library
paths, or the existing uv dependency cache. The bounded provisioning
command was:

```sh
UV_CACHE_DIR=/private/tmp/riemann-uv-cache-2002 uv pip install --python /opt/homebrew/bin/python3.13 --target /private/tmp/riemann-flint-2002 python-flint==0.9.0
```

It failed after three retries: DNS lookup of pypi.org failed. No
authorized runtime became available. The script's preflight run writes
`scripts/pollaczek/tilted-degree24-inertia-2002.json`, explicitly
reporting RUNTIME_BLOCKED, zero evaluated coefficients/determinants,
and no degree or inertia conclusion. Syntax parsing is only a
program check, not mathematical verification.

Reproduce after an authorized python-flint0.9 runtime is available:

```sh
PYTHONPATH=/private/tmp/riemann-flint-2002 /opt/homebrew/bin/python3.13 scripts/pollaczek/tilted_degree24_inertia_2002.py
```

Outcome STALLED: no mathematical evidence for either side of the
threshold. This is the first observed runtime failure for the ready
calculation, not persistent source blockage or an exhausted mechanism.
Retry only after actual runtime availability changes. The next target
and assessment remain unchanged. No uniform mechanism currently
justifies creative routing; merely extending a numerical pattern would
not supply one. PROOF/DAG and all canonical proofs remain unchanged.
