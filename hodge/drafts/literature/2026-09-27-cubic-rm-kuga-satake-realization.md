# Cubic RM through Kuga--Satake — literature assessment

TARGET: Review whether Schlickewei's Kuga-Satake decomposition for real multiplication gives a conditional algebraic realization of U for the cubic RM deformation family beyond the Dickson family, and identify the exact unproved algebraicity input.
CHECKED: 2026-09-27
DECISION: IMPORT
SEARCH_EVIDENCE: Searched exact cubic RM realization, Kuga-Satake algebraicity and newer conditional results; inspected the primary statements listed below, including Varesco's general tensor-transfer lemma and Floccari's 2025 extension.
SOURCE_EVIDENCE: Schlickewei, arXiv:0907.2503v1, Theorems 1--2 and section 4.5, https://arxiv.org/pdf/0907.2503v1#page=22; Varesco, arXiv:2203.09778v3, Lemma 1.6, https://arxiv.org/pdf/2203.09778v3#page=5; further inspected versions and locations below.
COMPARISON: The conditional transfer is already known; neither the decomposition nor the inspected geometric and similarity theorems establish the required algebraicity inputs for this rank-18 cubic setting.
GAP: Algebraicity of kappa on S x A^2 and of the transported tensor beta_U on A^4 remains unproved here; assuming both would leave the general Hodge target unresolved.
REASON: Import the conditional criterion without reproof. Test a specific known source of cycles for beta_U only after screening that narrower target; merely relocating the unknown class is not a mathematical advance.

## Hypotheses

Retain the [cubic family](../../foundations/05-cubic-rm-family.md),
E=Q(zeta_7+zeta_7^(-1)), and L006's generator U. Work at very general
points of its NS-fixed RM deformation locus. The saved data are
rho=4, dim_Q T=18, dim_E T=6, and four RM directions, of which the
Dickson construction attains three. No assertion about every
specialization or every K3 surface is made.

The [target audit](../../foundations/01-target-and-scope.md) is reused.
Rechecked [Deligne, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2)
and the [Clay page](https://www.claymath.org/millennium/hodge-conjecture/):
the target still uses rational coefficients on smooth projective
complex varieties; Clay labels it unsolved.

## Conclusion

The saved review target is complete. IMPORT refers to the published
conditional criterion below, not to unconditional realization of U.
This is LITERATURE / KNOWN_IMPORTED / EXPLORATION: one exploration
turn in the Kuga--Satake window, with no new theorem or calculation.
The 21-dimensional span on the Dickson family and the three-versus-four
deformation threshold are unchanged. No complete candidate appears.

## Proof

This section records named citations and applicability comparisons.

### The decomposition and its geometric application

Read Schlickewei, *The Hodge conjecture for self-products of certain
K3 surfaces*, [arXiv:0907.2503v1, 15 July 2009, Theorems 1--2, p. 2](https://arxiv.org/pdf/0907.2503v1#page=2),
[Corollary 3.7.1, p. 18](https://arxiv.org/pdf/0907.2503v1#page=18),
and [sections 4.3--4.5, pp. 21--23](https://arxiv.org/pdf/0907.2503v1#page=21).
Theorem 1 gives A isogenous to B^(2^(d-1)) and
End_Q(B)=Cores_(E/Q) C^0(Q_E), with Q_E the E-valued polarization.
It does not make the Kuga--Satake embedding algebraic.

Corollary 3.7.1 assumes dim_E T=3; here it is six. Theorem 2 treats
six-line double planes, whose transcendental rank is at most six;
here it is eighteen. Section 4.5 separately uses Paranjape's
algebraic embedding, an algebraic projection, and algebraic classes
on A^4 projecting to the desired RM tensor. Its Weil-cycle argument
has special abelian-fourfold hypotheses. No identification with those
hypotheses has been established for our family.

### The exact conditional criterion

Read Varesco, *The Hodge conjecture for powers of K3 surfaces of
Picard number 16*, [arXiv:2203.09778v3, 13 May 2024, Lemma 1.6 and proof, p. 5](https://arxiv.org/pdf/2203.09778v3#page=5).
For any K3 surface with algebraic Kuga--Satake correspondence, a Hodge
tensor of T is algebraic exactly when its Kuga--Satake image is.
The proof supplies an algebraic retraction. This lemma has no
Picard-rank-16 restriction.

Apply its statement with tensor degree two: let u_U be L003's tensor
for U, A=KS(T), kappa:T -> H^2(A^2,Q), and
beta_U=(kappa tensor kappa)(u_U) in H^4(A^4,Q). The two unproved
inputs are algebraicity of kappa and of beta_U. Under the first,
the second is equivalent to the original tensor's algebraicity.
It is therefore not independent progress just to assume it.

Also read [Theorem 0.2/4.3 and Theorem 4.1, pp. 2 and 25--26](https://arxiv.org/pdf/2203.09778v3#page=25).
The stronger family result requires generic Picard rank 16 and the
specified rank-six quadratic space. Our four-dimensional parameter
space does not satisfy that lattice hypothesis.

### Similarities and newer algebraicity results

Read Varesco, *Hodge similarities, algebraic classes, and Kuga--Satake
varieties*, [arXiv:2304.02519v3, 2 November 2023, Definition 1.2 and Remark 2.2, pp. 5--6](https://arxiv.org/pdf/2304.02519v3#page=5),
and [Conjecture 4.2, Lemma 4.4, Theorem 4.5 and Corollary 4.6, pp. 16--18](https://arxiv.org/pdf/2304.02519v3#page=16).
The transfer theorem requires a Hodge similarity and algebraic
Kuga--Satake correspondences. In the totally real case the adjoint
involution is trivial, and Remark 2.2 requires the square of a
self-adjoint similarity to be a rational scalar. L006's cubic U
does not satisfy that requirement. This is a hypothesis comparison,
not a new isometry-span theorem. Lemma 4.4 also provides the
polarization-and-transpose retraction used in such transfers; it
does not supply the missing abelian cycle. The quadratic-RM
Theorem 0.1 is not a cubic-RM realization result.

Read Floccari, *K3 surfaces associated with varieties of generalized
Kummer type*, [arXiv:2501.02315v2, 24 November 2025, Theorem 3.5 and Proposition 3.6, pp. 8--10](https://arxiv.org/pdf/2501.02315v2#page=8),
and [Theorems 5.10--5.12, pp. 25--26](https://arxiv.org/pdf/2501.02315v2#page=25).
Assuming Kuga--Satake algebraicity, Theorem 3.5 equates the Hodge
conjectures for all powers of S and of KS(S); it does not remove
that conjectural input. Theorem 5.11 proves both algebraicity and
the power results when T embeds in U_hyp^3 plus <-m>, a rank-seven
space. Our rank-eighteen T is outside this hypothesis. Theorem 5.12
concerns Weil fourfolds of discriminant one. The present decomposition
has not identified such a source for beta_U. Numbering is from v2;
the older author PDF found by search has different numbering.

Followed Schlickewei's reference and read van Geemen,
*Real multiplication on K3 surfaces and Kuga Satake varieties*,
[arXiv:math/0609839v1, 29 September 2006, sections 6.4 and 7.7--7.10, pp. 21--24](https://arxiv.org/pdf/math/0609839v1#page=21).
Its cubic example assumes dim_E T=3. Section 7.10 distinguishes
Kuga--Satake algebraicity from algebraicity of transcendental
endomorphisms. Twisting the polarization is not an algebraic
correspondence construction. These statements support the scope
distinctions above; the historical open-problem remarks are not
used as a current nonexistence theorem.

### Search record and source limits

Queries on 2026-09-27 included:

- `Schlickewei Kuga Satake real multiplication conditional Hodge conjecture cubic multiplication six dimension`
- `K3 real multiplication Kuga Satake correspondence algebraic endomorphisms Hodge conjecture 2025 2026`
- `Kuga Satake "real multiplication" "degree" "six" cubic Hodge endomorphism`
- `"Hodge conjecture" "cubic" "K3" "2025"`
- `"Kuga-Satake" "algebraic" "endomorphisms" totally real`

The prior [broad review](2026-09-26-current-target.md) supplied leads;
it did not contain Lemma 1.6 or this exact two-input comparison.
The essential conditional theorem and its proof were read. Kleiman,
*Algebraic cycles and the Weil conjectures*, Corollary 3.14, is cited
there for the projection but was not separately inspected; the
explicit transpose result above was inspected. Paranjape, Schoen
and Abdulali were read only as statements used in Schlickewei's
proof, not as independently checked constructions. They are not
essential uninspected inputs to the imported Lemma 1.6.

Search also returned Poon's 2026 Picard-rank-14 construction,
Moonen's Tate/Mumford--Tate paper and broad recent Hodge-conjecture
claims on Preprints.org. Their theorem statements were not read;
they are not evidence for coverage or failure of this target.
No originality follows from this bounded search.

### Relevance, overlap and the discriminating test

The bottleneck remains an algebraic representative beyond the
Dickson locus. L004's isometry restriction and the support, sheaf
and bundle failures remain in force within their recorded scopes.
They do not test a cycle on an auxiliary abelian power. The closed
doubled-source window is not reopened.

The review compares three supplies: the six-line construction,
similarity transfer, and the general tensor-transfer criterion.
Only the last matches the required conditional question. Its use
requires a concrete supply for beta_U, followed by kappa algebraicity
on the intended surfaces. Neither is established here.

A bounded intermediate test is whether beta_U is in the rational
span of products of divisor classes on A^4. A positive certificate
would discharge that one input while leaving kappa unresolved.
A negative certificate would stop this particular divisor recipe;
it would not show that beta_U or u_U is nonalgebraic. The threshold
is the full beta_U, not a scalar component or a dimension count.
The [separate pending assessment](2026-09-27-cubic-rm-kuga-satake-divisor-tensor.md)
preserves this proposed test before any calculation. Its screening
has not been completed in this turn.

## Mathlib

Coverage: **not checked**. Varesco's Lemma 1.6 matches the conditional
transfer statement; the other named results support the framework
or have the stated scope limits. No Mathlib declaration or absence
is asserted. No checked source gives unconditional cubic realization
beyond the existing family.
