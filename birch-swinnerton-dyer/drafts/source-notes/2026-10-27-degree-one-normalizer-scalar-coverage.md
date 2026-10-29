# Step 527 — Sources for the degree-one normalizer action

2026-10-27. Literature only. The exact target is recorded in
`drafts/literature/2026-10-27-degree-one-normalizer-scalar.md`.
No scalar comparison, operator-extension proof or new lemma is established here.

## Inspected primary statements and proof cases

1. Ralf Schmidt, *Some remarks on local newforms for GL(2)*,
   J. Ramanujan Math. Soc. **17** (2002), 115–147.
   [Author PDF](https://sites.math.unt.edu/~schmidt/papers/gl2.pdf),
   internal pp.7–8 and 23–28: Theorem 1.2.1, Section 3.1 definitions,
   Propositions 3.1.1/3.1.2, Lemma 3.2.1, Theorem 3.2.2 and its proof.
   Here F is nonarchimedean; pi is infinite-dimensional, irreducible,
   admissible, with trivial central character. The conductor-level
   K_0(p^n)-fixed line has normalized Atkin–Lehner eigenvalue
   epsilon(1/2,pi). The displayed matrix is A_n=(0,1;varpi^n,0).
   The proof checks the spherical case, n>=2 using the Kirillov
   characteristic function of O_F^times, and n=1 using an unramified
   quadratic Steinberg twist. Thus exponent two is included. The
   Steinberg-twist sign in Proposition 3.1.2 is -chi(varpi) for
   unramified quadratic chi and chi(-1) for ramified chi. This is
   a conductor-line theorem, not a scalar theorem at arbitrary old level.
   No reproof is needed. Internal pagination is not journal pagination.
   The author publication list confirms the journal reference.

2. Herve Jacquet and Robert P. Langlands, *Automorphic Forms on GL(2)*,
   LNM **114** (1970),
   [IAS author edition](https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2-rpl_1.pdf).
   Inspected Section 4 setup, Theorem 4.2(i)–(iv), pp.60–63,
   including its complete one-dimensional proof case; Theorem 4.3(i)
   statement, p.66; Section 15 setup and Theorem 15.1, p.239.
   Pagination is the IAS edition. For a nonarchimedean local field and
   its quaternion division algebra D, the character chi composed with
   reduced norm transfers to the special representation
   sigma(chi|.|^(1/2),chi|.|^(-1/2)); twisting is compatible, and the
   local transfer is injective with special/cuspidal image. This is the
   local Jacquet–Langlands theorem, including residue characteristic two.
   It provides the division-side comparison without extending a
   square-free global isogeny statement to squared level. The full
   proof of Theorem 15.1 was not replayed; it is imported by citation.

3. Michele Fornea, *Plectic Heegner classes*,
   [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2).
   Targeted extraction inspected Section 2.1.2, Section 2.2 level and
   direct-system definitions, Proposition 2.9 with proof, Corollary 2.10,
   (22)–(23), Theorem 2.20 and Corollary 2.21 with proofs,
   Section 2.4 through Corollary 2.26 with proofs, Lemmas 3.2–3.6
   with proofs, Lemma 4.12 with proof, the paragraph defining (63),
   and Section 4.2.3/Corollary 4.19 with proof. Other construction,
   CM-cell and descent inputs are reused from steps 515/520/523/525/526.
   The source uses covariant Jacobian correspondences, pullback direct
   limits, completion, ordinary control, residual localization and
   diamond invariants. Corollary 2.21 explicitly uses normalized
   ordinary pushdowns to level one. Formula (63) follows that descent;
   tensoring with I alone is not a quotient to V_p(A).
   Corollary 4.19 explicitly asserts the good spherical eigenspace
   property. Its stated algebra excludes bad conductor primes, so it
   cannot be quoted as the requested tame-normalizer eigenidentity.

4. Gonzalez–Rotger, *Non-elliptic Shimura curves of genus one*,
   [author manuscript](https://web.mat.upc.edu/victor.rotger/docs/ShimuraGenusOne.pdf),
   Appendix pp.13–14, especially the square-free-N standing assumption
   immediately before Theorem 5.4 and the theorem's ramified-prime sign
   correction. Rechecked its precise scope. Reuse the step-518 reading
   of the local CM-conjugation proof cases; none covers the current
   completed tower comparison. Theorem 5.4 is a convention check in its
   stated scope, not an arbitrary-level input.

## Remaining specialization, not a theorem attributed to the sources

The new local results remove the earlier lack of a prime-power
newvector-sign source. They do not supply b_W=epsilon b as a quotation.
A later attempt must identify the actual W_v cosets in L126 with the
appropriate local operators, including division places and good places;
the exact tame conductor of the A representation must be checked.
At squared split level, substituting U_q's eigenvalue for the
Atkin–Lehner eigenvalue is not authorized.

The other load-bearing obligation is extending the geometric W action
through the actual coefficient construction. Fornea's defined physical
Hecke algebra does not list W as a generator. The intended check is
functoriality at finite levels, compatibility with pullbacks and the
normalized ordinary pushdowns, the auxiliary good-Hecke map in (22),
completion and localization, diamond invariants, and finally (63).
One must verify the A summand rather than assume that every tame
normalizer commutes with every bad U operator. A geometric degree-one
automorphism or a scalar on classical differentials alone does not
complete this chain. These are explicit mathematical specialization
obligations eligible for one bounded attempt, not missing inaccessible
theorem statements and not conclusions of this review.

The actual transformed moment has Phi(h_t^(-1)W), whereas the original
has Phi(h_t). Inversion of the complete conductor-one CM list and
representative changes must therefore be justified using the retained
complete-moment contract. Keep original n, list, kernel and W; do not
substitute a shallow trace or the failed full-Hecke fiber. No pointwise
pr_A is defined. The final eigenvalue must be normalized for covariant
right translation; no product of remembered signs is accepted here.

Continue if that chain yields the normalized scalar comparison and
descent, or a first precise failed hypothesis/map. Stop the proposed
scalar inference at such a failure; do not promote good-Hecke
eigenbehavior to all-operator equivariance. A failed bounded attempt
needs a materially new input or mechanism before repetition.

## Search, duplicates, access and limits

Queries included: “Atkin Lehner operator quaternionic Shimura curve
normalizer action newform square level newvector eigenvalue”;
“Casselman new vector Atkin Lehner local epsilon factor GL2 theorem”;
“Ralf Schmidt Some remarks local newforms GL2 pdf Atkin Lehner
eigenvalue”; and “Jacquet Langlands automorphic forms GL2 pdf trivial
representation division Steinberg theorem 15.1”. Search snippets are
discovery only. The exact primary passages above were then inspected.

Steps 518/521 and 523/525 are reused; the L126 audit is step 526.
The failure comparisons in ATTEMPTS/003/004/030/058/059 and L125 with
ATTEMPTS/060 remain as recorded in the earlier assessments. The present
operator differs from the failed full-fiber substitution and scalar
kernel-sign cancellation. Neither failure proves nonscalarity.

Casselman's original paper was inaccessible through the author archive
link and publisher preview; no claim is based on those previews.
Schmidt is an inspected primary replacement for the needed local
eigenvalue theorem. Its old math.unt.edu URL redirected unsuccessfully;
the author-hosted sites.math.unt.edu URL was readable through the web
tool despite shell DNS failure. Zhang's GL2 PDF exceeded the retrieval
limit and is not an input. Gee–Savitt Section 3, author PDF p.5, and
Rozensztajn (2015) Section 3.1, p.187, were inspected as sign leads;
their standing odd-prime settings are not used to cover q=2. The IAS
Jacquet–Langlands statement supplies that general local input.
Hein–Tornaria–Voight's search hit had mismatched cached numbering;
no theorem from it is imported. These optional leads do not block
the bounded specialization. No absence or originality claim follows.

Mathlib coverage of the complete action is not checked. No rational
Kummer class, nonvanishing, finite local membership, rank criterion or
BSD case follows. This review does not spend or reset mathematical
exploration usage. No lemmas, mathematical scripts, PROOF or DAG changed.
