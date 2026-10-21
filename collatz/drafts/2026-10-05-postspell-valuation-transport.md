# Shifted-valuation transport — completed checkpoint

Approved target and scope: reuse the unchanged EXPLORE assessment
`drafts/literature/2026-10-05-postspell-inverse-to-height.md`.
Main gap: universal eventual descent. The intermediate objective is a
uniform divergent lower bound on roots of exact-tail postspell chains;
this would exclude infinite chains in this alphabet, leaving entry,
other tails and compensation unresolved.

The single test is transport of V(x)=v_2(11x+23), using L020's affine
identities and finite coding, L021's actual concatenation and L023's
preceding-word qualification. No least-root filters are imposed.
Stop a V-budget if replenishment is unbounded on guarded extendible
chains; this does not refute another root-height bound.

Work saved before witness verification: with y=B^J(n) and
z=O^H(y)=4m, exactness gives y+1=2^H u with u odd. Since H>=3,
v_2(11y+23)=v_2(11*2^H*u+12)=2. L020 then gives V(n)=4J+2.
Also 11m+23=(11*3^H*u+81)/4. This expression may have large
valuation. Imported finite coding of W(2,3) W(2,3) W(R,3), followed
by an O endpoint guard, and CRT with residue 20 supplies actual
positive chains for every R>=2. The middle word has an actual
preceding word; its boundary valuations are 10 and 4R+2.

Completed: the canonical proof and all qualifications are in
[L024](../lemmas/L024-postspell-shifted-valuation-replenishment.md).
The full three-word replay is `scripts/postspell-valuation/result.json`;
all checks pass and its complete states and per-word evidence were
inspected. The middle word violates boundary nonincrease, 14>10.
The proof gives unbounded replenishment and rules out any finite depth
bound depending only on the initial V, without ruling out a full
root-height bound. Outcome: NEGATIVE; stop this valuation-budget
mechanism in Attempt 013. The next proposed mechanism is bounded
coalescence on the surviving cylinder; it is REVIEW_REQUIRED, with no
new mathematical derivation or approval in this step.
