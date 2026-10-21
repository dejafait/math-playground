# C082a — Redistributed-H all-order allocation real-system exclusion

## Hypotheses

Use L055's complete indexed 25-row pair table, replacing only
H_0=40 by 39 and H_24=32670621 by 32670622, exactly as in L079.
Let b_i>=0 be integers with sum_i b_i=B=9250245, and attach
a_i=2+18b_i to outgoing indexed row i. Let pi be any permutation
of {0,...,24}. All logarithms are natural. Set

\[
\kappa=23/11,\qquad G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Consider real s_0,...,s_25 with s_25=s_0 and s_k>=540/11,
subject to all endpoints and both own-input guards

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4),\qquad
H_{\pi(k)}\log2<\log s_k+J_{\pi(k)}\log(27/16)
\quad(0\le k<25).
\tag{2}
\]

Every indexed pair and tail stays attached to its own outgoing input.
No minimum location, seed, junction integrality, parity, residue,
exact valuation, primitive orbit or count-ray premise is imposed.

## Conclusion

The real endpoint/domain/J/H system (1)–(2) is infeasible for every
such allocation and permutation. Consequently the full L051 (1)–(4)
system for this changed table is infeasible in every cyclic order over
the full nonnegative integer allocation simplex: its chronological
parameters are (J_pi(k),H_pi(k),a_pi(k)). Its extra count, minimum and
seed requirements cannot restore feasibility of this necessary subsystem.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-full-real-exclusion-assembly.md`.
It assembles audited local inputs; it claims no new general theorem or
originality beyond the sources checked. The separate critical audit below
found no defect in this assembly. Both original-table rational witnesses and Attempts
026–031 remain valid. Other tables, universal entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

## Proof

### Apply the certified necessary reduction

Suppose (1)–(2) has a tuple. Discard only its H guards temporarily.
The remaining endpoint/domain/non-strict own-input J conditions are
exactly C077a (6), with r=25, B=9250245 and tau=2. L055 supplies
the indexed pair data; only the two H replacements stated above are
made. The J_i are increasing integers at least 2 and the changed H_i
are integers at least 39. L079 certifies every independent C077a data
test on precisely this table and budget: the full order package, the
full support package (B>0), and the unconditional and boundary cutoff
packages (tau<=B). We import those audited certificates and C077a's
implication, without recalculating margins or inferring one test from
another. L079's stated necessary reduction therefore applies.

The permutation is a rotation of literal indexed order. Let z be its
unique position with pi(z)=0, define rho_i=(z+i) mod 25 for i<25,
rho_25=z, and set x_i=s_(rho_i). Then pi(rho_i)=i and x_25=x_0.
C077a gives

\[
b_0=\cdots=b_{22}=0,\qquad b_{23}=t,\quad b_{24}=B-t,
\qquad t\in\{0,1\}.
\tag{3}
\]

This is a necessary condition only; no survivor feasibility is used.

### Retain every endpoint and own-input H guard across both cuts

The rho_i biject all 25 input occurrences. If rho_i<24, the old
edge rho_i to rho_i+1 has output x_(i+1). If rho_i=24, its output
is s_25=s_0=x_(i+1). This includes i=24, whose output is x_25=x_0.
The old closing edge is now at i=24-z. The new closing edge is the
old edge z-1 to z modulo 25. For z=0 the cuts coincide; otherwise
both edges are retained at their respective positions. Thus (1) becomes

\[
x_{i+1}=2^{-a_i}(G_i x_i-Q_i)+\kappa
\quad(0\le i<25),\qquad x_{25}=x_0.
\tag{4}
\]

At the same old input k=rho_i, substitute pi(k)=i and s_k=x_i
in each inequality (2). This gives exactly

\[
4J_i\log2\le\log x_i+\log(11/4),\qquad
0<\log x_i+J_i\log(27/16)-H_i\log2.
\tag{5}
\]

Also x_i>=540/11, so every logarithm is defined. The strict H sign
is unchanged, including at the outgoing rows of both cuts. Coincident
junction values remain separate input occurrences. We do not claim
x_0 is a minimum or that a seed inequality at chronological input zero
holds at x_0. Neither premise will be used.

### Identify and reject both exact endpoint roots

If t=0, (3) gives a_i=2 for i<24 and
a_24=2+18*9250245=166504412. These are exactly L081's literal
tails and changed pairs. Its exact-root/uniqueness proof uses only
the cyclic endpoint equations, not a minimum, seed or other guards.
Hence the normalized endpoint solution (4) equals that unique root
at every index. L081's audited conclusion gives, at its own row 18,

\[
\log x_{18}+693015\log(27/16)-3295208\log2
<-\frac{457745289}{50000000000}<0.
\tag{6}
\]

If t=1, (3) instead gives a_i=2 for i<23, a_23=20 and
a_24=2+18*(9250245-1)=166504394. These match L082 at every row,
including both transferred tails. Its independently audited
endpoint-root uniqueness and unconditional H failure apply to (4),
again without a minimum or seed premise, and give the same strict
inequality (6). No t=0 root estimate is transferred to this case.

Both cases contradict the own-input row-18 H guard in (5), whose
parameters are exactly J_18=693015 and H_18=3295208. Since (3)
exhausts the integer survivor range, no tuple (1)–(2) exists.
The full L051 system contains this subsystem at every chronological
row, proving the stated consequence without transporting its seed
or minimum requirement.

The upstream finite affine identity is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-word and nonzero-denominator qualifications are already
checked in L081/L082 through positive Lambda. Their positive-real
analytic bounds use the precisely cited DLMF identities and complete
rational certificates there. This proof imports those canonical root
conclusions and the certified reduction; it neither reproves these
general inputs nor reruns their calculations. In particular it uses
no arithmetic nonintegrality or integer-cycle theorem on real tuples.

### Independent critical audit — 2026-10-18, step 329

This RESEARCH/REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-full-real-exclusion-critical-audit.md`.
It finds no defect in the all-order, full-allocation real exclusion.
The complete C082a proof was checked against L051 (1)–(4), L055's
complete indexed pair table, C077a's statement and audited normalization,
L079's certified reduction, and the statements, uniqueness arguments and
relevant completed audit passages of L081/L082. Their numerical
certificates are imported audited inputs, not newly executed checks.

**Exact domains and implication.** The table in all three changed-table
inputs has only H_0=39 and H_24=32670622 substituted into L055's pairs.
Its strictly increasing integer J_i and integer H_i>=39 satisfy C077a's
pair domains. The budget and cutoff are exactly r=25, B=9250245,
tau=2. L079 certifies every independent O/S/C test, including support
because B>0 and boundary cutoff because tau<=B. Removing H from (2)
leaves precisely C077a (6): real lower-domain junctions, every cyclic
endpoint and each own-input non-strict J guard. No count, minimum,
seed, or integer-junction hypothesis is needed for that implication.
The integer allocation, however, is essential: t=b_23 is integral,
so 0<=t<=B and t<2 leave exactly the possibilities 0 and 1. The
proof does not extend this statement to a real-valued allocation simplex.

**Independent cut and strictness check.** Only after the reduction gives
literal cyclic order is z, the position of indexed row 0, selected.
For 0<=i<25, rho_i=(z+i) mod 25 satisfies pi(rho_i)=i and
rho_(i+1)=rho_i+1 modulo 25, with rho_25=z. Thus the output of
old edge rho_i is x_(i+1): for rho_i=24 this uses s_25=s_0;
otherwise it uses the ordinary next endpoint. The old closing edge
has i=24-z. The new closing edge i=24 has old input z-1 modulo 25
and old output z. At z=0 both cuts coincide; at z=24 the old closing
edge becomes i=0 and the new closing edge is old 23 to 24. All
intermediate cuts satisfy the same formulas. Both affine offsets and
the indexed tail a_i therefore remain in (4) at every edge.

At old input rho_i the H inequality is exactly
H_i log2<log x_i+J_i log(27/16). Subtracting its left side gives
the strictly positive margin in (5), with no multiplication or change
of sign. In particular row 18's original input is old position
(z+18) mod 25; it is the normalized x_18, irrespective of coincident
junction values. The lower domain transfers pointwise, ensuring every
logarithm is defined. Neither this argument nor the component root
failures need x_0 to be a minimum or to inherit the old seed bound.

**Exact allocations and unconditional root identity.** At t=0 all tails
before row 24 equal 2 and the last is 166504412, exactly L081. At
t=1 the tails before row 23 equal 2, row 23 has 20 and row 24 has
166504394, exactly L082. Both use the same changed pairs and literal
normalization, not just the same total tail sum. Their already audited
uniqueness statements concern the endpoint equations alone. In each
case n_i=x_i-kappa obeys n_(i+1)=c_i(n_i+eta_i), and closure forces
n_0=C_25(n_0+R), with their C_25=exp(-Lambda)<1. Thus every real
endpoint solution has their unique n_0; the deterministic recurrence
identifies every subsequent coordinate, including x_18. This argument
uses neither survivor feasibility nor any full-system seed premise.

The unchanged row-18 pair is (693015,3295208), directly matching
L055 and both component statements. Each component separately proves
its unique root has that row's H margin strictly below
-457745289/50000000000<0. The needed sign from (5) is >0.
Hence both cases contradict the same necessary guard. Equal reported
upper bounds do not identify the two roots; each root uses its own
audited estimate and its own closing tail. No arithmetic nonintegrality
argument enters this contradiction.

**Full-system consequence and scope.** A full L051 tuple for any admitted
chronological order has exactly the endpoints and two guards above,
with h_k=log s_k and s_k>=540/11. Discarding its extra count, minimum
and seed constraints gives the infeasible subsystem. There is no need
to transport those discarded constraints to indexed row 0. The original
table's two rational witnesses have different H entries; Attempts
026–031 and C080a/C080b's distinct integer/actual-word conclusions are
unaffected. The inspected histories 327/328 contain assembly and source
comparison, not a previous independent C082a audit.

The precise upstream citation remains Halbeisen–Hungerbuehler (1997),
section 2, equations (2)–(4), Lemma 2, pp. 228–229, cited above.
The component audits already check the nonzero affine denominator and
positive-real analytic specializations; no pseudo-cycle converse or
integer-cycle theorem is applied to arbitrary reals. This audit checks
their conjunction and the finite relabeling, not the analytic machinery
again. The direct mathematical inputs remain exactly those in the
existing DAG row. The argument is unchanged, so PROOF.md and DAG.md
are unchanged; this canonical verdict supersedes their pending C082a
audit wording. This validates a restricted local input, not a new
general theorem beyond the sources checked or a Collatz candidate.
Other tables, universal entry, divergence and eventual descent remain
unresolved.

## Mathlib

Full matching coverage of this finite changed-table all-order real
exclusion has not been checked. Supporting affine and analytic results
are distinct from a full matching theorem; unknown coverage is not
evidence of absence. No Lean build or formal verification is claimed.
