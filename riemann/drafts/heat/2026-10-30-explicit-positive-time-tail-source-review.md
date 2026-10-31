# Fixed positive-time band: effective-source comparison

2026-10-30. Literature only. No new inequality, numerical cutoff, lemma,
mathematical script or source-proof audit is established in this step.

The main gap is actual-Xi all-degree positivity, or exclusion of the
finite positive-time collisions identified conditionally by C489a.
The reviewed intermediate target is a numerical common real/simple tail
on 1/100<=lambda<=11/200. Its potential use is a finite spatial domain
for collisions in that band. It cannot exclude those collisions or cover
0<lambda<1/100. L488's accepted identity F(lambda,z)=8 H_(4lambda)(2z)
sets the source band 1/25<=t<=11/50; multiplicities and reflection are
already checked there.

## Inspected primary source and exact inputs

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2).
Read (5)–(24), Corollary 1.4, Theorem 1.5(i)–(ii) and the absolute-constant
convention; Proposition 6.6(i)–(vi), its explicit (75)–(76), and its
proof of (ii); Proposition 9.1(i)–(iii) and proof; Lemma 9.2 and proof;
the proof of Theorem 1.5(i)–(ii), (102)–(104) and the following
whole-strip localization. These are precise source locations, not a
claim to have audited the saddle estimates underlying Theorem 1.3.
The versioned PDF is accessible at https://arxiv.org/pdf/1904.12438v2;
the theorem/formula comparison here uses the inspected HTML math.

Theorem 1.3 has the CLOSED spatial range x>=200, 0<=y<=1 and time
0<t<=1/2. Put z=x+iy, s_+=(1+y-ix)/2, s_-=(1-y+ix)/2. Its notation is

    alpha(s)=1/(2s)+1/(s-1)+(1/2)Log(s/(2*pi)),
    M_t(s)=exp(t*alpha(s)^2/4)*M_0(s),
    B_t(z)=M_t(s_+),       gamma=M_t(s_-)/M_t(s_+),
    s_*=s_++(t/2)*alpha(s_+),
    kappa=(t/2)*(alpha(s_-)-alpha(conjugate(s_+))),
    b_n^t=exp((t/4)*log(n)^2),
    N=floor(sqrt(x/(4*pi)+t/16)),
    f_t(z)=sum_(1<=n<=N) b_n^t/n^(s_*)
           +gamma*sum_(1<=n<=N) n^y*b_n^t/n^(conjugate(s_*)+kappa).

M_0 and its nonvanishing holomorphic logarithm are explicitly defined
in source (6)–(7) on C minus (-infinity,1]. All powers of positive
integers use their real logarithms. Theorem 1.3(13) states

    abs(H_t(z)/B_t(z)-f_t(z)) <= e_A+e_B+e_(C,0).

For the future numerical specialization the complete usable source
bounds are as follows, with L=log(x/(4*pi)) and u_+=max(u,0):

    abs(gamma)<=exp(0.02*y)*exp(-y*L/2),
    Re(s_*)>=(1+y)/2+t*L/4
             -t*(1-3*y+8*y*(1-y)/x^2)_+/(2*x^2),
    abs(kappa)<=t*y/(2*(x-6)),

    e_A+e_B <= sum_(1<=n<=N)
      (1+abs(gamma)*N^abs(kappa)*n^y)*b_n^t/n^Re(s_*)
      *[exp(((t^2/16)*log(x/(4*pi*n^2))^2+0.626)/(x-6.66))-1],

    e_(C,0) <= exp(-(1+y)*L/4)*exp(-t*L^2/16
      +1.24*(3^y+3^(-y))/(N-0.125)
      +(3*abs(L+i*pi/2)+10.44)/(x-12)).

The real-part bound is specifically Proposition 6.6(ii), and the other
bounds are Theorem 1.3(20), (22)–(24). The first real-part estimate in
the printed HTML proof of Proposition 9.1 instead displays t*L/2.
Use the explicit t*L/4 statement above for numerical work; this textual
difference is not adjudicated here and is not a refutation of the
asymptotic theorem. No unstated strengthened coefficient is approved.

## What is and is not effective at the zero-count stage

Theorem 1.5(i)–(ii) gives the desired qualitative reality/localization
and unique-disk count, but its C, c and O constants have no numerical
values there. Proposition 9.1(i) and Lemma 9.2 still use unspecified
thresholds/errors. A numerical value cannot be substituted for L488's
C_* by citation to these statements alone.

Corollary 1.4 tests strict nonvanishing. It does not supply a
multiplicity-one count near real zeros. Theorem 1.5's proof uses a
circle count and then exhaustion of zeros in |y|<=1. L488 already
records why the coarse (104) estimate alone is insufficient for a strict
circle comparison and retains the holomorphic factor from (102).
Making that replay numerical would still require quantitative phase
variation, separation, strict contour margins, whole-strip exhaustion
and threshold padding. The cited (6)–(10) and (75)–(76) offer explicit
inputs for later phase work; no such inequalities are proved here.

The extension to |y|<=10 in Proposition 9.1 explicitly requires adjusted
constants. Those unprinted values are not approved numerical inputs.
The narrower strip is sufficient for the proposed preparatory estimate;
a later zero count must justify its contours within that range and use
conjugation. It must also retain both closed time endpoints, threshold
equality, negative real parts and multiplicities. Global strip coverage
remains the accepted de Bruijn input in L488, not a new source audit.

## Search, overlap and decision

Queries: `"Polymath" "1904.12438" "explicit" "simple"`;
`"Effective approximation" "real and simple" zeros explicit`;
`"1904.12438" "real" "simple" "explicit"`;
`"H_t" "1+gamma" Polymath`; `"Polymath" "simple" "cutoff" zeros`.
Returned project discussions and unrelated hits supply no additional
imported theorem. No novelty or global absence is inferred. Only the
primary paper above supports the theorem comparison.

Narrow local searches checked positive-time literature assessments,
the Polymath audit notes, L488 and the October 30 heat/failure notes.
The existing common-tail assessment and L488 cover the existential
claim; no numerical residual certificate was found in those checked
paths. The endpoint inverse-gap source application remains parked for
its Hamiltonian/source gap. L487's generic bounded-energy obstruction
and the recorded kernel/shape limitations do not settle this different
effective question. No older stopped mechanism is reopened.

Decision: stop DIRECT NUMERICAL-CUTOFF EXTRACTION from Theorem 1.5;
it does not state the needed constants. This is informative source-scope
evidence, not a counterexample to an effective tail theorem. Theorem 1.3
does provide explicit inputs for a bounded preparatory calculation.
Propose testing abs(H_t/B_t-(1+gamma))<=1/100 on the source band,
0<=y<=1, x>=4*pi*exp(10000). The height and tolerance are TEST
PARAMETERS, not an achieved estimate or a certified cutoff.

Continue this preparatory target only with uniform analytic majorants
for both n>=2 sums and all three errors, including the moving floor N
and every x beyond the edge. A finite sample, unspecified constant or
floating-point underflow does not pass. If the bound fails, retain the
failing term/range and reassess before any counting claim. Even success
would leave the phase/count obligations and interior collisions open.
This specializes known asymptotics; it is not a new RH mechanism.
Matching full Mathlib coverage is unchecked. No theta-specific input
currently justifies a creative collision-exclusion attempt.
