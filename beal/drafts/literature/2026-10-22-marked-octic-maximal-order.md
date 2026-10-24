# Marked-octic maximal-order certification: source approval

TARGET: Determine and certify a maximal-order basis and field discriminant for L115's degree-eight field.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the local support/factorization/audit scopes and rational-cubic unit assessment, preserved ATTEMPTS/050–051, and searched exact octic coefficients plus maximal-order, p-radical, multiplier-ring and Round-2 terminology; no inspected exact-instance basis was located, while primary sources supply a complete certification method.
SOURCE_EVIDENCE: Read Lenstra, Algorithms in algebraic number theory, arXiv:math/9204234v1, Sections 2.4–2.5, 2.7, 2.10 and Theorem 4.5 with its complete relevant argument on manuscript pp.17–18; read Del Corso–Dvornicich–Simon, Acta Arith. 120.3 (2005), Section 2, Proposition 4 and Proposition 9 on printed pp.232–234,238, including the nonmonic order and all-prime hypotheses.
COMPARISON: The sources already cover an integral full-rank starting order for primitive nonmonic F and finite radical/multiplier certification at every possible index prime; the missing work is this field's exact basis, lattice and discriminant evidence, not a new maximal-order theorem. Neither L115 nor L114 supplies these values.
GAP: Execute and replay the exact instance certificate: starting-order multiplication/trace data, complete discriminant factorization, all required p-radical/idealizer steps and final stability checks, with every basis expressed in the entire Q[t]/(F).
REASON: Essential source coverage is now sufficient for a separate RESEARCH specialization of the unchanged TARGET; this literature turn computes no integral basis, field discriminant, local arithmetic or point bound.
SCOPE: Exactly TARGET for unchanged L114–L115's whole degree-eight field; the nonmonic-order construction and Lenstra's all-prime radical/idealizer algorithm, exact rational/integer lattice arithmetic, full discriminant/index verification and independent arithmetic replay; excludes class/unit groups, supported-class enumeration, complete local point images and rational-point control.

## Original proposed scope and relevance (retained)

Essential inputs: audited L115's entire field K=Q[t]/(F),
F=275t⁸−2860t⁶+6930t⁴−3564t²+243, and audited L114's unchanged
G=11F, polynomial discriminant and sufficient support {2,3,5,11}.
L113 fixes the marked model; L109–L111 matter only for eventual point
interpretation. No cross-notebook input is proposed.

The main gap is rational-point control followed by the independent
integer-lifting conditions. A certified maximal ring would provide an
exact basis for later prime-ideal and supported-square-class arithmetic.
This continuation asks only for the ring and its discriminant, not class
groups, units, fake Selmer completeness or a point bound. It does not
assume the displayed nonmonic generator integral or treat its polynomial
discriminant as the field discriminant. Any new integral generator must
come with a verified Q-field identification and exact basis transport.

The later source review should inspect primary theorem hypotheses and
essential proof cases for a practicable certification method, search for
an exact-instance result or duplicate, and decide whether an unconditional
finite certificate is feasible with the available exact arithmetic.
Software output without a documented maximality justification is not the
threshold. Reuse an already inspected suitable result if one is located;
do not infer novelty or absence from this narrow scope check.

Continuation test: approve a specific method only if it can certify an
integral full-rank order and maximality at every possible index prime,
with an exact discriminant and complete field identification. If essential
coverage is inaccessible, mark that limitation and park dependent work;
if a bounded implementation is infeasible, retain the obstruction and
select a materially different independently testable prerequisite.

Unresolved assumptions remain the ring certificate itself, supported
class/unit data including class-group two-torsion, complete local images,
points on surviving covers, degree-nine distinguished-root recovery,
remaining factors, both L095 integer systems and the minus-eleven route.
Known rational infinity points preclude an empty fake-Selmer-set shortcut.
ATTEMPTS/050–051 and unfinished L108 are preserved. Full matching Mathlib
coverage is not checked. The original proposal above is retained; the
source review below supplies approval, without executing its calculation.

## Primary coverage actually read

H. W. Lenstra, Jr., *Algorithms in algebraic number theory*, Bull. Amer.
Math. Soc. (N.S.) **26** (1992), 211–244, DOI
[10.1090/S0273-0979-1992-00284-7](https://doi.org/10.1090/S0273-0979-1992-00284-7).
The inspected primary text is
[arXiv:math/9204234v1](https://arxiv.org/pdf/math/9204234v1),
1 April 1992. Page numbers here refer to that 33-page manuscript.

- Sections 2.4–2.5, pp.6–7, describe exact field linear algebra and
  integer-lattice operations using Hermite/Smith reduction; Section 2.7,
  pp.7–8, specifies commutative unital rings by multiplication tables.
- Section 2.10, pp.10–11, defines orders as full-rank unital subrings,
  gives their trace discriminant and several exact encodings, and gives
  both integral-generator scaling and a generalized equation-order
  construction when the generator is not integral. Thus a monogenic
  maximal-order assumption is unnecessary.
- The setup of Theorem 4.5, p.17, permits an arbitrary order A in a
  number field, with C=Z an explicitly treated case. Its p-primary
  overorder A^(p) accounts for precisely the p-primary part of O_K/A.
  The direct-sum description there supplies assembly over the relevant
  rational primes. The proof on p.18 explains the full radical and
  multiplier-ring algorithm, including small primes, not merely a
  criterion for primes exceeding the field degree.

More explicitly, the p.18 argument uses the following **imported general
algorithm**, with n the degree and p a proved rational prime. Let I be
the inverse image in A of the nilpotents of A/pA. The nilpotent subspace
is the kernel of x -> x^(p^k), where k is the least positive integer
with p^k >= n. Set M={b in K : bI subset I}. The same proof identifies
pM/pA with the kernel of

    A/pA -> End_Fp(I/pI),   a -> multiplication by a.

If that map is injective, M=A and A is p-maximal. Otherwise replace A
by M and repeat. Lenstra gives the bound log|disc(A_initial)|/(2 log p)
on strict iterations. The proof uses I/pI in this second map, whereas
the nilpotent computation uses A/pA; confusing them would invalidate a
certificate. All orders encountered remain inside the same K. No GRH,
normality, class-group, signature or p>n hypothesis enters this method.
These are cited source results, not new derivations in this review.

Ilaria Del Corso, Roberto Dvornicich and Denis Simon, *Decomposition of
primes in non-maximal orders*, Acta Arithmetica **120.3** (2005),
231–244, [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82018).
Read the following precise parts of the published text:

- Section 2, p.232: R is Dedekind, F(X)=a_0 X^n+...+a_n is primitive
  and irreducible over its fraction field, with a_0 nonzero. With theta
  the image of X, define T_i(theta)=a_0 theta^i+...+a_i for
  1<=i<=n−1. Then R_F has R-basis 1,T_1(theta),...,T_(n−1)(theta)
  and is an order contained in the integral closure. This is an
  assertion about an actual order, not R[theta] for a nonintegral theta.
- Proposition 2 and its proof, p.233, identify that order with
  R[theta] intersect R[theta^(-1)]. Proposition 4 and its entire proof,
  p.234, give disc(R_F)=disc(F) by the triangular basis transformation
  and the embedding determinant. The introduction, p.231, records
  disc(K)[O_K:R_F]^2=disc(F) in the rational base case.
- Section 4 and Proposition 9, p.238: for an order O, the p-radical
  I_p=sqrt(pO) has multiplier ring O'={b in K : bI_p subset I_p};
  O' is an overorder, equals O exactly when O is p-maximal, and a
  strict enlargement has index p^j with 1<=j<=n. This includes primes
  dividing the nonmonic leading coefficient. The paper explicitly
  defines p-maximality using the maximal-order index, not the polynomial
  reduction pattern.

The order construction is credited there to Simon, *The index of
nonmonic polynomials*, Indag. Math. (N.S.) **12** (2001), 505–517;
Proposition 9 cites Cohen, *Advanced Topics in Computational Number
Theory* (2000), Proposition 2.4.4. Those upstream works were not read
and are not claimed as independently verified. The inspected published
statement of the order construction and Lenstra's explicit algorithmic
argument are sufficient inputs here. No reproof of their general theory
is proposed.

The SymPy **1.14.0** official
[round_two documentation](https://docs.sympy.org/latest/modules/polys/numberfields.html#sympy.polys.numberfields.basis.round_two)
was read through parameters, returns, explanation and examples. It
accepts an irreducible polynomial over ZZ or QQ and promises a maximal
order and field discriminant; it also exposes some computed radicals.
This is supporting implementation documentation only. A backend return
or its incomplete radical dictionary would not replace the complete
certificate specified below. The default python3 has no SymPy or
cypari2 import, and gp/sage were not found on the current shell PATH;
no installation or number-field calculation was attempted. Exact
rational lattice and finite-field operations in dimension eight remain
available for a direct implementation; performance is not yet tested.

Stein's [web Theorem 4.3.5](https://wstein.org/books/ant/ant/node29.html)
gives corroborating Pohst–Zassenhaus coverage,
but its displayed following lemma/proof has a scaling ambiguity. The
approved kernel formula is Lenstra's pM/pA formula above, with its
explicit domain and codomain; the web proof is not a certificate input.
A Cohen (1993) book PDF lead exceeded the web reader's size limit and
was not read. Neither lead is essential after the primary coverage above.

## Applicability, differences and duplicates

L115 already supplies primitivity, irreducibility, degree eight and the
entire quotient identification for the exact F in the proposal. R=Z is
Dedekind, so the nonmonic-order theorem applies with this unchanged F;
no new hypothesis about theta's integrality is needed. The future
calculation must instantiate the source basis and verify its arithmetic.
Using this order keeps every coordinate inside the original field and
does not require identifying a different field from numerical invariants.
If generator scaling is used instead, the exact transformed polynomial,
both field maps and basis transport must be certified, as required by
Lenstra Section 2.10. The direct R_F route is preferred.

The strongest inspected result already provides a complete maximal-order
algorithm. A citation therefore suffices for the general theorem but
cannot supply this instance's eight rational basis vectors, exact
discriminant or successful arithmetic tests. The proposed work is a
REPRODUCTION by specialization, not a new algorithm or certified novelty.
The local rational-cubic unit assessment does not give this octic ring;
the marked-octic factorization/audit scopes explicitly exclude maximal
orders. ATTEMPTS/050's failed bounded divisor detector and ATTEMPTS/051's
positive-rank obstruction remain in force for their own mechanisms;
neither is a prohibition on this independent ring prerequisite.

Queries actually used included `maximal order certificate p radical
multiplier ring criterion number field Zassenhaus round 2`, `Cohen
course computational algebraic number theory algorithm 6.1.8 pdf`,
`Lenstra Algorithms algebraic number theory 1992 multiplier ring radical
pdf`, `"Zassenhaus’s theorem" "Proposition 9" order`, and the exact
coefficient combinations `"275" "2860" "6930" "3564" "243"
"field"`, `"275t^8" "discriminant"`, `"275*x^8" "2860"`.
The exact-instance queries returned no inspected matching theorem or
basis. Irrelevant matches were not loaded as mathematical inputs.
This bounded search does not establish absence from the literature or
novelty. No cross-notebook source is used.

## Approved exact certificate and stopping test

The next turn may perform the unchanged TARGET, using the following
single coherent calculation and replay. These are required outputs, not
claims already established about the octic.

1. Represent all elements in 1,theta,...,theta^7 modulo F/275.
   Instantiate the source's eight-element R_F basis; save its invertible
   rational coordinate matrix and inverse, the coordinates of one and
   all products, and the complete integral multiplication table. Check
   closure and full rank exactly. Compute the trace Gram determinant,
   compare with the exact polynomial discriminant, and factor it
   completely with primality and residual-cofactor evidence. L114's
   unchanged G=11F is a cross-check; disc(G) must never be substituted
   directly for disc(K). Do not assume that descent support by itself
   is a maximal-order index-prime certificate.
2. At every prime with p^2 dividing that initial order discriminant,
   carry out Lenstra's radical/multiplier steps. Save the full Frobenius
   matrix and a complete kernel/rank certificate, an exact basis for
   I, the complete multiplication matrices on I/pI, and a complete
   kernel/rank certificate for their joint map. Reconstruct each
   overorder with rational lattice transformations and exact two-way
   inclusion checks. At strict steps verify the p-power index and the
   discriminant-index identity; at terminal steps verify injectivity.
   This includes every relevant small prime and every leading-coefficient
   prime. Do not use a trace-radical shortcut that loses small-prime
   nilpotents, or a kernel containment without its completeness.
3. On the final single basis, repeat the terminal maximality check at
   every relevant initial prime. The index/discriminant theorem excludes
   all other primes once the initial factorization is complete. Save
   the final integral multiplication table, exact trace Gram matrix,
   determinant and factorization, and the initial-to-final lattice index.
   Keep the signed discriminant and the entire field identification.
4. Independently replay the load-bearing matrices, kernels, lattice
   equalities and discriminants from the stored certificate, without
   treating the producer's passing flags as evidence. The eventual
   canonical lemma must import the named general theorems and state
   hypotheses, qualifications and Mathlib status. Its complete instance
   proof and citations belong there; no lemma is written this turn.

Bound each prime's strict enlargements by the source's discriminant
bound (or its exact valuation form floor(v_p(disc(R_F))/2)); never
increase a failed cap without reassessing the reason. An arithmetic,
factorization, lattice or replay failure means that the maximal-order
claim is unproved: save the partial certificate and the exact failure.
If this bounded implementation is infeasible, park it and propose a
materially different independently testable prerequisite for separate
review. Do not infer maximality from irreducibility, an integral-looking
basis, a matching determinant alone or a software label.

Successful completion would certify only O_K and disc(K). Supported
class/unit data (including class two-torsion), local images, rational
points on surviving covers, degree-nine root recovery, remaining
factors, both L095 systems and minus-eleven remain independent gaps.
The two rational infinity points still prevent an empty fake-Selmer
argument. Full matching Mathlib coverage remains not checked; supporting
formal ring/discriminant results are not a matching instance certificate.
This review approves a separate mathematical specialization and derives
no new result about the octic.
