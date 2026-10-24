# C094a — Uniform all-order full-allocation real-system exclusion

## Hypotheses

Fix an integer 6<=d<=33. Use the 25 indexed pairs in L055's complete
table, changing only H_0=40-d and H_24=32670621+d. Every J_i and
every other H_i is unchanged. Set B=9250245, kappa=23/11 and

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Let b_i be nonnegative integers with sum_(i=0)^24 b_i=B, put
a_i=2+18b_i, and let pi be any permutation of {0,...,24}.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 and,
for every 0<=k<25,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4),\qquad
H_{\pi(k)}\log2<\log s_k+J_{\pi(k)}\log(27/16).
\tag{2}
\]

All logarithms are natural. Each indexed outgoing row retains its
allocation and own input. There is no minimum-location, seed,
integer-junction, parity, residue, exact-valuation, primitive-count
or actual-word premise.

## Conclusion

No such real tuple exists for any specified d, any indexed cyclic
order and any allocation in the full stated integer simplex.
Consequently any stronger real system containing these hypotheses
is infeasible for these tables.

This is a local RESEARCH/REPRODUCTION assembly under the prior SPECIALIZE
assessment `drafts/literature/2026-10-22-uniform-all-order-real-exclusion-assembly.md`.
It adds the all-order consequence of audited inputs, without a new
analytic estimate, certificate or ordering mechanism. It makes no
claim of progress beyond the checked source machinery. The separate
critical audit below found no defect. Actual-word transfer and universal eventual
descent are not concluded; this is not a complete Collatz candidate.

## Proof

Assume such a tuple exists and keep its d, indexed table and allocation
fixed. Temporarily disregard only the strict H half of (2).
The remaining hypotheses coincide with every tuple hypothesis of
audited L094: identical changed pairs, B, nonnegative integer b_i,
tails a_i, permutation pi, lower domain, all 25 endpoints (1), closure
and non-strict own-input J guards. In particular both subtracted
endpoint offsets remain inside tail division, and kappa stays outside.
L094 therefore implies that pi is a rotation of literal order.
Only this order conclusion is used; no premise on a minimum at any
specified input is introduced.

Write pi(k)=(c+k) mod25 for the rotation parameter c. Let z be the
unique position with pi(z)=0, so c+z=0 mod25. Define

\[
\rho_i=(z+i)\bmod25\quad(0\le i<25),\qquad \rho_{25}=z,
\quad x_i=s_{\rho_i}\quad(0\le i\le25).
\tag{3}
\]

Then pi(rho_i)=i for 0<=i<25 and x_25=x_0. The map i to rho_i
bijects all 25 original input occurrences, with inverse k to
(k-z) mod25. Thus every x_i>=540/11. Equal numerical junction
values do not identify their labeled occurrences. The outgoing row
at x_i is row i with its original b_i and a_i; the indexed allocation
is unchanged, not replaced by b_(rho_i). Its integer nonnegativity
and full budget are therefore unchanged.

Fix any 0<=i<25 and set k=rho_i. The cyclic successor identity
rho_(i+1)=(k+1) mod25 holds also when i=24, since then
rho_24=(z-1) mod25 and rho_25=z. If k<24, the original output
s_(k+1) equals x_(i+1). If k=24, the same equality holds because
s_25=s_0=x_(i+1). Substitution in the original equation (1) gives

\[
x_{i+1}=2^{-a_i}(G_i x_i-Q_i)+\kappa
\quad(0\le i<25),\qquad x_{25}=x_0.
\tag{4}
\]

This retains both cuts explicitly. The original closing edge k=24
occurs at normalized position i=24-z. The normalized closing edge
i=24 is original edge k=(z-1) mod25, with output at position z.
When z=0 the cuts coincide and use the original closing equality.
When z=24 the original closing edge is normalized edge 0, and the
new closing edge is original edge 23. For all intermediate z both
equations occur at their respective positions. Each of the 25 tails
is retained exactly at its outgoing row, including any tail equal to 2
at either cut. No endpoint or offset has been estimated or discarded.

At the same old input k=rho_i, pi(k)=i and s_k=x_i. Substitute
these equalities into both original guards (2), obtaining

\[
4J_i\log2\le\log x_i+\log(11/4),\qquad
H_i\log2<\log x_i+J_i\log(27/16)
\quad(0\le i<25).
\tag{5}
\]

The non-strict J sign and strict H sign are unchanged. Each guard
remains at its own outgoing input, including both cuts. In particular
the row18 H guard is the original guard at position (z+18) mod25,
at x_18, with the unchanged pair (693015,3295208); it is not a guard
at the neighboring output. The lower domain ensures that every
logarithm in (5) is defined.

The normalized tuple x now meets all hypotheses of audited C093a
for this very d: identical indexed pairs and B, the original full
integer allocation, literal order, the lower domain, every endpoint
(4), closure and both own-input guards (5). C093a excludes such a
tuple over the entire simplex. This contradiction proves the result
for each 6<=d<=33 without choosing a root or assuming survivor
feasibility.

### Sources, overlap and qualifications

The mathematical inputs are L055's pair table, L094's audited order
conclusion and C093a's audited literal exclusion. The added argument
is the explicit occurrence bijection and guard transport (3)–(5).
Neither the upstream first-displacement proof nor the literal
early-support/last-pair/survivor estimates are reproved. No numerical
certificate is rerun or inferred from a preview.

The reused formal-affine source, already specialized in those inputs,
is Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal real affine algebra is used upstream; no integer or
parity-realization converse is imported. The corresponding inspected
positive-real analytic inputs are NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), version 1.2.8 as recorded
in the prior assessment. Their hypotheses and outward remainders
are reused through the audited inputs, without fresh retrieval or
a current-release claim.

C089a and its completed audit provide a checked d=5 comparison for
the relabeling cases, not a uniform theorem input. C093b concerns
literal actual words and does not supply this all-order real result.
The prior assessment checked these overlaps and the recorded failures;
no novelty follows from a local search. Attempt 032's failed full
support test remains valid: neither the full C077a conjunction nor
L083's full theorem is invoked. Both original d=0 rational witnesses
use a different table and remain valid.

No normalized minimum or seed, integrality of x_i or x_i-kappa,
primitive-count bound, actuality or realization converse is required.
Other tables, actual-word transfer, universal entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

### Independent critical audit — 2026-10-23, step 410

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-23-uniform-all-order-real-exclusion-critical-audit.md`.
The verdict is no defect in the stated all-order real-system exclusion.
It validates this existing local assembly as an input; it adds no new
table exclusion, numerical estimate or advance beyond the inspected
source machinery. L094's step-406 audit and C093a's step-398 audit
are imported, without reconstructing their upstream analytic proofs
or numerical certificates.

**Exact common hypotheses.** L055's complete table, L094 and C093a
agree with the statement after only H_0=40-d and H_24=32670621+d
are substituted. Here d is the transfer parameter, not the original
witness's period multiplier. Both endpoints d=6 and d=33 are included;
the changed H_0 ranges from 34 down to 7. Every J, every other H,
B=9250245, kappa=23/11, G_i and Q_i agree. L055 supplies its table
only, with no witness, minimum, seed or count-ray premise.

Removing only the strict H guards leaves exactly L094's statement:
the same nonnegative integer b_i and budget, a_i=2+18b_i, permutation,
lower domain, all cyclic endpoints and non-strict own-input J guards.
In particular Q_i is wholly inside tail division and kappa is outside
in both statements. L094 therefore applies without an extra assumption.
Its rotation conclusion suffices; its stronger minimum-rotation wording
is not needed to locate any minimum in this argument.

**Rotation and all occurrences.** A literal rotation means
pi(k)=c+k modulo25. Choosing its unique row0 occurrence z gives
c+z=0 modulo25. Hence pi((z+i) modulo25)=i for every 0<=i<25,
which verifies the direction of (3). The inverse k to (k-z) modulo25
composes to the identity in both directions on these finite index sets.
Thus all 25 input occurrences are retained even when values coincide.
At x_i the outgoing row is i, so its allocation is b_i, not b_(rho_i).
No reindexing of the budget or extra integrality of an input is used.

For i<24, modular addition gives the asserted successor identity;
for i=24, rho_24=(z-1) modulo25 and rho_25=z give it separately.
If k=rho_i<24 the old successor is s_(k+1); if k=24 it is s_25,
identified with s_0 only by the assumed closing equality. These are
exactly x_(i+1) in the two cases. Thus every equation (4), including
x_25=x_0, is the corresponding original equation with no offset change.
Solving rho_i=24 gives i=24-z in the allowed range. Conversely the
new closing edge is old edge (z-1) modulo25. At z=0 both cuts are
old edge24; at z=24 they are old edges24 and23 at new positions0
and24 respectively. The same formulas cover all intermediate z.
No tail size was used, so a tail equal to 2 at either cut is retained.

**Guard transport and final application.** At k=rho_i the equalities
pi(k)=i and s_k=x_i replace both sides of each original guard exactly.
They preserve the weak J inequality and the strict H inequality, not
merely a bound on their sum. All logarithms are defined because the
bijected inputs satisfy x_i>=540/11>0. In particular the original
row18 input is at k=(z+18) modulo25, and its unchanged pair is
(693015,3295208); its H guard becomes precisely C093a's guard at
x_18, not at x_19. This remains true if that occurrence is at a cut.

The same d, table, full integer allocation and literal tuple x now
satisfy every C093a hypothesis: lower domain, all endpoints, closure
and both guard signs. Its audited exclusion yields the contradiction
directly. Its internal early-support split, endpoint-root uniqueness
and row18 failure are imported, not assumed anew or transferred to
another root. There is no minimum/seed, integer-junction, primitive-count,
actuality or realization premise. The failed full C077a conjunction
and L083's full theorem are not invoked.

**Scope and documentation.** C089a is only the d5 transport comparison;
it supplies no uniform input. Attempt 032 and both d0 witnesses remain
valid. The primary citations in the proof retain their previously
assessed hypotheses and qualifications; no new source claim or numerical
verification is made. The direct mathematical inputs remain L055,
C093a and L094, exactly as in the DAG. Since the argument is unchanged,
PROOF.md and DAG.md are not edited for audit status alone; this canonical
audit supersedes their pending C094a-audit wording. Actual-word transfer,
other tables and universal eventual descent remain unresolved. Full
matching Mathlib coverage remains unchecked, with no formal verification
claimed.

## Mathlib

Full matching Mathlib coverage is unchecked. Supporting facts about
finite permutations, affine maps and positive-real logarithms are
not a formalization of this simultaneous table-specific exclusion.
Unknown coverage is not absence; no Lean verification is claimed.
