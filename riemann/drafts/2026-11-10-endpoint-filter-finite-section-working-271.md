# Exact inverse stability: finite-section attempt, step271

10 November 2026. RESEARCH under the unchanged, pre-existing EXPLORE
assessment `literature/2026-11-10-endpoint-filter-inverse-stability-review-267.md`.
The target remains exactly its E-to-S implication for L990's coefficients.
The supplied assessment, source-notes268, L990, C990a and working270
were read. L991's fixed-pivot obstruction is retained, not independently
audited or extended. No external theorem or cross-notebook input is needed.

Main gap: actual-Xi positivity L030-L032/C032a and L966/L968 signed
forcing. The intermediate target is an exact homogeneous sequence with
finite positive exponential growth. This would stop general recovery
of B_n from one filtered observable; success of recovery would still
leave the arithmetic identity, shifted intervals, prime powers, other
zeros, both complements and L984(H) unpaid.

## Saved plan before calculation

Form the exact finite homogeneous equations for n=32,...,M, retaining
all rows and both initial values x_32=1, x_33=0. Check each vector and
each elimination pivot exactly; a zero pivot is a reported obstruction
requiring implicit row treatment, never a deleted equation. In a section
with every forward pivot nonzero, forward elimination solves precisely
this finite implicit system, without claiming uniformly bounded ratios.

Use integer factorial-scaled Laguerre polynomials to compute exact
primitive cross-product rows, including both constant subtractions.
Enclose the uniquely determined rational solution by outward-rounded
dyadic intervals. Store complete row and interval evidence on disk.
Test endpoints M=64,128,256,512,1024 (solution through M+2), a fixed
upper envelope |x_k|<=2^(4*(k-32)), and endpoint lower threshold
|x_(M+2)|>=2^((M+2-32)/100). The latter can be certified more strongly
by its integer ceiling. These are diagnostic thresholds, not assumptions.

Continuation requires bounds uniform as M tends to infinity, with a
nonzero limit and positive growth that does not escape to the moving
right boundary. Fixed initial values avoid one normalization ambiguity
but do not establish either uniform estimate. Finite success alone is
EXPLORATION; a failure disproves only the specified finite envelope or
initial vector, not inverse stability. No leading-phase substitute,
all-index pivot assertion or infinite product estimate is licensed.

The onset in C990a is existential. The finite calculation checks every
row it uses directly; it does not assert 32 exceeds that onset. A genuine
infinite construction would need to reach and retain the entire tail.

## Completed finite calculation

EXPLORATION, not a theorem about the infinite operator and not a new
prime estimate. No lemma is added. All 993 rows n=32,...,1024 have
nonzero exact forward pivots. Thus the finite equations with the two
specified initial values have a unique exact rational solution through
index1026. Every row is retained; no all-index nonvanishing conclusion
is inferred. The certificate stores positively scaled primitive integer
cross products, so its homogeneous equations are exactly L990's,
including the orientation and both constant subtractions.

The complete certificate is
`scripts/endpoint-null-filter/finite-sections-271.json` (1024-bit
outward dyadic enclosures). Every intermediate index satisfies the
chosen upper envelope. The largest certified rounded log2 upper
bound divided by k-32 is 8/33, attained at k=131, below the required4.
The selected endpoints give the following inclusive enclosures:

| Last row M | Endpoint k=M+2 | Certified log2 absolute value interval | Required integer lower exponent |
| --- | --- | --- | --- |
| 64 | 66 | [5,6] | 1 |
| 128 | 130 | [21,22] | 1 |
| 256 | 258 | [36,37] | 3 |
| 512 | 514 | [98,99] | 5 |
| 1024 | 1026 | [227,228] | 10 |

Here each required exponent is ceil((k-32)/100); these integer
thresholds are stronger than the stated diagnostic lower thresholds.
The measured endpoint brackets are finite-index growth, not bounds on
an infinite Lyapunov exponent or on limsup as n tends to infinity.

## Complete finite evidence and verification method

Reproduce from the active notebook:

    python3 scripts/endpoint-null-filter/finite-sections-271.py
    python3 scripts/endpoint-null-filter/finite-sections-271.py --verify

Generation uses q_k=k! L_k^(2)(u), with q_0=1, q_1=3-u and
q_(k+1)=(2k+3-u)q_k-k(k+2)q_(k-1), the finite identity already
justified in L990. It forms K_m=(q_(m-1)-(m-1)!)/((m-1)!(m-1)),
clears only positive denominators, and computes the exact oriented
cross product. Dividing its integer entries by their positive gcd
does not change the homogeneous row. No asymptotic coefficients or
floating-point evaluation of Laguerre polynomials is used.

The independent replay computes each q_k by its defining finite sum
k! sum_r (-u)^r binom(k+2,k-r)/r!, checking every term division
exactly, and reproduces all 993 stored rows. For each row it evaluates
the four corners of -(d_0*x+d_1*y)/d_2 with exact Fraction arithmetic
and checks their enclosure in the next stored interval. This affine
map attains its extrema at those corners; induction from [1,1] and
[0,0] therefore encloses the exact rational solution, not a residual
approximation. Integer comparisons check all upper bounds and all
five selected lower bounds. The complete successful replay is
`scripts/endpoint-null-filter/finite-sections-replay-271.json`.
The verification covers every stored relevant value, not a preview.

The first 256-bit enclosure run lost sign information by index1026:
its interval contained zero and had rounded absolute upper exponent312.
This is a failure to certify the lower threshold, not a zero or a
counterexample to growth. It is preserved at
`scripts/endpoint-null-filter/finite-sections-271-first-pass-256bit.json`
and reproducible with `--precision 256`; no first-pass result is used
to prove a lower bound. Increasing precision to1024 repairs that
enclosure failure. The independent replay above validates the final
complete certificate. No expansion of the horizon or parameter search
was made after observing growth.

## What this attempt does and does not decide

The same fixed initial values are used in every reported section;
these are restrictions of a single finite solution, not separately
renormalized vectors at moving endpoints. That removes one possible
normalization escape within the tested range. It does not supply
nonempty sections of arbitrary length or a bound uniform in that
length. If a future pivot is zero, the new exact row may be incompatible
with this initial vector or may require a free-variable treatment.
Even nonzero future pivots might produce superexponential growth or
lose the positive limsup. The existing cofinite vector definition and
L991 do not settle any of these possibilities.

Continue the unchanged assessed target with an analytic finite-section
test, not a larger horizon alone: seek constants C,A<infinity and a>0,
independent of M, and unbounded fixed indices k_j, such that every
finite section admits the same anchored solution, all coordinates
obey |x_k|<=C*2^(A*(k-32)), and each included k_j obeys
|x_(k_j)|>=2^(a*(k_j-32)). Retain singular rows. The constants may
differ from this diagnostic's4 and1/100. A proof of such uniform
feasibility would support a compactness construction; this turn does
not assert that feasibility or derive a new compactness theorem.
An exact incompatibility stops this anchor, while failure of a proof
leaves the original implication open. Before another repeated finite
sample, a genuinely uniform mechanism is needed.

The inverse implication and all arithmetic transfer gaps remain open.
No new argument enters PROOF.md or DAG.md. Full matching Mathlib
coverage is unchecked; this is a reproducible finite calculation,
not formalization, certified novelty, or an RH candidate.
