# Prime cubic Jacobi-sum phase — completed source comparison

TARGET: Audit the prime cubic Jacobi-sum evaluation underlying gamma_2(p)^3=-alpha(p), including the unit normalization, for good primary primes.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the quadratic, reflection-phase and Mellin scopes; searched L540–L555, family003 audit notes and relevant histories for Jacobi/cubic-phase duplicates. Queries included cubic Jacobi sum Eisenstein integers primary prime congruent -1 modulo 3 theorem; site.math.uconn.edu kconrad gauss Jacobi sums cubic; cubic Jacobi sum primary inert prime Eisenstein theorem. The exact source and independent finite-field/Eisenstein statements were inspected; no novelty claim follows. Full search/access qualifications are in drafts/audits/2026-10-31-family003-prime-cubic-phase-source-notes.md.
SOURCE_EVIDENCE: OpenAI pinned commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a TeX, definitions 557–591 and complete lem:prime-gauss-identities 703–769; Dunn–Radziwill arXiv:2109.07463v3 Sections 1.2/2, (1.7)–(1.8) and (2.1)–(2.2); Conrad, Gauss and Jacobi sums on finite fields and Z/mZ, Definition 2.1, Theorems 2.2/2.4, Corollary 2.5 and equation (2.2), pp. 1–4; Booher, The 2011 T-shirt: Cubic Reciprocity, Definition 2, Theorem 13 and Proposition 14 with proofs, pp. 1,4–5. Exact links and Mathlib hypotheses are below.
COMPARISON: DR states a stronger exact cubic formula for all primary moduli, including the prime domain; its additive character is check-e rather than e. Booher independently fixes the split-prime Jacobi associate under the opposite primary-sign convention; Conrad supplies finite-field inputs for both residue degrees. Thus the target is known mathematics with a normalization specialization, not a new identity. L555 is only a quadratic contrast.
GAP: Coverage suffices for a separate finite application audit: verify character orientation, nontriviality of the notebook additive character, its conversion to the published convention, exact Jacobi unit and q_p normalization for split and inert primes. No such verification is completed here. Other Gauss identities, composite propagation, coefficients, arithmetic uniformity and Xi transfer remain outside scope.
REASON: Essential unread theorem coverage has now been inspected. SPECIALIZE permits only the bounded reproduction/application audit after separate next-turn approval; the literature step neither derives the identity nor discharges an L548 premise. Reproving standard finite-field theory is unnecessary; checking the retained source normalization is justified.
SCOPE: O=Z[omega], lambda=1+2omega, e(z)=exp(2pi i Tr(z/lambda)), good primary p=1 modulo 3 outside fixed S containing primes above 6, alpha(p)=p/|p| and gamma_2(p)=q_p^(-1/2) sum_(x mod p) chi_p(x)^2 e(x/p), with chi_p defined by the source sextic Euler convention and zero on nonunits. Include both split and inert primes. Exclude the sextic product identity, other prime identities, composite propagation, theta coefficients, arithmetic-uniform closure and Xi signs.
LITERATURE_REASON: At turn start this cubic identity had REVIEW_REQUIRED coverage and lay outside the ready quadratic scope; exact independent finite-field/Eisenstein statements and normalization comparison were essential missing inputs. Those source needs are now met; further browsing is not the default continuation.

The intended downstream use is to reduce one remaining finite Gauss
premise in L548 and the reflected coefficient chain. The independently
open raw theta/coefficient, arithmetic-uniform and signed-Xi inputs remain.
Essential local interfaces are L548 Hypotheses (3)/(4) and its retained
finite Gauss inputs, with L547's character convention. L555 is a contrast
and a completed quadratic audit, not a substitute cubic premise.

## Inspected primary coverage

Dunn and Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, 14 May 2024, Section 2](https://arxiv.org/html/2109.07463v3#S2),
defines g(c) with check-e(z)=exp(2pi i(z+bar z)), c=1 modulo 3,
and states (2.2): g(c)^3=mu(c)c^2 bar(c). The normalized version is
(1.8). Its basic-facts paragraph includes inert primes. These finite
identities are unconditional; the paper's GRH-conditional prime averages
are not inputs. The cited Hasse 1950, pp. 443–445, is an unread upstream
reference, not an independently inspected proof. DR is the inspected
published statement. The future audit must account for the notebook's
lambda in the additive character; merely identifying the two sums is
not justified by their notation.

Keith Conrad, *Gauss and Jacobi sums on finite fields and Z/mZ*,
[author's PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
pp. 1–4, uses the canonical finite-field trace additive character and
extends every multiplicative character by zero at zero. Theorem 2.2(2)
gives |G(A)|=sqrt(q) for nonprincipal A; equation (2.2) gives
G(A)G(bar A)=A(-1)q. Theorem 2.4 requires AB nonprincipal and gives
G(A)G(B)=J(A,B)G(AB); Corollary 2.5 requires all A,B,AB nonprincipal
and gives |J(A,B)|=sqrt(q). Complete proofs were read. These apply to
finite fields of prime-power order, but do not by themselves identify the
Eisenstein associate or the notebook's additive character. The PDF has
no inspected version date; checked 2026-10-31.

Jeremy Booher, *The 2011 T-shirt: Cubic Reciprocity*, dated 20 August
2011, [author's PDF](https://www.math.canterbury.ac.nz/~j.booher/expos/cubic_rec_promys.pdf),
Definition 2, Theorem 13 and Proposition 14 with complete proofs,
pp. 1,4–5, fixes primary as pi=2 modulo 3. In its split-prime setting
N(pi)=ell=1 modulo 3, Proposition 14 states J(chi_pi,chi_pi)=pi.
Its proof fixes both divisibility and the congruence modulo 3, rather
than only the norm. It is useful independent split-prime coverage,
not an all-residue-degree replacement theorem. Converting its primary
sign and preserving the character orientation remain audit tasks.
Jerry Shurman's [Reed lecture 12](https://people.reed.edu/~jerry/361/lectures/lec12.pdf),
p. 13, gives a second inspected split-prime derivation; it is not needed
to enlarge the scope.

The claimed formula to audit is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, [pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:prime-gauss-identities`, lines 703–769; its character definitions
are 557–591. Its proof works over O/(p), uses the cubic Euler exponent,
and fixes the unit by divisibility, absolute value and the congruence
J=-1 modulo 3. This describes the inspected source argument, not a local
verification of it. Neither the adjacent sextic identity nor L555 is
needed as a substitute cubic premise.

## Mathlib and bounded audit test

Inspected the official Mathlib master sources on 2026-10-31, without
running Lean. In
[JacobiSum/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/JacobiSum/Basic.lean),
`jacobiSum_mul_nontrivial` works over a finite field F into an integral
domain R, requires chi*phi != 1, and accepts any additive character.
`jacobiSum_eq_gaussSum_mul_gaussSum_div_gaussSum` additionally requires
a target field, nonzero image of #F and a primitive additive character.
These are supporting results; no full Eisenstein unit evaluation was
identified in the inspected files. Availability elsewhere is not checked.
In [GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean),
`gaussSum_mulShift_eq` handles unit shifts of an additive character;
`gaussSum_mul_gaussSum_eq_card` requires a nonprincipal multiplicative
character and a primitive additive character over a finite field, with
an integral-domain target. Both full statements and relevant proofs
were inspected. These mutable source URLs are supporting coverage,
not an assertion that the notebook has a formalization.

The later discriminating test is exact equality gamma_2(p)^3=-alpha(p)
for every good primary prime, with the residue field allowed to have
either degree. Verify all hypotheses, the additive-character conversion,
the unit modulo 3 and the normalization; cite the standard inputs rather
than reproduce them. If a sign, conjugation or inert-prime mismatch
survives those checks, preserve it and stop the proposed discharge.
Absolute value or an unspecified associate cannot count as a pass.
No individual cube-root formula, global closure or actual-Xi sign follows.
This is ready coverage for separate next-turn approval, not a mathematical
audit verdict. No cross-notebook input.
