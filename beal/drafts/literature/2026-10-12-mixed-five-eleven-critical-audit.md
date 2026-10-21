# Mixed five/eleven specialization and certificate audit — source coverage approved

TARGET: Critically audit L059's exact prime-five extension, mixed-class implication, and the complete sixteen-product certificate.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed mixed-prime and bounded-test searches; compared L059 with L038, L041, audited L045/L058 and ATTEMPTS/028, and inspected the new verifier's case scope. Narrowly reopened the cited primary statements; no generator search or novelty inference.
SOURCE_EVIDENCE: Milne https://www.jmilne.org/math/CourseNotes/ANT.pdf v3.08 (2020), Corollary 3.13 p.51, Example 3.19/Theorem 3.20 p.53, Theorem 3.29 p.57, Theorem 7.33/Remark 7.36 pp.121–122 and Corollary 7.42/Remark 7.43 p.124; Lynn https://crypto.stanford.edu/pbc/notes/commalg/extcon.html second operations list item 3; Sharifi https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html Definition 1.3.19 and Proposition 1.4.5 with proof; PARI https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf flags 0,1; SymPy https://docs.sympy.org/latest/modules/polys/domainmatrix.html#sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform 1.14.0, lll/lll_transform hypotheses and example.
COMPARISON: Known maximal-ring localization, extension, S-class and exact module methods cover the audit's general inputs; L059's field-specific applicability and every finite certificate case still require a separate mathematical audit. No source supplies beta, a class value or a generator-completeness bound.
GAP: Independently validate the exact local exponents, positive-product extension, quotient cancellation, supported valuations and full matrix evidence; no essential missing source was identified within this audit scope.
REASON: The new audit differs from constructing the exhausted list; comparing its complete scope with ready coverage approves a separate critical review without deriving new mathematics.
LITERATURE_REASON: The newly written critical-audit target had REVIEW_REQUIRED coverage; its exact localization, quotient and full-certificate scope needed comparison with the previously inspected sources.
SCOPE: Exactly TARGET for L059 and its saved sixteen-product certificate/replay; no generator retest, enlargement, new verifier construction, maximal-order enumeration or class/branch-emptiness inference.

The initial pending proposal is retained in history/173. This turn closes
its source gate only. It does not certify L059 or its computation.

## Reused evidence and primary scope

Reuse `2026-10-12-mixed-five-eleven-power-order-certificate.md` and
`2026-10-12-bounded-mixed-five-eleven-test.md` for exact-statement,
stronger-result and obstruction searches. Reuse
`2026-10-11-power-order-interface-critical-audit.md` for the already
inspected L058 scope and its completed canonical audit. Their targets
and source hypotheses remain unchanged; this comparison adds no
field-specific result. General theorems are cited, not reproved.

J. S. Milne, *Algebraic Number Theory*, v3.08, July 19, 2020, at the
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf): reopened
the localization statement/proof, DVR example, fractional-ideal
factorization, integral-closure theorem, coprime Hensel statement and
strict-coprimality, uniqueness and successive-correction proof cases,
and the local-degree formula/proof and normalized-valuation remark.
Printed locators are in SOURCE_EVIDENCE; PDF indices are one greater.
Dedekind hypotheses concern O_K. The Hensel input is monic integral
with coprime residue factors over a complete DVR; the degree formula
requires a finite separable extension of a complete discretely valued
field. These fit the fixed number-field/local inputs. They do not
identify ideals in the nonmaximal order R by residue factorization.
The later audit must match every local exponent to the actual maximal
primes using both full five factors and all eleven factors.

Ben Lynn, [*Extension and Contraction*](https://crypto.stanford.edu/pbc/notes/commalg/extcon.html),
live author notes, revision unspecified: reopened the definition for an
arbitrary ring homomorphism, the warning that extension need not preserve
primality, and second operations list item 3 on products. This covers
positive ideal powers under R -> O_K. It neither requires flatness nor
licenses arbitrary inversion in R or contraction of an O_K identity.
L059's literal equality and its principal extension remain audit obligations.

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
live author HTML, revision unspecified: reopened Definition 1.3.19,
Proposition 1.4.5 and its proof's ramification and power-sequence cases.
The S-class group quotients by finite-prime classes. The Kummer sequence
requires all infinite places and primes dividing n in S; at n=5 these
are retained by adjoining infinite places to L033's finite S. The
proposition imposes no mu_5-containment assumption. Audited L045 gives
the finer projection quotient using only prime-five freedom, rather
than killing the eleven classes too. Its exact quotient must be preserved
when checking h-cancellation and both claimed valuation witnesses.
The sources do not compute this field's ideal classes.

The [official PARI mathnf entry](https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf),
live manual, release unspecified: reopened flags 0,1 and the rectangular
example. Integer columns generate the output module; flag 1 supplies a
unimodular transform. L059 instead uses explicit two-way integer inclusion
certificates, already within L058's assessed elementary module interface.
No HNF backend assumption is needed. Both inclusions, full rank and
k-stability remain mandatory at every compression.

The [SymPy 1.14.0 DomainMatrix documentation](https://docs.sympy.org/latest/modules/polys/domainmatrix.html#sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform)
was reopened at lll/lll_transform: independent integer rows, m<=n,
1/4<delta<1, and the transformation equation/example. This is supporting
coverage for the reduction contract, not an assertion that the custom
stdlib implementation calls SymPy. Audit its exact integer transforms,
inverses and complete Gram–Schmidt size/Lovasz data independently.
No approximation or shortest-vector guarantee is needed to reject the
fixed list, and reduction supplies no principal-generator completeness.

All five primary URLs above were accessed on 2026-10-12. No uninspected
lead is essential to this audit. Stronger Sage/PARI Selmer/class methods
remain as assessed in the mixed-prime comparison; they require arithmetic
data not supplied by this finite relation test.

## Separate mathematical audit contract

Essential inputs: L033 exact K and power basis; L038's entire five
factors; L041's ordered eleven places; audited L045 and L058; new L059
and both complete mixed certificate/replay files. L044 is retained
through L045. No cross-notebook input, GRH or maximality of R is assumed.

The subsequent research audit must independently check:

- All prime-five generator orders, both residue factors and dimensions,
  every prime away from five, and the reused JO=P1 identification.
- Extension of the positive mixed equality, its ordinary-class relation,
  h prime to five in the exact L045 quotient, membership in K(S,5), and
  both explicit eleven-valuation witnesses. A witness is not presumed.
- Full J/Q generators and all pairwise products in the entire polynomial;
  every one of the 24 compression matrices, rank 12 and k-stability;
  both integer inclusions without saturation or maximal-order closure.
- All sixteen reductions, row/column conventions, integer unimodular
  transforms and inverses, and complete exact size/Lovasz conditions.
- Exact reconstruction of every one of 2,304 prescribed nonzero candidates,
  the entire principal inclusion before its index, and the reverse inclusion
  on any equality branch. Verify every recorded index, rejection and total;
  reconcile the complete replay with the complete original evidence.

For coverage comparison only, read verifier case ranges 100–214 and
inspected labeled JSON previews for report/schema orientation. These
previews establish no arithmetic claim. No certificate replay, new
calculation or independent mathematical correctness audit ran today.
The next audit must process complete relevant evidence, including
multiplication/determinant/Gram–Schmidt routines, not accept the old PASS
flag, reported minimum index or preview as proof. A needed correction
may repair this audited object within scope; a new mechanism needs review.

## Relevance, failures and stopping test

The main gap is global positive primitive integer emptiness of residual
signatures, locally the surviving 54a1 branch of ordered (3,4,11).
The intermediate target is correctness of this conditional input and
finite negative search. Its downstream use is safe recognition of a
future class certificate and an honest stopping point for the tested
ansatz. Passing gives no class value or integer exclusion.

L045 already states the global projected-survival criterion; L058's
rational-five interface and L059's individual five-prime interface are
canonical, so this audit creates no duplicate lemma. ATTEMPTS/028's
exhausted mixed list remains parked. ATTEMPTS/013,025,026,027 and their
obstructions are reused through the completed comparison and preserved;
no old search or blocked class computation is reopened.

Continue if every implication and full finite certificate case is
sound; record and repair any explicit omission or failed exact check.
Park any use requiring unsupported R-inversion, omitted local factors
or a generator-completeness claim, and review newly essential sources
before dependent work. No beta, class value, maximal basis or R-inverse
is known. Arbitrary fifth-power ideal factors, units, other places,
global points, positivity and integer lifting remain unresolved.

Reuse the primary Beal version in foundations/01-target-and-scope.md
and the mixed-prime assessment's 2026-10-12 Mauldin check, retaining its
explicit current-AMS access qualification. This audit does not select a
new main route or change the target. Mathlib: reuse the mixed-prime
assessment's inspected SelmerGroup support and exactness/finiteness TODO
qualification; a full matching explicit certificate remains unestablished
in those sources, and broader coverage is not checked. No absence claim.

Outcome EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: a new scoped coverage
comparison and approval, with no mathematical progress beyond sources,
new lemma, script write or change to PROOF/DAG. Mathematical exploration
usage remains 0/3. The unchanged exact target is now ready for a separate
research audit; further unchanged literature is unnecessary.
