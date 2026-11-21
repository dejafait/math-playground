# Corollary C032v: obstruction to the first-odd one-jump majorant

## Hypotheses

Retain precisely C032j/m/q/t/u's actual-zero Gaussian half-variance
normalization and qualifications. Thus the positive-ordinate divisor
counts multiplicities, excludes ordinate zero, and retains the strip,
counting, verification through height 100, first-zero/tail, heat and
two fixed-v1 external preprint inputs. Their source-wide correctness
and finite-zero data are not independently certified here. In particular,
nu_j, j=1,2, are Borel probabilities on X=[0,infinity), with

    L_j(s)=integral_X exp(-s*x) dnu_j(x)=exp(-B_j(s)), s>0,
    B_j(w^2)=b_j(w), w>0,
    b_j(w)=E_j(w)+O_j(w),
    E_j(w)=4*integral_0^w t*R_j(t) dt,
    O_j(w)=2*pi*integral_0^w p_j(i*t) dt.

These are the entire lifts of C032m/q. Set

    c_j=2*pi*p_j(0), k=p_2(0)/p_1(0),
    Pi(dt)=D(t)dt, D(t)=ell_2(t)-ell_1(t),
    M=Pi((0,infinity)).

C032t/u supply D>0, 0<M<infinity and

    nu_2=exp(-M)*sum_(n=0)^infinity (nu_1*Pi^{*n})/n!,
    Pi^{*0}=delta_0.                                    (1)

No RH, positivity of the full profiles p_j, density of nu_j,
finite first moment, exponential moment, full odd cancellation or
unsmoothed Xi realization is assumed.

## Conclusion

One has 0<c_1<c_2 and k=c_2/c_1>1. If a real constant C satisfies
the all-Borel finite-measure inequality

    nu_1*Pi <= C*nu_1,                                  (2)

then necessarily

    C >= M+k-1.                                        (3)

In particular the proposed value C=M+log(k) fails. More precisely,
for lambda_C=C*nu_1-nu_1*Pi and f_s(x)=1-exp(-s*x),

    lim_(w->0+) integral_X f_(w^2) dlambda_C / w
        =c_1*(C-M)-(c_2-c_1).                          (4)

At C=M+log(k) this limit is strictly negative, so a bounded
nonnegative test violates positivity for every sufficiently small
positive w. This does not refute nu_2<=k*nu_1.

If (2) did hold, positive convolution iteration would give

    nu_2 <= exp(C-M)*nu_1.                              (5)

Consequently no scalar bound (2) with C<=M+log(k) can establish the
desired paired constant by this iteration. The obstruction applies to
this sufficient mechanism, not to reverse domination by other means,
to positive output for the first-odd law, or to the continuum problem.
This result passed critical audit1569 under exactly the retained
external-input qualifications.

## Proof

### Inputs, citation reuse and width ordering

Use the unchanged EXPLORE assessment1564, including its covered
one-jump target and the primary coverage in source-notes1552/1562/1565.
The finite-activity series (1) is imported from C032u, which specializes
Jean Bertoin, *Subordinators, Levy processes with no negative jumps,
and branching processes*, Maphysto 2000 course,
[Theorem 1.2, pp.7-8, finite-activity case p.9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf),
and Steven P. Lalley, *Levy processes, stable processes, and
subordinators*,
[Definition 5.1 and (5.2)-(5.4), p.12](https://galton.uchicago.edu/~lalley/Courses/385/LevyProcesses.pdf).
Transform multiplication for finite positive half-line measures is
Ante Mimica, *Laplace transform*, Dresden course, 2015,
[Proposition 1.4(iv), pp.6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
The hypotheses are met: Pi is a finite positive measure on (0,infinity),
nu_1 is a probability, and all exponential tests used here are bounded.
No general construction, density theorem or uniqueness theorem is
reproved. The necessary constant and iteration check below are the
family-specific work not supplied by those citations.

C032j gives p_j(0)>0 and, with K(u)=sqrt(u)*H(u),

    p_j(0)=H(1/(4*j))/sqrt(4*pi*j)=K(1/(4*j))/sqrt(pi).

The assembly in C032t gives K'<0 on (0,1/4]. Since 1/8<1/4,
p_2(0)>p_1(0)>0. Thus c_2=k*c_1 with k>1. No numerical lower
bound on k or new zero-data calculation is needed.

### Exact bounded transform, with its mass term

The entire definitions give E_j(0)=O_j(0)=0,
E_j'(0)=0 and O_j'(0)=2*pi*p_j(0)=c_j. Hence

    b_j(w)=c_j*w+O(w^2),
    L_j(w^2)=exp(-b_j(w))=1-c_j*w+O(w^2), w->0+.

These are Taylor consequences of holomorphy. In particular

    (1-L_1(w^2))/w -> c_1,
    (B_2(w^2)-B_1(w^2))/w -> c_2-c_1.                 (6)

For s>0 write Delta(s)=B_2(s)-B_1(s). Both exponent integrals
are finite, and D is integrable, so ordinary linearity gives

    Delta(s)=integral (1-exp(-s*t)) dPi(t),
    PiHat(s)=integral exp(-s*t) dPi(t)=M-Delta(s).

The convolution has mass M and Laplace transform L_1(s)*PiHat(s).
Consequently, exactly and before taking any limit,

    integral_X f_s dlambda_C
       =C*(1-L_1(s))-[M-L_1(s)*PiHat(s)]
       =(C-M)*(1-L_1(s))-L_1(s)*Delta(s).               (7)

Every integral is absolutely defined against finite measures;
0<=f_s<=1. Retaining M is essential. There is no differentiation
at s=0, subtraction of divergent moments or moment-based Tauberian
step. Divide (7) by w at s=w^2 and use (6) and L_1(w^2)->1 to
obtain (4).

If (2) holds, lambda_C is positive, so (7) is nonnegative. Its
limit after division by w>0 must also be nonnegative, proving (3).
For k>1,

    log(k)=integral_1^k du/u < integral_1^k du=k-1.

At the proposed C, let h=c_1*(k-1-log(k))>0. Formula (4) says
the limit is -h; therefore (7) is <-h*w/2 for all sufficiently
small w>0. This is a strict bounded-test contradiction to (2).
It is an existential positive threshold from a proved limit, not a
numerical preview or an effective threshold claim.

### Convolution iteration and its precise limitation

Suppose now that (2) holds for some C. Testing the constant one
first gives C>=M>0. Convolution preserves order between finite
positive measures: for positive finite tau and alpha<=beta, the
quantity ((beta-alpha)*tau)(A) is the integral of 1_A(x+y) against
the positive product measure (beta-alpha)(dx)tau(dy), and is
nonnegative for every Borel A. All masses are finite.

Starting with nu_1*Pi^{*0}=nu_1, induction therefore gives

    nu_1*Pi^{*n} <= C^n*nu_1, n>=0.

Indeed convolve the n-th bound with Pi, then apply (2) and multiply
by C^n>=0. Associativity follows from Tonelli applied to the
nonnegative Borel indicator of a sum. In (1) all terms are positive;
their masses are M^n/n!, so the measure series is finite. Summing
the inequalities on each Borel set yields

    nu_2(A)<=exp(-M)*sum_(n>=0) C^n/n!*nu_1(A)
           =exp(C-M)*nu_1(A),

including all atoms and singular parts. This proves (5). Achieving
the requested coefficient by this bound would require
exp(C-M)<=k, or C<=M+log(k), incompatible with (3). In fact its
smallest permissible reported coefficient is at least
exp(k-1)>k. This says nothing about cancellations or sharper direct
estimates in the full series: the actual inequality nu_2<=k*nu_1
remains undecided. Full J_eta=0, the finite-family stop and the
independent Xi realization and all-degree positivity gaps are
unchanged. This is a classical bounded-transform specialization and
local obstruction, not certified originality or progress beyond all
sources checked. ∎

### Critical audit1569 — 18 November 2026

The bounded obstruction and conditional iteration pass the exact
SPECIALIZE assessment1566. This is local validation of the existing
specialization, not a stronger inequality, a new discovery, or an
independent certification of the external preprints and zero data.
Reuse the inspected primary hypotheses and proof cases in source
notes1552/1565/1567; the citations above supply only the general
finite-activity construction and transform rule. The full present
proof, C032u's series and its earlier audit, C032m's lift definitions,
C032q's bounded integration interface, and C032t's ordering assembly
were checked for this application. No new external input is needed.

First, the Gaussian normalization gives
p_j(0)=K(1/(4*j))/sqrt(pi). Both evaluation points belong to
(0,1/4], where the retained C032t assembly gives a continuously
differentiable K with K'<0. Integrating K' between 1/8 and 1/4
gives K(1/8)>K(1/4). C032j's qualified heat positivity supplies
the strictly positive denominator. Hence k>1 and c_2=k*c_1>0;
neither positivity of the full real profiles nor realness of every
zero was substituted for this input.

The primitives vanish at zero, E_j'=4*w*R_j(w) and
O_j'=2*pi*p_j(i*w). Holomorphy of R_j and p_j therefore gives
b_j(w)=c_j*w+O(w^2), for each of the two fixed widths.
Identification with B_j(w^2) is needed only for real w>0.
Exponentiation yields L_j(w^2)=1-c_j*w+O(w^2), while
Delta(w^2)=(c_2-c_1)*w+O(w^2). These are lift expansions,
not differentiation of a law transform at s=0. They use no first
moment, density or exponential moment, and require no width-uniform
remainder beyond these two fixed widths.

Pi is a finite positive measure of mass M on (0,infinity), and
nu_1*Pi has mass M. For every real C, lambda_C is a finite signed
measure of mass C-M, with total variation at most |C|+M.
The test f_s is continuous, Borel and between zero and one.
The convolution transform is L_1(s)*(M-Delta(s)), so subtracting
that transform from its own mass gives exactly

    integral f_s dlambda_C
      =(C-M)*(1-L_1(s))-L_1(s)*Delta(s).

In particular the mass term is C-M rather than C. Every integral
in this identity is finite before subtraction. Taking s=w^2 and
dividing by positive w gives (4), including its minus sign and
the full coefficient c_2-c_1. Positivity of lambda_C would force
this limit to be nonnegative. At C=M+log(k) it is
-c_1*(k-1-log(k))<0. The defining limit then gives the stated
strict negative integral for all sufficiently small positive w.
The threshold is existential; no effective value or numerical
certificate is asserted. A bounded nonnegative test is enough
to disprove measure positivity; no converse transform-order claim
is used.

For the conditional iteration, the constant-one test in (2)
first forces C>=M>0. Thus multiplying measure inequalities by
C^n preserves order, including the n=0 base case. Convolution
with Pi preserves order on all Borel sets by the positive product
integral, and its associativity follows from the same finite
nonnegative triple integral. Induction gives exactly the n-th
bound stated above. The positive series in (1) has total mass
exp(-M)*sum M^n/n!=1. Its upper bounding series is finite since
C is finite. Monotone summation on each Borel set, including
sets meeting atoms, therefore proves (5).

To obtain coefficient at most k by this particular iteration
would require C<=M+log(k), whereas its necessary condition is
C>=M+k-1. The two conditions are incompatible strictly because
k>1. No estimate on an individual summand is inferred from an
estimate on the full series. In particular neither failure of
nu_2<=k*nu_1 nor a negative signed output follows. The finite-family
full-cancellation stop, continuum feasibility and unsmoothed Xi
realization remain separate. No defect, improved bound or changed
mathematical dependency was found; the main argument is unchanged.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. Supporting finite-measure convolution, integration and
holomorphic Taylor results were not assessed here; unknown coverage
is not evidence of absence. No replacement for the qualified
fixed-v1 external inputs is claimed.
