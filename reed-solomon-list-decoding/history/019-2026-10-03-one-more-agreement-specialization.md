# 2026-10-03 — One additional agreement: coefficient-fiber specialization

Completed one mathematical attempt on the saved SPECIALIZE-ready target.
Reused the prior assessment without further literature work; preserved
existing changes, failed approaches and the parked ABF26/source route.

[L012](../lemmas/L012-one-more-agreement-coefficient-fibers.md) proves that
the fixed next coefficient gives an exact single-center subset-sum list
at k+1 agreements, with strict degree less than k and simultaneous
agreement for every m. It checks coset/subfield rescaling and imports
Li-Wan's Theorem 1.2 rather than reproducing its sieve. On the 16-point
domain F_17^* inside F_{17^32}, the four attained lists exceed the actual
epsilon*=2^-128 threshold, while that threshold is greater than one.
Thus t_star<=n-k-2: one more grid point is excluded beyond L011's
endpoint result. The proposed continuation test succeeds in this instance.

Outcome: ADVANCE, a relevant local mathematical input; STEP_KIND: RESEARCH;
classification: REPRODUCTION. The scalar construction and count are known.
No progress beyond the checked literature or complete candidate is claimed;
STATUS stays IN_PROGRESS. The exact general boundary and proper-subgroup
largest fibers remain unresolved. A failed lower estimate would not certify
safety, and the subfield count never replaces the ambient field in the
threshold. Exploration turns used: 0/3 following this local advance.

The next direction uses the assessment's verbatim preapproved count
application, with the proper order-1024 subgroup of F_65537 in the ambient
F_{65537^28} as specified in the checkpoint. This tests whether Zhu-Wan's
per-fiber estimate certifies an explicit zero-sum center when the exact
full-nonzero-field formula is unavailable. Coverage is already ready; no
new literature gate or calculation for that instance was undertaken here.

Independent interpolation, exhaustive subset-sum enumeration and the two
smallest scalar-message dimensions passed in
`scripts/coefficient-fibers/verify.py`; the
[saved output](../scripts/coefficient-fibers/results.json) also checks a
nontrivial coset in F_97, widths 1 and 3 and the exact cryptographic-threshold
arithmetic. These finite checks corroborate the symbolic proof and do not
enumerate the ambient extension or the general worst-case list.

Added only L012's genuine use of L001 to the ID-only DAG and updated the
short argument overview. The completed STEP_REVIEW is unchanged; the new
Next action exactly matches its existing COVERED_TARGET, with the instance
fixed in PROGRESS.md.

Validation: `PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with 13 nodes and 10 edges; `git diff --check -- .` passed. Unique
step fields, ready exact next-target coverage and lemma section order were
checked. The checkpoint has 14 lines and the overview 99. Structural
validation does not certify mathematical correctness; L012's only direct
local mathematical input is L001's root bound, support count and safe-index
existence, all represented by the single new DAG row.
