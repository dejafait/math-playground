# C096a — Literal d34 last-pair real-system exclusion

## Hypotheses

Use L055's 25 indexed pairs in literal order, changing only H_0=6
and H_24=32670655. Fix B=9250245, kappa=23/11 and an integer
0<=t<=B. Set a_i=2 for 0<=i<=22, a_23=2+18t and
a_24=2+18(B-t). Suppose real s_0,...,s_25 satisfy s_25=s_0,
s_i>=540/11 for every input i=0,...,24, and all 25 endpoints

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                 -(12/11)(3/2)^{H_i}-1\right)+\kappa.       \tag{1}
\]

At every outgoing row's own input require both guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16).                        \tag{2}
\]

All logarithms are natural. Closure is required in (1), including when
a_24=2. No minimum, seed, integer junction, parity, residue, valuation,
primitive count or actual-word realization is assumed.

## Conclusion

No such real tuple exists for any integer 0<=t<=9250245.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-last-pair-real-exclusion-assembly.md`.
It assembles audited local inputs; it is not a new general result beyond
the inspected source machinery. The separate step-426 critical audit
below found no defect within this restricted scope.
Early-support and cyclic-order reductions, actual-word transfer and
universal eventual descent remain unresolved. Attempt 032 and both
original d=0 rational witnesses remain valid.

## Proof

Suppose such a tuple exists and keep this t, literal cut and tuple
throughout. The lower domain makes every logarithm meaningful.
Discarding only the H half of (2) leaves precisely L096 (1): the same
changed table, budget, parameter, complete tail list, all endpoints,
lower domain and non-strict own-input J guards. In particular both
subtracted offsets in (1) remain inside tail division and kappa stays
outside. The completed step-422 audit of L096 found no defect in its
quantified cutoff, which we import without repeating its certificate.

If 2<=t<=B, L096 (2) says that this tuple's row24 margin satisfies

\[
\log s_{24}+\log(11/4)-4J_{24}\log2
<-4396220984253/250000000000<0.                           \tag{3}
\]

The J half of (2) at precisely s_24 requires that margin to be
nonnegative, a contradiction. This covers the whole closed interval,
not just a boundary sample. At t=B the tails are
(a_23,a_24)=(166504412,2); the closing endpoint remains in (1),
as required by L096. Hence t<2. Integrality and t>=0 leave exactly
t=0 and t=1.

For t=0 the last tails are (2,166504412); for t=1 they are
(20,166504394), since 18B=166504410. Every earlier tail is 2.
For each case these are exactly L095's tails on its identical d34
table and literal cut. Our complete equations (1) are L095 (1).
Its completed step-418 audit establishes uniqueness among all real
endpoint tuples, independently of guard feasibility or the lower
domain. Thus the assumed tuple is exactly the endpoint tuple to
which L095 applies. In particular the same input s_18 satisfies

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<-1338950347341/100000000000<0.                         \tag{4}
\]

Row18 is unchanged from L055 and has
(J_18,H_18)=(693015,3295208). The H half of (2) at that same
outgoing row's input requires the left side of (4) to be strictly
positive. This is a contradiction for both remaining integer cases.
Together the cases exhaust 0<=t<=B, proving the conclusion.

No rotation, root substitution at another cut, minimum or seed is
used. L095 does not assert feasible survivors, nor is their feasibility
needed to identify a hypothetical tuple with its unique root. Only one
failed necessary guard per case is needed; integrality of junctions or
parity realization is never asserted.

### Sources, overlap and qualifications

The direct inputs are L055's pair table only, audited L095 and audited
L096. C093a is a precedent for d=6,...,33, not an input for d34.
The prior assessment checked duplicates and recorded failures; neither
L084's failed full package nor the full C077a/L083 conjunction is
invoked. Attempt 032 and the different-table d=0 witnesses are unaffected.

The upstream formal affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The analytic inputs are [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), in the positive-real domains
already checked in L095/L096. These inputs enter through the completed
canonical specializations, without a new analytic or coding reproof,
external search or certificate rerun. The additional argument here is
only exhaustive integer cases and same-tuple applicability.

This excludes only the specified literal last-pair subsystem. Early
support, nonliteral orders, actual-word transfer, other tables,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. It is not a complete Collatz candidate.

### Independent critical audit — 2026-10-23, step 426

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-last-pair-assembly-critical-audit.md`.
It independently checks the assembly, importing the completed step-418
L095 and step-422 L096 audits rather than repeating their numerical
certificates. The test is to correct or narrow on any unmatched premise,
missing integer boundary, incorrect endpoint identification or guard sign.
No such defect was found. This validates an existing local input, without
extending its exclusion or claiming a new result beyond the checked sources.

**Common hypotheses and cut.** L055's complete pair table was compared
with the two replacements: 40-34=6 and 32670621+34=32670655.
Every other pair is unchanged, in particular row18 is (693015,3295208)
and J_24=30998279. L055 supplies only these pairs, not its original
allocation, positive witness, minimum or seed. C096a and L096 both fix
B=9250245, integer 0<=t<=B, literal order, and exactly the same 25
tails. Their endpoint expressions agree term by term: both negative
offsets lie inside multiplication by 2^(-a_i), and 23/11 lies outside.
The i=24 equation has output s_25=s_0 in both statements. Each lower
domain is s_i>=540/11>0; hence all 25 required logarithms exist. Removing
only the strict H guards from C096a leaves every L096 hypothesis, with
the same real variables and the same non-strict J guards. Nothing is
assumed about where a minimum occurs.

**Complete upper branch.** L096's conclusion and its completed audit
give the row24 margin bound in (3) for every integer 2<=t<=B, by its
already proved monotonicity, not merely at t=2. The numerator and
denominator of the positive magnitude in (3) are positive, so this
margin is strictly negative. The row24 J guard is exactly the assertion
that this same margin is nonnegative. At the upper boundary,
18B=166504410 and (a_23,a_24)=(166504412,2); all earlier tails remain 2.
This is inside L096's closed interval and retains the closing equation.
There is no omitted boundary or tail assumption. Thus the assumed
integer t must be below 2; nonnegativity leaves precisely 0 and 1.
No assertion that either remaining case is feasible is used.

**Both remaining endpoint identities.** At t=0 the two tails are
(2,166504412), and at t=1 they are (20,166504394). These agree separately
with L095's hypotheses; every earlier tail, pair, variable, offset and
the closing equation also agrees. L095 assumes only these real endpoint
equations, not J/H guards or domain. Its audited positive fixed-point
denominator gives uniqueness among all real endpoint solutions. Thus
any hypothetical C096a tuple in either case is the very tuple covered
by L095, without selecting a different cut or assuming a feasible root.
The domain conditions required here are additional restrictions, not
missing premises of that uniqueness statement.

At row18 C096a requires
3295208 log2 < log(s_18)+693015 log(27/16).
Subtracting its left side makes the margin strictly positive. L095 (2)
gives exactly this margin, at the identical input s_18, strictly below
-1338950347341/100000000000<0 for each of t=0 and t=1. This contradicts
the strict H guard in both cases. No J feasibility assertion for these
two roots is needed; all integer cases have now been exhausted.

**Scope and limits.** The direct mathematical inputs remain
L055 (table only), L095 and L096, exactly as recorded in DAG.md.
C093a is only a different-table precedent. Neither the failed full
O/S/C package of Attempt032 nor a minimum/seed, integer junction,
parity realization, early-support/order reduction or actual-word premise
enters the proof. Both d0 witnesses remain on their different table.
The primary citations and their qualifications above are inherited
through the audited inputs; no new source theorem, reproof or certificate
rerun is necessary for this assembly audit. Full matching Mathlib
coverage remains unchecked. No statement or argument changed, so
PROOF.md and DAG.md are unchanged; this canonical audit supersedes their
pending-audit wording for C096a only. Universal eventual descent and
the independent wider reductions remain unresolved.

## Mathlib

Full matching coverage for this assembly has not been checked.
Supporting affine, logarithmic and integer-interval facts would not by
themselves constitute a matching theorem. Unknown coverage is not
absence; no Lean verification is claimed.
