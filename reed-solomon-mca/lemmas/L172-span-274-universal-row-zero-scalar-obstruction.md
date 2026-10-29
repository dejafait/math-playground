# L172 — Universal row-0 scalar obstruction on saved span 274

## Hypotheses

Let E be any extension field of F_97. Order coordinates by
S=(1,8,12,18,22,27,33), and put J=(47,50,64,70,75,79,85,89,96).
Index supports by increasing pairs in S (outer) and J (inner), zero-based:
label a has I_a at index floor(a/36) and K_a at index a modulo 36.
Use L109's original maps, with O_a=S minus I_a, z_a=min(O_a),
g_a(X)=product_(y in J minus K_a)(X-y), and rows of Q_a

    c_ax(h)=g_a(z_a) h_x-g_a(x) h_z_a,  x in O_a minus {z_a}.

Use increasing covector pairs and increasing S-coordinate pairs for
N_a=exterior-square(Q_a). Fix the actual history T=(0,51,98,177,318).
The complete saved kernel is span 274 at node 1006 of
`scripts/pair-free-envelope/cover.json`, with the completeness and
actual-history identification furnished by the existing finite certificate
`scripts/pair-free-envelope/verification.json`. This is an explicit reused
computational input, not a new rank calculation or separate audit of that
cover. Its generating history (0,51,98,143,318) is different from T.
The precise reused evidence and its role are specified below.

For the coding consequence additionally assume L109's necessary-direction
hypotheses: F=F_(97^20), the order-sixteen subgroup H, k=8, unit
multipliers, 1/4<=delta<5/16, both coefficient syndromes in U_S,
sixteen original finite events, L104's t=0, actual nonzero determinant D
and every locator, arbitrary original weights/chart, distinct linear
two-overlap supports and degree at most four, with L010/L086/L104/L109's
inherited finite-certificate qualifications. Suppose all five labels of T
occur among the actual two-overlap rows. No such coding assumptions are
needed for the algebraic scalar assertion.

## Conclusion

Every nonzero tensor p in this complete saved kernel is decomposable.
Its plane L contains E e_1. If rank_E(Q_0 restricted to L)=1, the unique
recovery line is E e_1, and every nonzero representative h on it has

    lambda_0=h_12/g_0(12)=0.

In particular every plane from this kernel passing all five actual-history
exact-rank-one gates has lambda_0=0, over every extension E. The coding
hypotheses above are inconsistent by L109's full-weight necessity. The
rank-zero branch is retained and rejected by actual nonpersistence; it is
not treated as a recovery direction.

This is one history's exclusion under the stated saved-certificate
qualification. It supplies no uniform twelve-row bound, pair extraction,
representation theorem, challenge identification or improved radius.
No cover is pruned and all 1665 frontier obligations remain recorded.
The result is REPRODUCTION of the known recovery-gate method. The separate
step-546 critical audit below passes with the saved-completeness premise
retained; it is not a fresh audit of the cover or a stronger exclusion.

## Proof

### Reused inputs and exact completeness scope

Reuse the ready SPECIALIZE assessment
`drafts/literature/2026-10-28-span-274-full-weight-test-review.md`.
L109 equations (3)–(6) supply the quotient maps, unique rank-one recovery
line, nonzero-lambda necessity and actual rank-zero exclusion. Its coding
imports are J. I. Hall, *Notes on Coding Theory*, GRS chapter,
[Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening formula.
Here each row shortens precisely the seven distinct labels J minus K_a
from dimension eight to dimension one, with nonzero products of label
differences as multipliers. No distance or shortening theorem is reproved.
L115 is a method comparison on different labels, not a theorem input.
The only new algebra below binds the actual saved coefficients to that
known gate; no general exterior-power result requires reproof.

In increasing pair coordinates the saved basis, in its saved order, is

    B0=e_1 wedge e_8,
    B1=e_1 wedge (e_12+79 e_18+65 e_27+95 e_33),
    B2=e_1 wedge e_22.                                      (1)

The existing verification's selected `/spans/274` record agrees with
all 63 coefficients. It records a complete three-vector kernel for the
generating history, including its selected original rank-18 minor with
determinant 79 modulo 97. That prior computation is reused, not rerun.
It alone would not justify substituting the actual history T.
For T the saved verification also checks the complete child-kernel
identity at each of its five successive row additions. The new certificate
extracts those exact five transition records and binds their parent,
chosen label, resulting span, whole basis and actual history to node 1006.
The chain starts at the empty history's full exterior space and ends at
span 274. Induction using those already checked kernel-intersection
identities identifies the kernel for T with (1). No generating-history
gate is substituted for an actual-history gate. The saved verifier checks
complete kernels, not just necessary vectors; this completeness is the
reused finite-computation premise of the exclusion.

These are linear equalities and kernel identities over F_97. The invertible
row operations and nonzero minors establishing them remain valid over E,
so the same complete basis applies over every extension. No descent,
generic-rank or prime-field sampling argument is used. Hashes of the
cover, prior verification and prior verifier agree with the preapproved
source assessment; the full selected records are copied into the new
certificate. This step checks these bindings, not the earlier elimination
or all other cover entries. L170 and L159–L161 are not premises.

### Entire homogeneous locus and the scalar

For arbitrary (s,t,r) in E^3 put

    w=s e_8+t(e_12+79 e_18+65 e_27+95 e_33)+r e_22.

Every tensor in the kernel is uniquely p=s B0+t B1+r B2=e_1 wedge w.
The coordinates w_8,w_12,w_22 are s,t,r. Thus p nonzero is equivalent
to (s,t,r) nonzero; then w is nonzero and w_1=0, so e_1,w are
independent and L=span_E(e_1,w). This proves decomposability for the
whole kernel, including zero coefficients and every projective endpoint.
The recovered plane is determined by its nonzero wedge; equivalently,
for independent e_1,w, x wedge e_1 wedge w=0 holds precisely for x in
their span, as is seen by extending them to a basis. Hence this reasoning
does not choose a special plane among different reconstructions of p.

Original row 0 has I_0={1,8}, K_0={47,50}, z_0=12, so Q_0 e_1=0.
Its complete matrix in the specified coordinate order is

    Q_0 = [0 0 16 44  0  0  0
           0 0 55  0 44  0  0
           0 0 88  0  0 44  0
           0 0 64  0  0  0 44].

Its polynomial has roots (64,70,75,79,85,89,96); g_0(12)=44.
In particular the denominator is nonzero over E, both by that evaluation
and because 12 differs from each root. The symbolic row images are

    Q_0 w=(0,55t+44r,38t,73t).

There is no division by s,t,r or by a projection coefficient. If Q_0 w=0,
the restriction to L has rank zero. In the coding application L109
rejects that branch by nonpersistence. If Q_0 w is nonzero, then for
h=a e_1+b w the equation Q_0 h=0 is b Q_0 w=0, hence b=0.
The restriction has rank one and its kernel is precisely E e_1.
Every nonzero recovery representative is therefore h=a e_1, a nonzero;
its coordinate h_12 is zero and lambda_0=0/44=0.
This proves the asserted implication on every rank-one branch at once.
Imposing the other four exact-rank-one gates only restricts this locus.

In the coding application, L109 requires lambda_0 nonzero. Indeed the
two recovered weights at k in K_0 are -lambda_0 g_0(k), and g_0(k)
is nonzero, so lambda_0=0 makes them zero. Scaling the recovery vector
or imposing any prescribed finite chart cannot remove a zero weight.
Thus the rank-zero and rank-one branches are both inadmissible.
L171's geometric survivor remains a valid geometric survivor; the
additional scalar gate explains its failure to give full weights.

### Certificate and limits of checking

Run `make -C scripts/span-274-full-weight check`. The coefficient/provenance
certificate is `scripts/span-274-full-weight/certificate.json`; the
independent checker writes `scripts/span-274-full-weight/verification.json`.
The producer uses direct products; the checker imports no producer code
and independently specifies sparse factors by labels, expands g_0 and
evaluates it by Horner's rule. All 63/63 factor coefficients, 5/5 saved
transition bindings, the complete original Q_0, its common-factor image
and all Q_0 w coefficients agree. The recovery numerator is 0 and its
required nonzero denominator is 44. All 26 checks pass without failures.
These are exact coefficient identities, not evaluations used to infer a
universal assertion. No N block, stack rank, child rank or traversal is
newly tested; neither cover file is modified. Both paths share Python,
F_97 arithmetic and the prior saved completeness computation. Their
agreement is same-step verification, not a separate critical audit or
proof-assistant verification. No other history is covered.

### Separate critical audit, 2026-10-29

Step 2026-10-29-mca-546-l172-separate-critical-audit used the unchanged
SPECIALIZE scope in
`drafts/literature/2026-10-28-l172-critical-audit-review.md`.
It read the full proof and both coefficient programs, L109's original
maps, recovery proof and separate audit, all selected basis/row/transition
coefficients and the prior cover verifier's kernel-intersection logic.
The inspected prior history left this separate audit pending. The
existing source comparison and ATTEMPTS/056 were reused: a geometric
survivor does not pass a missing nonzero-scalar gate. No new theorem
search, claim of originality or mathematical dependency is introduced.

The complete coefficient replay `make -C scripts/span-274-full-weight check`
passes with no failures: 63/63 exterior coefficients, 5/5 saved transitions,
and all 26 named checker assertions. The checker independently expands
the original monic g_0, with constant-to-leading coefficients
(50,81,21,43,16,83,24,1), and evaluates by Horner's rule. Its values on S
are (28,72,44,81,42,9,33). Thus the original anchor coefficient is 44,
and the other anchor-column entries are -81,-42,-9,-33, namely
16,55,88,64 modulo 97. These give exactly the displayed Q_0.
For the middle factor the first image coefficient is
16+44*79=0, the third is 88+44*65=38 and the fourth is
64+44*95=73 modulo 97; the second image is 55t+44r.
All other factor coefficients, including every zero, are retained.
The report's check count is descriptive; the full set of 26 assertions
was inspected, rather than inferred from its self-reported count alone.

For homogeneous completeness, coordinates (8,12,22) recover (s,t,r)
without division and every factor w has coordinate 1 zero. Hence every
nonzero tensor yields the stated independent pair and its unique plane,
even when only one parameter is nonzero. Since Q_0 e_1=0, its restriction
to that plane has rank zero if Q_0 w=0 and rank one otherwise. In the
latter case b Q_0 w=0 forces b=0 over any extension field, so every
nonzero recovery representative is a e_1 and h_12/44=0. No assumption
about the other four row images is needed for this implication. L109's
necessary direction excludes rank zero by nonpersistence and rank one
by the two zero K_0 weights. Its r>=6 converse is not applied to five
rows. Representative scaling and the original finite-chart gate cannot
turn those zero weights into nonzero weights.

The actual saved node chain, in root-to-leaf order, is
0,1,2,3,921,1006, with chosen labels 0,51,98,177,318 and child spans
1,2,3,3,274. Each complete selected child basis agrees with the previously
verified transition for its actual parent, chosen label and span. The
prior verifier forms N_a times the parent-basis transpose, takes its
entire coefficient kernel and maps that kernel back through the parent
basis. This is precisely intersection with ker(N_a). Induction starts
at the full exterior space and identifies the actual-history kernel,
conditional on these saved identities. The generating history
(0,51,98,143,318), its recorded rank 18 and determinant 79 are distinct
evidence; they alone do not identify the actual-history kernel. All
three saved input hashes match the preapproved values. The earlier
elimination and its determinant have not been recomputed in this audit.
Kernel completeness over extensions follows from the retained base-field
kernel identities by invertible row reduction, not finite-field sampling.

No defect was found in this qualified local argument. Its direct lemma
input is L109, as recorded in DAG.md; L010/L104/L086 remain inherited
coding hypotheses, not newly applied converse inputs. The raw programs'
`separate_critical_audit=false`/same-step language still describes their
original role; this separately dated proof scrutiny supplies the later
audit. It does not certify the entire cover, extend to a shorter history,
prune any obligation, or resolve the uniform or original challenge gaps.
All 1665 frontier obligations and the exhausted rank-test cap remain.

## Mathlib

Full matching saved-span scalar obstruction: **not checked**.
Supporting exterior-product, kernel, rank and finite-field results:
**not checked**. Unknown coverage is not evidence of absence. The coding
inputs are imported through L109 with their precise citations and unchanged
hypotheses above. The complete-kernel identification retains the explicit
saved finite-certificate qualification. The separate local proof audit
passes without independently reauditing that prior completeness computation.
