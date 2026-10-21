# Global eleven-adic projection — bounded attempt

Approved target: Determine the image of K(S,5) under the three eleven-adic valuations modulo five and intersect it with L044's two-vector set.

Prior assessment: drafts/literature/2026-10-10-global-eleven-valuation-image.md,
SPECIALIZE, saved before invocation. Main gap: global emptiness of L032's
54a1 branch, independently of four other twists and infinitely many signatures.
Intermediate target: the exact projection, retaining every prime above five.
Downstream test: empty intersection obstructs this branch; one survivor
narrows it; both survivors retire this projection as an exclusion test.

Inputs read: L033's complete finite-class proof; L041's complete local
algebra and ordered places; L044's statement and source interface; its
independent audit recorded in history/111. ATTEMPTS/008,009,012 record
different exhausted tests, not a proof that this projection fails.
No cross-notebook input. Ready source coverage is reused without browsing.

Working plan saved before arithmetic: prove the ideal criterion using the
assessed principal-ideal/class sequence, then test exact small elements in
Z[k] whose nonzero absolute norm has support only at five and eleven.
Such an element is integral in the maximal order and has no prime-ideal
support elsewhere, without asserting that Z[k] is maximal. Complete exact
norms and local valuations are required. A bounded failed search proves
neither absence nor exactness. No uncertified class data, GRH, rank, Sha,
or Selmer/point-class equality will be used.

Initial unfinished criterion: if P1,P2,P3 are L041's global primes over eleven
and Q ranges over all primes above five, a vector d is attainable exactly
when sum d_i[P_i] belongs to 5 Cl(K)+span_Z{[Q]}. Necessity factors
(alpha) with arbitrary exponents at Q and exponents divisible by five
outside S; sufficiency must produce a principal fractional ideal after
choosing the free Q-exponents and a fifth power of a fractional ideal.
This still needs its complete proof and, absent enough exact witnesses,
certified field-specific ideal data. No projection was claimed at that stage.

## Completed bounded step

The full criterion and its sufficiency are now proved in
[L045](../lemmas/L045-global-eleven-projection-ideal-criterion.md).
The principal ideal (11)=P1 P2 P3^10 reduces the projection to a
two-class kernel in the ordinary class group modulo five and all
five-prime classes. The local intersection is both L044 vectors or
empty; a single survivor cannot occur. Which alternative holds remains
unknown, as does the numerical projected image. This is REPRODUCTION
of assessed ideal methods, not a newly discovered general theorem.

The exact search saved in scripts/global-eleven-valuation/small-norm-certificate.json
contains every norm for 103,532 elements. No supported-norm witness was
found. All three checks pass; the eight independent determinant
comparisons, exact bounds and empty hit list were inspected in full.
The script's norm identities and completeness of its finite boxes are
justified in L045. This search is incomplete for K(S,5), supplies no
class-group certificate and cannot establish absence.

The useful partial input is the proved criterion and dichotomy, not an
evaluated image. Park dependent ideal-class arithmetic and this bounded
witness search until materially new certified data or a specific new
construction is available. The next proposed mechanism concerns the
fourth-power condition at two; it is independently local and remains
REVIEW_REQUIRED. No two-adic calculation or new theorem is undertaken
in this step.
