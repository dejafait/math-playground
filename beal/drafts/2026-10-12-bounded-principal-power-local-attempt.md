# Bounded principal-power attempt: local exact backend

The approved target is the unchanged ten-exponent, at-most-1,440 candidate
list in drafts/literature/2026-10-12-bounded-principal-power-test.md
(SPECIALIZE before invocation). Main gap: primitive integer emptiness in
remaining Beal signatures, here the 54a1 ordered (3,4,11) branch.
Intermediate target: literal beta R=J^h with gcd(h,5)=1, then a verified
L058 identity. Downstream use: u=0 in audited L045 and survival of both
L044 valuation vectors, without global-point or integer-lifting claims.
Stop at the fixed list or an implementation defect. Finite failure is
not a nonprincipality or class-nonvanishing certificate.

Inputs: audited L058, L033's field and power basis, L041's complete ordered
eleven places and audited L045 (retaining L044). No cross-notebook input.
Prior failures ATTEMPTS/013,025,026 were inspected narrowly. No duplicate
witness is recorded. The SymPy provisioning command failed at DNS access;
its installation failure is an implementation observation, not mathematics.

Work in progress: implement the already-assessed exact lattice operations
with Python integers/Fraction. Basis compression is accepted only with
both complete integer inclusion matrices. Lattice reduction is candidate
generation only: check its integer unimodular transformation, its exact
Gram-Schmidt size/Lovasz conditions, and the whole basis lattice. This is
an implementation of the covered interface, not a new general theorem,
a different mathematical target or an expansion of its candidate scope.
Write full evidence before interpreting any candidate. If successful,
verify inverse, conditional Bezout specialization and entire L058 identity;
otherwise preserve all rejections. Principal-power existence, arbitrary
prime-five freedom, units, other places, global points and integer lifting
are still unresolved. General source locators are in the reused assessment;
full matching and supporting Mathlib coverage remain not checked.

## Completed computation and verification

The local backend ran the original bounded scope to completion. The full
certificate is scripts/power-order-principal-power/power-test-certificate.json;
the independent replay report is
scripts/power-order-principal-power/power-test-verification.json.
Reproduce with:

    python3 scripts/power-order-principal-power/test_powers.py
    python3 scripts/power-order-principal-power/verify_powers.py

All twelve consecutive powers needed to reach h=12 have rank twelve,
index 11^h and verified k-stability. J's full generators are [11I|T-8I].
Each subsequent product uses all 144 pairwise basis products. Both integer
inclusion matrices are saved for each compression and independently
verified against freshly recomputed products using the full defining
polynomial. No maximal-order closure or saturation is inserted.

For each of the ten approved exponents, exact reduction at delta=3/4
has a saved integer transformation and integer inverse; determinant is
+/-1, both basis equations hold, and independently recomputed complete
Gram-Schmidt data satisfy every size and Lovasz condition. This replaces
the unavailable software implementation while retaining the assessed
lattice-reduction requirements. No shortest-generator guarantee is used.
The known column-module interface and its two-inclusion alternative are
cited in canonical L058; the reused literature assessment supplies the
precise LLL documentation. No general lattice theorem is reproved.

All 144 prescribed candidates per exponent, 1,440 total, are checked.
For each beta the certificate stores its twelve coordinates and an
integer matrix C with M_beta=B_h C, where B_h is the certified basis of
J^h. The independent verifier reconstructs M_beta by convolution and
monic reduction and checks every entry of this inclusion. Each exact
absolute determinant of C exceeds one. Thus the included full-rank
principal lattice is a proper sublattice: a reverse integer inclusion
would yield an integer inverse of C and force determinant +/-1.
This is a rejection using a verified inclusion, not acceptance based on
a norm or covolume alone. The smallest sublattice index over the entire
list is 25,079 (h=1), against required index one. Complete per-exponent
indices and every matrix are retained, not inferred from a preview.

The independent verifier imports no generation code, reconstructs all
products and candidates, uses rational Gaussian determinants rather than
the generator's integer Bareiss routine, and processes the entire saved
certificate. It passes with no failures: 12/12 powers, 10/10 reductions,
1,440/1,440 candidates, zero equalities. Its 222,706 assertions include
routine monic-reduction and dimension checks; this count is not a measure
of mathematical advance. No principal relation was obtained, so no
inverse or Bezout construction is invoked and L058 identity is NOT_RUN.

Outcome: EXPLORATION / REPRODUCTION. Backend repair enabled the actual
bounded test but supplies no new ideal-class input. Finite failure cannot
show nonprincipality, nonzero u, a class-order bound, branch emptiness or
an integer solution. L058 and L045 remain unchanged; no new lemma,
DAG edge or PROOF assembly change is warranted. Park the exhausted fixed
candidate list (ATTEMPTS/027), preserving ATTEMPTS/013,025,026. Do not
simply enlarge its h or coefficient list. A proposed mixed-prime
power-order certificate would use independent prime-five freedom omitted
here, but its local ideal identification and quotient specialization are
unassessed. The sole continuation is its separate literature assessment;
no mixed-prime mathematics or search has been performed in this turn.
