# Maximal-prime decomposition at the marked-octic support

TARGET: Determine the complete maximal-prime decompositions of 2,3,5,11 in L116's field, with residue degrees, ramification indices and exact ideal-basis certificates.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused marked-octic maximal-order assessments; searched Lenstra algorithms algebraic number theory prime ideals finite algebra and Del Corso Dvornicich Simon decomposition primes nonmaximal order; inspected primary results below and scoped local duplicates/failures.
SOURCE_EVIDENCE: Lenstra arXiv:math/9204234v1 Sections 2.7–2.8, Theorem 4.9 and complete algorithm sketch manuscript pp.17,20; Del Corso–Dvornicich–Simon (2005) Theorem 3 and full proof p.240; Milne ANT v3.08 Theorems 3.20,3.29,3.34 and relevant proofs pp.53,57,59–60.
COMPARISON: Known algorithms cover arbitrary orders, including the audited maximal ring; their general results give no evaluated support-prime lattices for this fixed field. The nonmonic Kummer shortcut requires an index hypothesis and cannot replace that input.
GAP: No essential source gap remains; execute and certify the fixed instance, retaining all primes and complete ideal products. Supported class/unit arithmetic and rational-point control are separate gaps.
REASON: Exact implementation and instance verification are necessary for later supported arithmetic; a general theorem citation alone does not supply the requested lattices.
SCOPE: Exactly TARGET for unchanged L113–L116; known arbitrary-order prime discovery, exact finite-field and integer-lattice verification, ramification and complete product certificates. Excludes class/unit computations, local point images and point completeness.

## Relevance and existing evidence

The main Beal gap remains primitive integer emptiness for residual
signatures. On this route the immediate gap is rational-point control on
the marked curve followed by degree-nine root recovery and integer lifting.
The intermediate target supplies actual support primes for later S-unit
and S-class two-torsion arithmetic. It can help without closing those
independent gaps.

Inputs are audited L115's entire field
K=Q[t]/(275t^8−2860t^6+6930t^4−3564t^2+243), audited L116's maximal
basis and multiplication table, and L114's support {2,3,5,11} for L113.
The local search of marked-octic assessments and L116 found no duplicate
complete decomposition certificate. L116's nilpotent dimensions and
terminal multiplier ranks concern maximality, not individual prime data.
ATTEMPTS/050–051 concern unsuccessful bounded rank detection and a false
rank-zero premise respectively; neither tests this ring prerequisite.
Their evidence and unfinished L108 remain preserved. No cross-notebook
result is used. The target/scope source assessment in
foundations/01-target-and-scope.md remains applicable; this step changes
neither the Beal formulation nor the selected route.

## Primary theorem coverage

H. W. Lenstra, Jr., *Algorithms in algebraic number theory*, Bull. Amer.
Math. Soc. (N.S.) 26 (1992), 211–244,
[arXiv:math/9204234v1, 1 April 1992](https://arxiv.org/pdf/math/9204234v1).
Read Sections 2.7–2.8 and Theorem 4.9, manuscript p.20, with its entire
algorithm sketch and setup p.17. For an order A in a number field,
a subring C and a nonzero prime ideal p of C, the theorem determines
all primes over p and the p-primary maximal overorder. Its sketch treats
C=A by successive nonsingular-pair refinement, factoring residue
polynomials when enlargement is needed; C!=A uses C+pA and contraction.
It also describes valuation evaluation. Section 2.8 certifies a finite
field by a primitive-element quotient isomorphism and irreducibility.
Take A=O_K from L116, C=Z, p=(2),(3),(5),(11); all are nonzero prime
ideals. No monogenic, normality, tame or p>8 premise is imposed.
The deterministic alternative allows these fixed small primes;
probabilistic discovery still needs exact verification. Import this
algorithm, without reproof. No claim that its general theorem evaluates
our particular field is made.

I. Del Corso, R. Dvornicich and D. Simon, *Decomposition of primes in
non-maximal orders*, Acta Arith. 120.3 (2005), 231–244,
[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82018).
Read Theorem 3 and its full proof, printed p.240. For the paper's primitive
irreducible nonmonic polynomial and equation order R_F, its Kummer
factorization requires p coprime to [O_K:R_F]. The proof localizes to
identify R_F with O_K and transfers the primary powers and residue fields.
L116 records [O_K:R_F]=2^32*3^10*5^2. Therefore this shortcut is inapplicable
at 2,3,5 for that starting order. Its hypothesis is available at 11,
but this review chooses the single arbitrary-order method for all four
primes. No assertion about a new generator's index is assumed.

J. S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
Read Theorems 3.20,3.29 and their proofs (printed pp.53,57), the extension
setup, Lemma 3.33 and Theorem 3.34's proof of the general degree formula
(pp.59–60); also inspected its separate Galois clause. The integral
closure of a Dedekind domain in a finite separable extension is Dedekind;
nonzero ideals factor uniquely into prime ideals. For all primes above p,
sum(e_i*f_i) equals the extension degree; equal e_i and equal f_i require
the additional Galois hypothesis. Here the base is Z and L115 supplies a
finite characteristic-zero field, so these apply to L116's maximal ring
and give total eight. No normality is assumed. These are imported
standard results; no reproof is needed.

These inspected sources cover the algorithm and its checking framework.
Upstream references in their proofs were not independently audited;
we import the stated theorems. Broader class-group and point algorithms
are outside this assessment. Full matching Mathlib coverage is not
checked; this is not evidence of absence.

## Approved instance contract and discriminating test

The research continuation may implement the cited arbitrary-order
algorithm using the fixed audited multiplication table. It must retain
complete discovery evidence rather than treat a Frobenius rank as a
prime list. Implementation choices may use exact finite-ring linear
algebra and polynomial factorization within that method; an essential
new mathematical criterion would require a separate assessment.

For each support prime require the following outputs and checks:

1. Every proposed maximal ideal has a full rank-eight integer basis in
   the fixed O_K basis, contains pO_K, is proper and stable under all
   eight basis multipliers. Retain full lattice inclusion evidence.
2. Supply an explicit quotient map to F_p[X]/(g_i), with g_i monic
   irreducible of degree f_i, preserving one and every product. Certify
   surjectivity and equality of its kernel with the proposed ideal;
   dimensions or norms alone do not identify that kernel. Use complete
   finite-field irreducibility evidence as in L115 where appropriate.
3. Establish distinctness of the ideal lattices, positive exponents e_i,
   and the exact lattice equality product(P_i^e_i)=pO_K. Generate ideal
   products with the full multiplication table and verify equality in
   both directions, with Hermite/Smith evidence as needed. Retain the
   complete product basis, not merely its determinant. Verify separately
   sum(e_i*f_i)=8 and the individual quotient sizes.
4. Replay the complete load-bearing arithmetic; save full certificates
   under scripts/pair-genus-two/ and print only conclusions, actual and
   required bounds, failures and paths. A partial factor list or a
   precision preview is not success. Canonical proofs must cite the
   imported results and justify all instance specializations.

Continue only on complete certificates at all four support primes.
If a check fails, save the exact failure and any partial work without
claiming completeness. A missing essential theorem returns the dependent
work to literature review; a persistent source blocker parks it for an
independently testable target. Increasing the old rank-search caps or
retesting rank zero is not this continuation.

Supported unit generators, S-class two-torsion, real and finite local
point images, surviving-cover point completeness, degree-nine root
recovery, compatible remaining factors, both L095 integer systems and
the minus-eleven alternative remain unresolved. The known rational
infinity points prevent an empty fake-Selmer-set shortcut. This review
approves a prerequisite calculation; it proves no new decomposition,
lemma, rational-point bound or Beal exclusion.
