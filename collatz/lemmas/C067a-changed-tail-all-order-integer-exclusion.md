# C067a — Changed-tail all-order integer exclusion

## Hypotheses

Use the complete indexed J_j,H_j table of L055, with attached tails
a_23=20, a_24=166504394 and a_j=2 otherwise. The fixed totals are
K=397573379 and N=630138897. Let sigma be any permutation of
{0,...,24}, interpreted cyclically. At position k the outgoing triple
is (J_sigma(k),H_sigma(k),a_sigma(k)); its input is s_k.
Require real junctions s_k>=540/11, s_25=s_0, every exact endpoint

\[
s_{k+1}=2^{-a_{\sigma(k)}}\left\{
(27/16)^{J_{\sigma(k)}}(3/2)^{H_{\sigma(k)}}s_k
-\frac{12}{11}(3/2)^{H_{\sigma(k)}}-1\right\}+\frac{23}{11},
\qquad 0\le k<25,
\tag{1}
\]

and every non-strict own-input J guard

\[
4J_{\sigma(k)}\log2\le\log s_k+\log(11/4),
\qquad 0\le k<25.
\tag{2}
\]

These are L051 (4) and the J part of L051 (3), specialized to the
stated allocation. All logarithms are natural. Put n_k=s_k-23/11.
No initial minimum, H guard, seed, primitive-count condition, parity,
residue, exact valuation or actual-orbit realization is assumed.

## Conclusion

There is no solution of (1)–(2) with all n_k integers, for any sigma,
including every cyclic presentation of the intact rows.

This is a local RESEARCH/REPRODUCTION applicability assembly under the
prior SPECIALIZE assessment
`drafts/literature/2026-10-14-changed-tail-integer-exclusion-assembly.md`.
It combines audited local inputs, without claiming originality beyond
the inspected sources. The separate critical audit below found no defect
within these hypotheses. Both positive rational witnesses remain valid. Other allocations,
actual-cycle bridges, unrestricted cycles, entry, divergence and universal
eventual descent remain unresolved; this is not a Collatz candidate.

## Proof

### Cyclic normalization retains every input and edge

Suppose such a solution exists with every n_k integral. Since sigma is
a permutation, there is a unique t in {0,...,24} with sigma(t)=24.
For 0<=k<25 define

\[
j(k)=(t+1+k)\bmod25,\qquad
\widetilde s_k=s_{j(k)},\qquad \pi(k)=\sigma(j(k)),
\]

and set tilde s_25=tilde s_0. The map j permutes the positions and
j(24)=t. Thus pi(24)=24 and pi restricted to positions 0,...,23
permutes rows 0,...,23. Each entire triple rotates together with
its original input; no tails or guard inputs are reassigned.

For k<24, j(k+1) is j(k)+1 modulo 25. If j(k)<24, original edge
j(k) of (1) is exactly the new edge k. If j(k)=24, original edge
24 has output s_25=s_0, so it too becomes the new edge k with the
same input and outgoing triple. At k=24, the new closing edge is
original edge t: its output is s_(t+1) if t<24, or s_25=s_0 if
t=24. In both cases that output is tilde s_0. This accounts for all
25 edges, including the old cut and the new closing edge, whether
those edges coincide or differ. The large tail remains attached to
row 24, now on the closing edge; row 23 keeps tail 20 wherever it
occurs.

For each k, original guard j(k) is precisely (2) for outgoing row
pi(k) at input tilde s_k. Domain and guard signs are unchanged.
Every tilde n_k=tilde s_k-23/11=n_j(k) is still integral. Hence the
rotated tuple meets all hypotheses of L067, without needing an
assumed minimum or any extra L051 condition.

### Literal-root identification and contradiction

Audited L067 forces pi to be the identity. Its endpoint uniqueness
then applies to this literal order. Audited L064 at j=23 provides a
real cyclic endpoint tuple for exactly the same J,H table and tails,
so the normalized tuple is that tuple. In particular tilde n_0 is
L064's literal j=23 unshifted cyclic root. Existence here uses only
L064's endpoint/J conclusion; L065's H/seed result is unnecessary.

Audited L066 identifies that very root as

\[
\widetilde n_0=\Phi/\Delta,\qquad
\Delta=2^N-3^K>0,\qquad
\Phi\equiv21\pmod{25},\quad\Delta\equiv5\pmod{25},
\]

where Phi and Delta are integers. This identification concerns
n=s-23/11, rather than s or an old-tail numerator. Its chronological
composition includes both changed tails. If tilde n_0 were an integer,
Phi=tilde n_0 Delta would imply 5 divides Phi because 5 divides Delta.
But Phi=21 modulo 25 implies Phi=1 modulo 5, a contradiction.
This contradicts integrality of the normalized tuple and proves the
conclusion for the original arbitrary cyclic presentation.

The known affine input underlying L064, L066 and L067 is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The imported formal word is nonempty, its denominator is nonzero,
and the unshifted-coordinate specialization is already justified in
those audited inputs. This assembly supplies only the missing scope
and cyclic applicability argument; it does not reprove general coding
or recompute the finite residues. C063a has different tails and is a
precedent, not a mathematical input to this conclusion.

The contradiction requires all original unshifted junctions integral,
which ensures integrality of the normalized starting junction. It does
not assert that every individual junction of a rational solution is
nonintegral. Nor does it establish any parity/valuation converse or an
actual-cycle bridge. The rational witnesses and the distinct diagnostic
stops in Attempts 027–031 are therefore preserved.

### Independent critical audit — 2026-10-14

The approved RESEARCH/REPRODUCTION audit under
`drafts/literature/2026-10-14-changed-tail-integer-exclusion-critical-audit.md`
found no defect. This verifies the existing conjunction, without a
stronger theorem or progress beyond the inspected sources. Audited input
conclusions are reused; no upstream numerical certificate is recomputed.

**Normalization.** Extend the original junction indices periodically
modulo 25 using s_25=s_0. The bijection j satisfies
j(k+1)=j(k)+1 modulo 25 for every k, including k=24. Hence the
original edge with input s_j(k) and row sigma(j(k)) has exactly output
s_j(k+1). For 0<t<24 the original cut edge 24 becomes new edge 23-t,
whose output is original s_0 at new position 24-t. The new closing
edge is original edge t, whose output is s_(t+1)=tilde s_0.
For t=0 these are new edges 23 and 24. For t=24 the rotation is the
identity and the cuts coincide. These cases exhaust all positions of
row 24 and account for both edges across the cuts.

The row label, J,H parameters, tail and input rotate together. Thus
every guard appears once with its own input, the same non-strict sign
and the same domain. Row 23 retains tail 20 and row 24 retains tail
166504394. All normalized unshifted junctions remain integers. The
normalized labels are exactly a permutation of 0,...,23 followed by 24.

**Input applicability and root identity.** L067's Hypotheses require
precisely that normalization, L055's indexed table, these attached tails,
domain, closure, endpoints and own-input J guards. No minimum, H guard,
seed or primitive-count hypothesis is required. L051 supplies formulas
only, not its entire real system. L067 therefore forces the identity
order. Its endpoint uniqueness holds before imposing any guards: the
product multiplier 3^K/2^N=exp(-Lambda) is in (0,1), so the closing
equation has nonzero coefficient 1-3^K/2^N. L064 at j=23 supplies a
tuple for these very literal endpoints and tails. Consequently the
entire normalized tuple is that tuple. L065's extra real-system guards
are unnecessary for this application.

L066 explicitly takes L064's literal j=23 root n_0=s_0-23/11.
Its checked identities A_i eta_i=F_i and Phi=3^K B identify
B/(2^N/3^K-1) with Phi/(2^N-3^K). Both changed tails enter the
chronological prefixes and closing product. Thus the quotient is the
unshifted root at the normalized cut, not a shifted or old-tail root.
L066 supplies integers Phi,Delta with Delta>0, Phi=21 modulo 25
and Delta=5 modulo 25. An integer normalized root m would imply
Phi=m Delta and hence Phi=0 modulo 5, contradicting Phi=1 modulo 5.
All-original-junction integrality is sufficient to give integrality at
this selected cut; integrality at an unspecified single original
junction would not justify that step.

**Direct inputs and limits.** The DAG row contains the five direct
inputs actually used: L051's formulas, L055's table, L064's root,
L066's nonintegrality and L067's rigidity/uniqueness. C063a is only
an old-tail precedent, and L065 only names the allocation. The precise
Halbeisen–Hungerbuehler citation above underlies the imported affine
machinery; no general coding reproof or parity-realization theorem is
needed. Attempts 027–031 concern different old-allocation diagnostics
and remain valid. Both rational witnesses are preserved. This audit
establishes no actual-cycle bridge, other-allocation exclusion or claim
that every rational junction is nonintegral. No proof correction or
input change was needed, so the argument overview and DAG are unchanged.

## Mathlib

Full matching coverage and Lean builds for this all-order conjunction
were not checked. L066 records supporting valuation and rational-reduction
declarations in
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean).
The present contradiction needs only its audited integer residues and
elementary divisibility; those supporting declarations do not formalize
this allocation, guard rigidity or cyclic assembly. Unknown full coverage
is not evidence of absence.
