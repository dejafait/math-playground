# Centered derivative: source gate for a different signed comparison

TARGET: Assess whether a contour-displaced saddle comparison for C999f's centered derivative can furnish a uniform signed bound on 1<=w<=3/2 and 40<=t<=45, retaining the theta-logarithm branch, vertical boundary terms and all tails; first resolve the recorded shifted-contour normalization issue in Lagarias–Rains Theorem4.4.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step428 searched "Lagarias" "Rains" "two-variable" "saddle"; "theta" "power" "centered" "derivative" "Lagarias" sign; "Lagarias" "Rains" "Theorem 4.4" correction; "theta power" "Lagarias" sign derivative contour; "two-variable zeta" "derivative" "sign"; and "two-variable zeta" "saddle point". No adequate signed theorem identified. Reused assessments421/425/426 and checked backend stop425 and the distinct two-copy saddle source stop of 2026-11-06. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 (7July2002), Proposition3.2/(3.3),(3.7) p12, Theorem4.4 and Lemmas4.5-4.7 pp21-24, especially complete proof (4.6)-(4.9), inspected in PDF text and https://arxiv.org/html/math/0104176v5 ; https://arxiv.org/pdf/math/0104176v5 . NIST DLMF20.5.3 and 2.4(iii)-(iv)/(2.4.10)-(2.4.16) inspected. Published AIF53(2003),1-68 Section4.2 pp26-31 text compared, but its displayed formulas are not legible in the available extraction; no independent published-formula confirmation claimed.
COMPARISON: Source proof (4.8)-(4.9) resolves the intended shifted normalization as exp(s(x+iy)), retaining exp(isy); the theorem display exp(sx) omits that factor. A fixed shift strictly inside |Im(z)|<pi/4 and compact-parameter decay are covered, but neither the source nor the inspected saddle expansion supplies an effective signed main term on this finite box. C999f's real-axis tail constant does not transfer to a displaced line.
GAP: Quantitative bounds for the centered parameter derivative on complex tails and an evaluated signed finite contribution with its entire complement paid remain open. No saddle phase, nondegeneracy, admissible saddle path, finite-height remainder or positive leading real part has been established.
REASON: Normalization and branch coverage remove a source ambiguity, not the sign gap. Park an unspecified saddle approximation. A single fixed-line signed-core comparison is precisely nominated in assessment428, for separate next-turn approval; no calculation or new lemma was performed here.
SCOPE: Completed literature-only step428. No contour deformation, asymptotic derivation, lemma, mathematical script, root search, parameter sweep, smaller favorable box or source-theorem reproof was performed. This assessment does not certify a sign or authorize arbitrary saddle searches.

The main gap is L030-L032/C032a actual-Xi all-degree positivity,
with L966/L968 forcing and L984(H) separate. The intermediate
observable remains the original unconditional G_w sign on the same
box. A positive result would pay only one factor at a prospective
decreasing-w collision. Curvature, event existence/nondegeneracy,
higher multiplicities, all heights, initialization and global transport
would still be needed. C997s's E_n bridge also remains separate.

Essential local inputs are C999f and L018/L019. Step428 read C999f
completely and the relevant normalization passages in assessments421
and425; it read L018/L019 for the distinguished slice and convention.
C999f remains unaudited; this source review is not its critical audit.
No cross-notebook input is involved.

Compare an admissible horizontal contour displacement (pi/8 is a
candidate to assess, not an established choice) and a saddle contour
only insofar as the primary hypotheses justify them. Check whether
the source supplies an effective signed main contribution with a
remainder smaller than it on this finite box, or whether a specific
uncovered signed estimate can be nominated. Keep all logarithm and
boundary hypotheses explicit. Merely acquiring exponential decay or
another centered absolute bound does not pass the test.

The review identifies an applicable fixed-horizontal-line identity and
one independently estimable signed-core comparison, described below
and in assessment428. It does not identify a paid saddle comparison.
Full matching Mathlib coverage is unchecked and unknown.

## Normalization: use the proof's equation, not the theorem display

The source defines h=(theta(exp(2z))^w-1)/w, continued at w=0,
and gamma=(d_z^2+w*d_z)h. Theorem4.4's displayed statement uses
exp(s*x). Its proof instead gives these exact source formulas:

    xi_Q(w,s) = (1/2) integral_R gamma(w,x+i*y)
                                   exp(s*(x+i*y)) dx,          (4.8)
    xi_Q(w,sigma+i*t) = (1/2) exp(-t*y+i*sigma*y)
                integral_R exp(sigma*x) gamma(w,x+i*y)
                                   exp(i*t*x) dx.             (4.9)

These are imported by equation number, not locally derived contour
identities. They specify the intended normalization without silently
treating the inconsistent theorem display as a second identity. The
outside factor depends on w when the center is sigma=w/2; it may not
be discarded before differentiation. The proof initially uses w!=0,
sigma outside {0,Re(w)}, and extends the completed formula to all
w,s by holomorphy and Lemma4.6. Our real center is strictly between
those two lines and w is bounded away from zero. No boundary-line
integral or w=0 formula is needed.

The inspected cases are Lemma4.5's coefficient majorization on
|w|<=R, Re(tau)>=epsilon>0; Lemma4.6's positive half-line estimate
and reflected negative half-line estimate; Lemma4.7's Heaviside
corrections, with nonzero-w and zero-w cases separated; and both
integrations by parts in (4.6)-(4.9). The source constants are finite,
not numerical sign budgets. The remark after Lemma4.7 does not itself
prove uniform subtraction constants. For the completed gamma formula
use the uniform statement of Lemma4.6 instead. The source's w=0
subtraction line is not imported as an independent formula here.

The published text has the same proof structure at pp27-30; its
mathematical displays are lost by OCR. Screenshot calls exposed no
readable page images in this session, and a local PDF fetch failed
DNS resolution. This review does not assert that the published
statement repairs, or repeats, the arXiv typo. The readable arXiv
proof suffices for the particular normalization import above.

## Branch, compactness and boundary scope

Use the holomorphic logarithm of theta(tau) on Re(tau)>0 normalized
by the real logarithm for tau>0, equivalently the branch tending to
zero as tau tends to positive infinity. Lagarias–Rains Proposition3.2
and (3.7), also [DLMF20.5.3](https://dlmf.nist.gov/20.5.E3), give
the theta_3 product with q=exp(-pi*tau), |q|<1. Its nonvanishing
is explicitly used in Lemma4.5. The usual holomorphic logarithm
theorem on a simply connected domain fixes this branch; it is not
the pointwise principal logarithm chosen independently along a path.
Fractional theta powers and parameter derivatives must use this
same branch throughout. This is applicability of the source branch,
not a new logarithm or theta theorem.

For z=x+iy with |y|<pi/4, exp(2z) lies in Re(tau)>0. Thus y=pi/8
is inside the source strip. Closed sub-strips containing the segment
0<=y<=pi/8 stay away from its boundary. Compact w neighborhoods
and bounded t neighborhoods are compatible with Lemma4.6. Cauchy
estimates in a slightly larger w neighborhood are the standard
applicability tool for parameter derivatives; a quantitative version
still needs constants, and the centered derivative includes moving s.

The source full-line identity has no finite endpoint at x=0. Its
boundary scope concerns infinity. Shifting a truncated real half-line
instead introduces finite vertical connectors at x=0 and at the
truncation; no source assertion deletes them. Uniform strip decay in
Lemma4.6 is the relevant input for passing infinite vertical ends to
their limits, not for setting finite connectors equal to zero. No
local contour deformation was done. Effective derivative-tail bounds
are future mathematical work.

## Saddle comparison and a bounded alternative

[DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv), including (2.4.14)-
(2.4.16), gives asymptotic saddle expansions under the analytic-path
and endpoint conditions of 2.4(iii). The usual leading term assumes
an interior minimum at a simple zero of the phase derivative and a
consistent square-root branch. No such phase/path for this derivative,
or uniform finite-box error smaller than a positive real leading term,
has been supplied. An asymptotic expansion as the large parameter
tends to infinity does not itself certify t in [40,45]. Olver's book
and the error-bound lead Boyd1993 in DLMF were not read and are not
imported. No unread lead is an essential premise of the alternative.

Specifically, 2.4(iii) assumes p,q analytic on an open domain containing
the path except possibly its ends, convergent local expansions with
mu>0, Re(lambda)>0 and nonzero leading phase coefficient, continuous
power branches, absolute convergence at the other end uniformly in
the large parameter's ray/sector, and strict real-part separation
from the endpoint phase, bounded away from zero near the other end.
The saddle case applies this after splitting at the interior point;
the simple-saddle formula additionally requires p'' there nonzero
and the branch condition following (2.4.16). This review verifies
none of these for a proposed theta saddle: no such phase is specified.

The specific alternative is a fixed-line comparison, not a saddle
theorem application: take y=pi/8 and keep the real part of the exact
centered derivative of the normalized (4.8) integral over -2<=x<=2
as the signed core. Bound the differentiated full complement |x|>2
with the same normalization and branch. Seek a strictly positive
lower core bound exceeding the whole complement and approximation
errors uniformly on the original box, or a complete upper bound
<=0 at an explicitly chosen rational point in that box. None of
these bounds has been evaluated. The core is specified independently
of an unknown sign or zero location; the proposed comparison retains
its sign rather than estimating the absolute value of the whole
integral. There is no established dominant term yet.

Assessment428 restricts this to one analytic attempt with no scripts
or backend changes. If it yields only decay or a zero-straddling
enclosure without an informative signed obstruction, park it rather
than renaming it as a saddle attempt. This is established-route
development, not a justified creative central-gap mechanism. The
absence of a specified phase and signed dominant contribution blocks
a creative nomination at present.
