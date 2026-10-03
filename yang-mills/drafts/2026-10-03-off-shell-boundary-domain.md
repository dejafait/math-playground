# Off-shell boundary-domain test — working record

## Preflight and scope

Read the shared GOAL.md and PROMPT.md, the local goal, checkpoint, whole overview and DAG, the saved assessment and relevant existing failures. Preserved the unfinished local and unrelated notebook changes. The incoming recovery reports an exact-target mismatch; the current saved Next action is already an exact COVERED_TARGET of the unchanged EXPLORE assessment in drafts/literature/2026-10-03-boundary-brst-counterterms.md. The read-only gate accepts that coverage. Reuse it for RESEARCH with classification REPRODUCTION; no additional source search or assessment amendment is needed.

The main local gap is a justified physical-boundary Ward formulation before any boundary-counterterm exclusion for L011. This step tests only a necessary premise: whether the proposed strong smooth domain is preserved off shell by the standard BRST algebra. A successful test would leave source identities, corner compatibility and gauge equivalence to the forest coefficient unresolved. A failure stops this particular domain shortcut. Neither outcome supplies the O(1) remainder, finite matching or required interacting reflected error <= c_box/2.

The prior records contain source qualifications but no explicit off-shell cube calculation. This is a specialization of the inspected standard BRST/domain issues, not a novelty claim. The stopped bulk-locality route and its three-turn exhaustion remain preserved; this is a different, preapproved compatibility test.

## Calculation saved before completion

On any flat face with c = 0, tangential derivatives of c vanish. With sA = D_A c, the normal condition varies as

\[
s(\partial_n A_n)|_F
=\bigl(\partial_n^2c+[A_n,\partial_nc]\bigr)|_F.
\]

The proposed Dirichlet ghost trace does not force either term to vanish. Test at A = bar c = b = 0, so the commutator vanishes. Put

\[
H(u)=(1-u^2/16)^3,\qquad
R(v)=\frac{(4-v)^2(v+4)^3}{1024},\qquad
\phi(x)=R(x_4)\prod_{j=1}^3H(x_j).
\]

For a nonzero odd Grassmann generator xi and T = (i/2) diag(1,-1), take c = xi T phi. On every face phi and its first normal derivative vanish. H has a triple root at both lateral endpoints, and R has a triple root at -4 and a double root at 4. Thus R''(4) = 1, while all second normal traces on the other seven faces vanish. On the upper face, s(partial_n A_n) = xi T product_j H(x_j), nonzero at (0,0,0,4). All other proposed boundary traces are preserved by this test. No field or ghost equation is imposed.

This rejects the strong off-shell domain. A Dirichlet Laplacian eigenfunction obeys an additional boundary relation and is outside the tested unrestricted-ghost hypothesis; the result does not contradict the spectral statements or L003's Gaussian construction.

The full statement, proof, source qualifications and Mathlib coverage are recorded in L012. No other research target is calculated in this step.

## Completion and checks

Outcome: NEGATIVE; classification: REPRODUCTION. The explicit necessary-domain premise fails, so the strong-domain route is stopped. The changed auxiliary-field covariance question is queued with REVIEW_REQUIRED coverage, not calculated here. This result does not improve the required reflected error <= c_box/2. No complete candidate exists.

The polynomial factors, all normal orientations, all eight face traces, intersections, remaining BRST constraints and the ghost-eigenfunction qualification were checked against the full proof. Exact rational arithmetic independently checks expanded and factored polynomials and the endpoint jets:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction as F
from math import factorial

H = [F(1), F(0), -F(3,16), F(0), F(3,256), F(0), -F(1,4096)]
R = [F(1), F(1,4), -F(1,8), -F(1,32), F(1,256), F(1,1024)]
def jet(p, x, k):
    return sum(p[j]*F(factorial(j), factorial(j-k))*x**(j-k)
               for j in range(k, len(p)))
def mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out
hfactor = [F(16), F(0), -F(1)]
rfactor_minus, rfactor_plus = [F(-4), F(1)], [F(4), F(1)]
assert H == [v/F(4096) for v in mul(mul(hfactor,hfactor),hfactor)]
assert R == [v/F(1024) for v in mul(mul(rfactor_minus,rfactor_minus),
              mul(mul(rfactor_plus,rfactor_plus),rfactor_plus))]
assert [jet(H,-4,k) for k in range(3)] == [0,0,0]
assert [jet(H,4,k) for k in range(3)] == [0,0,0]
assert [jet(R,-4,k) for k in range(3)] == [0,0,0]
assert [jet(R,4,k) for k in range(3)] == [0,0,1]
assert jet(H,0,0) == 1
print('Exact polynomial boundary jets passed.')
PY
```

The documentation command `PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem yang-mills` passes with 12 nodes and 21 unique edges. Read-only literature validation accepts the unchanged prior COVERED_TARGET, RESEARCH/REPRODUCTION and the exact REVIEW_REQUIRED next target. Turn-start hashes confirm every existing lemma, mathematical script and assessment is preserved; only PROGRESS.md, PROOF.md and DAG.md change among existing files. The compact checkpoint has 14 lines and the overview 80. `git diff --check -- .` passes. These are documentation and arithmetic checks, not validation of a Yang–Mills construction.
