# L115 — Complete rational factorization of the marked octic

## Hypotheses

Work over Q with L114's unchanged polynomial and entire algebra

    G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673,
    A=Q[t]/(G).

No rational-factor pattern, maximal-order basis, class group, unit group,
local image or point completeness is assumed.

## Conclusion

The complete primitive integral factorization, with positive content, is

    G=11F,
    F=275t⁸−2860t⁶+6930t⁴−3564t²+243.

F is irreducible over Q and occurs with multiplicity one. Equivalently,
the complete monic Q-factorization is G=3025(F/275), with the single
degree-eight factor F/275. In particular the entire algebra A is one
degree-eight number field. No factors are omitted or replaced by selected
root fields; the assertion is about this marked octic, not L095's octic.

L114's support remains all maximal-ring primes above {2,3,5,11} in this
one field, with the real place retained. This identifies the field needed
for supported-class arithmetic without computing that arithmetic.

## Proof

### Imported criteria and exact specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-22-marked-octic-rational-factorization.md`.
Import J.S. Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Propositions 1.13–1.14 p.12 (Gauss/integral factors), Remark 1.18 p.14
(irreducible reduction with preserved degree), Proposition 4.20 and
Corollaries 4.21–4.22 pp.53–54 (finite-field Frobenius/factors), and
Exercise 4-8 p.60 (the finite-field irreducibility test). These are the
version and pages inspected in the prior assessment. The latter test,
for monic f of degree n over F_p, requires

    X^(p^n)=X modulo f,
    gcd(f,X^(p^(n/r))−X)=1 for each prime r dividing n.

The general criteria are imported, not reproved. The necessary difference
from those sources is this instance's exact coefficient/product and
finite-field certificate; no new factorization method is claimed. No LLL
fallback or proof of a general rational-factorization algorithm is needed.

The ascending coefficient lists are

    G: [2673,0,−39204,0,76230,0,−31460,0,3025],
    F: [243,0,−3564,0,6930,0,−2860,0,275].

Termwise multiplication by 11 recovers all nine coefficients of G.
The positive coefficient gcd of G is 11; F is primitive, already because
gcd(243,275)=1. Thus the scalar/content and complete product are exact.

Use p=19, prime by trial division by 2 and 3. The leading coefficients
of G and F reduce to 4 and 9, respectively, so both degrees remain eight.
Since 9^(−1)=17 modulo 19, the monic normalized reduction of F is

    f=t⁸+t⁶+10t⁴+3t²+8 in F_19[t].

The following are the complete ascending coefficient vectors of
R_k=t^(19^k) modulo f. All omitted coefficients, including the constant
coefficient, are explicitly zero in the vectors.

| k | R_k |
| --- | --- |
| 1 | [0,13,0,11,0,9,0,3] |
| 2 | [0,8,0,8,0,11,0,2] |
| 3 | [0,18,0,2,0,10,0,8] |
| 4 | [0,18] |
| 5 | [0,6,0,8,0,10,0,16] |
| 6 | [0,11,0,11,0,8,0,17] |
| 7 | [0,1,0,17,0,9,0,11] |
| 8 | [0,1] |

These residues can be verified successively from R_0=t by computing
R_(k−1)^19 and reducing with

    t⁸=−t⁶−10t⁴−3t²−8.

The full exact multiplication/division witnesses are retained in the
certificate below. In particular R_8=t and R_4−t=17t. The explicit
polynomial identity in F_19[t]

    12f+(18t+3t³+6t⁵+6t⁷)(17t)=1

proves gcd(f,R_4−t)=1. Since the only prime divisor of n=8 is 2, this
is the sole proper-index gcd required by the imported test. Therefore f
is irreducible. Gauss and degree-preserving reduction imply that the
primitive F is irreducible over Q: any positive-degree rational
factorization would give integral factors with nonvanishing leading
coefficients modulo 19 and hence a positive-degree factorization of f.
The displayed single factor already recovers G, so no further rational
factor or multiplicity is left. Over Q the ideals (G) and (F) coincide;
the irreducible degree-eight quotient is the asserted entire field.

### Complete evidence and bounded method

Run from the notebook directory:

    python3 scripts/pair-genus-two/marked_octic_factorization.py
    python3 scripts/pair-genus-two/replay_marked_octic_factorization.py

The complete producer certificate is
`scripts/pair-genus-two/marked-octic-factorization-certificate.json`.
It stores every visited prime through the first success 19 (within the
approved cap 101), including skipped primes 5,11 and unsuccessful tests
at 2,3,7,13,17. Those failed reduction tests are not evidence of rational
reducibility. Each tested prime retains all eight Frobenius residues,
binary-power multiplication/division witnesses, the complete relevant
Euclidean trace and Bezout multipliers. The selected prime is 19; the
four final producer checks pass with no failures.

The separate arithmetic replay, which imports no producer code, is
`scripts/pair-genus-two/marked-octic-factorization-replay.json`.
It recomputes all eight selected residues by nineteen successive
multiplications, using shift-and-reduce quotient multiplication rather
than the producer's binary powering and polynomial long division.
It also checks every selected producer division identity and remainder
degree, the full Bezout identity, exact product, content, prime condition
and monic normalization. All 167 checks pass with no failures. The full
eight residues and both Bezout multipliers were inspected; the printed
passing-check count alone is not the proof. The arithmetic replay is
part of this calculation, not a separate critical mathematical audit.

### Scope, downstream use and remaining gaps

The intermediate threshold is met: there is exactly one Q-simple field
factor of degree eight, with exact scalar and multiplicity. This is
local progress by reproduction of standard criteria, not a new general
theorem or certified novelty. The initial single-prime mechanism succeeds
at 19, so neither an enlarged search nor the approved fallback is used.

A subsequent descent must still compute certified maximal-ring supported
classes (including class-group two-torsion), complete required local
images and points on surviving covers. The degree-nine distinguished-root
recovery, compatible remaining factors, both L095 integer systems and
minus-eleven alternative remain unresolved. Known rational infinity
points prevent an empty fake-Selmer-set exclusion. This lemma does not
bound rational points, prove an integer exclusion or resolve Beal.
Its separate critical application audit passes as recorded below.

### Independent critical audit, 2026-10-22

The approved audit confirms the complete claim without a correction.
The prior scope approval is
`drafts/literature/2026-10-22-marked-octic-factorization-critical-audit.md`.
The general criteria remain the imported Milne results cited above;
this is independent instance verification under SPECIALIZE, classified
REPRODUCTION, with no claim of a new general result.

Run the independent auditor from the notebook directory:

    python3 scripts/pair-genus-two/audit_marked_octic_factorization.py

It imports neither earlier implementation and writes the complete evidence
to `scripts/pair-genus-two/marked-octic-factorization-audit-certificate.json`.
All 1809 checks pass, with no failures. The certificate identifies the
two original evidence files by SHA-256 and retains every checked value,
the independent monomial reductions, operation records and exact
Euclidean evidence. Neither original certificate is overwritten.

The arithmetic audit proceeds as follows.

1. The input agrees coefficient by coefficient with L113–L114's G.
   All nine equalities G_i=11F_i hold; gcd of G's coefficients is
   positive 11 and gcd of F's coefficients is 1. Exact rational
   multiplication also checks 3025(F/275)=G, including zero coefficients.
   The stored factor list has one degree-eight factor of multiplicity
   one. No factorization of the polynomial in t² is substituted for
   factorization in t.
2. Trial division verifies p=19; neither 3025 nor 275 vanishes modulo
   19. The residues are respectively 4 and 9, and 9·17=1 modulo 19.
   Multiplication of every coefficient by 17 gives the displayed monic
   f of degree eight. Thus the normalization is by a unit and preserves
   every possible factor degree.
3. Independently form M_d=t^d mod f, starting with M_0=1 and using a
   single shift and the monic relation at each step through d=7·19.
   In characteristic 19, the Frobenius of a representative sum a_i t^i
   is sum a_i M_(19i). Iterating this substitution independently recovers
   every entry in the eight-row table above. In particular R_4=−t and
   R_8=t. This method uses neither earlier powering implementation.
4. All 56 selected binary-power division identities have exact products
   qf+r and deg r<8. In addition, the auditor checks each operation's
   kind, both operands, evolving accumulator and base, terminal result,
   and complete trace length. Thus correctly formed but disconnected
   operations cannot pass as an exponentiation. The original replay did
   not itself verify this state linkage; the audit supplies it without
   finding an error in the saved trace or changing the mathematical claim.
5. The full selected Euclidean chain is

       f=(8t+14t³+9t⁵+9t⁷)(17t)+8,
       17t=(14t)·8+0                 in F_19[t].

   Both divisions, their linked operands, strict remainder degrees and
   termination check. Normalizing the nonzero constant 8 gives gcd 1.
   Independently multiplying both stored Bezout terms gives exactly
   12f+(18t+3t³+6t⁵+6t⁷)(17t)=1, with every positive-degree
   coefficient zero. This is a coprimality certificate, not an assumption
   that the quotient is already a field.
6. All complete historical records at 2,3,7,13,17,19 were likewise
   checked; the degree-dropping skips at 5 and 11 are correct, and 19
   is the only passing recorded test. No additional primes were searched.
   The replay's eight residues, two Bezout multipliers, identity and
   entire 56-row arithmetic record agree with independent computations;
   all its 167 saved actual/required comparisons and flags are consistent.
   Failure of earlier finite-field tests is not used to infer rational
   reducibility.

The theorem application needs both finite-field conditions. The only
prime divisor r of n=8 is 2, so the required proper index is n/r=4;
R_8=t and gcd(f,R_4−t)=1 are precisely Milne's criterion, not a
partial subset of its tests. Its monicity, degree and prime hypotheses
have now all been checked. The resulting irreducible reduction and
primitive F meet Gauss and degree-preserving reduction: if F had two
positive-degree integral factors, their leading coefficients would
multiply to 275 and hence both remain nonzero modulo 19. Their
reductions would contradict the certified irreducibility of f.

Finally, 11 and 275 are units in Q, so (G)=(F)=(F/275) in Q[t].
The standard polynomial quotient-field theorem (an irreducible
polynomial generates a maximal ideal in a polynomial ring over a field)
therefore applies to the entire stated quotient. Division by the monic
degree-eight F/275 gives the basis 1,t,...,t⁷, so its Q-dimension is
exactly eight. No other component can remain, since the full product is
already G; no repeated factor can remain, since its square would have
degree sixteen. Characteristic zero also ensures separability. This
checks the whole-algebra interpretation, not merely existence of a root
field isomorphic to one component.

This audit makes no integrality assertion about t, no identification of
Z[t] with a finite or maximal order, and no identification of L114's
polynomial discriminant with the field discriminant. L114's support
still means every maximal-ring prime above {2,3,5,11}, with the real
place retained and the even-degree scalar quotient unchanged. The two
known rational infinity classes survive. Maximal-ring arithmetic, local
image completeness, rational-point control and every independent
integer-lifting gap stated above remain unresolved.

## Mathlib

Full matching Mathlib coverage of this instance factorization and its
complete certificate was not checked. General polynomial/finite-field
support is not asserted to be a matching formal theorem, and no absence
claim is made.
