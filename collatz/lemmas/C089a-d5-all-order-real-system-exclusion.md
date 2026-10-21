# C089a — d=5 all-order full-allocation real-system exclusion

## Hypotheses

Use the 25 indexed pairs in L055's complete table, changing only
H_0=40 to 35 and H_24=32670621 to 32670626. All J_i and other H_i
are unchanged. Put B=9250245, kappa=23/11 and

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Let b_0,...,b_24 be nonnegative integers with sum_i b_i=B, put
a_i=2+18b_i, and let pi be any permutation of {0,...,24}. Suppose
real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 and, for every
0<=k<25,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4),\qquad
H_{\pi(k)}\log2<\log s_k+J_{\pi(k)}\log(27/16).
\tag{2}
\]

All logarithms are natural. Each outgoing indexed row keeps its
allocation and own input. There is no minimum-location, seed,
integer-junction, parity, residue, exact-valuation, primitive-count or
actual-word premise.

## Conclusion

No such real tuple exists, for any cyclic order and any allocation in
the full stated nonnegative integer simplex. Consequently any larger
real system containing these hypotheses is infeasible for this table.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-all-order-real-exclusion-assembly.md`.
It composes audited implications without a new certificate or ordering
mechanism and makes no originality claim beyond the sources checked.
The separate critical audit below found no defect. No actual-word application
or universal eventual-descent conclusion is supplied. Attempt 032 and
both original d=0 rational witnesses remain valid.

## Proof

Assume the proposed tuple exists. Ignore the H half of (2) only while
applying L089. Its indexed table, B, b_i, a_i, G_i, Q_i and kappa
are identical to those here. The permutation, nonnegative integer
budget, lower domain, every cyclic endpoint (1), closing equality
and non-strict own-input J guards match all its tuple hypotheses.
Thus audited L089 implies that pi is a rotation of literal order.
Only that conclusion is used; no minimum-location assertion is needed.

Let z be the unique position in {0,...,24} with pi(z)=0. For
0<=i<25 define rho_i=(z+i) mod 25, and set rho_25=z. Since pi is
a rotation of literal order,

\[
\pi(\rho_i)=i\quad(0\le i<25).
\tag{3}
\]

Set x_i=s_(rho_i) for 0<=i<=25. Then x_25=x_0, and the rho_i
for i<25 biject all original input occurrences. Thus x_i>=540/11
and all normalized logarithms are defined. Indexed b_i and a_i stay
attached to row i; their values, integrality, nonnegativity and total
budget are unchanged.

For each 0<=i<25 put k=rho_i. If k<24, then rho_(i+1)=k+1,
including i=24, where rho_25=z=k+1. Hence the original output
s_(k+1) equals x_(i+1). If k=24, then rho_(i+1)=0 and the output
s_25=s_0=x_(i+1); this also includes i=24 when z=0. Substitution
of (3) and s_k=x_i into (1) therefore gives every equation

\[
x_{i+1}=2^{-a_i}(G_i x_i-Q_i)+\kappa,
\quad0\le i<25,\qquad x_{25}=x_0.
\tag{4}
\]

The old closing edge k=24 occurs at i=24-z. The new closing edge
i=24 is original edge k=(z-1) mod 25 into position z. When z=0
the cuts coincide; otherwise both original equations occur at their
respective normalized positions. For z=24 the old closing edge is
the first normalized edge and the new closing edge is old edge 23.
Neither cut loses an equation. No tail is replaced or discarded,
including any tail equal to 2 at either cut.

At that same old input k=rho_i, substitute (3) and s_k=x_i in both
halves of (2). This gives exactly

\[
4J_i\log2\le\log x_i+\log(11/4),\qquad
H_i\log2<\log x_i+J_i\log(27/16)
\quad(0\le i<25).
\tag{5}
\]

The J sign remains non-strict and the H sign remains strict, with
each guard belonging to the input of its own outgoing row at both
cuts. Coincident junction values remain separate occurrences; the
argument needs a bijection of occurrences, not distinct real values.

The same normalized tuple x now satisfies every hypothesis of audited
C088a: identical changed indexed table and budget, the same integer
allocation and tails, literal order, lower domain, all equations (4),
closure and both own-input guards (5). C088a excludes exactly such
a real tuple over the full allocation simplex. This contradiction
proves the conclusion.

### Sources, overlap and qualifications

L089 supplies the audited order implication and C088a the audited
literal real exclusion. L055 supplies its indexed table only. No
upstream analytic estimate, support calculation, last-pair split or
endpoint-root identification is reproved. The additional argument
(3)–(5) is the finite relabeling needed to transport every strict H
guard along with the endpoint/domain/J subsystem on the same tuple.

The reused primary affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its formal finite-word affine scope and nonzero fixed-point
denominator have already been specialized upstream. The corresponding
positive-real analytic inputs are NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), version 1.2.8 as recorded
in the ready assessment. Their hypotheses and outward bounds are
imported through the audited results. No fresh analytic estimate or
current-source-version claim is made here.

The ready assessment's scoped duplicate/failure comparison found no
completed matching d=5 all-order assembly; this is no originality
evidence. C082a treats a different d=1 table and is a normalization
precedent, not an input. C088b gives a literal actual-word application,
not this all-order real result. Attempt 032's full C077a support test
remains failed; neither that conjunction nor L083's full theorem is
invoked. The independent L089 and C088a statements suffice. Both
original d=0 rational witnesses remain valid for their different table.

No minimum or seed at normalized row0, integrality of x_i or
x_i-kappa, or realization converse enters. Actual-word transfer,
other tables, universal entry, unrestricted cycles, divergence and
universal eventual descent remain unresolved. This restricted result
is not a complete Collatz candidate.

### Independent critical audit — 2026-10-20, step 373

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-all-order-real-exclusion-critical-audit.md`.
It found no defect in the stated all-order real-system exclusion.
The checked result is applicability of the two audited implications
to the same tuple; it adds no exclusion family or analytic estimate
and makes no claim of progress beyond the inspected source machinery.

**Exact input matching.** L055's complete indexed table has H_0=40
and H_24=32670621. Both replacements here, in L089 and in C088a
are exactly H_0=35,H_24=32670626, with every other pair unchanged.
In particular the row18 pair remains (693015,3295208).
All three statements use B=9250245, kappa=23/11, the same G_i,Q_i,
natural logarithms and a_i=2+18b_i for nonnegative integers b_i
of sum B. The entire domain, permutation, endpoint, closure and
non-strict J premise set here is literally L089's. Removing only
the H requirement therefore licenses that implication, without
removing an equation or modifying an allocation. The step-369
audit supplies its independent O-test application. Its stronger
minimum-based conclusion is unnecessary: only the rotation conclusion
is used here. No minimum or seed premise is added at row0.

**Occurrence bijection and orientation.** To check the rotation direction,
write pi(k)=(c+k) mod 25 for its rotation parameter c. The unique z
with pi(z)=0 satisfies c+z=0 mod 25. Hence
pi((z+i) mod 25)=i for 0<=i<25, as claimed in (3).
The inverse occurrence map sends k to (k-z) mod 25, so no input
is omitted or duplicated. Allocation b_i is indexed by the row,
not by its chronological position; it is not replaced by b_(rho_i).
Thus x_i=s_(rho_i) has exactly outgoing row i and its original
tail a_i. Equal numerical junction values do not affect this
bijection of labeled occurrences.

**Every endpoint and the two cuts.** For i<24, rho_(i+1) is the
cyclic successor of rho_i. For i=24 the same statement holds
because rho_24=(z-1) mod 25 and rho_25=z. If rho_i<24 this
successor is rho_i+1; if rho_i=24 it is 0 and the original
closing equality s_25=s_0 supplies the endpoint value. These
two cases prove (4) for all 25 edges, including i=24.

The old closing edge k=24 lies at i=24-z, since 0<=z<=24.
For z>0 it is an interior normalized edge, from x_(24-z)
to x_(25-z); the latter is s_0. The normalized closing edge
is old k=z-1, from s_(z-1)=x_24 to s_z=x_25=x_0.
At z=0 the two edges coincide and use the original s_25=s_0
once. At z=24 the old closing edge is i=0, from s_24 to s_0,
while i=24 is old edge 23, from s_23 to s_24. These cases
agree with the written proof. No tail value was bounded, divided
out or replaced in the transport; a_i=2 is included at any edge.

**Every guard retains its own input and sign.** For each i<25,
the original guard at k=rho_i has row pi(k)=i and input s_k=x_i.
Substitution is equality of operands, not an inequality estimate,
so both the non-strict J sign and strict H sign in (5) are
unchanged. At the old closing edge the outgoing row is 24-z
and its guard is at x_(24-z); at the new closing edge the row
is 24 and its guard is at x_24, not at the output x_0.
For z=0 these are the same outgoing row24 guard. For z=24
the old closing edge instead carries row0's guard at x_0,
and the new closing edge carries row24's guard at x_24.
In particular the normalized row18 H guard is precisely the
original guard at position (z+18) mod 25, with input x_18.
No guard from a neighboring occurrence is substituted.
The lower domain transfers to every x_i and to x_25=x_0,
so all required logarithms remain defined.

**Literal exclusion and dependency scope.** The normalized tuple
therefore meets every C088a hypothesis with the original indexed
allocation: full integer simplex, literal order, all endpoints and
closure, lower domain, and both own-input guards. Its step-361 audit
establishes the literal exclusion over that whole simplex. No new
choice of root or survivor is made when invoking it. This supplies
the stated contradiction without integrality of any junction or
actual-word realization.

The direct mathematical inputs remain L055 (table only), L089
(order implication) and C088a (literal exclusion). Their internal
inputs are used through these audited results, not added as new
direct dependencies. The primary citations and their qualifications
above remain unchanged; no source theorem is newly specialized or
reproved, and no discrepancy requires rerunning upstream certificates.
The ready assessment's known-result and duplicate comparisons were
reused, and the scoped local search found the construction and
proposed audit, not a prior completed C089a audit. This is not
evidence of originality. C082a and C088b remain comparison results,
not mathematical inputs to this proof.

Attempt 032's failed full support test and both d=0 rational
witnesses remain intact. Neither the full C077a conjunction nor
L083's full theorem enters. Actual-word transfer, other tables,
unrestricted cycles, divergence and universal eventual descent
remain unresolved. The proof and direct DAG inputs are unchanged,
so PROOF.md and DAG.md are not edited for audit status alone.
This canonical audit supersedes their pending-audit wording for C089a.

## Mathlib

Full matching Mathlib coverage has not been checked. Supporting facts
about finite permutations, modular indices and real inequalities do
not by themselves constitute a matching fixed-table exclusion.
Unknown availability is not absence; no Lean verification is claimed.
