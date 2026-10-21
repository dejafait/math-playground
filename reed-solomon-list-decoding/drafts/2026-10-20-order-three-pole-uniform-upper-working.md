# Order-three-pole uniform upper: working record

2026-10-20, step 370. The prior SPECIALIZE assessment and supervisor's
gate approve exactly the uniform upper-certificate test for L099.
Main gap: arbitrary-center 67/68 safety and the 955–957 bracket.
Intermediate target: cap every L099 fiber below T=65537^28/2^128.
Downstream use: exclude this family as an unsafe-index-957 witness only.
Continue the family exclusion if the rigorously justified cap is <=T;
otherwise park this certificate without a lower-fiber conclusion.

Inputs read: complete audited L099, C012a's subgroup/field facts,
L001's list model/root argument, foundations/01–02 and the completed
phase review. ATTEMPTS/083 stops averaging only; ATTEMPTS/007–008
are different residual-energy diagnostics. No duplicate upper certificate
was found in these scoped inputs. No cross-notebook input is used.

Initial calculation, not yet a proof: the truncated logarithm identifies
units modulo X^3 with E^* times two additive E coordinates (2 invertible).
Its constant-H subgroup has nQ² characters. A character nontrivial on
the additive part remains so at powers 1,...,67, since 67<Q. Extend its
constant-H character to E^* and average over the 64 annihilator twists.
Li–Wan Lemma 4.1 should bound every complete degree-one sum by
2 sqrt(Q)<513. The absolute weighted sieve then suggests error
binomial(579,67). Constant-only characters need exact treatment: a
nonprincipal order d divides 1024; its cycle sums vanish unless d
divides the cycle length, and d cannot divide 67. Thus their entire
67-subset character sums should vanish. Candidate cap:
binomial(1024,67)/(1024 Q²)+(1-Q^(-2))*binomial(579,67).
Initial exact arithmetic gives cap/T about 0.00157179010335, below 1.
Group normalization, signs, all powers and sieve factorial still need
full symbolic justification and a saved arithmetic certificate.

Completion is recorded in L100 and its full certificate. The bound above
is proved with error E=binomial(579,67), and the cap ratio lies strictly
in (1571790,1571791)/10^9. All 234 constructor checks and 214 independent
integer reconstruction checks pass. No character estimate is reproved.
The same proof gives a two-sided uniform discrepancy estimate; the
reported conclusion is only the approved family upper bound. Exact
cycle coefficients and small-example root/logarithm and extension
checks use no floating point. A separate critical
audit is proposed with REVIEW_REQUIRED coverage; no audit is performed
in this invocation. The finite RS bracket remains 955–957.
