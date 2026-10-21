# Maximal-field discriminant lower bound — source coverage

TARGET: Certify a maximal-field discriminant lower bound for L051's degree-36 field and test whether its true Minkowski cutoff exceeds 10^6.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched local L051, ATTEMPTS/018, workload assessment and history/137, plus exact 96a1/degree-36/discriminant and polynomial-coefficient queries; no matching field-specific lower-bound certificate was inspected. Primary theorem searches located Sutherland's different/tower results and Conrad's complete tame/wild proof.
SOURCE_EVIDENCE: Sutherland 18.785 Fall 2021 Lectures 11 (October 18) and 12 (October 20), Theorem 11.23 and Propositions 12.4,12.28, Theorems 12.17,12.27; Conrad The Different Ideal, Theorem 4.13 and Corollary 4.16, pp.12-14; Milne ANT v3.08 Proposition 7.44 pp.125-126 and retained Theorem 4.3 p.70; FNS final June 10, 2019 manuscript pp.4,27 and section7.magma lines 265-267,315-334.
COMPARISON: Known theorems cover the maximal-ring local-different and tower mechanism unconditionally; only the field-specific ramification certificate and rigorous cutoff comparison remain to be specialized. L051's order upper bound does not supply either result.
GAP: No local ramification/different exponents, maximal-field discriminant lower bound, signature or threshold decision has been established; a one-sided lower bound below the threshold cannot prove that the true cutoff is below it.
REASON: Adequate primary coverage now permits one bounded calculation on the saved target without a class/unit backend; this changes the previous uncovered decision but establishes no new mathematical input.
SCOPE: One exact local-ramification/different lower-bound certificate and Minkowski comparison for L051's L96, allowing its K96 and cubic subfields; no class/unit computation, GRH, Selmer image, point classification or signature exclusion.

## Gap, relevance and test

The main gap is unconditional emptiness of all surviving ordered
(3,4,11) branches, with independent residual signatures still unresolved.
This intermediate test asks whether maximal-order refinement could meet
the proposed 10^6 naive-enumeration entry threshold. It is a routing
measurement, not a Beal lemma or a necessary complexity bound.

Continue only for one certificate attempt using accessible exact local
evidence. A certified lower cutoff above 10^6 parks enumeration at the
true Minkowski cutoff; a weaker lower bound leaves the threshold
undecided. If the bounded method cannot decide it, park this test rather
than enlarge searches or run a class group. An upper cutoff at most
10^6 would require separate evidence before reopening ATTEMPTS/018.

## Primary coverage actually inspected

Andrew V. Sutherland, [Lecture 12, October 20, 2021](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf),
uses A Dedekind, K its fraction field, L/K finite separable and B the
integral closure. Proposition 12.4 (p.2) identifies completed differents;
Theorem 12.17 (p.6), whose trace-dual proof was read, identifies the
discriminant ideal with the different's ideal norm. Theorem 12.27 (p.10)
requires separable residue extension and gives

    e_q-1 <= v_q(Different) <= e_q-1+v_q(e_q),

with equality at the lower end precisely in the tame case. Proposition
12.28 (p.10), for a further finite separable extension M/L with integral
closure C, gives

    Different(C/A) = Different(C/B) Different(B/A) C,
    Disc(C/A) = Disc(B/A)^[M:L] N_{B/A}(Disc(C/B)).

These concern maximal integral closures, not polynomial orders. The
statements are imported; the proposed computation only verifies their
field-specific premises. Derivative evaluation in Proposition 12.24
(p.9) requires B=A[alpha]; it is unavailable without that proof.

Keith Conrad, [The Different Ideal](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf),
undated author PDF retrieved October 10, 2026, Theorem 4.13 (pp.12-14),
proves for every number field and prime above p that the different
exponent is e-1 when p does not divide e, and at least e when p divides
e. The full relevant proof was read: nilpotent multiplication gives the
first bound, then the prime-power filtration makes the residual trace
e times a nonzero finite-field trace, distinguishing tame and wild
cases. Corollary 4.16 (p.14) supplies the discriminant exponent
sum (e_i-1) f_i in the entirely tame case, and a strict improvement in
the wild case. Neither result requires a Galois field or a power-order
index assumption. They cover a lower-bound test without exact wild
ramification groups; a stronger wild formula is outside this assessment.

Sutherland, [Lecture 11](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf),
Theorem 11.23 (pp.8-9), states that completion decomposes the entire
finite separable algebra into its prime completions, preserving e and f,
with local degree ef. Lemmas 11.2,11.4 and Theorem 11.5 (pp.1-2) give
Eisenstein irreducibility and the maximal local DVR for an Eisenstein
generator, including its total ramification. Their statements and proof
cases were inspected. All factors must be accounted for before claiming
an exact local discriminant; a selected factor can supply only a justified
partial contribution.

Milne, [ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
July 19, 2020, Proposition 7.44 (printed pp.125-126), supplies root
valuations and slope-factor descent for characteristic-zero complete
discretely valued fields. The statement and proof were inspected; his
coefficients are indexed in descending order, so his slopes equal root
valuations. An ascending-coefficient polygon reverses the sign.
Reused Theorem 4.3 (p.70) gives the cutoff

    (36!/36^36)(4/pi)^s sqrt(abs(Delta_L96)), 0<=s<=18.

Use the actual signature only with proof, or a valid uniform lower
comparison. Retain strict inequalities and exact rational rounding;
L051's conservative upper-signature choice cannot be reused as a lower
choice. No Newton-polygon computation or new bound is performed here.

## Exact field interface and duplication check

FNS, *Compositio Mathematica* 156 (2020), 77-113,
[final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, printed p.4 identifies the degree-36 fields obtained by
adjoining a two-torsion x-coordinate to the degree-twelve fields. Table 5
(p.27) gives the exact 96a1 polynomial. The inspected
[section7.magma](https://www.mathe2.uni-bayreuth.de/stoll/magma/GenFermat/section7.magma)
lines 315-334 instantiate that polynomial and cubic quotient; lines
265-267 send the integral cubic generator to four times the
2-division coordinate. Keep L051's T=4 theta, not the source code's
informal theta naming. The adjacent Selmer computation is not imported.

L051 provides the exact models and cited absolute degree 36. L050
provides K96's identity; L032 supplies only downstream branch relevance.
The tensor-field degree does not imply local tensor products remain
fields. No L033/L045 or cross-notebook arithmetic is used. ATTEMPTS/018
parks enumeration at an order-based upper cutoff; it does not rule out
this distinct lower-bound certificate. The smaller-factor stop in
history/138 is not a ramification obstruction. The searches did not
establish novelty or locate a ready numerical field certificate.

## Approved attempt and remaining qualifications

Work on the exact TARGET above. Certify local factors or ramification
constraints from the exact L051 models (e.g. coprime Hensel blocks,
Eisenstein shifts or complete Newton polygons). Use the cited different
bounds and tower formula only in the appropriate maximal-field setting.
Report actual/required lower bounds and failures, and save complete
coefficient valuations, factor coverage and exact comparison evidence.
A discriminant of an unproved power basis is insufficient. Do not add
new source-dependent ramification-group mechanisms during that attempt.

No special field lower bound has been derived or approved as true in
this source review. Unresolved inputs include local factorization,
ramification, different contributions and sufficient cutoff evidence.
No GRH, maximal order computation, class/unit completeness, rank, Sha,
point equality or integer solution is assumed. Mathlib coverage of the
full field-specific result and supporting different/tower formulas was
not checked; unknown coverage is not evidence of absence. Import the
standard theorems by the precise citations above; any field-specific
proof belongs in a later research turn's canonical lemma file.
