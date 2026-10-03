# 2026-10-03 — Endpoint attainment on the prescribed domain

Completed one mathematical reproduction of the exact saved action using the
prior SPECIALIZE assessment. The ready coverage was reused; no further
literature work or parked source retrieval was performed. Existing recovery
changes and all inactive branches were preserved.

[L011](../lemmas/L011-root-product-endpoint-attainment.md) constructs the
single center and checks strict degree cancellation, prescribed roots,
distinct evaluation words and simultaneous agreement for every m>=1.
Combined with L001, it proves B_m((n-k)/n)=binomial(n,k), hence the necessary
and sufficient endpoint condition q>=epsilon*^(-1)binomial(n,k). This
corrects L001's earlier statement that the condition was not necessary;
its support-counting proof is retained. The root-product construction and
scalar endpoint count are known by the precise source citations in L011.
Classification: REPRODUCTION; no progress beyond the checked literature
or novelty is claimed.

Outcome: ADVANCE, a relevant local endpoint input and mathematical
correction. The largest safe grid index is n-k exactly under this condition;
with 1<=epsilon* q<binomial(n,k), it is strictly smaller and still unknown.
The general challenge, higher-agreement levels, small-characteristic cover
and ABF26 comparison remain unresolved. No complete candidate appeared;
STATUS stays IN_PROGRESS. Exploration turns used: 0/3 after this local
advance; the prior exploration and source failures remain in their histories.

Updated the argument overview and the sole ID-only DAG with L011's actual
use of L001. L001's references to L011 explain the superseded limitation;
they are not mathematical inputs to the earlier support-counting proof.
The checkpoint has one future coefficient-fiber target at A=k+1 and a new
[REVIEW_REQUIRED assessment](../drafts/literature/2026-10-03-root-product-one-more-agreement.md),
because the ready assessment covers only A=k. This target is motivated by
the now-proved need to move below the endpoint in the smaller-field regime;
no calculation for it was made.

Validation: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/root-product-endpoint/verify.py`
passed; [saved output](../scripts/root-product-endpoint/results.json).
Independent Lagrange interpolation on the nontrivial coset 2<8> in F_97
gave 12870, 1820, 120 and 16 distinct candidates at rates 1/2, 1/4, 1/8
and 1/16, with exactly k common agreement columns at widths 1 and 3.
The reused exhaustive toy enumeration confirmed endpoint maxima 2, 6 and
6 against thresholds 2, 4 and 13/2, respectively, at widths 2, 2 and 1.
These check equality, endpoint unsafety and endpoint safety independently
of the root-subtraction implementation. They are finite corroboration;
the general proof is symbolic and the cryptographic threshold was not
tested numerically.

`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with 12 nodes and 9 edges, and `git diff --check -- .` passed.
The overview has 97 lines and the checkpoint 14. The completed and next
assessment fields match their exact targets; the new one remains
REVIEW_REQUIRED. Structural validation does not prove the mathematics.
