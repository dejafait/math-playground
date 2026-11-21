# Corollary C033h: ordered Jordan-sign annihilator exclusion

## Hypotheses

Retain C032m's full actual-zero Gaussian normalization on W=[1,2]:

    z_rho=gamma_rho-i*delta_rho,
    G_s(z)=exp(-z^2/(4*s))/sqrt(4*pi*s),
    p_s(z)=(1/2)*sum_rho [G_s(z-z_rho)+G_s(z+z_rho)],
    R_s(w)=integral_0^infinity (p_s(x)-p_s(i*w))/(x^2+w^2) dx,
    E_s(w)=4*integral_0^w t*R_s(t) dt,
    O_s(w)=2*pi*integral_0^w p_s(i*t) dt,
    kappa_w(s)=exp(-E_s(w))*sinh(O_s(w)),
    J_eta(w)=integral_W kappa_w(s) deta(s).

The divisor includes every positive-ordinate nontrivial zero with
multiplicity and conjugation symmetry, gamma>14 and |delta|<1/2.
Use the removable values of R, the zero-normalized primitives, and
C032m's joint continuity and uniform entire-integral conclusions.
Retain all inherited fixed-v1 preprint and finite-height qualifications,
including V(3*10^12); this application does not reverify those sources.

Use C033g's audited, source-qualified sign conclusion. In particular
retain its corrected inclusive Bellotti--Wong v2 counting input and
its external certified low-zero input: exactly one simple positive
zero has ordinate <=20, that zero is real in the z-coordinate with
ordinate r0 in (14,15), and all remaining ordinates exceed20. Define

    A_s(y)=2*pi*integral_0^y p_s(x) dx,
    e_s(y)=E_s(i*y), k_s(y)=exp(-e_s(y))*sin(A_s(y)),
    f(s)=k_s(1/8), g(s)=k_s(1/4), r(s)=g(s)/f(s).

C033g gives f>0, g>0 and r'(s)<-1/2000 on W, with endpoint
regularity; in particular r is strictly decreasing on the whole
closed interval. No reality of the remaining divisor or RH is assumed.

Let eta be a real finite signed Borel measure on W. Assume that some
c in [1,2] and epsilon in {-1,1} satisfy

    (epsilon*eta)|_[1,c) >= 0,
    (epsilon*eta)|_(c,2] <= 0.                              (1)

These are inequalities of measures on all Borel subsets of the
indicated sets. The atom at c has arbitrary sign. Empty restrictions,
one-sign measures, atoms, infinite support and singular continuous
parts are allowed. No density, mass normalization, positive output
law or moment hypothesis is imposed.

## Conclusion

For every eta satisfying (1),

    integral_W f deta = integral_W g deta = 0
        implies eta=0.                                    (2)

Consequently J_eta identically zero on C implies eta=0 in this
ordered-sign class. Thus C032q's mass-one feasible measures, if any
exist, cannot satisfy (1), regardless of their output positivity.

This excludes only the stated sign-cut class. It does not decide
unrestricted signed cancellation, constant-span completeness,
positive output, exponential moments, unsmoothed Xi realization or
L030-L032/C032a all-degree positivity. No quantitative lower bound
in a measure norm is asserted. This is a local reproduction and
specialization of known ordered-law mathematics. Proof attempt1733
is complete below; separate audit1735 validates its qualified application.

## Proof

### 1. Imported measure theorems and source scope

Use the standard Jordan decomposition theorem in Richard F. Bass,
*Signed measures*, Chapter12, version4 November2011,
[Theorem12.8, printed p.97](https://webspace.science.uu.nl/~kraai101/SignedMEasures).
For a real finite signed Borel measure mu it gives unique mutually
singular positive measures mu^+, mu^- with mu=mu^+-mu^- and
|mu|=mu^++mu^-. Both parts are finite. The theorem and complete proof
were inspected in sources1542 and reused in source-notes1731/1732.
The source's signed-integration exercise is not imported as a proof.

Use Moshe Shaked and J. George Shanthikumar, *Stochastic Orders*,
Springer2007, Section1.A, pp.3-5 and8,
[chapter DOI 10.1007/978-0-387-34675-5_1](https://link.springer.com/chapter/10.1007/978-0-387-34675-5_1).
Usual stochastic order X<=_st Y means
Pr(X>t)<=Pr(Y>t) for every real t. Theorem1.A.1, p.5,
characterizes it by an ordered coupling; Theorem1.A.8, p.8, says
that if X<=_st Y and E[h(X)]=E[h(Y)] for a strictly increasing
function h, with both expectations finite, then X and Y have the
same distribution. We apply Theorem1.A.8, not a density-only variant.

The Note p.1, definitions and complete relevant proofs were inspected
in the [reproduced primary book text](https://www.slideshare.net/slideshow/stochastic-orders-1st-edition-moshe-shaked-j-george-shanthikumar-eds/279576121)
in source review1731 and checked for access1732. Publisher definition
pages were separately inspected1731; the full publisher chapter was
not available and no scan-image verification is claimed. These access
qualifications are retained. The source covers arbitrary real laws;
it supplies no theorem about this kernel. No general coupling or
equality theorem is reproved here.

Assessment1730/1731 covers precisely the specialization (1), including
atoms. Scoped duplicate and failure checks retain stops1534/1536/1711,
park1725 and closure1730. The proof uses C033g's established sign;
it does not repeat its Gaussian estimate or claim new mathematics
beyond the cited general results and this qualified application.

### 2. The two real tests are kernel evaluations

Conjugation symmetry makes p_s real on the real axis, and its
definition makes it even. The real even entire function R_s and
its primitive E_s therefore have real even Taylor coefficients;
in particular e_s(y) is real for real y. Equivalently these are
the real functions already used in C033g. Substituting t=i*x in
the straight-segment primitive for O and using p_s(-x)=p_s(x) gives

    O_s(i*y)=i*2*pi*integral_0^y p_s(x) dx=i*A_s(y).

It follows exactly, with no omitted factor or conjugation, that

    kappa_(i*y)(s)=i*exp(-e_s(y))*sin(A_s(y))=i*k_s(y).       (3)

C032m gives continuous bounded width sections at these fixed
arguments. Since |eta|(W)<infinity, (3) is integrable against each
Jordan part and may be integrated and its imaginary part taken.
Thus

    J_eta(i/8)=i*integral_W f deta,
    J_eta(i/4)=i*integral_W g deta.                         (4)

No infinite series is interchanged here. In particular entire
annihilation implies the two real zero integrals in (2); the
converse for unrestricted signed measures is not asserted.

### 3. Orientation, support and the cut atom

Put mu=epsilon*eta. The two zero integrals are unchanged. Apply
Jordan decomposition to mu. On [1,c), the restrictions of mu^+
and mu^- remain mutually singular and their difference is the
nonnegative measure mu|_[1,c). Uniqueness of Jordan decomposition,
compared with (mu|_[1,c),0), gives mu^-([1,c))=0. Applying the
same reasoning to -mu on (c,2] gives mu^+((c,2])=0. Therefore

    mu^+ is carried by [1,c],
    mu^- is carried by [c,2].                              (5)

At the singleton {c}, mutual singularity and the difference formula
give

    mu^+({c})=max(mu({c}),0),
    mu^-({c})=max(-mu({c}),0).                             (6)

Thus the atom goes to its actual sign; it is never counted in both
parts. These conclusions concern measures, not pointwise signs of
a density, and include singular continuous restrictions.

### 4. Faithful positive weighting and the zero-mass case

By C032m/C033g, f is continuous and strictly positive on compact W.
Hence there are finite constants 0<m<=f(s)<=M on W. Define

    lambda_+(B)=integral_B f dmu^+,
    lambda_-(B)=integral_B f dmu^-                         (7)

for Borel B. These are finite positive measures with the carriers
in (5). They remain mutually singular: a Borel Hahn partition for
mu^+,mu^- also carries lambda_+,lambda_- on disjoint parts.
Moreover lambda_+(B)>=m*mu^+(B) and similarly for the minus part.

The first zero integral in (2) says

    lambda_+(W)=lambda_-(W)=q.                            (8)

If q=0, the lower bounds in (7) give mu^+=mu^-=0, and eta=0.
This handles any initially vanishing Jordan part and all one-sign
measures, before division. If eta is nonzero, (8) therefore forces
q>0, and both

    P_+=lambda_+/q, P_-=lambda_-/q                        (9)

are Borel probability laws on W, viewed also as laws on R by zero
extension. They are mutually singular and have the carriers (5).

### 5. Order and the finite strict-test expectation

For every real t<c, P_-((t,infinity))=1, so
P_+((t,infinity))<=P_-((t,infinity)). For every t>=c,
P_+((t,infinity))=0, and the same inequality holds. At t=c this
uses the open tail, so an atom at the cut creates no exception.
These two cases exhaust R and prove P_+<=_st P_-.

The continuous function r=g/f is bounded and strictly decreasing
on W. Set h=-r there and extend it to all real x by

    h(x)=h(1)+(x-1), x<1,
    h(x)=-r(x),      1<=x<=2,
    h(x)=h(2)+(x-2), x>2.                                 (10)

The extension is continuous and strictly increasing: it has slope1
on each exterior interval, is strictly increasing on W, and its
values meet at the endpoints. Both laws are carried by W, so their
h-expectations are finite despite the extension being unbounded.
Using r*f=g in (7)-(9), the second zero integral in (2) gives

    integral h dP_+=-(1/q)*integral g dmu^+
                  =-(1/q)*integral g dmu^-
                  =integral h dP_-.                      (11)

All four integrals are finite: f,g,r are bounded on W and the
original Jordan parts have finite mass. Theorem1.A.8 now applies
with the order just proved and the strictly increasing test (10).
It yields P_+=P_- as Borel probability measures on R.

### 6. Equality, endpoint cases and the conclusion

Let H be a Borel carrier of mu^+ disjoint in measure from mu^-,
so mu^+(W\H)=mu^-(H)=0. Positive weighting and normalization give
P_+(H)=1 and P_-(H)=0, contradicting equality. Hence the nonzero
case q>0 is impossible and (2) follows.

There is no exceptional common atom: by (5), equal laws would be
carried by [1,c] intersect [c,2]={c}, hence both would be the unit
atom there, in conflict with (6) and mutual singularity. If c=1,
mu^+ is carried by {1}; if its mass vanishes, section4 applies,
and otherwise the same equality contradiction applies. If c=2,
mu^- is carried by {2} and the identical dichotomy applies. Thus
both endpoint cuts and either sign or absence of the cut atom are
included, without requiring mass away from c.

By (4), J_eta=0 implies (2) and hence eta=0. C032q's feasible
class requires eta(W)=1 and J_eta=0, so none of its members can
satisfy (1). Output positivity is not used to obtain this necessary
restriction. No conclusion about measures outside (1), their
existence or their outputs follows. This completes the bounded
application. The separate review is recorded below.

### 7. Application audit1735, 19 November 2026

Verdict: (2) and its two stated consequences pass the bounded audit
under exactly the hypotheses above. Reuse assessment1733, approved1734,
and the complete relevant general-law source coverage in
source-notes1731/1732. This verifies the local specialization, not a
new measure theorem or a fresh verification of the analytic sources.
No hypothesis, bound or conclusion is strengthened.

The input comparison retains C032m's full signed-integral interface
and C033g's audited conclusion, including conjugation, multiplicities,
the corrected inclusive count, first simple real zero and separation,
fixed-v1 qualifications and V(3*10^12). No positivity of the remaining
Gaussian summands or reality of the remaining zeros is used. Strict
decrease of g/f on the closed width interval follows from C033g's
qualified derivative margin and endpoint regularity. Its numerical
proof is not replayed in this application audit.

For (3), substituting t=i*x gives dt=i*dx and i*t=-x.
Evenness of p therefore gives O(i*y)=i*A(y), while sinh(i*A)=i*sin A.
Reality of e follows from the real even entire coefficients. Thus the
factor in both formulas (4) is +i. C032m section4 bounds these fixed
width sections against each finite Jordan part; neither division by
a zero kernel nor interchange of a conditionally convergent sum is
present. Only entire annihilation implies these two zero integrals;
the reverse implication has not been used.

On each open side of the cut, uniqueness of the restricted Jordan
decomposition gives exactly (5). Its restrictions remain mutually
singular. The arbitrary cut atom has the allocation (6); adding c
to both carriers does not assign its mass to both measures. This
argument also applies when either open side is empty or consists
only of a singular continuous restriction.

Continuity and strict positivity of f give a strictly positive compact
minimum m. Weighting is consequently finite and faithful, preserves
the disjoint Borel carriers and bounds the original masses by the
weighted masses divided by m. Equation (8) follows from the first
zero integral with the correct orientation. If either weighted mass
is zero, both original parts vanish. Normalization (9) occurs only
after the nonzero case has forced q>0.

For t<c the right-carried law has open-tail mass one; for t>=c the
left-carried law has open-tail mass zero. These are precisely the
inequalities P_+<=_st P_-, including t=c and the endpoint cuts c=1,2.
Because r decreases, the required increasing test is -r. Extension
(10) is strictly increasing across both joining points, and compact
carriers make its expectations finite. The identity g=r*f proves
(11) against each positive part. Hence all hypotheses of the cited
Theorem1.A.8 hold for general Borel laws, without a density assumption.
Its equality conclusion contradicts P_+(H)=1, P_-(H)=0 for the same
Hahn carrier H. Equal laws concentrated at c would give the same
contradiction, so the common-carrier singleton is not an exception.

Finally eta(W)=1 in C032q rules out eta=0; that is the only additional
condition needed for its necessary exclusion. No assumption about
the output law enters this proof. The audit finds no failed case or
missing applicability premise in the approved scope. Unrestricted
oscillation, constant-span closure, positive outputs, moments and
actual-Xi realization remain unresolved. This is local validation of
a known-theorem specialization, not progress beyond the sources checked.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. Jordan decomposition, weighted finite measures and stochastic
order would be supporting inputs; neither a full formal version of
this specialization nor formal coverage of C033g's qualified divisor
and source inputs is asserted. Unknown coverage is not evidence of
absence.
