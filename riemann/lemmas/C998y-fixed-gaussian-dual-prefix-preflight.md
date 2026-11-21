# C998y: Whole-line Gaussian dual restriction; one aggregated-loop stop

## Hypotheses

Use exactly C998x's real f,g,h=P0Uf, ell=log(3)/2, complete signed
measure mu=Dh and256 energies Q_a from C998u(5)-(9). Keep C999l(1)'s
exact Z, all512 raw modes,334 U shifts,identity2187,full K14/K7 and
both exact P0 moments. C998s supplies its full-image bounds and exact
projection; C744v supplies the complete16-shift T. The ambient triple
scalars remain complex. Retain the analytic-response,neutral-core,
IEEE754/Decimal and unreplayed c_* qualifications. No inherited
matrix, response or c_* certificate is independently revalidated.
Witness: `scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
SHA256 `99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.

Invocation-start SPECIALIZE assessment746, separately approved747,
is `drafts/literature/2026-11-13-prefix-energy-gaussian-preflight-review-746.md`.
Import, rather than reprove, these inspected general results:

- Sriperumbudur--Fukumizu--Lanckriet, *Universality, Characteristic
  Kernels and RKHS Embedding of Measures*, JMLR12(2011),2389-2410,
  Lemma7/full proof p2407 and Proposition4 proof p2402,
  [primary PDF](https://jmlr.org/papers/volume12/sriperumbudur11a/sriperumbudur11a.pdf):
  bounded measurable RKHS kernel and finite signed Borel measure,
  integration representer and its squared norm as double kernel integral.
- Novak--Ullrich--Wozniakowski--Zhang, arXiv:1709.02568v1,
  equation(1) p2 and explicit K_(1,1) p3,
  [primary PDF](https://arxiv.org/pdf/1709.02568v1): full-line H1 norm
  integral(u^2+u'^2) has kernel exp(-|x-y|)/2.
- Bauschke--Goebel--Lucet--Wang, *The Proximal Average: Basic Theory*,
  SIAM J.Optim.19(2008),766-785, Section2(1)-(2) p767 and
  Proposition3.3(i)/citation proof p769,
  [primary PDF](https://webpages.math.luc.edu/~rgoebel1/publications/journals/BauschkeGoebelLucetWang08SIOPT.pdf):
  real Hilbert quadratic conjugacy q*=q for q=norm-squared/2.
- Reuse719's Trefethen, *Is Gauss Quadrature Better than
  Clenshaw-Curtis?*, SIAM Review50(2008),67-87,
  Theorem4.5/(4.14) p77 and Gaussian proof pp79-80,
  [primary PDF](https://people.maths.ox.ac.uk/~trefethen/CC.pdf):
  N exact Gauss nodes, ellipse parameter rho, bound M, error at most
  64M/[15(1-rho^-2)rho^(2N)] on[-1,1]. Node/value rounding is additional.

Only their normalization, fixed Gaussian restriction and analytic-panel
application below are derived. The standard Gaussian integral is used
to evaluate the whole-line Gaussian products. No new quadrature theorem,
Hilbert duality theorem or assertion of originality is intended.

## Conclusion

Put s=32/ell, phi_k(x)=exp(-(sx-k)^2), k=0,...,32. Define

    b_k=integral_R phi_k dmu=-integral_0^ell h(x)phi_k'(x)dx,
    S_kl=sqrt(pi/2) exp(-(k-l)^2/2)/s,
    D_kl=s sqrt(pi/2)(1-(k-l)^2)exp(-(k-l)^2/2),
    H_a=(a S+a^-1 D)/2.                                (1)

H_a is positive definite for every a>0. For any real vectors c_j
(j=0,...,255), with a_j=2j+1/2,

    E=a0(h,h)>=L_G:=d0 q
       +sum_(j=0)^255 [2 b^t c_j-c_j^t H_(a_j)c_j]/a_j^2. (2)

The loading b is rate-independent, including all density and atom
effects, outer traces,K14 and both projection terms. No condition
h in H1 is asserted. Maximization within the finite span would give
b^t H_a^-1 b; no numerical inverse, conditioning or coefficient
accuracy is certified. Expression(2) is a lower comparison, with
uncontrolled variational and omitted-prefix deficits, not a two-sided
energy approximation.

ONE specified implementation aggregates translated cosine coefficients
on the joint U/T partition, uses64 Gauss nodes on each of350 panels,
and evaluates common phases directly for both h and v=Tg. In exact
arithmetic, with the complete analytic images supplied, its Gauss
errors satisfy

    |error(q)|<2^-33, |error(t)|<2^-46,
    |error(b_k)|<2^-66 (each k), t=integral v h.         (3)

These are only quadrature errors, not complete numerical certificates.
The common trigonometric loop alone costs102816000 scalar arithmetic
and elementary-function operations, above the TOTAL cap10^8. It
therefore parks before any load, profile, norm-matrix or Gram evaluation.
Precision,bytes,all-entry errors and a Schur margin remain unpaid.
This is an implementation-specific negative, not a lower complexity
bound for other algorithms or evidence of a negative Gram.

## Proof

### 1. Whole-line normalization and compact-source pairing

For a>0 consider the real full-line H1 norm

    ||u||_a^2=(1/(2a))integral_R u'^2+(a/2)integral_R u^2.

Under t=ax and w(t)=u(t/a), this is half the cited standard H1 norm
of w. Scaling that norm by1/2 multiplies its kernel by2; dilation
then gives precisely exp(-a|x-y|). The continuous representatives
are used. C998u supplies a real finite signed Borel measure with
compact support[0,ell],TV<B=2^23. The kernel is continuous,bounded,
and has diagonal1, so the signed-measure theorem applies without
positivity,probability normalization or an L2 density. Its representer
r_a has norm-squared Q_a. The cited Hilbert conjugacy, with its
variable rescaled by2, gives

    Q_a>=2 integral u dmu-||u||_a^2                  (u in H1(R)).

Each phi_k and its derivative are polynomial times a Gaussian and
belong to L2(R); thus these are admissible trials. Choose a compact
smooth cutoff chi identically1 on a neighborhood of[0,ell]. By
mu's support, integral phi_k dmu=integral chi phi_k dmu.
The defining distributional derivative identity gives the latter
as -integral_R h(chi phi_k)'. Since h is zero outside[0,ell] and
chi'=0 there, this is exactly the first formula in(1). This argument
keeps both outer atoms; it does not integrate only the classical
interior derivative or impose a zero boundary condition on a trial.
Substituting C998u's entire h, not its head or atomic part, also
retains its full continuous kernel and both projection corrections.
There is no rate a in this pairing, proving the claimed reuse.

Complete the square with u=sx-(k+l)/2. Then

    phi_k phi_l=exp(-(k-l)^2/2)exp(-2u^2),
    phi_k'phi_l'=4s^2[u^2-(k-l)^2/4]phi_k phi_l.

The Gaussian integral and its second moment
integral u^2 exp(-2u^2)du=(1/4)sqrt(pi/2) give S and D in(1).
These are WHOLE-LINE integrals, including the exterior of[0,ell].
Hence for u=sum c_k phi_k, ||u||_a^2=c^t H_a c.
Linear independence holds: multiply an identically vanishing linear
combination by exp(s^2x^2) to obtain the polynomial
sum c_k exp(-k^2)(exp(2sx))^k vanishing on(0,infinity).
All coefficients vanish. Almost-everywhere vanishing first becomes
everywhere vanishing by continuity. A nonzero combination therefore
has positive norm, so H_a is positive definite. Finite-dimensional
quadratic conjugacy gives the optional exact maximum b^t H_a^-1 b.
No numerical use of that inverse follows merely from existence.
Apply the individual lower bounds and C998x's E>=L256 to obtain(2).

### 2. One non-density organization and exact analytic quadrature

Freeze N=64,rho=2, with no tuning. Form the union of the334 U
pieces and the breakpoints of v=Tg's16 shifted terms. For separation
m, a nonidentity shift has entrance log(n)-m ell if n^2>3^m,
or exit log(n)-(m-1)ell otherwise. Identity2187 has no event.
There are333 U and16 T events. The small script compares all event
locations by their exact rational exp(2x)=n^2/3^a, including the
two endpoints1 and3. Every adjacent comparison is strict; there
are350 open panels. Every adjacent ratio is<51/50, proving
each panel length L<(1/2)log(51/50)<1/100. The certificate retains
the entire event list and every ratio, not a sampled gap check.

On each panel, expand each active translated cosine by the ordinary
angle-addition formula and aggregate its cosine/sine coefficients
once. This retains all334 U and16 T shifts without the55725
shift/panel/node loop of stopped745. Both profiles have the same
frequencies k_n=n pi/ell, n=0,...,511. Keep K14 f,K7 g and the
two projected exponentials separately and completely. This defines
analytic extensions on each panel; a breakpoint is not an interior
point of the quadrature panel. One-sided analytic formulas may be
continued outside that real piece for applying the Gauss theorem.

For the rho=2 ellipse of a panel, |Im z|<=3L/8<3/800, and its real
extension beyond either panel end is L/8<1/800. C998s gives
ell in(1/2,3/5), k_511<4088 and raw coefficient l1 norms<6,
with cosine normalizations<2. Thus either base profile has
modulus<=12 exp(4088|Im z|), and 4088|Im z|<16. The U shift
weights sum<112. The16 T weights are each<1 since n>=29,
Lambda(n)<5 and sqrt(n)>5. For m=7 or14, the full kernel series
has Re(m ell+z-y)>=6ell-L/8>2, y in[0,ell]. Its absolute geometric
sum is<1, without truncating it, and integration against f or g on
the REAL y interval has modulus<8. Uniform geometric convergence
also proves analyticity of these parameter integrals on the whole
ellipse (the already assessed713 argument reused in C998s).

C998s bounds each projection coefficient by294912. On these
ellipses |exp(+/-z/2)|<2. Consequently

    |h(z)| <=(1344+8+4*294912)exp(16)<2^47,
    |v(z)| <=(192+8)exp(16)<2^34.

Here exp(16)<3^16<2^26 is a deliberately coarse elementary bound.
Both products h^2 and vh are analytic: the profiles are real on
the real interval, so these equal the required q and signed t
integrands there; no nonholomorphic complex conjugation is used.
Their ellipse bounds are2^94 and2^81 respectively.

For the Gaussian loading, s<64, |Im(sz-k)|<1/4,
|Re(sz-k)|<33, hence |sz-k|<34 and

    |phi_k'(z)|<=2*64*34*exp(1/16)<2^14.

Thus the bound for h phi_k' is2^61. Rescale the cited exact
N-node Gauss bound to each panel, and sum their lengths ell<3/5.
At rho=2,N=64 the total error for a uniform ellipse bound M is

    < (128/45)(3/5) M 2^-128 <2 M 2^-128.

The three bounds above give(3), simultaneously for all33 loads.
This statement assumes exact nodes,weights,profiles and moments;
it neither certifies their numerical values nor bounds the weighted
expression(2) without coefficient information.

### 3. Discriminating total-work failure before numerical evaluation

Freeze a direct common-phase implementation on all350*64=22400
nodes. For every mode n=2,...,511 it performs exactly the following
scalar operations, reusing the common trigonometric values across
the two profiles and across ALL33 loads and256 rates:

    theta=k_n*x; sn=sin(theta); cs=cos(theta);
    uh=A_n*cs+B_n*sn; uv=C_n*cs+D_n*sn.

These are one phase multiplication,two separate elementary calls,
four coefficient multiplications and two internal additions:9
operations. Accumulating uh and uv into the profile sums is granted
at zero cost. The fixed loop visits every specified mode even if an
aggregated coefficient happened to cancel. It does not use a mode
recurrence,fused multiply-add or a combined sine/cosine service.
Thus its required work is at least

    350*64*510*9=102816000>100000000.

This already favorable count omits indices0,1,all preparations,
coefficient updates,full kernels,projection,q/t/load products,
quadrature weighting,all elementary-function accuracy work,
Gaussian norm entries,solves,leading entries,d0,output and replay.
An actual certified implementation of these elementary calls would
cost more. No free library accuracy or transcendental oracle is
being asserted. Other recurrences or reassociations are DIFFERENT
algorithms; this is no lower bound on them. No node order was
reduced or other prescription tested after this failure.

The cap is for ALL work, so this necessary condition is decisive
before assigning a precision or byte budget. They are explicitly
UNPAID, not zero. Also unpaid are the full errors in all evaluated
comparison entries: the old709 intervals for F,G,p exceed1e-6;
the new q,t and loads have no node/value/rounding certificates;
neither Gaussian norms nor coefficients have been numerically
enclosed. For fixed exact candidate vectors, load and norm-entry
errors epsilon_b,epsilon_H would contribute at most
2||c||_1 epsilon_b+||c||_1^2 epsilon_H per rate before the a^-2
weight; this does not certify any such errors or coefficient bounds.
No weighted1e-6 lower-expression budget or inverse conditioning
claim is inferred from(3).

Any future successful numerical prescription must still enclose
C998x's entire signed debt, including2pqt,positive determinant,
q's local d0 q role and its cross-entry role, and BOTH h cross
entries. The only sufficient sign test is a strict outward positive
Schur margin. A nonpositive LOWER comparison cannot refute the
true Gram. This step computes neither side of that test.

### 4. Evidence and remaining gaps

Run `python3 scripts/separation-seven/gaussian-dual-preflight-748.py`.
It writes `scripts/separation-seven/gaussian-dual-preflight-748.json`:
20/20 checks, no failures. Complete exact event/ratio and work evidence
is saved; the script does not verify RKHS duality or analytic estimates
by computation. No profile,loading,norm-matrix or Gram was evaluated.
Separate conceptual audit750 below upholds the proof and the specified
implementation count under the unchanged inherited contracts.

This is REPRODUCTION/specialization of the checked methods. The local
formula(1)-(2) is retained, alongside an informative failure of ONE
new panel-aggregated implementation, rather than a new general theorem.
Preserve745's direct-density stop, C998u's full-tail loop stop and
C998w's original-measure production stop. None is a global ban.
The fixed comparison remains unevaluated. Uniform control of
V14+R^2 against BOTH defects,all-vector middle minimization,
defect localization,C744q/H2 and actual-Xi/global assembly remain
open. No complete RH candidate,zero exclusion or disproof results.

### 5. Separate conceptual audit — 13 November2026, step750

Invocation-start SPECIALIZE assessment748, separately approved749,
covers this exact audit. Reuse its inspected primary statements and
proof cases, including the four citations in the Hypotheses. Read the
whole proof above, C998u(5)-(9)/audit726, C998s Section1/audit714,
C998x(1)-(3), C744v(1) and C999l(1). No mathematical error requiring
a correction was found. This verifies a local application of known
methods; it establishes no result beyond the sources' general methods.

**The rate, amplitude and lower direction.** For w(t)=u(t/a), change
of variables gives integral w^2=a integral u^2 and integral w'^2=
a^-1 integral u'^2. Thus the displayed norm is exactly half the
reference whole-line H1 norm after dilation. The reference kernel's
factor1/2 cancels this norm scaling, leaving exp(-a|x-y|), with no
extra a in its amplitude. Its diagonal is1. C998u's real signed mu
has TV<B and compact support, so the double-kernel integral is
absolutely bounded by B^2. The cited signed-measure representation
therefore gives Q_a=||r_a||_a^2. Quadratic conjugacy gives the supremum
of 2<u,r_a>_a-||u||_a^2 as Q_a; restricting u can only lower it.
All weights a_j^-2 are positive. C998u(8) gives nonnegative omitted
energies, so retaining j<256 and then restricting their trials gives
(2), while preserving the exact d0 q term. Nothing signs d0 favorably.

The compact cutoff equals1 on a neighborhood of the entire closed
support, not merely on its open interior. Consequently chi'=0 at
both support ends as well, and testing Dh with chi phi_k gives exactly
-integral_0^ell h phi_k'. This uses the whole distributional derivative,
including h(0+)delta_0-h(ell-)delta_ell from C998u(6). It requires no
H1 property of h and no vanishing Gaussian endpoint. Neither the
classical density alone nor the atomic part alone is substituted.
The full K14 image and both moment corrections occur inside h.

The Gaussian product computation has shift d=k-l and centered
coordinate u=sx-(k+l)/2. Its derivative product has factor
4s^2(u^2-d^2/4); changing dx to du/s gives exactly
D_kl=s sqrt(pi/2)(1-d^2)exp(-d^2/2). The mass product gives S_kl
as stated. The full-line H1 membership and polynomial independence
argument prove strict positive definiteness for every a>0, even if
some off-diagonal D entries are negative. The inverse expression is
only an exact finite-dimensional maximum. No numerical conditioning
or useful trial quality follows. Independent complex triple scalars
do not alter these real-measure trial calculations or remove either
of C998x's signed h cross entries.

**Every event and the analytic extensions.** For either separation m,
the translation is x+m ell-log n. Its entrance is log n-m ell
when n^2>3^m, and its exit is log n-(m-1)ell otherwise. The strict
active interval is 3^(m-1)<n^2<3^(m+1); endpoint overlaps have zero
length. Only2187 is an identity among the two active lists. The
independent finite audit below compares every event, including both
separations, and all350 ratios with the complete original certificate.
The maximal ratio is5442889/5340721<51/50, at zero-based panel34.
Since L=log(ratio)/2<(ratio-1)/2, every panel has L<1/100.

On each open panel the active shift set is constant. Its finite sum
of translated cosines has an entire extension; an indicator is not
continued as a holomorphic function. Each panel uses its own one-sided
formula at the ends. Those endpoint assignments change no integral.
The rho=2 ellipse has semiaxes5L/8 and3L/8, hence real overhang L/8.
For m=7 or14 and real y in[0,ell], the entire ellipse satisfies
Re(m ell+z-y)>6(1/2)-1/800=2399/800>2.

An open neighborhood of each closed ellipse still has this strict
last inequality. The full kernel series there has geometric absolute
majorant sum_(j>=1)exp[-(2j+1/2)*2]<1. Each parameter integral
against the finite real cosine f or g is holomorphic: apply Jiří
Lebl, *Guide to Cultivating Complex Analysis*, version1.10,
5November2026, Lemma3.4.1/proofs pp81-82 and Theorem3.4.5 pp84-85,
[primary text](https://www.jirka.org/ca/ca.pdf), as inspected in
assessment748/749. The integral theorem's joint continuity on the
complex neighborhood times the compact real interval holds termwise;
the geometric bound and ||f||_1,||g||_1<12ell<8 give locally uniform
convergence of their integrals. Its limit theorem therefore preserves
holomorphy. This checks the open-neighborhood hypothesis, not only a
bound on the ellipse boundary. Neither K14 nor K7 is truncated.

The raw l1 bound<6, normalizations<2 and k_511<4088 give
12 exp(4088|Im z|), with exponent<1533/100<16. All334 U weights
sum<112, including the identity; all16 T weights are<1. The exact
projection coefficients have modulus<294912. Since
|Re z|/2<(3/5+1/800)/2=481/1600<1/2, both projection exponentials
have modulus<sqrt(e)<2. Thus the h and v prefactors are respectively
1181000<2^21 and200<2^8; e^16<3^16<2^26 gives2^47 and2^34.
These bounds include all smooth and shifted terms on every ellipse.

For k=0,...,32, |Im(sz-k)|<6/25<1/4 and
|Re(sz-k)|<32+64/800=802/25<33. Therefore |sz-k|<34 and
|exp(-(sz-k)^2)|<=exp((Im(sz-k))^2)<exp(1/16)<2.
The derivative bound is<2*64*34*2=8704<2^14. This verifies the
loading majorant2^61, including the two extreme trial centers.
For real x each panel's h,v is real, so the analytic products h^2
and vh equal the required real integrands. No conjugation of z is
used. Their bounds are2^94 and2^81.

**Exact quadrature versus numerical evaluation.** The cited Gauss
theorem uses n+1 nodes; setting n=63 gives exponent128. The affine
Jacobian L/2 changes its constant to128L/45 at rho=2. Summing over
all panels gives128ell/45<128/75<2, proving precisely the three
strict bounds in(3). Jump endpoints cause no missing integral term.
The sign in b=-integral h phi_k' does not change its error bound.
Exact nodes, weights, moments and values remain hypotheses; the
theorem pays none of their numerical errors. For fixed candidate c,
the displayed load/matrix entry estimate in Section3 follows by
triangle inequalities and must still be summed with weights a_j^-2.
No such coefficient bounds or total weighted-error ledger is supplied.

**Complete finite evidence and limited stop.** Run
`python3 scripts/separation-seven/gaussian-dual-audit-750.py`.
The new certificate is `scripts/separation-seven/gaussian-dual-audit-750.json`.
Unlike748's prime-power generation, this script factors every integer
in each strict active interval. It compares the complete prime-power
maps, all349 ordered event records, all350 ratios, the maximum record,
all20 original assertions, exact-rule constants, every work category
and the witness hash. All2948 checks pass, with no failures. Complete
factorizations and panel evidence are saved. This is exact finite
verification, not numerical sampling or software verification of the
analytic proof. The original748 files and witness remain unchanged.

There are22400 prescribed nodes and510 counted modes per node. The
literal loop uses one phase multiplication, two separate elementary
calls, four coefficient products and two additions, hence9 operations
per visit. The resulting102816000 exceeds the total cap100000000
by2816000 even when all other work is free. Cancellation does not
shorten the explicitly fixed loop. No alternative algorithm or order
is tested or nominated by this audit. Precision, storage, leading-entry
refinement, complete K/moment/value errors, Gaussian norm entries and
weighted-dual errors remain unpaid. A nonpositive lower comparison
would not prove a negative actual Gram. The formula is retained and
this implementation remains parked, with all earlier stops preserved.

No direct mathematical input was added, so the DAG is unchanged.
Inherited analytic-response, neutral-core, IEEE754/Decimal and
unreplayed c_* qualifications persist. Full S3 against both defects,
all-vector minimization, C744q/H2 and actual-Xi/global assembly remain
unresolved. This audit supplies no complete RH candidate.

## Mathlib

Full matching coverage for the scaled signed-measure Gaussian
restriction and specified implementation is not checked. No supporting
Mathlib theorem was used or inspected here. Unknown coverage is not
evidence of absence.
