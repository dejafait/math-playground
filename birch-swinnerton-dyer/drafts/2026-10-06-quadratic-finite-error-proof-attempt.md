# Conditional quadratic enclosure — saved working reasoning

Approved target: the exact TARGET in
drafts/literature/2026-10-06-quadratic-finite-error-specialization.md.
This draft preserves the reasoning saved before the canonical proof was written.
Completed disposition: L027 now contains the full conditional proof; this
working checkpoint is retained, and its former obligations are not additional
claims or current instructions.

Main gap: rank equals complex analytic order in order at least two.
Intermediate target: with certified exact normalization, all-level symbol
denominator C and unit-root residual precision M, prove
v_p(a_2-b) >= min(n-1-C,M-C). Its possible use is L026's independent
coefficient premise. No actual coefficient or uniform production is supplied.

Working argument: every ordinary measure summand has valuation >= -C,
so every coefficient of every P_k has that bound. Import
Stein--Wuthrich Propositions 3.1/3.5 (Math. Comp. 82 (2013),
pp. 1763--1765). Since binomial(p^(k-1),1) and
binomial(p^(k-1),2) both have valuation k-1 for p>=5, adjacent
quadratic errors are >= k-1-C. Finite telescoping and a closed
p-adic lattice should yield the tail >= n-1-C.

Conrad's Hensel Theorem 4.1 applies to X^2-a_p X+p at u:
the derivative is a_p modulo p, a unit, and the residual valuation
is >= M>=1. It should give v_p(alpha-u)>=M. Differences of inverse
unit powers have valuation >=M for any exponent, hence the finite
quadratic root-replacement error should be >=M-C.

Remaining obligations to finish explicitly: define exact integer
Teichmuller residues and finite symbol arguments; check their simple-root
certification; establish all coefficient bounds without sample-only C;
justify the closed-lattice limit; retain every exponent j in taking
the exact binomial degree-two coefficient; match the primitive series
and fixed coordinate before invoking L004. Continue only if each
obligation holds under the approved inputs. N<=v_p(b) gives no
nonvanishing conclusion. Rational membership, finite Sha and complex
order comparison remain independent gaps. ATTEMPTS/021 is unchanged.
