# L168 — Exterior exclusion for L167's complete twelve-row E_2

## Hypotheses

Let E be any field extension of F_97. Fix the ordered sets

    S=(1,8,12,18,22,27,33),
    J=(47,50,64,70,75,79,85,89,96).

Use exactly the following rows of L167's canonical sixteen-row table,
with their original numerical labels:

| L167 row | I | K |
|---|---|---|
| 2 | 8,12 | 70,75 |
| 3 | 18,22 | 79,85 |
| 4 | 27,33 | 89,96 |
| 5 | 1,18 | 70,89 |
| 7 | 8,27 | 50,79 |
| 8 | 12,33 | 64,85 |
| 9 | 1,33 | 75,79 |
| 11 | 12,18 | 50,96 |
| 12 | 8,22 | 64,89 |
| 13 | 1,8 | 85,96 |
| 15 | 22,33 | 50,70 |
| 16 | 18,27 | 64,75 |

These are the **complete** E_2, not a replacement labeling or a subset
of a larger E_2. For each row set g(X)=product_(y in J minus K)(X-y),
O=S minus I, z=min(O). Let Q:E^S -> E^4 have rows
g(z)w_x-g(x)w_z for x in O minus {z}, in increasing order.
Form each six-by-21 exterior block N_j exactly by L109 (1), using
lexicographic covector pairs and increasing pairs of S as columns.
Stack blocks in the table order to obtain N.

For its conditional coding application, retain all L109 hypotheses:
F=F_(97^20), dimension eight with unit multipliers, the fixed order-sixteen
subgroup H=S union J, L010's shifted moments, the pinned event on
1/4<=delta<5/16, both coefficient syndromes in U_S, sixteen original
finite events, t=0, and D and every locator nonzero as polynomials.
Original weights and chart remain arbitrary; L104/L086/L010's inherited
finite-computation qualifications are not re-audited here.

## Conclusion

The 72-by-21 matrix N has rank 21 over F_97 and every E. Its entire
kernel is zero. No two-dimensional subspace L of E^S has
rank(Q_j restricted to L)<=1 for every displayed row. In particular,
these twelve rows cannot all occur in a represented equality pencil
satisfying the conditional coding hypotheses.

This is a fixed finite specialization, classified REPRODUCTION under
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-27-l167-twelve-row-exterior-rank-review.md`.
It supplies a new local certificate, not a new general theorem or a
claim of mathematical originality beyond the sources checked. L079's
existing full-sixteen-family exclusion is not used or re-established.
Other labelings/families, uniform twelve-row exclusion, representation,
challenge identification and the 11/q–16/q interval remain unresolved.

## Proof

### Exact rank certificate

All g values and all entries of Q_j and N_j lie in F_97. Choose residues
0,...,96. Number stack rows from zero, six per displayed support row.
The square minor using all 21 columns and the following ordered row list
is nonsingular:

    6,7,2,3,4,8,9,13,14,10,12,15,16,11,18,0,1,17,5,19,20.

The entire integer minor and the support/pivot/covector-pair identity of
each selected row are saved in
`scripts/l167-twelve-row-exterior/certificate.json` under `minor` and
`minor_row_identities`. Its determinant is

    det = -564277021063479563603400000, congruent to 95 modulo 97.

This is the integer determinant of the saved residue matrix. Thus rank(N)>=21,
and its 21 columns give rank(N)=21. The minor already lies in blocks
for L167 rows 2,3,4,5; no assertion about a different four-row labeling
is inferred. All twelve original blocks are nonetheless constructed
and checked, as required by the approved target.

Reproduce from the notebook directory:

```bash
make -C scripts/l167-twelve-row-exterior check
```

`produce.py` parses the complete canonical L167 table and checks the
complete E_2 row set and fixed label partition. It directly evaluates
the seven-factor g products, all covectors and exterior entries. The
stack's successive prefix ranks, computed independently by the verifier, are

    6,12,18,21,21,21,21,21,21,21,21,21.

It saves all twelve blocks, their full 72-by-21 stack, row identities,
RREF, pivots, minor and complete empty kernel basis. Its modular
determinant residue is 95.

`verify.py` imports no producer routine and does not rerun the producer.
It compares a separately transcribed complete sixteen-row numerical
table against canonical L167, then takes **all** its overlap-two rows.
It regenerates H by powers of 8 (8^8=-1, 8^16=1 in F_97). For each row
it expands g into polynomial coefficients and uses Horner evaluation
at every label in H. The zero set is exactly J minus K. On O it uses
the normalized covectors d_x(w)=w_x/g(x)-w_z/g(z); these are defined
because all g values there are nonzero. The identity

    c_x=g(z)g(x)d_x

reconstructs Q, and multiplying d_x wedge d_y by g(z)^2 g(x)g(y)
reconstructs the original exterior block. Every g value, covector,
block entry, stack entry and row identity agrees with the producer.
The four quotient rows have rank four and each exterior block rank six.

The verifier uses incremental column elimination for its separate rank
computation, recovering rank 21 and the same prefix ranks. Independently,
rational Gaussian elimination of the entire selected integer minor
gives the displayed exact determinant, hence residue 95. This establishes
the lower bound without trusting the producer's row selection or rank
routine; the upper bound is the number of columns. Its complete kernel
is therefore {0}; no extension-field kernel is dropped. All 67 checks
pass with zero failures. Full reconstructed blocks/stack, independent
polynomial coefficients and normalized covectors, integer minor,
determinant and check records are saved in
`scripts/l167-twelve-row-exterior/verification.json`.

These are exact finite-computation certificates, sharing Python and
integer/residue arithmetic. Same-step independent reconstruction and the
separate critical audit below pass. No finite-point sampling,
nonlinear solver or unverified generic-rank assertion is used.

### Geometric and coding implications

The nonzero 21-by-21 minor remains nonzero in every extension E of F_97.
Consequently N_E is injective. Import L109's exterior necessary condition:
an independent pair u,v spanning a plane whose every Q_j restriction
has rank at most one supplies the nonzero vector u wedge v in ker(N_E).
This contradicts injectivity. This argument also excludes rank-zero
branches rather than dividing by their images, and it uses no
decomposability sufficiency or coding-weight recovery.

Under the coding hypotheses, L109 already proves independence of the
coefficient pair and rank exactly one for every actual row, with all
nonpersistence, full-weight and original-chart qualifications retained.
The necessary condition just excluded applies to these twelve rows.
Thus such a conditional equality pencil cannot contain them. No converse
or realization construction is needed or claimed.

The standard coding results remain imports through L109: J. I. Hall,
*Notes on Coding Theory*, GRS chapter,
[Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, accepted manuscript 2016-02-29,
[section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
Their distinct-label/nonzero-multiplier shortening specialization is
unchanged. Supporting exterior facts are covered by Keith Conrad,
*Exterior Powers*, [Theorems 4.2, 7.1 and 7.5, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
as inspected in the reused assessment. No general source theorem is
reproved: only the previously unevaluated fixed matrix is calculated.

### Separate critical audit, 2026-10-27

Step 2026-10-27-mca-531-l168-critical-audit is a REPRODUCTION audit under
the prior SPECIALIZE assessment
`drafts/literature/2026-10-27-l168-critical-audit-review.md`.
It reads this proof, the complete producer/verifier and Makefile, L167's
complete numerical table and audit, L109's necessary-condition proof,
independence and rank-zero cases, and the relevant L104 shortening and
L010 injectivity hypotheses. The ready assessment's inspected primary
coverage is reused; no new general theorem or source read is claimed.

`scripts/l167-twelve-row-exterior/audit_l168.py` imports neither original
program and leaves both original certificates unchanged. It parses the
canonical sixteen-row table and takes exactly its twelve overlap-two
rows, checking the fixed partition, all sixteen IDs and all original
source hashes. Integer polynomial convolution without intermediate
reduction and integer products agree at every label. All g zeros are
exactly J minus K; all sixty normalization denominators are nonzero,
and their inverses are checked individually. Standard basis images of
Q reconstruct every exterior column with the sign/order in L109 (1).
The complete normalized quotient and exterior rescaling identities are
also checked, without assuming that a nonzero image was sampled.

All block fields, all 1,512 stack entries, all 72 row identities, all
polynomial/normalized-covector records, all prefix ranks and all 441
entries of the selected minor agree with the saved evidence. A third
determinant path uses fraction-free Bareiss elimination over the integers,
checks every division for exactness and saves all twenty pivot/divisor
records. It reproduces the exact displayed determinant and residue 95,
independently of both original determinant routines. The selected row
ordering is checked against the complete list in this proof, rather
than trusting an arbitrary reported minor. The nonzero minor proves
rank at least 21; 21 columns prove the matching upper bound. Thus the
empty kernel basis is complete by rank-nullity, not merely a list of
tested vectors. The entire reported RREF and free/pivot column lists
agree with this conclusion. All 151 audit checks pass, with no failures.

The geometric implication needs no finite-field point search. For any
independent u,v over any extension E, u wedge v is nonzero by the
standard exterior-power theorem imported above. Evaluating the covector
wedges gives exactly the two-by-two minors of (Q_j u,Q_j v). If its
rank is zero or one, every such minor vanishes. Hence all twelve
rank-at-most-one restrictions would put a nonzero wedge in ker(N_E).
The base-field minor remains 95, so N_E is injective and this is
impossible. No normalization by an image, decomposability converse or
extension-field descent is required.

For the coding application, the distinct full errors and eight-column
syndrome injectivity used in L109 force u,v to be independent: otherwise
the two nonzero error syndromes could be scaled to agree, contradicting
their distinct supports. Their nonzero syndromes follow from injectivity
on four coordinates. L104's shortening gives Q_j(u+gamma_j v)=0 at
every actual finite event; the coefficient pair (1,gamma_j) is nonzero,
so each restriction has rank at most one. L109 moreover excludes rank
zero by its all-parameter representative on A_j and the resulting
identically-zero locators. This stronger statement is consistent with,
but unnecessary for, the geometric contradiction. All prescribed
weights/chart, nonpersistence, t=0, original field/code/cell and inherited
L104/L086/L010 finite-input qualifications remain in force. No inherited
large computation is newly replayed. L159–L161 are not premises.

Verdict: L168 passes this separate audit; no mathematical correction or
new dependency is needed. The prefix-rank attribution above is clarified:
the producer reduces the full stack, while the verifier computes prefixes.
Full reconstructed evidence, checks, determinant trace and immutable input
hashes are in `scripts/l167-twelve-row-exterior/l168-critical-audit.json`.
Reproduce without regenerating the original certificates:

```bash
make -C scripts/l167-twelve-row-exterior audit
```

The paths still share Python and integer/residue arithmetic. This is not
formal verification. The result concerns exactly this numerical labeling;
it supplies no symmetry transport, other-family exclusion, code realization
or challenge solution. Existing rank-only failures are unchanged.

## Mathlib

Full matching coverage for this fixed numerical twelve-row certificate:
**not checked**. Supporting finite-field, matrix-rank, scalar-extension
and exterior-square coverage: **not checked**. Unknown coverage is not
absence. The exact certificates are not proof-assistant verification.
