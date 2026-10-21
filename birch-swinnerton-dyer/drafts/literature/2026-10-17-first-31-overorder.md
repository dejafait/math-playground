# One strict 31-overorder — primary construction reviewed

TARGET: Construct and independently verify one strict 31-overorder of L077's starting order from the radical-multiplier construction, without iterating to maximality.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the maximal-order source comparison and residual-prime assessment; checked L077, C077a, histories 287/289/291 and ATTEMPTS/040. Searched “Del Corso Dvornicich Simon multiplier order radical” and “Decomposition of primes in non-maximal orders enlargement”; inspected the publisher's primary theorem and proof rather than secondary abstracts. Targeted records contain no executed overorder construction; this is not a novelty claim.
SOURCE_EVIDENCE: Del Corso--Dvornicich--Simon, Decomposition of primes in non-maximal orders, Acta Arith. 120 (2005), 231--244, DOI 10.4064/aa120-3-2, https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; Section 2 definitions and Proposition 3 pp.232--233, Proposition 6 and Proposition 7 statements pp.236--237, Proposition 9 and Theorem 2 with complete proof pp.238--240, inspected as publisher PDF text on this date.
COMPARISON: Proposition 9 supplies the radical multiplier order; Theorem 2(ii) supplies its explicit nonmonic lattice and index p^(deg G). These cover the construction theorem, including strictness after C077a, but not this field's explicit rank-48 basis or complete finite arithmetic certificate. Only that fixed known-method implementation and verification is approved.
GAP: The enlarged basis, complete lattice-equality witnesses, inverse transports, product table and exact index certificate remain uncomputed. Feasibility within the caps below is unproved. No essential source gap remains for this first enlargement; later maximality and descent are outside scope.
REASON: The target changes from a completed nonmaximality verdict to an actual correction. Primary coverage now specifies the previously undefined denominator-ideal factor; no general construction needs reproof.
SCOPE: Audited L067/L077/C077a, the whole degree-48 field, original nonmonic H, all original basis/transports/product slots, and prime 31 only. No L026 or cross-notebook input, second enlargement or new prime search.

LITERATURE_REASON: The starting assessment was REVIEW_REQUIRED for the explicit enlargement formula and nonmonic lattice hypotheses. This review addresses that essential unread construction scope and reuses completed prime/audit coverage.

## Gap and discriminating test

The main gap remains rational-rank equality for arbitrary E/Q of analytic
order at least two. The intermediate target is one complete strict
31-overorder in the fixed torsion field. Correcting the order could
support later complete units/classes and L066's descent enclosure. It
does not itself bound a Selmer group or supply a rational direction.
Continue only if the full lattice, source identification and independent
checks below pass. At a cap or identity failure preserve partial evidence
and stop without retry or iteration. A changed mechanism or another
independently testable target then needs assessment.

## Exact primary statement and essential proof cases

The source assumes a Dedekind ring R and a primitive irreducible
F=a_0 x^n+...+a_n with a_0 nonzero. Its root is alpha and its order is
R_F=R+T_1(alpha)R+...+T_(n-1)(alpha)R, with the same truncated polynomials
as L077. Section 2 defines the invertible denominator ideal
B=a_0 R_F+T_1(alpha)R_F+...+T_(n-1)(alpha)R_F, also equal as an R-module
to a_0 R+T_1(alpha)R+...+T_(n-1)(alpha)R.
The notation B^d means an ideal power, not a prefix of the order basis.
Proposition 3 states that B^d times all evaluations at (alpha,1) of
degree-d homogeneous polynomials generates R_F. Its proof uses alpha B=A
and A+B=R_F. A monic-order shortcut omitting B is therefore not justified.

For the squarefree homogeneous factor lift H_1 of degree h, Theorem
2(i) states I_p=pR_F+B^h H_1(alpha,1). Proposition 9 states that
(I_p:I_p)={x in L: x I_p subset I_p} is an order containing R_F,
equals R_F exactly at p-maximality, and otherwise has p-power index.
With the source's H_2,H_3 and homogeneous
G=gcd(H_1bar,H_2bar,H_3bar), let g=deg G. For any homogeneous lift U of
Fbar/G of degree n-g, Theorem 2(ii) states

\[
 (I_{\mathfrak p}:I_{\mathfrak p})
 =R_F+\mathfrak p^{-1}B^{n-g}U(\alpha,1),\qquad
 [(I_{\mathfrak p}:I_{\mathfrak p}):R_F]=\mathfrak p^g .
\]

The inverse prime is a base-ring fractional ideal. For R=Z it means
multiplication by 1/p, and the index ideal becomes an ordinary positive
integer index. This is an imported theorem, not a new derivation or
construction in this literature turn.

The complete Theorem 2 proof through the final lcm on p.240 was inspected.
Part (i) uses intersection of prime radicals and Proposition 6.
Part (ii) classifies pO' by a divisor P of Fbar and imposes membership
in I_p and multiplication into pI_p. Proposition 7 converts these to
H_1bar dividing Pbar and
(H_1bar/gcd(H_1bar,H_3bar)) H_2bar dividing Pbar. The final lcm is Fbar/G.
These are the source's essential containment and equality cases;
one inclusion alone would not identify its order.
Proposition 9 is cited by the paper as Zassenhaus's theorem, Cohen,
Proposition 2.4.4; no reproof is needed. The earlier Stein partial proof
and unread implementation leads are not substitutes for this coverage.

## Applicability, duplicates and limitations

Set R=Z, F=H=343h and n=48 using audited L067/L077. They supply
primitivity, irreducibility and precisely the source order R_H in the
whole field, not an order in a selected factor. C077a supplies original
homogeneous lifts of degrees 46,2,48, the leading unit modulo 31 and
the homogeneous degree-two gcd with affine representative T^2+24.
Thus the source requires a degree-46 U and the ideal power B^46.
The required index check is 31^2, the source's predicted value, not a
computed index of any new basis in this turn. Nonzero top coefficients
exclude a factor at infinity here. No integrality of t or replacement
by Z[t] is assumed. The next attempt must record every U coefficient
and check the complete reduction identity G Ubar=Hbar.

L077 certifies the starting order and C077a only its nonmaximality.
Neither is an executed overorder construction. Step 287's four-prime
support failure remains intact. ATTEMPTS/040 stops repeated starting-order
source confirmation, not this different target. The residual need not
be refactored; the completed prime-selection/audit need not be repeated.
No progress beyond the checked general source results is claimed.
Complete matching Mathlib coverage has not been checked; no absence
claim follows.

## Approved certificate contract for a subsequent research turn

1. Use a new isolated output directory. Keep original L067/L077/C077a
   evidence read-only, with hashes and exact polynomial/basis matching.
   Retain all 48 dimensions, both original coordinate transports and all
   original product slots. Reuse the fixed prime/factorization; do not
   search more primes or refactor the residual.
2. Construct exactly O_H+(1/31)B^46 U(t,1), where
   B=(343,b_1,...,b_47) in L077's coordinates. Choose a full homogeneous
   degree-46 U lifting Hbar/G, retaining the leading unit. Exact ideal
   powering and rational-lattice reduction are permitted. Store
   intermediate bases and integral generation witnesses sufficient to
   replay equality at each reduction; do not enumerate exponentially
   many unreduced products. Dropping B or switching to a scaled-root
   order is outside this approval.
3. Save a rational 48-by-48 basis M in O_H coordinates, its inverse and
   both transports to L067. Verify both inverse identities and integral
   generation witnesses in both directions between M Z^48 and the source
   lattice. Rational-span equality or an HNF label alone is insufficient.
   Reconstruct all intermediate generator containments independently.
4. Verify every old basis element and 1 belongs to the new lattice.
   Reconstruct all ordered new-basis products in the original field and
   all 48^3 integer table slots, including zeros, with independent
   arithmetic. Check 31M integral and exact index using the full integral
   inclusion matrix M^(-1), with complete determinant or unimodular Smith
   witnesses; require absolute determinant 31^2>1. Source-lattice equality
   and the cited theorem identify the radical multiplier order; no second
   enlargement is authorized.
5. Permit one producer stage and one independently implemented full replay,
   each capped at 180 seconds internally / 181 seconds externally, with
   combined outputs at most 134217728 bytes. These are feasibility
   limits, not guarantees. Print actual/required rank, index, slot coverage,
   limits, failures and paths; keep complete witnesses on disk. Hash
   original inputs before and after. At a cap or failed identity stop
   without retry, resumed computation or larger caps. Optional malformed
   basis/index controls must name their actual rejection conditions and
   supplement, rather than replace, complete positive verification.

No enlarged lattice, lemma or mathematical script has been produced.
Success would remain known-method reproduction awaiting separate critical
audit. It would not supply 31-maximality, global maximality, all index
primes, a field discriminant, complete units/classes, Selmer bounds,
localization, rational membership or arbitrary-curve rank equality.
The current argument and DAG do not change.
