# L084 — Complete table of the index-two multiplier order

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, with original primitive integer H=343h.
Use audited L077's basis b and both complete rational transports,
audited L078's full order R with basis m and complete integral table,
and audited L080's identification

\[
R^+=(\sqrt{2R}:\sqrt{2R})
=\mathbf Zm_0+\cdots+\mathbf Zm_{46}+\mathbf Z(m_{47}/2),
\qquad [R^+:R]=2.
\]

All field coordinates are retained. No selected factor, further radical
test, 31-maximality transfer, stopped ideal-power certificate or L026
premise is used. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-index-two-multiplier-table.md`.

## Conclusion

Put n_i=m_i for 0≤i≤46 and n_47=m_47/2. The files
`scripts/seven-torsion/index-two-table-321/product-00.json` through
`product-47.json` give the complete integer multiplication table

\[
n_i n_j=\sum_{k=0}^{47}d_{ijk}n_k\quad(0\le i,j\le47).
\]

Every one of the 110592 coefficient slots, including zeros, and all
2304 ordered product identities are independently verified in Q[T]/(H).
`basis.json` gives all basis representatives, both full rational
transports to the original power basis and L067's two-coordinate algebra,
their inverses, both transports to b, the actual identity and integral
old-order inclusion of index two. Thus the table is the table of the
entire already identified multiplier order, rather than an abstract ring
or an arbitrary index-two lattice.

One production stage and one independent verification stage pass their
respective strict 180-second caps; combined artifacts are below 134217728
bytes. All 435 inventoried original files are preserved. This is known
construction reproduction. Its separate critical audit passes below.
No new maximality test, global maximality, field discriminant, complete
units/classes, descent/Selmer bound or general BSD rank comparison follows.

## Proof

**Imported mathematics.** L080 already applies Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 and the following action/kernel/lifting paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
These results establish multiplier integrality and identify the full
lattice from the radical action; that general theory and L080's fixed
application are imported, not reproved. The hypotheses hold for the full
order R in L067's number field; the source has no odd-prime restriction.
The present task constructs the table for the already established basis,
without invoking a new local stopping criterion.

**Production and exact transports.** Matrices act on column coordinates.
Let B₀ be L077's basis-to-power matrix, A L078's m-to-b matrix, and
C=A⁻¹. Set S=diag(1,…,1,1/2) and T=S⁻¹=diag(1,…,1,2).
The new basis-to-b matrix is Z=AS and its inverse is TC. If P and P⁻¹
are L067's power-to-two-coordinate maps, the two requested transport
pairs are

\[
B_0Z,\quad (TC)B_0^{-1};\qquad
PB_0Z,\quad (TC)B_0^{-1}P^{-1}.
\]

The producer validates H=343h coefficientwise, the original nonmonic
basis formula, both original power-basis inverses, and original and
changed L067 transports. It checks all entries of L080's saved multiplier
matrix S, inverse T, numerator 2S and index. All six new rational
transport matrices, including Z and TC, are saved and checked with both
inverse products. No denominator is discarded.

Let s_i=1 for i<47 and s_47=2. From m_i m_j=Σ_k c_ijk m_k and
n_i=m_i/s_i, substitution gives

\[
d_{ijk}=\frac{s_k c_{ijk}}{s_i s_j}.
\]

The producer constructs every coefficient by integer division with its
remainder checked zero. All 48³ slots are saved, including zeros.
This is exact coordinate transport of the audited old table, not a new
multiplier theorem. The actual identity has coordinates u=(TC)e₀,
with all entries integral, and matches L080's saved identity. Both
identity actions on all 48 basis elements are checked. In particular
u₀=31, u₁=0, and e₀ is not substituted for the identity.

**Independent identification in the original field.** `verify.py`
imports no producer routines. Its matrix multiplication uses a different
loop order. It reconstructs H from the canonical L067/L077 data and
every b_i from the nonmonic formula. It checks both L067 inverse products,
all original transports and both original power-basis inverses. It
reconstructs the entire matrix A from L078's explicit r₀,r₁ columns
divided by 31 and the remaining unchanged b-columns, and verifies its
two inverse products and full L067 transports.

The verifier separately reconstructs S and T from the displayed L080
basis, checking the complete saved multiplier and numerator, both inverse
products and the actual index. It checks every entry of all six supplied
new transport matrices against the reconstructed matrices above and
both inverse products of each pair. These 13824 entries retain both
L067 coordinate components. The actual identity is checked in the power
basis as well as against L080. The full integral inclusion matrix T
satisfies ZT=A. Every diagonal and off-diagonal entry of T is checked;
its determinant is the product 1⋯1·2=2. This proves the inclusion and
index for the actual L080 lattice.

For complete independent field arithmetic, write W_i(T)=31m_i(T),
an integer polynomial obtained from the original b-basis. Define

\[
V_i(T)=62n_i(T)=
\begin{cases}2W_i(T)&i<47,\\ W_{47}(T)&i=47.\end{cases}
\]

All coefficients of W and V and their agreement with 62 times the
new power-basis matrix are checked. The old scale 31 is retained;
it is not replaced by the enlargement denominator two. For every
ordered pair the verifier reads every integer coefficient d_ijk and
forms the entire polynomial

\[
F_{ij}(T)=V_i(T)V_j(T)-62\sum_{k=0}^{47}d_{ijk}V_k(T).
\]

It performs full division by the original degree-48 H in Q[T] and
checks that every coefficient of the remainder is zero. At a nonzero
leading coefficient x, the quotient step is x/343. An integer fast path
is used only after checking its exact division; otherwise the code
uses a rational quotient and continues in Q. Thus there is no assumption
that an untested integer division is exact. In this completed instance
all quotient steps have integer results. All 95 coefficient positions
after division are checked for each polynomial, 218880 checks in total.
Division in the field by 62² then proves every claimed product.
This verifier does not reproduce the producer's table-scaling formula
as its product check.

The invertible full power-basis matrix identifies the 48-dimensional
space faithfully with K. Integral coefficients prove closure of the
whole lattice, and both actual identity actions are checked in the
verified table. L080 identifies this same lattice with R⁺. No field
embedding is selected and no conclusion is drawn from a dimension or
index label alone.

**Execution evidence and limits.** The only mathematical execution is

```bash
python3 -B scripts/seven-torsion/index-two-table-321/run_once.py
```

It refuses an existing start marker or output. Each stage includes
input validation, preservation checks and report writing. An external
watchdog stops a stage at 180 seconds or the combined byte cap, and
does not proceed after a failure. The producer uses 0.684513 external
seconds; independent replay uses 0.971167, both below 180. The aggregate
records 4733141 bytes before its final report, with more than 129 MB
remaining under the 134217728-byte cap. The directory's final size is
also checked when documenting this result.

`producer-report.json` and `verification-report.json` record all
110592 required slots, 2304 verified product identities, all 96 identity
actions, index two and empty failure lists. `input-hashes.json` and both
`preservation-*.json` records certify equal hashes for all 435 original
files before and after. Hashes supplement the complete arithmetic
replay. `produce-watchdog.json`, `verify-watchdog.json` and
`aggregate-report.json` retain the stage bounds and successful exits.
There is no retry, iteration, additional prime test or enlarged cap.

The construction supplies one usable full order table for subsequent
arithmetic. Global maximality and all subsequent BSD gaps remain open.
The separate critical audit of this fixed assembly is recorded below.

**Separate critical audit (2026-10-18, step 323).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-index-two-table-critical-audit.md`.
The complete proof and verifier were inspected against L077's original
nonmonic basis, L078's explicit r₀,r₁ basis and L080's audited multiplier
identification. The Stevenhagen applicability argument above is reused:
the entire order lies in the audited number field, and no new stopping
criterion or maximality inference is made. Columns, denominators 31 and
62, both original coordinates and the actual identity are retained.

Fresh evidence is in `scripts/seven-torsion/index-two-table-audit-323/`.
The single stage copies 51 required files, including the byte-unchanged
independent verifier, into that fresh sibling directory. Upstream paths
still resolve to the canonical inputs. The audit inventories all 435
upstream files plus all 63 construction files, 498 distinct originals.
`copy-manifest.json`, `original-hashes.json` and `audit-preservation.json`
record exact sources and equal before/after hashes. No producer is run.

Fresh complete replay checks all 110592 integer slots, all 2304 products
and all 218880 polynomial-division positions, with zero remainders and
no rational fallback needed in this instance. It verifies all 13824
transport entries, six inverse products, 96 actual identity actions,
the full lattice identification and index two. The checked rational
fallback remains valid: division is over Q[T], and an integer quotient
is used only when its remainder on division by 343 is zero.

The distinct supplement in `audit.py` imports no verifier/producer
routines. It reconstructs B₀ directly from the coefficients of H and
A from L078's canonical full numerator divided by 31. Let F=B₀A and
G be F with its last column divided by two. It checks every coefficient
of G against the saved new power-basis matrix. Exact rational
Gauss--Jordan elimination on

\[
 [G\mid I_{48}\mid F\mid e_0]
\]

produces `[I₄₈ | U | J | u]`, with all reversible row operations
retained. Full matrix multiplication independently checks GU=UG=I,
GJ=F and Gu=e₀. Every entry of J and u is integral and agrees with
the saved inclusion and actual identity. Thus J is the actual integral
inclusion of the old lattice into the new one, not an assumed diagonal
matrix or a copied index label. A separate elimination of F yields its
full inverse and signed determinant. Elimination of J likewise yields
its inverse and determinant, with both inverse products checked.
The complete pivot products and swap signs give

\[
 \det J=\det F/\det G=2.
\]

Since F and G are invertible full rational basis matrices, the lattice
index is |det J|=2. This uses the standard determinant/index identity
for full integer lattices; it supplies no maximality conclusion.
Elimination of B₀ against G reconstructs Z; elimination of Z against
I reconstructs its inverse. Finally elimination of PG against I
reconstructs the full inverse in L067's two-coordinate basis. Both
inverse products and all six saved transport matrices agree. These six
exact elimination systems use no saved inverse as an input.
`exact-elimination-certificate.json` retains all matrices, right-hand
sides or their explicitly identified identity matrices, elementary row
operations, complete solutions and signed determinants. Full computed
matrix equalities, not sampled entries or report previews, are checked.

The one-shot reproduction command is

```bash
python3 -B scripts/seven-torsion/index-two-table-audit-323/run_once.py
```

It refuses an existing start marker and writes reports exclusively.
The single external watchdog covers copying, validation, replay, all
six eliminations, preservation and report writing. Through watchdog
writing the stage takes 3.451272 seconds (rounded upward), below 180;
the completed directory occupies 7146088 bytes, below 134217728.
`verification-report.json`, `audit-report.json` and `watchdog.json`
all pass with empty failure lists. All 498 originals are preserved.
No retry, altered-evidence fixture, further correction or maximality
test was performed. The audit validates this fixed known-method table
under its audited dependencies, without progress beyond the checked
general construction or removal of any BSD rank gap.

## Mathlib

Full matching coverage for this explicit degree-48 multiplier-order
table and its transport certificates has not been checked. The cited
general multiplier theory and exact finite replay are the inputs;
unknown Mathlib availability is not evidence of absence.
