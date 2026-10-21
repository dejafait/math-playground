# L076 — Full mixed supplied-unit incidence certificates

## Hypotheses

Use L067's full nonzero seven-torsion algebra A of the exact curve
E: y²+y=x³+x²−2x, in short coordinates Y²=X³−3024X+46224.
Retain both complete source bases (X^i,X^iY), 0<=i<24, and
(1,Y,...,Y^47), and the audited inverse basis matrices.

Use L074's audited entire incidence algebra
B=D[T,V]/(k,V²−c′), I=B[X]/(N−Tq²), and its exact point pullback
X↦X, Y↦Vy_f. The global B-basis is (1,X,...,X^6).
Every B entry has the full 48 rational coordinates Z^jT^iV^e,
j fastest, 0<=j<8, 0<=i<3, 0<=e<2. Its full incidence coordinate
index is 48r+24e+8i+j, 0<=r<7. All fibers and both V components
are retained. No fieldness of B or I is assumed.

Accept the complete audited inputs of L067/L074, including
L070/L071/L072/L073 and incidence-269/audit-271. The known algorithms
and source coverage in audited L075 are reused; its two coordinate
norm values are not mathematical inputs to the new mixed determinants.
No L026, S-unit, global power-class, local-descent, Selmer, analytic-order
or rational-rank hypothesis is used.

## Conclusion

For the fixed elements

\[
a=X+Y,\qquad b=1+Y,\qquad a'=a b^7
\]

complete exact source vectors, inverse vectors, both source-basis
transports and incidence pullbacks are supplied and independently replayed.
All three are units in A and in their full incidence images.
For each image, every coefficient of its 7-by-7 multiplication matrix
and its determinant norm ν(u)=N_(I/B)(u) is independently verified.
The three norms satisfy the full coefficientwise identity

\[
\nu(a')=\nu(a)\nu(b)^7\quad\text{in }B.
\]

Scalar two and zero are additional complete matrix/determinant controls.
Thus the full comparison covers 11760 rational matrix slots and 240
norm slots; the three mixed elements account for 7056 and 144 of these.
Zero is only a determinant control, never a supplied unit.
For scalar two the explicit unit root β=2, β^(-1)=1/2 in B verifies
β^7=ν(2)=128. No mixed root, power-class nonmembership or faithful
power-class quotient coordinates are asserted.

All coefficients, including zeros, are canonical finite evidence in
`scripts/seven-torsion/supplied-unit-278/supplied-inputs.json`,
`input-pullbacks.json`, `supplied-matrices.json` and `supplied-norms.json`
in that directory. Independent full outputs and all intermediate records
are retained there too. This is a fixed known-method reproduction.
The separate fixed critical audit below passes. It supplies neither
arithmetic descent generators nor a Selmer bound or BSD candidate.

## Proof

**Imported mathematics and applicability.** The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-17-incidence-supplied-unit-certificate-replay.md`;
its complete finite contract reuses items 1–5 of the arbitrary-unit review.
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209–1231, DOI 10.1090/S0002-9947-03-03366-X,
[author long version dated 13 June 2001, Proposition 7.10, preceding incidence proof and following matrix paragraph, printed p.19](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf#page=19),
supplies the point-pullback/incidence-norm map on units and induced
seventh-power classes. Its number-field/odd-prime setup applies to Q,7;
its Section 3 permits products of separable fields. L074 supplies the
specified entire incidence projections, not just a rank-seven presentation.
L072's inverse ordinary-functional indexing and Cartier convention remain
unchanged. No Galois-image hypothesis or trivialization of μ_7 is added.

[Stacks Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
identifies the norm with the multiplication determinant for finite locally
free maps of constant degree. L074's global seven-element basis verifies
this hypothesis over every component. The multiplicative norm sends units
to units, as in [Stacks Section 31.18, tag 0BCX](https://stacks.math.columbia.edu/tag/0BCX).
Consequently the certified unit images have unit norms. Explicit mixed
norm inverses are not asserted or needed. Proposition 7.10 supplies
universal representative compatibility; the finite equality here checks
this implementation and is not a proof of a new general quotient theorem.

The determinant methods are the ordered cofactor expansion over a
commutative ring, supported by
[Mathlib Matrix.det_succ_row_zero and Matrix.det_fin_zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_succ_row_zero),
and Christian Bär,
[*The Faddeev–LeVerrier algorithm and the Pfaffian*, arXiv:2008.04247v3, Section 2.1, pp.3–4, equations (1)–(6)](https://arxiv.org/pdf/2008.04247v3#page=3).
The latter works over a commutative Q-algebra: N_1=Id,
c_k=−tr(MN_k)/k, N_(k+1)=MN_k+c_k Id; at size seven det(M)=−c_7.
B has the required Q-algebra structure, regardless of zero divisors.
Neither method divides by a B matrix entry. These results and their
proof cases are reused from the ready assessments; no reproof is claimed.

**Exact supplied units.** The producer computes in
Q[X]/f ⊕ Y Q[X]/f, with Y²=c(X) and L067's complete degree-24 f.
Rational polynomial Euclidean arithmetic constructs inverses of
X²−c and 1−c modulo f, giving candidate inverses
(X−Y)/(X²−c) and (1−Y)/(1−c). It checks the full products with a,b
as one. It constructs a'=ab^7 and its candidate inverse a^(-1)b^(-7)
and checks their full product too. The scalar-two inverse is 1/2.
These are finite identity witnesses, not an assumption that a nonzero
value at one embedding is a unit.

Every source vector and inverse is retained in both length-48 bases.
The producer and verifier check both full transports on all eight
vectors, without inferring coefficients from an embedding or preview.
The verifier independently uses fixed-length Horner arithmetic modulo f,
checks all four inverse products, verifies the exact proposed a,b,a',2,
and verifies a'=ab^7. Its binary powering differs from the producer's
successive multiplication. All 48 coordinates of each source inverse
product are retained in `independent-inputs.json`.

Both programs reconstruct the whole B and F=N−Tq² from the accepted
quotient/dual inputs. They compare the full coefficients with L074.
The verifier independently recovers y_f=q³M^(-1) and checks MM^(-1)=1
and c′y_f²=c(X). It independently recomputes all 48 standard and all
48 Y-power point columns, both entire source transports, both original
model coordinate maps, all 48 line inclusions and all 336 rational
basis round trips. Thus the full point substitution, including inverse
vectors, is retained in the whole incidence algebra.

Each input and inverse is evaluated by the point substitution. Both
implementations check all coefficients of each incidence inverse product
and the representative equality. The complete independent products and
pullbacks agree with the producer in every one of their 336 coordinates.
The independent source/ring arithmetic is fixed-length Horner reduction;
the producer uses sparse convolution and monic reduction. They share
only I/O/limits, not arithmetic routines. The source and incidence
identities justify unit status without fieldness of B or I.

**Full operators and determinants.** For each u=a,b,a',2,0, column j
is the full normal form of uX^j for j=0,...,6. The producer multiplies
and monically reduces; the independent verifier uses separate Horner
shifts. All 49 entries retain all 48 B coefficients. Every one of the
11760 entries agrees; no determinant is formed from scalar norm
linearity or by discarding the odd-V component.

The producer saves its ordered remaining-column minors, with row
7−number of columns, inherited increasing column order, position sign
(−1)^j and empty minor one. There are 127 recorded nonempty reachable
minors for each mixed matrix, seven for scalar two and one for zero.
A zero entry contributes zero and needs no descendant branch.
The verifier independently computes all seven Faddeev coefficients,
retaining N_k, MN_k, trace, c_k and N_(k+1) at every step for every
matrix: 35 complete recurrence records. Every full final matrix is zero,
and the independently obtained −c_7 agrees in all 48 coordinates with
the producer's determinant and saved norm. Terminal zero alone is not
used to certify the determinant. Full scalar determinants are zero and
128 respectively.

The producer and verifier separately check ν(a')=ν(a)ν(b)^7 in all B,
using successive and binary powering respectively. Both sides are saved.
The supplied scalar root and inverse have full length-48 witnesses;
the verifier checks ββ^(-1)=1 and β^7=ν(2). It asserts no mixed root.
The unit norm map on seventh-power classes is the imported theorem;
these finite checks do not construct faithful global quotient data.

**Execution, evidence inspection and qualifications.** The single stages were

```bash
python3 -B scripts/seven-torsion/supplied-unit-278/run_stage.py build_norms
python3 -B scripts/seven-torsion/supplied-unit-278/run_stage.py verify_norms
```

Internal times are 46.44635712495074 and 127.80613070901018 seconds,
each below 180. External watchdog times are 46.58124641701579 and
127.94559379201382, each below 181. Neither watchdog fires. No retry,
cap increase, arithmetic subdivision or extra determinant execution occurs.
The full fresh directory remains below the combined 134217728-byte cap.

`complete-evidence-inspection.json` is a complete saved-output comparison
and shape inspection after these stages, not a third arithmetic replay.
It checks all input/pullback vectors, matrices, norms, all 35 recurrence
records and their adjacent matrices/characteristic coefficients, every
terminal matrix, all recorded minor shapes and determinant roots, the
representative sides and scalar witness. Full accepted incidence-269/
audit-271 evidence and both source transport arrays agree. A preview
is not used to establish correctness.

Each stage also rejects five deliberately altered full-data fixtures:
a wrong inverse, zero supplied as a unit, a missing source coordinate,
one wrong odd-V matrix coefficient and one wrong norm coefficient.
These are explicitly limited named-condition rejections, with
`full_malformed_replay: false`, not complete malformed-certificate runs.
The input failures are checked before determinant work. They supplement
the full successful original replay.

Both stages and final inspection preserve all 529 inventoried original
noncache files, including the earlier 404/464-file inventories and
successful coordinate-norm-273/audit-275 evidence. No original is changed
or missing; the executed stage-source hashes also agree. Stopped columns
and failed drafts remain intact and are not mathematical inputs.

This establishes the fixed finite certificate only. It does not produce
S-unit/class completeness, faithful power-class coordinates, descent
functions, local identifications or upper bounds, Selmer containment,
other L026 premises, successful localization, rational Kummer membership,
divisible-Sha removal or arbitrary-curve rank/complex-order comparison.
An absent mixed root supplies no power-class nonmembership. The separate
critical audit below validates only this fixed assembly.

**Separate critical audit (2026-10-17, step 280).** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-17-supplied-unit-incidence-critical-audit.md`.
The complete canonical proof, executed producer, independent verifier,
I/O and watchdog, saved-output inspection and audit-275 method were read.
The previously assessed primary norm, unit and determinant results above
are reused; no additional source discovery or general theorem reproof is
claimed. The full source algebra and its transports come from L067; the
entire incidence presentation and point/line maps come from audited L074.
These are exactly the direct mathematical inputs. L075's arithmetic norm
values, L069 and stopped relation/action columns are not used.

The single command, with no retry or producer execution, was

```bash
python3 -B scripts/seven-torsion/supplied-unit-audit-280/run_stage.py
```

The fresh sibling directory holds 18 byte-identical source/input copies,
including the executed verifier and I/O, with hashes and original paths in
`input-inventory.json`. `originals.json` retains all 529 earlier inventory
entries and every current noncache file in supplied-unit-278, totaling
617 files. The audit checks the prior expected hashes rather than merely
accepting newly hashed bytes. All executed stage-source hashes from the
original source manifest match. Preparation writers and the producer are
not executed. The copied construction report records original provenance.

One alarm covers fresh replay, all extra arithmetic, comparisons and
preservation; the copied verifier's start/finish are overridden only to
retain this timer and route reporting. Output tracking and final exit are
also intercepted. Arithmetic code is byte-identical, upstream reads use
the accepted originals, and exclusive-create outputs stay in the fresh
directory. The full fresh verifier completes after 126.22627508302685
seconds of aggregate elapsed time.

The reviewed fixed-length Horner shift replaces the top power using the
negative monic-modulus coefficients. It therefore computes exact normal
forms in the full source and incidence algebras; quadratic-pair arithmetic
retains both V components. All four source inverse products, eight source
vectors and their inverse basis transports, all four incidence inverse
products and full pullbacks, source/incidence representative changes, both
point bases and original-model coordinates, all line columns and all 336
basis round trips pass. Transport of a product identity through the
certified source algebra isomorphism justifies it in the power basis too.
No selected embedding, B/I fieldness or matrix-entry division is used.

The fresh replay checks every one of the 11760 rational matrix slots and
240 norm slots. Matrix column j is multiplication of X^j by the supplied
whole-algebra element. All 35 Faddeev recurrences are recomputed, starting
at the identity; trace, rational division by k, characteristic coefficients,
intermediate matrices and final determinant sign are retained. The entire
51 fresh output objects agree with the originals. The only excluded fields
are `seconds`, `preserved_files`, `changed_or_missing` in the verification
report: independent preservation requires an empty changed/missing list.
No arithmetic value, recurrence, rejection fixture or condition is excluded.
`complete-output-comparisons.json` records every compared object and hashes.
The full accepted incidence-269 and incidence-audit-271 replay evidence also
agree; all five transport arrays match the latter's dense evidence. Complete
F and y_f values agree, and all retained upstream residual coefficients are
zero. This is evidence comparison, not upstream reconstruction.

The audit additionally checks **every saved ordered Laplace minor** using
the fresh verifier's B arithmetic, without importing producer arithmetic.
Starting at columns (0,...,6), it follows every nonzero matrix-entry branch
and requires exact equality of the reachable nonempty key set with the
saved set. Row is 7 minus the number of remaining columns; increasing order
is inherited on deletion. The empty minor is the full 48-coordinate one.
In increasing minor size, each value is recomputed from all nonzero children
with position sign (-1)^j; zero entries contribute zero and require no
child. This remains valid over a ring with zero divisors. Every 48-coordinate
saved value agrees. Counts are 127 each for a,b,a', seven for scalar two and
one for zero: all 389 records. Full terms and values are retained in
`checked-laplace-<label>.json`. Every root agrees with the fresh Faddeev
norm, saved Laplace norm, `supplied-norms.json` and its `norm-<label>.json`.
Thus terminal zero alone is never used as a determinant certificate.

Both full sides of the norm representative identity and the scalar root,
inverse and seventh power pass fresh arithmetic and original comparison.
All five named-condition rejections are reproduced exactly and agree with
the producer's records; its first three input-rejection records agree too.
The wrong inverse, zero-as-unit, missing source coordinate, odd-V matrix
coefficient and norm coefficient fixtures retain `full_malformed_replay:
false`. They are condition tests, not complete malformed-certificate replays.
The explicit mixed-root disclaimer remains; no missing root implies
nonmembership or a faithful global power-class coordinate.

`audit-report.json` records zero failures, 143.7144495829707 internal seconds
against 180; `watchdog.json` records 143.83701179199852 seconds against 181,
exit zero and no watchdog firing. The entire fresh directory, including
copies, reports and logs, contains 30925193 bytes against 134217728.
`audit-preservation.json` checks all 617 originals with none changed or
missing, including earlier inventories, failed drafts and stopped evidence.
No budget renewal, subdivision, additional arithmetic stage or cap increase
occurs. The original construction-stage evidence is left intact.

This is an ADVANCE in local certificate reliability by known-method
REPRODUCTION, not progress beyond the assessed mathematical sources.
It validates the fixed mixed-unit certificate and changes neither its
hypotheses nor the missing arithmetic premises. Complete S-units/classes,
faithful power classes, descent/local evidence, Selmer containment,
successful localization, rational membership, divisible-Sha removal and
arbitrary-curve rank comparison remain absent. No new lemma, DAG edge or
BSD candidate is asserted.

## Mathlib

[Algebra.norm_eq_matrix_det](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Defs.html#Algebra.norm_eq_matrix_det)
and `Algebra.norm_algebraMap_of_basis` support the finite-basis norm and
rank-seven scalar convention. These and the determinant support above
are reused from the ready coverage. Full matching Mathlib coverage for
this explicit mixed-input executable certificate and its power-class
handoff was not checked. Unknown coverage is not evidence of absence;
this is not a Lean proof or universal software-correctness theorem.
