# Ideal-lattice witness search — source review and narrow park

TARGET: Assess a P1 ideal-lattice search for a principal-ideal witness (alpha)=P1*a^5*product(Q^e_Q) in L045's field, with Q ranging over all primes above five.
CHECKED: 2026-10-11
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Reused the global-eleven valuation and critical-audit assessments; read L045 and ATTEMPTS/013 and relevant L033/L041 ranges. Searched ideal-lattice enumeration, Fincke-Pohst and PARI certification; inspected official interfaces and failure cases. No exact-field witness or novelty is established.
SOURCE_EVIDENCE: PARI official stable HTML entries nfbasis, nfcertify, idealprimedec, idealhnf, idealfactor, idealfactorback, idealmul, idealpow, idealval and qfminim, accessed 2026-10-11; SymPy 1.14.0 documentation round_two and prime_decomp. Fincke-Pohst 1985 primary paper could not be retrieved; its theorem/proof is unread.
COMPARISON: Exact ideal interfaces support positive-witness verification without a full class group, but qfminim flag 2 does not certify exhaustive enumeration. No certified maximal-order/P1/Q5 data are supplied. The established L045 criterion is reused; no new field-specific result is derived.
GAP: Rigorous enumeration coverage and actual certified ideal data are missing; GP, Sage, cypari2, SymPy and FLINT are absent in the checked environment. The bound below specifies a parked diagnostic, not an approved calculation.
REASON: Park this certified maximal-order enumeration implementation; do not repeat unavailable backend searches or enlarge ATTEMPTS/013. A proposed sufficient certificate in the power order is independently testable at the interface level and needs a separate assessment.
LITERATURE_REASON: The gate required coverage of the changed ideal-lattice construction; earlier coverage concerned class structure, not enumeration certification.
SCOPE: Exactly TARGET for L033's degree-twelve 54a1 field, L041's P1 and every prime over five. No computation, lemma, full class-group assumption or evaluation of u is approved by this review.

## Proposal retained from the prior checkpoint

The main gap remains integer emptiness in the surviving branches of
ordered (3,4,11), including independent 54a1 and 96a1 obligations, and
all other residual signatures. This continuation addresses only L045's
unevaluated global class criterion for 54a1. It does not assert that
the witness exists or that a surviving valuation vector lifts to a
descent class satisfying every local and global constraint.

Essential inputs for subsequent assessed work are L033's exact
degree-twelve field, L041's identification of P1 (generator residue 8),
L044's complete local vector filter, and L045's quotient criterion.
Here a is a nonzero fractional ideal and the e_Q are arbitrary integers;
the product includes every prime above five. These are the existing
criterion's variables, not a derived new lemma. This is the 54a1 field,
not L051's L96. There is no cross-notebook input.

The specific new idea is enumeration in the prime ideal lattice,
followed by verification of a fifth-power cofactor, rather than a
larger version of the unsuccessful polynomial coefficient boxes.
Retain ATTEMPTS/013: finite failure cannot show u is nonzero, and
ordinary saturation cannot certify absent ambient generators.
Retain ATTEMPTS/024 and all L96 stops as independent evidence.

Continue only if primary sources and available exact interfaces specify
a finite lattice test whose successful output proves the entire ideal
identity unconditionally. The review must name a concrete enumeration
bound and required certified input data before any calculation is
approved. Park this proposal if it reduces to the old unsupported
polynomial-box search, presupposes the missing class-group certificate,
or cannot supply the required exact ideal representation. A finite
search failure would establish only failure at the specified bound.

Maximal order, primes above five, a suitable lattice and its certified
enumeration, the witness, other-place compatibility and global
integer-power lifting remain unresolved. This is a proposed source
review, not a ready mathematical target or claim of novelty. Mathlib
coverage is not checked.

## Completed source review — 2026-10-11

The gap remains unconditional integer emptiness in ordered (3,4,11) and
the other residual Beal signatures. The intermediate target is a
sufficient witness for u=0 in L045. Its downstream use would be to show
that both L044 vectors survive this valuation filter, without producing
common descent classes, modular points or integer powers. L045 already
proves that conditional consequence; no duplicate lemma is needed.

### Inspected primary interfaces

[PARI official stable general-number-fields manual](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
live HTML accessed 2026-10-11; no release number identified on the page.
Entry nfbasis gives a maximal order for an irreducible integer polynomial;
restricted-prime input can give a strict suborder. Empty nfcertify output
certifies the basis; nonempty output leaves unresolved factors.
Entry idealprimedec gives every prime unless its optional degree filter
is used. HNFs use nf.zk coordinates. Entries idealhnf, idealmul, idealpow,
idealfactor, idealfactorback and idealval supply principal-ideal construction,
arithmetic, factorization, reconstruction and valuations. A factorization
limit makes the result partial. Use zero reduction flags when checking
literal equality, rather than replacing ideals by class-equivalent ones.
These are exact verification interfaces, not computed data for K. The
prior bnf assessment is reused; a supplied identity does not require
computing the full class group.

[PARI official stable linear-algebra manual](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html),
entry qfminim, read through every flag and precision caveat. Input must
be positive definite and symmetric. B bounds a quadratic-form value,
not an algebraic norm or a radius. Only one vector per sign pair is
stored, and a storage cap can omit vectors. Flags zero and one can fail
for large entries; even flag two uses floating-point arithmetic without
rigorous error tracking. It can generate candidates, but cannot certify
bounded exhaustion. Exact positive-witness verification is separate.

Ulrich Fincke and Michael Pohst, *Improved methods for calculating vectors
of short length in a lattice, including a complexity analysis*, Math.
Comp. **44** (1985), no.170, 463–471,
[DOI](https://doi.org/10.1090/S0025-5718-1985-0777278-8),
[publisher PDF](https://www.ams.org/journals/mcom/1985-44-170/S0025-5718-1985-0777278-8/S0025-5718-1985-0777278-8.pdf).
The bibliographic lead and official implementation attribution were
inspected; the paper itself was not. Both publisher PDF paths and DOI
failed web retrieval; a shell fetch failed DNS resolution. No theorem
number, theorem hypotheses or proof is imported from this unread paper.
An algorithm name does not justify certified rounding or exhaustion.

[SymPy 1.14.0 official number-field documentation](https://docs.sympy.org/latest/modules/polys/numberfields.html),
entries round_two and prime_decomp: the former documents Zassenhaus's
Round 2 algorithm for an irreducible rational/integer polynomial,
returning a maximal-order Submodule and field discriminant; the latter
accepts maximal-order data and a rational prime. This is a distinct
backend lead, not a run or independently checked field certificate.
The referenced Cohen book proof was not retrieved for this algorithm.

Read-only availability checks found no gp, sage or Magma on PATH and
no sympy, cypari2 or flint via importlib.util.find_spec in current python3.
These do not exhaust every installation elsewhere. No installation or
arithmetic ran. The older assessment already recorded GP/cypari2 absence;
repeatedly seeking that same missing backend is not a new mechanism.

Queries included `PARI nfinit nfcertify maximal order idealfactor qfminim
ideal lattice enumeration`, `Fincke Pohst 1985 Improved methods for
calculating vectors of short length in a lattice theorem enumeration`,
`number field S class group fifth power ideal principal witness lattice
enumeration`, and a publisher-domain search for Fincke–Pohst. Reuse the
2026-10-10 global-eleven valuation and critical-audit assessments for
principal-ideal/S-class theory; no new search establishes a witness or
novelty for this field.

### Concrete parked test

Proposed finite specification: given a certified integral basis omega
and P1 HNF matrix H, use G=H^t H and B=100, enumerate nonzero z in Z^12
with z^t G z<=100, and form alpha=sum_i (Hz)_i omega_i. This fixes a
diagnostic coefficient length; it is not an intrinsic height bound or a
guarantee of finding a witness. It is a proposed test, not a calculation
or a new field theorem. Exact enumeration or a rigorous interval
certificate is required to claim exhaustion; qfminim supplies candidates
only. Preserve candidate outputs and every enumeration failure.

Required data: certified nf.zk and basis change from L033's k; every prime
above five; and all three eleven-prime HNFs matched to L041's residues
8,2,10 and ramification/residue degrees. For a nonzero candidate, factor
the entire principal ideal with no rational-prime limit and verify
(alpha)=P1*a^5*product(Q^e_Q) by literal HNF equality of unreduced ideal
products. Record all exponents. A norm shape alone is insufficient.
L045 specifies the downstream implication without an uncertified class
table. No basis, ideal matrix, candidate or equality was obtained here.

Continue only with these data and rigorous enumeration coverage, or with
clearly labeled candidate generation plus independent exact verification
of a successful identity. Failure of any finite or incomplete search
cannot show u!=0. Current missing data and unread enumeration coverage
fail the admission test. ATTEMPTS/025 parks this implementation; do not
enlarge old polynomial boxes or assume an install resolves the arithmetic.

### Different proposed continuation, still uncovered

Assess a sufficient identity in R=Z[k], extended to O_K, as a possible
way to avoid computing the maximal order. The proposed restricted
certificate uses J=(11,k-8)R, a nonzero full-rank fractional R-ideal A,
and rational powers of (5R). Source coverage and a proof must establish
that J extends to exactly P1, that extension preserves the relevant
products and principal ideals, and that the whole certificate implies
L045's u=0 without losing the five contribution. None is proved here.
Restricting that contribution to a rational ideal would seek sufficient
witnesses, not characterize every witness allowed by L045.

This changes the certification mechanism: its algebraic interface is
testable without the absent backend. It does not guarantee existence of
a witness, search success or cheap computation. A separate REVIEW_REQUIRED
assessment must precede derivation. Park if it requires missing maximal
data, silently equates power-order primes with maximal-order primes,
or turns sufficient certificates into absence tests. Other-place
compatibility and integer-power lifting remain independent gaps.

NEGATIVE is a source-level implementation decision, not a new class
obstruction or progress beyond the checked mathematics. No lemma,
mathematical script, argument in PROOF.md or DAG input changed. Mathlib
coverage is not checked.
