# C099a — d34 all-order full-allocation real-system exclusion

## Hypotheses

Use the 25 indexed pairs in L055's complete table, changing only
H_0=6 and H_24=32670655. All J_i and all other H_i are unchanged.
Set B=9250245, kappa=23/11 and

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Let b_i be nonnegative integers with sum_(i=0)^24 b_i=B, put
a_i=2+18b_i, and let pi be any permutation of {0,...,24}.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 for
0<=k<25 and,
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

All logarithms are natural. Each outgoing indexed row keeps its
allocation and own input. No minimum-location, seed, integer-junction,
parity, residue, exact-valuation, primitive-count or actual-word premise
is imposed.

## Conclusion

No such real tuple exists in any cyclic order over this full integer
tail-allocation simplex. Consequently any stronger real system containing
these hypotheses is also infeasible for this table.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-d34-all-order-real-assembly.md`. It combines
audited inputs, without a new analytic estimate, certificate or mechanism,
and makes no claim of progress beyond the checked source machinery.
The separate step446 critical audit below found no defect. Actual-word transfer, arbitrary
tables and universal eventual descent remain unresolved; this is not a
complete Collatz candidate.

## Proof

Assume such a tuple exists and keep its indexed table and allocation
fixed. Disregard only the strict H guards in (2). Every remaining
hypothesis is precisely a hypothesis of audited L097: the identical
d34 pairs, B, nonnegative integer b_i, tails a_i, arbitrary permutation,
all lower domains, all 25 equations (1), closing equality and non-strict
own-input J guards. Thus L097 implies that pi is a rotation of literal
order. Use only that conclusion, without locating a minimum.

Write pi(k)=(c+k) mod25. Let z be the unique position carrying indexed
row0, so pi(z)=0 and c+z=0 mod25. Define

\[
\rho_i=(z+i)\bmod25\quad(0\le i<25),\qquad
\rho_{25}=z,\qquad x_i=s_{\rho_i}\quad(0\le i\le25).
\tag{3}
\]

For 0<=i<25, pi(rho_i)=i. The map i to rho_i bijects all 25
original input occurrences, with inverse k to (k-z) mod25.
Consequently x_i>=540/11 and x_25=x_0. Equal numerical junctions
remain distinct indexed occurrences. The outgoing row at x_i is i,
with its original b_i and a_i; the allocation is not replaced by
b_(rho_i). Hence its integer nonnegativity and budget are unchanged.

For any 0<=i<25 put k=rho_i. The cyclic successor of k is
rho_(i+1): for i<24 this is modular addition, while for i=24 it
follows from rho_24=(z-1) mod25 and rho_25=z. If k<24 the
original output is s_(k+1)=x_(i+1). If k=24 the original output
is s_25=s_0=x_(i+1), using closure. Thus (1) becomes exactly

\[
x_{i+1}=2^{-a_i}(G_i x_i-Q_i)+\kappa\quad(0\le i<25),
\qquad x_{25}=x_0.
\tag{4}
\]

Both cuts are retained. The original closing edge k=24 occurs at
normalized position i=24-z. The normalized closing edge i=24 is
original edge k=(z-1) mod25, with output at original position z.
When z=0 the two cuts coincide at original edge24. When z=24 the
old closing edge is normalized edge0 and the new closing edge is old
edge23. Every intermediate z satisfies the same identities. All 25
allocated tails remain at their outgoing rows, including tail2 at either
cut. In particular Q_i remains wholly inside tail division and kappa
outside; no endpoint or offset has been estimated or omitted.

At the same original input k=rho_i, substitute pi(k)=i and s_k=x_i
into both guards (2). This gives

\[
4J_i\log2\le\log x_i+\log(11/4),\qquad
H_i\log2<\log x_i+J_i\log(27/16)\quad(0\le i<25).
\tag{5}
\]

Both signs are preserved, and the lower domain ensures every logarithm
exists. In particular row18's strict H guard is the original guard at
position (z+18) mod25, at x_18 with its unchanged pair
(693015,3295208), even if this occurrence lies at a cut. It is not a
guard at the neighboring output.

The normalized tuple x, original b_i and changed pairs now satisfy
every hypothesis of audited L099: literal order, full integer simplex,
all lower domains, all endpoints (4), closure and non-strict own-input
J guards (5). Its conclusion gives b_0=...=b_22=0. Set t=b_23.
Nonnegative integrality and sum b_i=B imply

\[
t\in\mathbb Z,\quad 0\le t\le B,\quad b_{24}=B-t,\qquad
a_i=2\ (0\le i\le22),\quad
a_{23}=2+18t,\quad a_{24}=2+18(B-t).
\tag{6}
\]

No allocation is dropped: (6) describes the complete remaining closed
integer interval, including t=0,1 and every 2<=t<=B. At t=B the last
tails are (166504412,2); equation (4) still supplies its closing edge.

On this same tuple x, (4) is exactly the endpoint system of audited
C096a, with its identical table, kappa and tails (6). Its lower domain
and both own-input guard signs are exactly those already established.
Every C096a hypothesis therefore holds for this integer t. C096a
excludes such a tuple throughout 0<=t<=B, a contradiction. Its upper
branch rejection and two endpoint-root H failures are imported as
proved consequences, without assuming either survivor is feasible or
substituting a tuple at another cut. This proves the conclusion.

### Sources, overlap and qualifications

The mathematical inputs are L055's table only, audited L097, audited
L099 and audited C096a. The added proof is their same-tuple assembly
via (3)–(6). No upstream ordering, first-recipient or endpoint-root proof
is repeated and no numerical certificate is rerun. C094a's d6–33
normalization is a checked precedent, not a d34 exclusion input.
C096b concerns only literal last-pair actual words and is not a premise.

The inherited formal-affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2, equations (2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-word real affine/nonzero-denominator specialization is
already justified in the audited inputs; no integer realization theorem
enters here. The inherited analytic inputs are NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), version1.2.8 as recorded in
the reused assessment, without a current-release claim. Their positive
arguments and finite remainder estimates are reused through the inputs;
this assembly makes no new analytic application or source reproof.

Attempt032's failed full support and fixed d34 C/H caps remain valid.
Neither the full C077a/L083 conjunction nor a failed sufficient test is
a premise. Both original d0 rational witnesses remain on their different
table. No minimum/seed, junction integrality, primitive count, realization
or actual-word premise was introduced. Other tables, universal entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. The separate step446 audit below validates this assembly
within precisely its stated real-system scope.

### Independent critical audit — 2026-10-24, step446

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-d34-all-order-real-critical-audit.md`.
This RESEARCH/REPRODUCTION proof audit found no defect in the
same-tuple assembly (1)–(6). It secures an existing local input;
it supplies no additional exclusion or progress beyond the checked
source machinery. The test was to withhold verification or correct
the statement on any missing premise, index, boundary or strict sign.

**Identical table and original tuple.** Read L055's complete pair
table and the statements and completed audits of L097 (step434),
L099 (step442) and C096a (step426). Each changes exactly H_0 from
40 to 6 and H_24 from 32670621 to 32670655, with every J and
other H unchanged. In particular row18 is (693015,3295208).
All three use B=9250245 and kappa=23/11. L055 contributes only
its indexed pairs, not its witness allocation or extra hypotheses.

Deleting only the H guards from C099a leaves exactly L097's
original-tuple hypotheses: the same integer allocation, permutation,
lower domain, cyclic endpoints, G_i,Q_i and non-strict own-input J
guards. Its completed audit licenses the cyclic-order conclusion
without adding a minimum-location premise. C099a uses only that
conclusion; it does not need the stronger assertion about a chosen
minimum. No H guard is used to justify the ordering input.

**Occurrence map, inverse and both cuts.** From pi(k)=c+k modulo25,
choose the unique z in {0,...,24} with c+z=0 modulo25. For every
i in this index set, pi((z+i) mod25)=i. Subtracting z modulo25
inverts this map; thus all 25 original occurrences appear exactly
once, even when their numerical values coincide. Keep b indexed
by the outgoing row. At new position i the outgoing row is i,
so its tail is a_i=2+18b_i, not a_(rho_i).

For i<24, rho_(i+1) is the cyclic successor of rho_i. At i=24,
rho_24=(z-1) mod25 and rho_25=z give the same successor identity.
If rho_i<24, the original edge outputs s_(rho_i+1), which is
x_(i+1), including the new closing edge when z>0. If rho_i=24,
its original output is s_25=s_0, which is x_(i+1). The equality
s_25=s_0 is used here rather than discarding the original edge.

Solving rho_i=24 gives i=24-z, already in {0,...,24}. Thus the
old closing edge is retained there. The new closing edge has old
index (z-1) mod25. For z=0 both are edge24; for z=24 the old
closing edge is new edge0 and the new closing edge is old edge23.
For 1<=z<=23 the old closing edge lies at 24-z and the new
closing edge is old edge z-1, with output s_z=x_0. This exhausts
the cuts. Every edge retains its full Q_i inside 2^(-a_i) and
kappa outside. No restriction excludes a_i=2 at either cut or
any other occurrence.

**Both own-input guards and early support.** Substitution uses the
same equalities pi(rho_i)=i and s_(rho_i)=x_i in both guards.
Consequently the J sign remains <= and the H sign remains <;
all logarithms exist because x_i>=540/11>0. Row18's input is
precisely original occurrence (z+18) mod25. Its H margin is
log(x_18)+693015 log(27/16)-3295208 log2>0. No output or
neighboring input is substituted, including when row18 occurs
at an original or normalized cut.

After this substitution the identical table, unchanged integer
allocation and budget, literal order, lower domains, all endpoints,
closing equality and non-strict J guards are exactly L099's full
hypotheses. Its audited conclusion b_0=...=b_22=0 therefore holds
for this normalized tuple. Extra H guards cause no missing premise;
neither a minimum, seed nor a failed support-offset test is required.

**Full residual interval and final contradiction.** Nonnegativity,
integrality and the unchanged sum now give t=b_23 in Z, t>=0
and b_24=B-t>=0, hence t<=B. Conversely every integer t in this
closed interval describes an allowed remaining allocation; this
asserts allocation coverage, not endpoint feasibility. Every earlier
tail is 2. Since 18B=166504410, the last tails are
(2,166504412) at t=0, (20,166504394) at t=1, and
(166504412,2) at t=B. All intermediate integers are included.

On precisely this same x tuple the endpoints, lower domains and
both guards equal C096a's hypotheses term by term, including its
closing edge at final tail2. C096a's audited conclusion excludes
every integer 0<=t<=B. Its step426 audit covers the whole upper
branch 2<=t<=B and both unique endpoint roots t=0,1, whose row18
H margin is strictly negative. The transported guard requires that
same margin strictly positive. Neither root's feasibility is assumed,
and no alternate cut or alternate endpoint tuple enters this application.

**Evidence and limits.** The independent work here is the complete
finite-index argument and hypothesis matching above. The upstream
analytic constants, quantified exclusions and their completed audits
are imported, not reverified by a certificate rerun. The precise
primary citations and qualifications in the preceding source section
remain in force; there is no new external theorem application or
unnecessary source reproof. Histories444–445 and the assembly working
note recorded no earlier completed C099a audit. C094a is only a
different-table precedent, and C096b is not a premise.

The direct inputs remain L055(table), L097, L099 and C096a, exactly
as in DAG.md. No proof argument or dependency changed, so PROOF.md
and DAG.md receive no status-only edit; this canonical audit supersedes
their pending-audit descriptions of C099a only. Attempt032, failed
S/C/H data, both d0 witnesses and unfinished work remain valid.
No integer-junction, realization, primitive-count or actual-word
premise was introduced. Actual-word transfer, other tables and
universal eventual descent remain unresolved. Full matching Mathlib
coverage remains unchecked, and no formal verification is claimed.

## Mathlib

Full matching Mathlib coverage is unchecked. Supporting finite cyclic
indexing, affine-map and logarithm facts are not a formalization of
this simultaneous table-specific exclusion. Unknown coverage is not
absence; no Lean verification is claimed.
