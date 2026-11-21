# Corollary 947a: one simple zero of the fixed tilted primitive on the compact interval

## Hypotheses

Use precisely L938's real continuous density v on [0,infinity), with
its 34 signed rows, twelve labelled factors, factorials and retained
M_0^12 normalization. Put a=1/4, b=4 and, as in L947, define

    U(E)=U_(1/10)(E)=integral_0^E exp(t/10)v(t)dt.

The letter b here denotes the right energy endpoint, not the tilt.
Use L946's conclusion that every zero c of v in the closed interval
[a,b] has a two-sided derivative v'(c)>0. Its actual differentiation
scope is inherited from C944a through L946, not from differentiating
a numerical error inequality. Use L947's strict inequalities

    U(a)<0<U(b).                                                   (1)

Both numerical inputs retain their stated execution contracts:
L938's unchanged degree256 polynomial, 257 nodes, theta cutoff8,
precision200 and grid10^-120; directed Decimal, exponential and pi
inclusions; exact-integer implementation trust; and the reused step50
identity and step75 audit. L946 has its step78 conceptual audit.
L947's numerical implementation has the independent step85 audit.
This corollary does not strengthen either certificate.
No global convexity, finite-zero-set, contact, parameter-sign,
realization or RH premise is assumed.

## Conclusion

Subject to these inherited contracts and inputs, U has exactly one
zero r in (1/4,4), and

    U'(r)=exp(r/10)v(r)>0.                                        (2)

In particular it is a simple zero, where simplicity means a nonzero
first derivative of this differentiable real function. This is an
ordinary local specialization of standard calculus, not a new general
zero-count theorem. It supplies no global count, effective head/tail
join, determinant parameter signs, contact exclusion, other-degree
claim or resolution of all-degree Xi mixed positivity. The inference
below is written out; the independent combined input/inference audit
is recorded below under the same qualifications.

## Proof

### Standard inputs and the exact derivative

Import Jiri Lebl, *Basic Analysis I: Introduction to Real Analysis,
Volume I*, author-hosted HTML with the displayed theorem numbers
inspected on 9 November 2026:

- [Theorem5.3.3, fundamental theorem of calculus](https://www.jirka.org/ra/html/sec_ftc.html):
  the integral of a Riemann-integrable function on a compact interval
  is continuous, and its derivative at an interior continuity point
  equals the integrand.
- [Theorem3.3.2 and Lemma3.3.7](https://www.jirka.org/ra/html/sec_minmaxint.html):
  a continuous real function on a closed bounded interval attains its
  extrema; strict negative and positive endpoint values give an
  interior zero.
- [Lemma4.2.2 and Theorem4.2.4](https://www.jirka.org/ra/html/sec_mvt.html):
  differentiability at an interior relative extremum forces zero
  derivative; a function continuous on a closed interval and
  differentiable in its interior satisfies the mean value theorem.

These are imported theorems, not reproved here. The local sign and
extremum arguments below are the required specialization to the
particular hypotheses, including the nonzero derivative conclusion.

L938 supplies continuity of v, including at zero. Thus
w(t)=exp(t/10)v(t) is real continuous, hence Riemann integrable, on
[0,4]. The FTC with the original base0 makes U continuous there and
differentiable at each 0<E<4, with

    U'(E)=exp(E/10)v(E).                                          (3)

This derivative is continuous. In particular all closed subintervals
used below satisfy the continuity and interior differentiability
hypotheses of the cited extrema and mean value theorems. There is no
improper-integral or transform step here.

### Every interior stationary point is a strict local minimum

Let c in (a,b) satisfy U'(c)=0. Positivity of the exponential in (3)
implies v(c)=0, and L946 gives ell=v'(c)>0. By the definition of the
two-sided derivative, there is delta>0, with (c-delta,c+delta)
contained in (a,b), such that

    v(c+h)/h > ell/2 > 0,             0<|h|<delta.                 (4)

Consequently U'<0 on (c-delta,c) and U'>0 on (c,c+delta).
For any x in the left interval, MVT on [x,c] gives
U(c)-U(x)=(c-x)U'(xi)<0 for some xi in (x,c).
For x in the right interval, MVT on [c,x] gives U(x)-U(c)>0.
Thus U(x)>U(c) at every sufficiently close x other than c:
c is a strict local minimum. This argument uses only v'(c)>0 at
the zero, not continuity or a uniform positive lower bound for v'
away from the zero.

It follows that U has no local maximum in (a,b). Indeed Fermat's
Lemma4.2.2 would make such a maximum stationary, while the strict
local-minimum conclusion gives larger values arbitrarily close to it,
contradicting the definition of a local maximum. Constant plateaus
are also excluded by this argument.

### Every primitive zero has positive derivative

Let r be any zero of U in (a,b). Suppose first that U'(r)<0.
The derivative definition gives U(r+h)>0 for all sufficiently small
negative h, because U(r)=0 and U(r+h)/h<0. If instead U'(r)=0,
the preceding strict-minimum argument also gives U(r+h)>0 for all
sufficiently small negative h. In either case select y in (a,r)
with U(y)>0.

By Theorem3.3.2, U attains a maximum on [a,r]. Its value is at
least U(y)>0, whereas U(a)<0 and U(r)=0. Thus a maximizing point
is interior to [a,r] and is a local maximum in (a,b), which is
impossible. Both U'(r)<0 and U'(r)=0 are ruled out. Therefore
U'(r)>0 for every such zero. This excludes stationary zero tangencies
and flat crossings, not merely crossings in the wrong direction.

### Existence, arbitrary pairs, and accumulation

Continuity and (1) give at least one r in (a,b) by Lemma3.3.7.
Suppose there were any two distinct zeros r<s in (a,b).
Since U'(r)>0, its derivative definition gives a point y in (r,s)
with U(y)>0. A maximum of U on [r,s] has positive value, while
both endpoints have value zero. It is therefore an interior local
maximum, again impossible. This proves uniqueness for an arbitrary
pair, without selecting consecutive zeros or assuming their set is
discrete. Any accumulation of distinct zeros would in particular
provide a pair and is excluded by the same proof. The endpoints
themselves are nonzeros by (1). Equation (3) and the established
strict derivative prove (2) and simplicity.

Only compact energy intervals have been used. In particular the raw
cumulative positive-tilt transform-domain stop is unaffected. The
ratio and simplex-field obstructions concern different tests and are
not premises here. The prior SPECIALIZE assessment is
`drafts/literature/2026-11-09-tilted-primitive-compact-zero-scope-81.md`;
no new numerical enclosure or source theorem is asserted by this
specialization.

### Independent combined audit — 9 November 2026, step85

The unchanged SPECIALIZE assessment83, approved separately in step84,
covers this exact claim. L947's canonical step85 subsection supplies the
independent complete signed endpoint reconstruction and both error
allowances; its full certificate passes114230 checks. L946's step78
closed-cover audit and C944a's dominated differentiation are reused
under their original contracts. No additional numerical enclosure is
needed for the following logical audit.

L938(9) supplies a continuous actual representative, including at0,
by positive-parameter beta domination and its E^17 factor. Hence the
integrand in (3) is continuous on [0,4]. Lebl Theorem5.3.3 applies
with base0 and gives a continuous U and the exact derivative at each
interior energy. The argument never differentiates a numerical value
error. At a stationary c, L946 gives the two-sided v'(c)>0 for this
same representative; C944a supplies that derivative using dominated
difference quotients on an open positive-energy neighborhood.

Check (4) on both sides: division by negative h makes v(c+h)<0
on the left, while positive h makes v(c+h)>0 on the right. The
positive exponential preserves these signs. MVT on [x,c] or [c,x]
therefore gives strictly larger U values on either side. No C^2
hypothesis or lower derivative bound away from c is needed. Fermat's
lemma then excludes every interior local maximum, including a
non-strict maximum or a plateau.

For an arbitrary zero r, either nonpositive-derivative case in the
proof supplies an actual left point y with U(y)>0. The maximum on
[a,r] is attained by compact continuity, and its positive value
excludes both endpoints using U(a)<0 and U(r)=0. Its location is
interior to (a,b), so the no-maximum argument applies. This forces
U'(r)>0, rather than only a sign change. For any two zeros r<s, choose
y strictly between them and sufficiently close to r using U'(r)>0;
the maximum on [r,s] is again positive and interior. This contradiction
handles an arbitrary pair, and thus any accumulation, without a
consecutive-zero or analyticity assumption. The two endpoint signs
provide existence and exclude endpoint zeros; no endpoint derivative
is required. Equation(3) yields the asserted positive simple slope.

No defect or unstated hypothesis was found in the compact inference.
The audited conclusion is conditional precisely on the inherited
execution contracts. It is a verified local specialization of the
cited calculus, not progress beyond those general source theorems or
a complete RH candidate. Global primitive variation, the effective
head/tail join and determinant parameter signs remain independent gaps;
the raw-U domain and ratio/field stops are unchanged.

## Mathlib

Full matching coverage for this fixed-density corollary and supporting
formal versions of the imported calculus theorems have not been
checked. Availability is unknown. This informal proof and certificate
audit are not formal verification of the inherited execution libraries.
