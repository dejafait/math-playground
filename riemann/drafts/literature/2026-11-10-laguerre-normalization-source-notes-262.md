# Laguerre first correction: source comparison, step262

Literature-only review, 10 November 2026. No endpoint nonvanishing
theorem is proved here. L990 and its diagnostic are preserved.

## Sources actually inspected

- NIST DLMF, live version1.2.8 (15 September2026),
  [18.15.17–20](https://dlmf.nist.gov/18.15#iv), including the
  fixed-alpha/fixed-M hypotheses and uniformity statement immediately
  after18.15.19. The [errata index](https://dlmf.nist.gov/errata/)
  searches for18.15.19 and18.15.20 found no correction to these
  equations. This is an access/search report, not proof of correctness.
- A. Gil, J. Segura and N. M. Temme, *Efficient computation of
  Laguerre polynomials*, Computer Physics Communications210 (2017),
  124–131, DOI[10.1016/j.cpc.2016.09.002](https://doi.org/10.1016/j.cpc.2016.09.002).
  Inspected [arXiv1609.00829v1, section2.1.3, equations20–34,
  manuscript pp.6–8](https://arxiv.org/html/1609.00829v1#S2.SS1.SSS3),
  especially20–25 and the parity/recursive construction32–33.
  The PDF endpoint labels itself v1/3September2016 but its displayed
  preprint footer says25June2018; cite the equation numbers and this
  retrieved version, without inferring its revision history.
- The same authors, *Asymptotic approximations to the nodes and
  weights of Gauss–Hermite and Gauss–Laguerre quadratures*,
  [arXiv1709.09656v1, 27September2017](https://arxiv.org/html/1709.09656v1#S3.SS3),
  section3.3, equations77–87 (manuscript pp.20–21), and section3.3.1,
  equations91–98 (pp.21–22). Read the integral, parameter convention,
  uniform series statement, explicit first coefficient and parity
  construction. The two papers share authors and cite Frenzen–Wong;
  they are corroborating presentations, not independent proofs.
- [DLMF10.17.1–3 and section10.17(iii)](https://dlmf.nist.gov/10.17#iii):
  fixed Bessel order, positive real argument, and the separate
  cosine/sine truncation restrictions. Also inspected
  [DLMF18.9.1/Table18.9.1](https://dlmf.nist.gov/18.9#T1) for the
  diagnostic's polynomial convention.
- C. L. Frenzen and R. Wong, *Uniform asymptotic expansions of
  Laguerre polynomials*, SIAM J. Math. Anal.19(5) (1988),1232–1248,
  DOI[10.1137/0519087](https://epubs.siam.org/doi/10.1137/0519087).
  Both publisher PDF/epdf routes exposed only abstract/access pages.
  Its original coefficient formulas and detailed error proof remain
  UNREAD. N. M. Temme, *Asymptotic estimates for Laguerre
  polynomials*, ZAMP41 (1990),114–126,
  [section2.1/equation2.1, pp.115–116](https://ir.cwi.nl/pub/2379/2379D.pdf),
  was inspected: it summarizes the fixed-alpha>-1 Bessel expansion,
  the coefficient recursion and existence of remainder order bounds,
  but does not print the needed explicit first coefficient.

## Exact normalization dictionary and discrepancy

This is comparison of the displayed source formulas, not a derivation
of a new Laguerre expansion. Write N for DLMF's nu, v for GST's nu,
and t for the scaled argument. In the common positive bulk domain:

    N=4n+2alpha+2=2v, v=2n+alpha+1,
    b=xi_DLMF(t)=[sqrt(t-t^2)+arcsin(sqrt(t))]/2,
    zeta_GST=b^2, q=t/(1-t),
    P=exp(N*t/2)/[2^alpha*t^(alpha/2+1/4)*(1-t)^(1/4)].

DLMF18.15.19 has leading term P*sqrt(b)*J_alpha(N*b).
Denote its printed coefficient18.15.20 by D(t):

    D(t)=-1/2*[(1-4alpha^2)/8
           +b/sqrt(q)*((4alpha^2-1)/8+q/4+5q^2/24)].

GST2016 equation25 prints

    C(t)=(1-4alpha^2)/16
           +b/(8sqrt(q))*[(4alpha^2-1)/2+q+5q^2/6].

The terms match with C=-D. GST2016 equations20–23 have the same
leading prefactor, since chi(zeta)/zeta^(alpha/2)
=sqrt(b)/[t^(alpha/2+1/4)*(1-t)^(1/4)]. Their next Bessel term is

    -P*sqrt(b)*J_(alpha+1)(N*b)*C(t)/(v*b)
      =P*J_(alpha+1)(N*b)*2D(t)/(N*sqrt(b)).

DLMF18.15.19 instead prints D(t)/(N*sqrt(b)). Thus these displayed
formulas have a factor2 incompatibility at the first correction;
the scaling dictionary does not remove it. GST2017 equations81–87
agree with GST2016: its B_1 equals C and its B-series starts at1/v.
Equation86 prints an undefined a in the alpha-dependent coefficient;
the explicit alpha convention is supplied by GST2016 equation25.
No higher explicit coefficient or potentially mistyped recursive
identity is imported from these displays.

The diagnostic's p_0=1, p_1=3-u and
(k+1)p_(k+1)=(2k+3-u)p_k-(k+2)p_(k-1) agree with the standard
Laguerre normalization at alpha=2. N=4n+6, b=xi_DLMF and the
displayed amplitude in step261 also match that normalization.
DLMF10.17.1–3 give the J_2 sine coefficient -15/(8z).
Consequently there is a genuine displayed-source incompatibility,
not evidence here of an incorrect recurrence or a missing polynomial
normalization factor in the saved script. This does not certify every
operation in that script or determine the endpoint phase coefficients.

## Remainder contract and permitted later use

GST2017 equation82 states uniform asymptotic expansions for
rho<=1-delta, with delta fixed in(0,1); equations81,83–84 fix
the prefactor and argument. Use only fixed alpha=2 and a compact
positive subinterval of(0,1), not the negative-argument or turning
point cases. In its coefficient convention the Poincare contract is
A=1+O(v^-2), B=C/v+O(v^-3), uniformly on that compact interval.
The coefficient construction uses analytic functions near the two
saddles and parity; no differentiation of an asymptotic remainder
is licensed. The source's later *assumed* expansions of individual
zeros are not inputs. Finite-precision accuracy tables are not bounds.

This accessible primary statement supplies an alternate source for
the first correction and its required asymptotic control. A later
specialization must use this contract directly, retain the N=2v
conversion, bound the smooth coefficient terms on a specified compact
interval, and combine it with the real-positive Bessel remainders.
For order2 the first cosine and sine truncations satisfy the
DLMF10.17(iii) conditions with ell=1; for order3 use enough terms
(ell=2 for the cosine bound) before dropping bounded higher terms.
No effective onset or numerical remainder constant is imported.

Do not attach DLMF18.15.19's remainder to a silently replaced B_0.
The present review documents which published contract can be used;
it neither adjudicates the original Frenzen–Wong text nor announces
an official DLMF erratum. The original-source access block is no
longer essential for this restricted alternative specialization.
The proposed endpoint gamma values and integer-norm limit in
step261 still require mathematical proof from the chosen contract.

## Searches, overlap and decision

Queries included Frenzen–Wong1988 Laguerre B_0/PDF, DLMF18.15.20
factor2/correction, and Gil–Segura–Temme Laguerre Bessel expansions.
Search snippets were leads only. The exact local step258/259 source
assessments and step261 working record were searched; no earlier
normalization resolution was found in that scoped set. Their
Christoffel/exterior comparison and steps233/235/244 scoped failures
are reused, not reopened. No novelty is inferred from searches.

The literal single-D(t) second-order branch is not an approved input.
Use the GST presentation for one later REPRODUCTION specialization;
derive no corrected endpoint formula or degeneracy exclusion in this
literature turn. Continue only if an additive uniform second-order
endpoint bound is justified and actually rules out the exact L990
conditions; an unresolved error or a surviving degeneracy leaves
cofinite definition open. Full matching Mathlib coverage is unchecked.
L990's first-order result is not audited or revoked here. Actual-Xi
positivity, realization, other zeros, the prime-power compensator,
original B_n/L984(H) transfer and both complements remain open.
