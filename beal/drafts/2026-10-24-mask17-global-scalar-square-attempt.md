# Fixed mask-17 global scalar-square attempt

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-mask17-global-scalar-square.md`.
Work only on delta=theta²−9 in L115's entire field. Preserve
ATTEMPTS/052–054 and all existing artifacts.

Main gap: complete supported arithmetic and point control in the
conditional marked branch. Intermediate target: an exact scalar-square
identity or a complete obstruction for this fixed product. A decision
clarifies L124's local collision, without determining rational points.
Continue only to exact identity or complete nonsquare evidence; bounded
failure is unfinished evidence, not nontriviality.

Inputs read: L115 irreducibility/actual theta; L116 maximal discriminant;
L124 complete support and generator/mask definitions; audited C124a local
identity; recorded failures ATTEMPTS/052–054. No duplicate global relation
is recorded in these scoped inputs. Known methods and their source
comparison are reused from the assessment; no literature refresh needed.

Working scalar reduction: outside {2,3,5,11}, delta has valuation zero
at every maximal prime by L124, while L116 and Milne ANT v3.08,
Theorem 3.35 imply e(P/p)=1. A putative delta=c*h² gives
0=v_p(c)+2v_P(h), so every outside rational valuation is even.
Remove the corresponding rational square: the 32 signed squarefree
support products exhaust scalar classes. Both signs must be retained.

Exact exploratory reduction: put u=theta² and v=1−9/u. Direct
substitution in 275u⁴−2860u³+6930u²−3564u+243 gives
v⁴+128v³+1920v²+4352v+1024=0. A square root of c*v
inside Q(u) yields delta=(1/c)*(theta*sqrt(c*v))².
A positive identity will be checked directly modulo the original F;
this exploratory reduction is not itself a decision.

Execution status: system Python has no SymPy; do not repeat the parked
class-backend probes. Use standard-library exact rational arithmetic.

## Completed positive decision

C124b is the canonical proof and citation record. The exact identity
proves delta=−11h². The producer and independent integer-only replay
certificates are under `scripts/pair-genus-two/mask17-global-scalar-square-*`.
All six producer checks and eighteen replay comparisons pass. A first
manually transcribed coefficient vector in the lemma draft was corrected
against the complete replay before completion; the final vector matches
all fifteen exact coefficients. The scalar-support argument above is
unneeded for this positive decision; no negative certificate, complete
scalar enumeration or class-group conclusion is claimed.

The coefficient search found the quartic factor at c=−11 with
(a,b,d,e)=(44,264,−1936,−3872). Its bounded search is only discovery,
not a completeness argument. The displayed positive identity is verified
in the entire quotient and does not depend on a backend. The main gaps
remain unchanged; the separate critical audit is proposed and requires
its own approval turn.
