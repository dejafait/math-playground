# Mixed five/eleven power-order certificate — source comparison

TARGET: Assess mixed-prime power-order identities beta R=J^h Q^t with gcd(h,5)=1 and Q=(5,k-a)R at a simple root a modulo five as certificates for L045's u=0.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched S-class quotient, mixed principal ideal relations, power-order certificates and the explicit field/54a1; compared primary ideal/Selmer statements with L038,L045,L058 and ATTEMPTS/013,025,026,027. No field-specific witness was identified; no novelty inference.
SOURCE_EVIDENCE: Milne https://www.jmilne.org/math/CourseNotes/ANT.pdf v3.08 (2020), Corollary 3.13, Example 3.19, Theorems 3.20/7.33, Remark 7.36 and Corollary 7.42; Sharifi https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html Definition 1.3.19 and Proposition 1.4.5 with proof; Lynn https://crypto.stanford.edu/pbc/notes/commalg/extcon.html operations item 3; official Sage selmer_group and PARI mathnf/bnfsunit entries below.
COMPARISON: Known extension, maximal-order ideal and S-class theory cover the general conditional mechanism; L038 supplies the complete local-five input for candidate Q=(5,k)R. A mixed R-ideal equality is a sufficient ansatz, with no necessity, existence or generator-completeness guarantee.
GAP: Prove the exact extension of Q using both complete local factors, specialize a successful mixed equality to L045, and test the fixed sixteen mixed products with complete lattice certificates; these field-specific obligations remain research work.
REASON: Essential source coverage is available for a bounded different mechanism using an individual five-prime factor; the exhausted ordinary principal-power list and maximal-order source blocker remain parked.
LITERATURE_REASON: The changed independent prime-five factor and mixed relation were outside the previous ready assessment.
SCOPE: L033 field, R=Z[k], J=(11,k-8)R; candidate Q=(5,k)R; positive h,t in {1,2,3,4}; exact positive certificates only, without inversion in R or maximal-order enumeration.

The initial REVIEW_REQUIRED proposal is preserved by its unchanged
TARGET. This turn supplies coverage, not a new mathematical result.
No mixed relation, generator, ideal extension proof or class value was
constructed. The companion bounded continuation is newly written and
requires separate supervisor approval before invocation.

The main gap is primitive integer emptiness in remaining Beal signatures,
here the surviving 54a1 branch of ordered (3,4,11). The proposed
intermediate target permits an individual five-prime ideal factor, which
is absent from the exhausted ordinary J-power test and from L058's
principal rational-five factor. Its plausible downstream use is a
certificate for L045's projected class-survival question, with units,
other-place compatibility, global points and integer lifting still open.

Essential inputs: audited L045 and L058, L033's exact field/power basis,
L041's entire ordered eleven places, and L038's complete five-adic
factorization; L044 is retained through L045. No cross-notebook input.

## Primary statements and applicability

J. S. Milne, *Algebraic Number Theory*, [v3.08, July 19,
2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf): Corollary 3.13,
p.51, gives localization equality; Example 3.19/Theorem 3.20, p.53,
give DVR ideals and Dedekind fractional prime factorization. Read inverse
and denominator-clearing cases. Apply to O_K, not R; reuse Theorem 3.29,
p.57, through L058.

Theorem 7.33 and Remark 7.36, pp.121–122, lift coprime monic residue
factors over a complete DVR. Read strict coprimality, uniqueness and
successive-correction cases. Corollary 7.42, p.124, gives the local
degree formula ef.

L038 supplies the monic integral input and coprime factors x,H,
with irreducible H of degree eleven and H(0)=1. This complete local
evidence does not assert maximality of R. The next proof must check
normalized generator orders in both factors and at every prime away
from five; this review does not prove QO_K equals a prime.

Ben Lynn, [*Extension and Contraction*](https://crypto.stanford.edu/pbc/notes/commalg/extcon.html),
live author notes, revision unspecified, operations item 3: extension
preserves integral ideal products under any ring homomorphism. It neither
requires flatness nor says prime extensions are prime. Use positive
products under R -> O_K; literal two-way lattice equality remains
necessary. No arbitrary inverse in R is used by the selected test.

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
live author HTML, revision unspecified: Definition 1.3.19 defines the
S-class quotient by finite-prime classes. Proposition 1.4.5 assumes S
contains all infinite places and primes dividing n; its exact sequence
retains S-units and S-class n-torsion. Read the proof's ramification cases
and n-power exact sequence. At n=5 the hypotheses hold after adjoining
infinite places; containment of mu_5 in K is not required. L045 already
provides the projected criterion. The next research step must justify
the mixed relation's specialization and the use of gcd(h,5)=1 in V;
this is a proof obligation, not a claimed result today.

All primary pages above were opened directly on 2026-10-12. General
theorems will be cited, not reproved; the only necessary proof is their
field-specific applicability and the exact identity verification.

## Stronger known computations and remaining difference

The [official Sage Selmer module](https://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/selmer_group.html),
live docs, release unspecified (copyright 2005–2025), was read at its
introduction, `basis_for_p_cokernel(S,C,p)` input/output and quadratic
example, and `pSelmerGroup` hypotheses and algorithm. The former requires
a class group C. The latter includes units, generators of powers of
torsion ideals, and supported ideals whose classes are pth powers;
`proof=True` requests proved class arithmetic. This is stronger than a
single supported principal relation, and explains why finite failure
of our ansatz cannot evaluate L045. No such arithmetic data are supplied.

The [official PARI bnfsunit entry](https://pari.math.u-bordeaux.fr/dochtml/html/General_number_fields.html#bnfsunit)
requires `bnfinit` and `idealprimedec` data and returns S-unit and S-class
information. Read its six output components. This does not remove
ATTEMPTS/025's missing-data dependency. It is a comparison, not a chosen
implementation or a calculation run here.

The [official PARI mathnf entry](https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf),
flags 0 and 1, specifies the full column module and unimodular transform.
Read those hypotheses and its rectangular example. Reuse audited L058's
exact two-inclusion alternative and the existing principal-power
assessment's SymPy 1.14.0 LLL-transform requirements. No installed package
is newly assumed. The prior local implementation's independently
verified reduction is documented in
`drafts/2026-10-12-bounded-principal-power-local-attempt.md`; copying its
backend in a later research step still requires new complete certificates.

## Duplicate/failure comparison and bounded test

ATTEMPTS/013's 103,532 low-degree element candidates lack completeness;
ATTEMPTS/025 lacks certified maximal-order inputs;
ATTEMPTS/026 records the old unavailable-backend preflight;
ATTEMPTS/027 exhausts the 1,440 ordinary principal-power candidates.
All four were read. L058's rational-five factor is principal, so that
interface does not test individual prime-five freedom. L045's broader
criterion is already known locally; do not create a duplicate of it.

The distinct proposed test uses J^h Q^t for exactly
(h,t) in {1,2,3,4} x {1,2,3,4}, omitting t=0. For each certified reduced
rank-twelve basis test its twelve vectors and all pairwise sums and
differences: at most 144 per pair, 2,304 overall. These are diagnostic
choices, not bounds on generators, ideals, units or class orders.
No computation ran, and no lattice index of Q is asserted here.

Continue only after the complete local Q identification is proved and
rank, k-stability, product generation, compression, reduction transforms
and two-way equality can all be checked exactly. Accept a witness only
by beta R=J^h Q^t, then write its justified L045 consequence. Stop at
the fixed list or a verification blocker. Failed candidates give no
nonprincipality, u!=0 or emptiness conclusion. Do not enlarge this list
or rerun the exhausted one without a different assessed mechanism.

Even success concerns only projected valuation survival. Arbitrary
fifth-power ideal factors, unit classes, other local constraints, global
points, positivity and integer lifting remain outside this certificate.
No branch or Beal solution is claimed.

Queries actually run included `"S-class group" quotient prime ideals
principal ideals`, `"orders" "principal" "ideal" "S-class" certificate`,
`"principal ideal" "mixed" "powers" "S-units" number field`,
`"k^12" "774" "380" "54a1" class group`, and
`"power order" ideal principal certificate simple root`.
Unrelated class-field/principalization and quantum S-unit search results
were not inspected and are not inputs. Searches establish no originality.

## Mathlib and exact target source

Read the [official Mathlib SelmerGroup documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/DedekindDomain/SelmerGroup.html),
2026-10-12, revision unspecified. Supporting declarations include
`IsDedekindDomain.selmerGroup`, `.valuation`, and `.valuation_ker_eq`.
The module explicitly marks maps/exactness and global finiteness as TODO.
The full explicit mixed certificate was not found on this inspected page;
broader supporting ideal/extension coverage is not checked. This is not
an absence claim about all Mathlib.

Rechecked [Mauldin's primary opening assertion](https://sites.math.unt.edu/~mauldin/beal.html)
on 2026-10-12: positive integer bases and exponents greater than two,
with a prime common to all three bases, exactly match GOAL.md. Revision
unspecified; no current AMS-page or prize-rule inspection is claimed.
Reuse `foundations/01-target-and-scope.md` and its recorded AMS access
qualification. The present step changes neither the main argument nor
any canonical lemma.
