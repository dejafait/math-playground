# Kim--Lee unshifted scope: source work1460

Literature-only source review, completed after the interim checkpoint below. The exact
entry target is assessment1459's DOI10.4134/JKMS.j210622 applicability
test at shift n=0 and unbounded degree. No lemma or mathematical script
is authorized. Main gap: L030--L032/C032a actual-Xi all-degree positivity.
A useful intermediate source result would count actual unshifted real
roots without an unpaid zero-location premise; initialization, signs and
overlap would remain independent obligations.

Read L018/L021 and C019j's definitions/source setup; actual positive
coefficients are gamma(j)=j!M_(2j)/(2j)!. Reused the November4
prescribed-primitive stop and actual-Jensen discovery assessment, and
source-notes1459. Existing unrelated notebook changes are preserved.

Primary author preprint retrieved: Kim--Lee,
https://arxiv.org/pdf/2105.05386v1 (12 May2021), four pages.
Its Theorems1--4 and the relevant derivative/finite-height proofs are
available; its published 2022 version is thirteen pages, so equivalence
of versions must not be assumed. Publisher DOI view was firewall-blocked.
Preprint Theorem1 bounds an eventual derivative threshold, not n=0.
Theorems3--4 and final remark give finite degree ceilings under a
zero-location premise up to height T. The published hypotheses and
essential proof cases are still being sought before final comparison.

Continuation/abandonment test: retain the lead only if its primary
conclusion applies at n=0 for unbounded degree under independently
established actual-Xi hypotheses. A positive derivative threshold, a
fixed finite-height ceiling or an unpaid root-location premise stops
automatic import. No inverse Rolle or prescribed-constant choice is
permitted. Full Mathlib coverage remains unchecked.

## Primary statements and proof cases inspected

The primary text actually read is **arXiv:2105.05386v1**, 12 May2021,
pp.1--4, also rendered at https://arxiv.org/html/2105.05386v1 .
The following is a compact hypothesis/quantifier extraction, not a reproof.
Write S={z:|Im(z)|<1/2}, f(z)=f_0(z^2) in the even case, and
J(g;d)(X)=sum_(j=0)^d binom(d,j)g^(j)(0)X^j.

- Theorem1, p.2: f transcendental real entire, order rho<2,
  Z(f) subset S; for every c>rho, N(f;d)=O(d^(c/2)); if f is even,
  also N(f_0;d)=O(d^(c/2)). Here N is the least eventual derivative
  threshold, not a nonreal-root count.
- Its proof, p.3, uses Theorem2's positive onset and
  n>=max{n_1,(d/4)^(c/2)} for f. The f_0 branch is stated analogously;
  that explicit f-bound is not asserted for f_0.
- Theorem3, p.2: real polynomials P,Q, delta>0,
  Z(P) subset {z:|Im(z)|<=delta|z|}, Q hyperbolic,
  deg(Q)<=delta^(-2) imply P(D)Q hyperbolic.
- Theorem4, pp.3--4: f even, transcendental real entire, order<2,
  T>=1/2, Z(f) subset {z in S:|Re(z)|>=T} union R;
  J(f^(n);d) is hyperbolic for every n>=0, d<=1+4T^2.
  The final f_0 remark gives d<=T^2(1+1/(4T^2))^2.
  Its proof uses convex-sector Gauss--Lucas, f_0' and z(f_0')^2,
  then even-derivative induction. Multiplicities are not excluded.

Theorem2 cites Kim1996, Proc.AMS124,819--830, Theorem2, and
J.Korean Math.Soc.33,657--667, Theorem1. Theorem3 cites Obreschkoff1961,
Acta Math.Acad.Sci.Hungar.12,175--184. Those original proofs were not
retrieved; this step is an applicability review, not an audit of them.
No precise published2022 theorem numbering or equivalence of versions is claimed.

## Actual-family convention and decision

The f used for the even branch must be L018's Xi, not C019j's
f(w)=xi(1/2+w). L021 and C019j give, by comparing their existing series,

    Xi_0(z)=F(-z),
    J(Xi_0^(n);d)(X)=(-1)^n J^{d,n}(-X),
    J^{d,n}(X)=sum_(j=0)^d binom(d,j)gamma(n+j)X^j.

Thus the source derivative index n for Xi_0 is exactly the coefficient
shift, and n=0 matches J_d after reflection. A derivative of Xi itself
does not have this same index convention. The reflection and nonzero
scalar preserve real-rootedness; L021's positive gamma values ensure
the actual polynomial has degree d and nonzero constant coefficient.
This is normalization matching, not a new sign or root-count theorem.

The relevant distinction is between an upper bound for N and a proof
that N=0. A positive upper bound does not disprove N=0, but cannot
certify it either. No backward-differentiation principle is available.
For a fixed verified height T, the displayed f_0 ceiling is finite.
Allowing T to grow with d requires a new zero-location input for each
such height; it cannot be supplied by changing a parameter in the
finite-height theorem. This stops the proposed automatic unshifted,
unbounded-degree import from the inspected preprint. It does not refute
the actual family, bound its remaining deficit, or ban Jensen methods.
No source here supplies simple roots or a sign margin.

For comparison, L832/C832a already exploit a rigorous finite-height
sector for ordinary-coefficient PF conclusions; their index and
factorials differ from this Jensen family. No PF-to-Jensen conversion
or enlargement is made. The November4 prescribed-primitive stop is
reused; L827's finite reciprocal-moment diagnostic remains closed.
The three mechanisms of source-notes1459 are not re-screened.

## Access evidence and exact unresolved coverage

Queries included the exact DOI with pdf/theorem/download/JAKO, exact
title plus 2022/pdf, and title constrained to the publisher/KoreaScience.
The DOI publisher view and DOI PDF endpoint returned the publisher's
web-firewall block. The publisher homepage and 2022 archive were
accessible, but the volume59/no.4 list and page775 PDF requests did not
yield article text. Crossref and an author-homepage fallback did not
yield the published text; the shell Crossref request failed DNS.
KoreaScience probes yielded no verified article and no evidence.
KCI supplies bibliographic/abstract evidence only. Search results for
an Oberwolfach report and secondary reviews were not adopted as theorem
evidence. No login, payment, API key or outside-notebook write was used.

The thirteen-page published article may contain additional hypotheses
or conclusions absent from this four-page preprint. Its precise main
theorems and essential proof cases remain **SOURCE_BLOCKED**. The
preprint's negative applicability result is established at source scope;
the stronger assertion that *no published theorem applies* is not.
This blocker is parked rather than scheduled for repeated retrieval.

## Continuation nomination only

One independently testable next source question concerns a sector
preserver with a finite exceptional divisor, instead of a derivative
shift or a coefficient-CZDS premise. A degree-dependent cone might
separate most of the actual divisor from exceptional factors; whether
any theorem controls root loss in this setting is **unreviewed**.
No such inequality is derived, assumed or approved here. The separate
nomination1460 requires comparison with the already recorded bulk
deficit and actual exceptional-divisor obligations before mathematics.
If it merely renames a finite-global-nonreal-zero premise or yields
only an existing weaker deficit, stop it. A creative proof target is
not yet justified. Mathlib matching coverage remains unchecked.
