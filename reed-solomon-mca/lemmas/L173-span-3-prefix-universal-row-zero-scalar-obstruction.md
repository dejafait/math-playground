# L173 — Universal row-0 scalar obstruction for actual prefix (0,51,98)

## Hypotheses

Let E/F_97 be any field extension. Order coordinates by
S=(1,8,12,18,22,27,33), and put J=(47,50,64,70,75,79,85,89,96).
Label supports by increasing pairs of S (outer) and J (inner), zero-based:
I_a has index floor(a/36), K_a has index a modulo 36. Use L109's original
maps: O_a=S minus I_a, z_a=min(O_a),
g_a(X)=product_(y in J minus K_a)(X-y), and

    (Q_a h)_x=g_a(z_a)h_x-g_a(x)h_z_a, x in O_a minus {z_a}.

The exterior coordinates are increasing pairs of S. Fix actual history
T=(0,51,98), node 3 and span 3 in
`scripts/pair-free-envelope/cover.json`. Reuse the complete-kernel
identities in `scripts/pair-free-envelope/verification.json`, including
the root-to-node-3 child-kernel transitions. This saved finite computation
is an explicit premise, not independently reaudited elimination here.

For the coding consequence assume additionally L109's necessary-direction
hypotheses and inherited L010/L104/L086 finite-certificate qualifications:
F=F_(97^20), the order-sixteen H, k=8, unit multipliers,
1/4<=delta<5/16, both coefficient syndromes in U_S, sixteen original finite
events, L104's t=0, nonzero actual D and every locator, arbitrary original
weights and possibly nonrational chart, distinct linear two-overlap
supports and degree at most four. Suppose T occurs among the actual rows.
These coding assumptions are unnecessary for the algebraic scalar claim.

## Conclusion

Every nonzero tensor in the complete saved kernel for T is decomposable,
and its unique plane L contains E e_1. If rank_E(Q_0 restricted to L)=1,
then L intersect ker(Q_0)=E e_1, and every nonzero recovery representative
h satisfies lambda_0=h_12/g_0(12)=0. In particular this holds on the locus
passing all three original exact-rank-one gates, over every E/F_97.

Consequently the stated coding hypotheses are inconsistent. This is an
earlier-prefix exclusion under the saved-completeness qualification, not
a uniform bound, coding realization, challenge identification or improved
radius. No cover is modified or pruned; all 1665 frontier obligations
remain. The separate step-551 critical audit below passes under the
explicit saved-completeness premise.

## Proof

### Imported tools and saved input binding

Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-29-span-3-prefix-scalar-test-review.md`.
L109 equations (3)–(6), its reconstruction argument and separate audit
supply the original maps, unique rank-one recovery line, rank-zero
nonpersistence obstruction and nonzero-scalar necessity. The coding
inputs are imported through L109: J. I. Hall, *Notes on Coding Theory*,
[GRS chapter, Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula.
Each row shortens seven distinct labels from dimension eight to one,
with nonzero retained multipliers. No general coding theorem is reproved.
The coefficient argument below is a REPRODUCTION/specialization of this
known gate method. L115/L172 are comparisons, not premises; the latter's
five-row exclusion alone would not imply the present three-row result.

The complete saved six-vector basis is, in saved order,

    B_x=e_1 wedge e_x, x=8,12,18,22,27,33.                 (1)

All 126 entries agree with the selected prior verification basis. That
record gives generating history T, rank 15 and original minor determinant
16 modulo 97. These rank/minor claims are reused, not recomputed. The
actual chain is nodes 0,1,2,3 with histories (), (0), (0,51), (0,51,98),
chosen labels 0,51,98 and child spans 1,2,3. For each step the saved
verification contains a unique matching (parent, chosen, span) transition,
whose entire child basis equals the saved basis for that child.

The inspected prior verifier forms the new block on the full parent
basis, takes its complete coefficient kernel, maps back and row-reduces
the resulting basis. Its asserted child identity is therefore exactly
intersection with the new block kernel. Induction from the root's full
21-dimensional exterior space identifies (1) with the entire kernel for
the actual history, conditional on these saved identities. The chain and
all its basis entries are copied into the new certificate. Hashes bind
the unchanged cover, prior verification and verifier to the assessed
inputs; hashes do not prove kernel completeness. Base-field kernel
identities established by invertible elimination remain valid under
field extension, so the reused complete kernel over E is the E-span of
(1). No descent or sampling argument is used.

### Full homogeneous locus and original scalar

For arbitrary parameters t_x in E, x in S minus {1}, let

    w=sum_x t_x e_x,       p=sum_x t_x B_x=e_1 wedge w.

All six coordinates w_x recover the parameters, and w_1=0. Thus p is
nonzero exactly when some t_x is nonzero; then e_1,w are independent.
Every nonzero tensor is decomposable, including every zero-coefficient
stratum and projective endpoint. Its plane is uniquely span_E(e_1,w):
extend this independent pair to a basis; expansion in that basis shows
x wedge e_1 wedge w=0 precisely for x in their span. This characterizes
the plane intrinsically and covers every reconstruction of p.

Original row 0 has I_0={1,8}, K_0={47,50}, z_0=12, and
g_0 has roots (64,70,75,79,85,89,96). Its values on S are
(28,72,44,81,42,9,33). Hence

    Q_0 = [0 0 16 44  0  0  0
           0 0 55  0 44  0  0
           0 0 88  0  0 44  0
           0 0 64  0  0  0 44],

and, without any normalization of the parameters,

    Q_0 e_1=0,
    Q_0 w=(16t_12+44t_18,55t_12+44t_22,
           88t_12+44t_27,64t_12+44t_33).                (2)

The restriction of Q_0 to L has rank zero if Q_0 w=0 and rank one
otherwise. In the rank-one case h=a e_1+b w satisfies Q_0 h=0 exactly
when b Q_0 w=0, hence b=0. Its unique recovery line is E e_1.
For every nonzero representative on it, h_12=0; since g_0(12)=44 is
nonzero in every extension, lambda_0=0/44=0. No division by a parameter
or projection coefficient was used. Imposing the other two exact-rank-one
gates only restricts the locus already covered; their coefficients and
new rank tests are unnecessary for this implication.

For an actual coding pencil, L109 rejects the rank-zero branch by
nonpersistence, even with deficient weights. In the rank-one branch it
requires lambda_0 nonzero: the two K_0 weights are -lambda_0 g_0(k),
with g_0(k) nonzero. Our zero scalar makes both weights zero. Scaling
the representative or imposing the prescribed finite chart cannot fix
this. This uses only L109 necessity; its converse requiring r>=6 is
not applied to three rows. No original row parameters or chart are
replaced, and no coding realization is claimed.

### Coefficient checking and limits

Run `make -C scripts/span-3-prefix-scalar check`. The full certificate is
`scripts/span-3-prefix-scalar/certificate.json`. The checker imports no
producer or elimination code and never forms N or computes any rank.
It independently constructs the 126 exterior coefficients and checks
the three complete saved transitions, original label convention and
row-0 coefficients. Direct products and expanded-polynomial Horner
evaluation agree on every used g_0 value; the expanded coefficients,
constant first, are (50,81,21,43,16,83,24,1). Both paths yield (2),
numerator 0 and required nonzero denominator 44. All 27 named checks
pass with no failures. This checks coefficient identities and provenance,
not universal vanishing by finite samples. The homogeneous argument
above supplies the all-extension conclusion. Python arithmetic and
the saved completeness computation remain limitations; same-step
checking is not a separate critical audit or proof-assistant proof.

### Separate critical audit, 2026-10-29

Step 2026-10-29-mca-551-l173-separate-critical-audit uses the unchanged
SPECIALIZE scope in
`drafts/literature/2026-10-29-l173-critical-audit-review.md`.
It read this full proof, the entire short coefficient checker, L109
including its separate audit, and the prior verifier's kernel and
transition construction. No mathematical defect or new dependency was
found. This validates the qualified local specialization, with no claim
of a result beyond the imported recovery-gate method.

The prior verifier computes a complete coefficient kernel on each full
parent basis and maps it back to the exterior space. Thus its saved
child identities have the intersection meaning used in the induction.
This audit checks their binding and all selected entries; it does not
recompute or independently certify that elimination. The complete
21-vector root basis, all three actual transitions and every selected
parent/child basis are retained in the separate audit certificate.
The actual parent/chosen pair selects a unique transition in both the
cover and verification records, before its child span is compared.
The saved basis dimensions along this chain are 21,15,10,6. The saved
final rank 15 and minor determinant 16 are read as premises, not retested.
The full root and final basis agree in both saved files. All unchanged
input hashes, including the prior verifier hash, match their records.
None of these provenance checks upgrades the saved-completeness premise
to an independently audited elimination theorem.

The independent coefficient path uses elementary symmetric sums of the
seven roots to construct the polynomial, evaluates by exact powers, and
builds each quotient covector from h_x/g_0(x)-h_12/g_0(12), clearing by
g_0(x)g_0(12). It imports no earlier checker/producer routines. It checks
all 126 exterior entries, all 441 root entries, all 28 Q_0 entries,
all seven polynomial evaluations, all six parameter vectors and the
entire original row record against the selected saved records. This
reproduces denominator 44, numerator zero and formula (2), not samples
of a purported universal identity.

For the logical audit, nonzero p=e_1 wedge w with w_1=0 implies w is
nonzero and independent of e_1 over any E. Extending them to a basis
proves the plane-uniqueness statement, including all zero-coordinate
strata. Q_0 kills e_1, so its restriction to this plane has rank zero
or one. If rank one, Q_0 w is nonzero and b Q_0 w=0 forces b=0 for
every h=a e_1+b w on the recovery line. Thus every representative has
h_12=0 and scalar zero; rescaling or a prescribed finite chart cannot
make that scalar nonzero. At rank zero, L109's nonpersistence argument
applies even to deficient weights. It excludes that branch rather than
assuming it away. L109 necessity applies to selected rows of the actual
t=0 equality pencil; its converse with r>=6 is not applied to this
three-row prefix. Other row gates merely restrict the excluded domain.
The stated coding and inherited finite-certificate qualifications remain
essential; no arbitrary representation or coding converse is inferred.

Run `make -C scripts/span-3-prefix-scalar audit`. All 48/48 assertions
pass, including 3/3 transitions, with no failures. Full evidence is in
`scripts/span-3-prefix-scalar/critical-audit.json`, including the complete
root, selected transitions, exterior basis and reconstructed row.
No N block, rank test, traversal, cover mutation or pruning is performed.
All 1665 obligations remain and the exhausted rank-test cap is unchanged.
Python, residue arithmetic and the explicit saved-elimination premise
remain limitations; no proof-assistant verification is claimed.

## Mathlib

Full matching saved-prefix scalar obstruction: **not checked**.
Supporting exterior-product, field-extension and rank facts: **not
checked**. Unknown coverage is not evidence of absence. General coding
inputs are imported through L109 with the precise citations and unchanged
hypotheses above. The saved finite-computation qualification is retained.
