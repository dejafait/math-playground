# Rational-factor attempt checkpoint

Target: Determine whether L093's coefficient-one algebra can have a rational direct factor for a positive primitive solution.
Prior EXPLORE coverage: drafts/literature/2026-10-18-ordered-three-five-eleven-rational-factor.md.

Main gap: global algebra elimination and integer lifting. Test: reduced root t=m/n,
keeping both phi(t)=s and 1−phi(t)=1−s. A finite exact power-twist
reduction is a continuation threshold; an unbounded search is not.

Working calculation (not yet audited): Q=3m²+mn+n², L=n−5m.
B^5 n^11=C^11 Q^5 L. Primitivity restricts each v_p(s) to
5k, 0, or −11k, and v_p(1−s) simultaneously. The proposed conclusion
is n=C or n=5C, with gcd(C,15)=1. At 3, a denominator valuation
one or at least two seems incompatible with the permitted valuations;
at 5, only denominator valuation one survives, with v5(L)>=11.
Next check: full complementary polynomial, exceptional valuations,
and exact finite systems. No signature exclusion is claimed.

Completed: the full argument and both converses are canonical in L095.
Two finite power-twist systems were obtained, with gcd(C,15)=1 and
coprimality conditions proved. Thirteen exact checks passed. No system
emptiness or signature exclusion was obtained. The next target is a
separate critical audit; its coverage remains REVIEW_REQUIRED.
