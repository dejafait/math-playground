# C108a — All-order d35 full-simplex real-system exclusion

## Hypotheses

Take the 25 indexed pairs from L055's table, changing only H_0 to 5
and H_24 to 32670656. Put

\[
B=9250245,\qquad \kappa=23/11,\qquad
b_i\in\mathbb Z_{\ge0}\ (0\le i<25),\qquad \sum_{i=0}^{24}b_i=B,
\]
\[
a_i=2+18b_i,\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Let pi be any permutation of {0,...,24}. Suppose real junctions
s_0,...,s_25 satisfy s_25=s_0 and s_k>=540/11 for 0<=k<25.
At every occurrence k require the exact endpoint and both own-input
guards

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

All logarithms are natural. A permutation moves each intact outgoing
indexed row, including its pair and tail budget; both guards refer to
that row's actual input. Every zero budget is allowed, including a tail2
on the closing edge. No prescribed minimum, seed, integer/parity/residue
junction, exact valuation, word realization or primitive period is assumed.
Equal junction values remain distinct occurrences; repeated periods
within this specified language are not excluded by an added hypothesis.

## Conclusion

No such real tuple exists for any intact-row permutation and any
allocation in the full stated integer simplex.

This is a local RESEARCH/REPRODUCTION assembly of audited inputs under
the prior SPECIALIZE assessment
`drafts/literature/2026-10-27-d35-all-order-full-guard-assembly.md`.
It removes the order restriction from C107a for this fixed table and
budget. The separate step529 critical applicability audit below finds
no defect relative to the audited inputs.
It is neither a complete Collatz candidate nor a claim of progress
beyond the checked source machinery; actual-word transfer is not proved here.

## Proof

Assume such an allocation, permutation and tuple exist. Keep this same
allocation and these coordinates throughout. Every s_k>=540/11>0,
so all logarithms in (2) are defined.

**Apply the order conclusion.** L108, including its step525 audit,
has exactly this indexed table, B, kappa, integer simplex and tails.
Its endpoint equations, lower domains, closure and non-strict J guards
are exactly (1) and the first inequalities of (2). Forget only the
H guards when applying L108; do not infer them from the J guards.
The minimum of the finite nonempty list s_0,...,s_24 is attained.
Choose any occurrence q in {0,...,24} attaining it. No initial minimum
location or uniqueness is assumed. L108 gives

\[
\pi(\rho(i))=i\quad(0\le i<25),\qquad
\rho(i)=(q+i)\bmod25.
\tag{3}
\]

**Construct the same rotated tuple.** For 0<=i<25 set
t_i=s_{rho(i)}, and set t_25=t_0. The map rho is a bijection on
the occurrence indices, with inverse k -> (k-q) mod25. Hence no
input or outgoing edge is removed or duplicated. Keep the indexed
budgets b_i unchanged: the row at occurrence rho(i) has label i by
(3), so it already carries b_i, a_i, J_i and H_i. This is not a new
allocation or a newly solved endpoint root. In particular the integer
nonnegativity and sum B remain unchanged.

For i<24, rho(i+1) is rho(i)+1 modulo25. For i=24, rho(24)+1
is rho(0) modulo25. Thus in every case the successor of the old
occurrence k=rho(i) is represented by t_{i+1}: if k<24 it is s_{k+1},
and if k=24 it is s_25=s_0. Substituting (3) in the old equation (1)
at that very occurrence therefore gives all25 equations

\[
t_{i+1}=2^{-a_i}(G_i t_i-Q_i)+\kappa
\quad(0\le i<25),\qquad t_{25}=t_0.
\tag{4}
\]

Both terms of Q_i remain inside the division by 2^{a_i}; kappa
remains outside. Moreover t_i>=540/11 for every i<25, because it
is one of the original inputs.

**Transport both guards at their own inputs.** For each i substitute
k=rho(i), pi(k)=i and s_k=t_i into each original inequality in (2).
They become, without any estimate or change of strictness,

\[
4J_i\log2\le\log t_i+\log(11/4),\qquad
H_i\log2<\log t_i+J_i\log(27/16)
\quad(0\le i<25).
\tag{5}
\]

In particular the strict H guard is an assumption carried from the
same original occurrence, not a consequence of order rigidity or of
the J guard. This also covers row0 with H_0=5 and row24 with
H_24=32670656; neither changed H value is assigned to another row.

**Both cuts and boundary budgets.** The original closing edge24 to0
occurs at the unique new index i_*=(24-q) mod25 and is included in
(4) by s25=s0. The new closing edge i=24 to i=0 is the old edge
(q-1) mod25 to q. Its outgoing label is24 by (3), so it carries
precisely a24=2+18b24 and has both own-input guards at t24.

If q=0, rho is the identity and both closing edges are the old24 to0
edge. If q=24, the old24 to0 edge becomes t0=s24 to t1=s0,
whereas the new closing edge is t24=s23 to t25=s24, the old23 to24
edge. If 1<=q<=23, the old closing edge occurs at i_*=24-q<24,
and the old q-1 to q edge closes the new tuple. These cases cover
every possible q. The original closing tail is a_{pi(24)}=a_{i_*};
it stays on that edge even when it becomes internal. If its budget
is zero it remains exactly2. Independently, if b24=0 the new
closing tail is2, and its endpoint and both guards still occur in
(4)–(5). All other zero budgets are likewise retained. No budget
has been replaced by a comparison tail.

No sorting or identification by junction value occurred: rho acts on
positions even when values coincide. We used only attainment of a
minimum to apply L108, and impose no strict-minimum or primitive-period
condition on the original tuple or the result.

**Apply the literal exclusion.** C107a, including its step519 audit,
requires the same literal indexed pairs and two H changes, B, kappa,
integer allocation, tails, G_i and Q_i. These have all been retained.
The rotated real tuple has its lower domains and closure, every
endpoint (4), and exactly the non-strict J and strict H guards (5).
They are all C107a's hypotheses on one allocation and one tuple;
C107a requires no minimum, seed or realization premise. Its exclusion
therefore contradicts existence of this tuple. This proves the claim
for the arbitrary original pi and b, hence for their entire stated domains.

### Sources, verification and qualifications

L055 supplies only its indexed pair table, not its original-H witness,
fixed allocation, seed or minimum. L108 and C107a supply their audited
conclusions. The only additional work is the explicit occurrence
reindexing and the hypothesis matching (3)–(5). No new analytic estimate,
certificate or numerical replay is needed because no operand in the
component proofs changes.

The prior assessment reuses the primary affine coverage in Halbeisen
and Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-word and nonzero-denominator qualifications remain in the
audited components; it supplies no integer-itinerary realization here.
The finite-maximum coverage used upstream is Blanchard, Higham and
Higham, *Accurate Computation of the Log-Sum-Exp and Softmax Functions*,
MIMS EPrint2019.16, author version2019-09-08,
[equation(1.6), section4 equations(4.1)–(4.2), printed pp.3,8](https://eprints.maths.manchester.ac.uk/2728/1/paper.pdf).
The components retain their positive-real analytic domains and certified
remainders from NIST DLMF version1.2.8,
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
These are reused precise citations, not new source retrievals or claims
that a primary source states this particular exclusion. No source
theorem is reproved or stronger ordering theorem asserted.

Attempts027,032–035 remain preserved. In particular failure of the
joint S/C/H package is not used as a feasibility verdict and does not
invalidate L108's independent O argument. Original-H witnesses and
the endpoint-only counterexample use different hypotheses. This result
does not extend to fractional budgets, changed tables or arbitrary word
languages. Actual-word transfer, entry, other tables, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

### Independent critical applicability audit — 2026-10-27, step529

This RESEARCH/REPRODUCTION proof audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-27-c108a-all-order-assembly-critical-audit.md`.
Read the complete C108a, L108 and C107a, including the latter two
canonical audits, and L055's complete indexed pair table only. Reuse
the primary statements and proof-case coverage recorded in that
assessment; no source theorem is reproved and no numerical operand
in the audited components changes. This audit checks the finite
application, not the components' certificates afresh.

**L108 applies to the original object.** All three statements change
exactly L055's H_0=40 to5 and H_24=32670621 to32670656; the other
23 H values and all25 J values remain identical. They use the same
B=9250245, kappa=23/11, nonnegative integer indexed budgets summing
to B, and a_i=2+18b_i. In C108a and L108, pi is a permutation of
these same intact indexed rows. Their endpoint equations coincide,
including both summands of Q_i inside the division and kappa outside;
so do their closure, lower domains and own-input non-strict J guards.
Every input is positive. Forgetting only the H inequalities therefore
supplies every L108 hypothesis on the original tuple. L108's audited
conclusion is explicitly valid at any attained minimum occurrence q,
not at a prescribed, unique or strict minimum. The finite list has
such an occurrence. Its conclusion is exactly (3).

**Bijection and all endpoints.** On occurrence indices modulo25,
rho(i)=q+i has inverse k -> k-q. In particular it is a bijection,
even if some junction values are equal. For i<24 the cyclic successor
of rho(i) is rho(i+1); for i=24 it is rho(0). If rho(i)<24, the old
endpoint's output is s_{rho(i)+1}; if rho(i)=24, its output is
s_25=s_0. These are precisely t_{i+1}, including t_25=t_0 in
the i=24 case. Thus each of the 25 original equations supplies
exactly one equation (4), and none is replaced by a freshly solved
endpoint. By (3) that equation has label i, with the original b_i,
a_i, G_i and Q_i. The integer simplex is unchanged; C107a restricts
neither its support nor the position of a minimum. Every t_i for
i<25 is an original input and hence has the required lower domain.
Closure gives the same positive lower domain at t_25.

**Every guard, with its original sign.** At occurrence rho(i), the
original assumptions are

\[
4J_{\pi(\rho(i))}\log2
 \le\log s_{\rho(i)}+\log(11/4),\qquad
H_{\pi(\rho(i))}\log2
 <\log s_{\rho(i)}+J_{\pi(\rho(i))}\log(27/16).
\]

Substituting pi(rho(i))=i and s_{rho(i)}=t_i gives exactly (5),
for every i=0,...,24. No logarithm is evaluated at an output in
place of the original input, and no exponential or limiting argument
changes either inequality. In particular H_0=5 and H_24=32670656
remain attached to their own rows. The H guards are carried from
C108a's assumptions, independently of the J-only order theorem.

**Two cuts, including the endpoints of q's range.** Solving
rho(i)=24 gives i_*=(24-q) mod25. Thus the old24-to0 edge is
present at exactly i_*, carrying a_{pi(24)}=a_{i_*} and both
guards at t_{i_*}. The new closing edge i=24 is the old edge
(q-1) mod25 to q, with label24, tail a_24 and guards at t_24.
For q=0, i_*=24 and these are the same old24-to0 edge. For q=24,
i_*=0: the old24-to0 edge is t_0=s_24 to t_1=s_0; the new
closing edge is t_24=s_23 to t_25=s_24. For 1<=q<=23,
i_*=24-q is internal and the old q-1 to q edge closes the new
tuple. Hence no boundary case drops an equation or its guards.
If b_{i_*}=0 the old closing tail remains2, and if b_24=0 the
new closing tail remains2, independently. The proof uses no positive
lower bound for any b_i, sorting by values, distinctness or primitive
period condition. All permitted zero budgets, ties and repetitions
remain in the quantified scope.

**C107a applies and the dependency direction is sound.** Equations
(4), closure, all lower domains and both guard families (5), on
the same unchanged integer allocation, are every C107a premise.
The additional attained-minimum property of t_0 is unused by C107a.
Its audited exclusion is therefore a contradiction. L108 imports
L075/L084 and does not assume C107a or C108a; C107a imports C103a
and L107 and does not assume L108 or C108a. There is no circular
application. L055 contributes its table only, with no witness,
seed, minimum, junction integrality or word-realization premise.

**Verdict and limits.** No defect, repair, narrowing or dependency
change is required: C108a is valid as stated relative to its audited
inputs. Direct inputs remain L055 (table only), C107a and L108,
exactly the existing DAG row. This secures an existing restricted
exclusion by checking its applicability; it neither strengthens the
theorem nor establishes progress beyond the checked source machinery.
Attempts027,032–035 retain their recorded scopes and supply no premise.
No arithmetic defect was found that would justify certificate replay.
The mathematical argument is unchanged, so PROOF.md and DAG.md are
unchanged by this audit; this canonical verdict supersedes pending
C108a-audit wording in the overview. Actual-word transfer, entry,
other tables, unrestricted cycles, divergence and universal eventual
descent remain unresolved. No complete candidate is asserted.

## Mathlib

Full matching coverage for this exclusion is unchecked, not known absent.
Supporting finite cyclic reindexing and guard-substitution coverage is
also unchecked here. No Lean verification is claimed; the informal
application and its exact hypotheses are given above.
