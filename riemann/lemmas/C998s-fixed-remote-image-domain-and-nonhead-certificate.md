# C998s: The fixed remote image is in V0 and outside the neutral head

## Hypotheses

Use C744v's normalized cosine basis e_n on (0,ell), ell=log(3)/2,
the logarithmic form a=D+S and its two-moment map C. Use C744z's
H0=ker C, V0=V intersect H0, orthogonal projection P0 and COMPLETE
separation14 operator U in (1). The restricted form is a0. Both
single-cell response parities, including j=0, remain in S.

Let f=Zalpha and g=Zbeta be exactly C998r's frozen real pair, with
C999l(1)'s exact completion Z, not its rounded numerical substitute.
The witness is `scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
SHA256 `99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.
Set w=Uf and h=P0w. No input, endpoint, tolerance or witness is changed.
The ambient spaces and independent triple scalars remain complex.

Retain the analytic-response, neutral-core, IEEE754/Decimal and
unreplayed c_* source qualifications of C744v/w/z and C998r. The
regularity proof below needs no positivity or inverse estimate and
does not replay those inherited sources or numerical matrices.

The standard Fourier input is M. Thamban Nair, *Topics in Fourier
Analysis*, July-November2018, Theorem2.5.15 and its full proof,
printed p43/PDF p49, [primary PDF](https://home.iitm.ac.in/mtnair/FS-2018.pdf).
For a complex BV function on the circle it bounds its normalized
nonzero Fourier coefficient by total variation divided by the index.
The projection input is Teschl, *Mathematical Methods in Quantum
Mechanics*, GSM99 author PDF, 12February2009, Theorem1.7 p43,
[primary PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The form realization is already supplied by C744z using Teschl
Theorems2.13/2.18. C744w(12) imports the digamma recurrence/remainder
from [DLMF5.11.2 and5.11(ii)](https://dlmf.nist.gov/5.11).
Assessment710/comparison711 inspected these inputs and approved this
specific preparation. They are cited, not reproved. Only their local
normalization, jump, projection and truncation applications are derived.

For Section3's analytic applicability, use Jiří Lebl, *Guide to
Cultivating Complex Analysis*, v1.10, 5November2026,
Theorem2.4.7 pp49-50 (identity theorem), Theorem3.3.1 pp71-72 and
Corollary3.3.2 p73 (analyticity), Lemma3.4.1 pp81-82 (parameter
integration), and Theorem3.4.5 pp84-85 (locally uniform limits),
[author PDF](https://www.jirka.org/ca/ca.pdf). Assessment712/comparison713
inspected the statements and relevant proof cases. These general
theorems are imported; their local hypotheses are checked below.

## Conclusion

With one-sided endpoint values chosen for its BV representative,

    ||h||_2 < 768 < 2^10,
    ||h||_infinity < 886088 < 2^20,
    Var_(0,ell)(h) < 18140569/5 < 2^22,
    |<h,e_n>| <= 2^24/n, n>=1.                         (1)

Consequently h lies in V0. Moreover

    (I-P_<512)h != 0,     <Uf,h> = ||h||_2^2.           (2)

The first assertion in(2) is a structural non-head certificate at the
single preselected shift n=3125. It does not give a numerical lower
bound or identify one nonzero scalar cosine coefficient. Completeness
implies at least one such coefficient with n>=512 is nonzero.

For the single sufficient truncation N=2^136, Section4 pays all
TRUNCATION errors of an ideal six-entry Hermitian surrogate by less
than1e-6 per entry. Its largest bound is less than2^-25. This is NOT
a complete entry certificate: evaluation of the retained entries,
continuous responses, moments, diagonal values and rounding is unpaid.
The specified direct U-coefficient subtask alone has334*512*N shift
primitive evaluations, approximately1.49e46. No such batch was run.
This parks this coarse direct BV prescription; it is not a necessary
complexity lower bound or a claim that no affordable method exists.

Separate audit714 in Section6 repairs an exit-location error and
upholds (1)-(2) and the stated ideal truncation bounds under the
retained contracts. This is a local REPRODUCTION/specialization,
not a result beyond the general sources checked. No Gram sign, full S3 sign,
higher/mixed endpoints, C744q/H2 or actual-Xi/RH conclusion follows.

## Proof

### 1. Full image and exact projection bounds

All510 free coordinates of each frozen vector were summed as exact
rationals. The complete l1 sums are respectively

    23595897189007350019277/9444732965739290427392 < 3,
    11797948594503673988871/4722366482869645213696 < 3.

Every free coordinate is nonzero. C999l's completion factors r_n
satisfy0<r_n<1: for odd n>=3 this follows by comparing denominators
with index1; for even n>=2, nu_n/nu_0=sqrt2<2 and k_n>10 give
r_n=sqrt2/(1+4k_n^2)<2/401<1/200. The two completed coordinates
are minus the same-parity r_n-weighted sums, so their absolute values
sum to less than the full free l1 sum. This includes every coordinate
and proves that each full raw vector has l1 norm<6. Since
1/2<ell<3/5 and3<pi<4, nu_n<2 and k_511<4088. It follows that

    ||f||_2,||g||_2<6,  ||f||_infinity<12,
    ||f'||_infinity<49056<50000.                         (3)

Use every334 prime powers in C744z(1). The small certificate below
independently enumerates them by exact integer tests. For each such n,
1024<n<4096, sqrt(n)>32 and Lambda(n)<=log(n)<9, so its weight is
less than9/32<1/3. Their total weight is less than112. The zero-delay
n=2187 identity term is included. For each translated, zero-extended
f, its interval variation is bounded by ell||f'||_infinity+2||f||_infinity
<30024. This bound includes every interior jump and is still valid
for the zero-delay term. No H1 assertion across a jump is made.

For t=14ell+x-y>=13ell>13/2, put q=exp(-2t). The entire kernel and
its absolute first x derivative are

    K14(x,y)=exp(-5t/2)/(1-q),
    sum_(j>=1)c_j exp(-c_j t)
       =exp(-5t/2)[(5/2)/(1-q)+2q/(1-q)^2].             (4)

Here q<1/4 and exp(-5t/2)<1/16, so both quantities are less than1.
The same geometric convergence with any fixed power of c_j justifies
each derivative, uniformly on the square. In particular ||K14||<1
by the row/column integral bound, its image of f has supremum<8,
and its variation is less than ell^2*12<5. Hence

    ||U|| <113,  ||w||_2<678<768,
    ||w||_infinity<1352,  Var(w)<112*30024+5=3362693.     (5)

Let u_+(x)=exp(x/2), u_-(x)=exp(-x/2), and m=(<w,u_+>,<w,u_->)^t.
These are bounded L2 moments; no numerical moment residual is used.
Their Gram matrix and determinant are exactly

    G=[[exp(ell)-1, ell],[ell,1-exp(-ell)]],
    det G=2 cosh(ell)-2-ell^2 >= ell^4/12 >1/192.        (6)

The nonnegative cosh series proves the displayed strict lower bound.
Each entry of G has modulus<1, and ||u_+||_2,||u_-||_2<1.
Thus each inverse entry has modulus<192, |m_+|,|m_-|<768,
and both coordinates of t=G^-1m have modulus<294912.
The cited projection theorem, or the defining orthogonality equations,
now gives exactly

    h=w-t_+u_+-t_-u_-,       Ch=0.                     (7)

This is the full L2 projection, not head completion or an energy
projection. Since exp(ell/2)<3/2, the correction has supremum<884736
and variation less than(3/5)(3/4)*589824=1327104/5. Together with(5)
this gives the variation and supremum in(1). Orthogonal-projection
contraction gives ||h||_2<=||w||_2<768. No approximate moment or
projection coefficient is being asserted to equal its exact value.

### 2. Fourier normalization and the full logarithmic domain

Define the even2pi-periodic BV representative F(theta)=h(ell|theta|/pi)
for -pi<=theta<=pi, using the one-sided traces at0 andell. Reflection
doubles the interior variation. There is no seam jump at +/-pi or
reflection jump at0 because the traces match. Each shifted-function
jump was already included in(5). Hence Var_circle(F)<=2 Var(h).

For n>=1 its normalized Fourier coefficient satisfies

    Fhat(n)=ell^-1 integral_0^ell h(x)cos(n*pi*x/ell) dx,
    <h,e_n>=sqrt(2ell) Fhat(n).

Nair's cited BV theorem and sqrt(2ell)<2 therefore give
|<h,e_n>|<=4 Var(h)/n<2^24/n. This explicitly matches the theorem's
periodic convention and includes all jumps. Since
sum_(n>=1)(1+log(n+2))/n^2 converges, the COMPLETE defining weighted
coefficient series for V converges. Equation(7) then gives h in V0.
This does not identify V0 with a compact-smooth or generator domain.

### 3. The frozen3125 structural certificate

Before evaluating this test, draft712 fixed n=3125=5^5. It obeys
3^13<3125^2<3^15 and3125>3^7. Thus its translated zero extension
starts at x0=log(3125)-14ell in(0,ell), with nonzero coefficient
log(5)/sqrt(3125). An entrance from any other shift has a different
location. Coincidence with an exit from an integer m would imply

    log(3125)-14ell=log(m)-13ell,
    3125/m=sqrt3, hence 3125^2=3m^2,

which is impossible modulo3. Indeed the shift with index m is
supported where log(m)-14ell<x<log(m)-13ell. This corrects the
original712 exit formula, as recorded in Section6. Every interior
entrance has m>2187 and every interior exit has m<2187; m=2187
is the identity with no interior boundary. There are finitely many
boundaries. Choose a disk centered at x0 of radius r>0 smaller than
the distance to every other boundary and to both cell ends. Each other
shifted term has a fixed active indicator on the real diameter, and
extends there as either the entire cosine polynomial or zero.

The full continuous image is analytic there as well: the series in(4)
converges locally uniformly for complex x in this disk, uniformly in
y in[0,ell], since Re(14ell+x-y)>13ell>0. Its terms, including
any fixed-order x derivative, have geometric majorants multiplied
by a fixed power of c_j. Lebl Theorem3.4.5 gives a holomorphic
kernel jointly continuous with y. The finite cosine profile is
continuous, so after y=ell s the hypotheses of Lemma3.4.1 hold
on the disk times[0,1]. Integration preserves holomorphicity.
The correction in(7) is entire. Therefore
locally h is an analytic function plus

    [log(5)/sqrt(3125)] 1_(x>x0) f(x-x0).               (8)

If h were equal almost everywhere to ANY finite cosine polynomial,
subtracting the other analytic terms would give an analytic function
zero on the left open half-neighborhood. Continuity first upgrades
the almost-everywhere equality there; Lebl Theorem2.4.7 applies to
the connected complex disk and its interior accumulation of zeros,
and makes
it identically zero throughout the neighborhood. Equation(8) would
force f to vanish almost everywhere, and by continuity everywhere,
on a right open interval, hence identically by the same theorem, since
f is a finite cosine polynomial. This contradicts its nonzero free
coefficients. The proof also covers f(0)=0 of any finite order;
it assumes neither a nonzero endpoint value nor an unverified jump
amplitude. In particular h is outside the raw512-mode head, and
therefore outside its neutral subspace parametrized by C999l's Z.

Finally w=h+(I-P0)w is an orthogonal decomposition, giving
<Uf,h>=<w,h>=||h||_2^2 in the stipulated first-slot-linear convention.
This exact simplification does not sign the other two pairings or S3.

### 4. A costed truncation, with the complete finite-entry plan unfinished

Let P_N retain n=0,...,N-1, h_N=P_Nh, B=2^24 and H=2^10.
The coefficient bound gives

    ||h-h_N||_2^2 <= B^2/(N-1)=:epsilon_N^2.            (9)

For completeness the required logarithmic bound follows from the
already assessed C744w(12), with z=1/4+ik_n/2 and recurrence64.
Here |z+64|>=64.25, |z+j|>=1/4, k_n<8n for n>=1, k_0=0,
and its remainder is<1.
For every n>=0 the shifted argument has real part64.25 and
|arg(z+64)|<pi/2, so C744w(12)'s undifferentiated sector bound
applies uniformly. Also 1<|z+64|<65+4n,
|Re log(z+64)|=log|z+64|, and the64 recurrence summands have
total absolute value at most256. Using log(pi)<2 gives

    |d_n| <= log(65+4n)+260 < log(n+2)+512.

This uses an absolute bound on the recurrence, not a differentiated
asymptotic. For x>=1 the integrand (512+log(x+2))/x^2 decreases,
and log(x+2)<=log x+2. Consequently

    sum_(n>=N)|d_n| |h_n|^2
       <= B^2[515+log(N-1)]/(N-1).                     (10)

C744v's FULL bounded-response bound is ||S||<64: a=ell/2 lies in
(1/4,3/10), 1-exp(-a)>=a/(1+a)>1/5 and4a+2pi<46/5.
Orthogonality gives ||h_N||<=||h||<H. Thus, retaining every cross
product between the retained and omitted parts,

    |<Sh,h>-<Sh_N,h_N>| <=64(||h||+||h_N||)epsilon_N
                         <=128H epsilon_N.             (11)

There is no parity or independence assumption in this bound.
Choose the single sufficient cutoff N=2^136. Then

    epsilon_N<2^-43,
    logarithmic tail in(10)<2^-77,
    response difference in(11)<2^-26.                 (12)

The remaining entries of C744z(5) can use the ideal surrogates
<Tg,h_N> and ||h_N||^2; the original f,g diagonal entries and
<Tf,g> are unchanged. By C744v's ||T||<4.71 and(3), their errors
are respectively<30epsilon_N<2^-38 and epsilon_N^2<2^-87.
Hermitian conjugates have identical errors. The remote surrogate
uses(2), NOT the generally false identity <Uf,h_N>=||h_N||^2.
In particular h_N need not be neutral. Its diagonal surrogate is
the unrestricted form a(h_N,h_N), not an asserted a0 value or the
energy of an admissible truncated triple. Equations(9)-(12) compare
its individual scalar entries to those of the original actual triple.

These bounds pay all infinite OUTPUT truncation errors, but assume
the retained scalar expressions are evaluated exactly. To evaluate
them directly using C744w's shift primitives, one possible subtask
would loop over N outputs, all334 shifts and all512 input modes to
form the prime part of Uf. It has exactly

    334*512*2^136
      =14896897792618456258545859806129105485994917888

shift-primitive evaluations. The analogous Tg subtask adds16*512*N.
Storing h_N in this prescription takes N coefficient slots, already
2^140 bytes if one were to allow only16 bytes per slot; that byte
figure is illustrative and is NOT a sufficient precision specification.
Streaming can reduce storage but does not execute this fixed direct
loop with fewer primitive calls. Faster reorganizations are unassessed.

This is already an unaffordable sufficient subtask. Stop before
deriving or executing its full batch. Finite S entries with both
complete response parities and j=0, the full K14/K7 contributions,
projection moments and their tails, D values and all finite arithmetic
errors/precision remain unpaid. No total all-entry work bound exists
in this result, and the required1e-6 certificate was NOT completed.
The count is for this chosen sufficient prescription only, not a
lower bound for the mathematical problem or evidence of a negative
Gram. An affordable direct physical or analytic evaluation would
require a separately assessed, materially improved implementation.

### 5. Small exact evidence and retained limits

Run `python3 scripts/separation-seven/remote-image-preparation-712.py`.
Its full certificate is `scripts/separation-seven/remote-image-preparation-712.json`.
All24 checks pass. It sums every frozen free coefficient, verifies the
witness hash, enumerates all334 prime powers, checks the rational
bound comparisons, and records the exact truncation counts. No large
coefficient vector, response matrix, eigenvalue or Gram is computed.
The analytic and non-head arguments above are prose proofs, not claims
of software verification. Section6 records the separate audit714;
the original712 script and certificate are preserved unchanged.

The old617/603/635/640/652/705 stops are unchanged. This result does
not reopen an inverse/reference repair or place f,g or h inside a
defect spectral window. It supplies two relevant prerequisites for
an actual fixed signed test, leaving its feasible evaluation unresolved.
All inherited source qualifications and global gaps persist.

### 6. Separate conceptual audit — 13 November2026, step714

Invocation-start SPECIALIZE assessment712, approved in comparison713,
licenses this audit. It upholds the fixed domain, non-head and ideal
truncation assertions after correcting one mathematical proof error.
No witness, cutoff, tolerance, endpoint or operator was changed.

**Correction and analytic isolation.** The original Section3 wrote
the exit of f(x+14ell-log m) as15ell-log m and inferred
3125m=3^(29/2). That is not this shift's exit equation. The corrected
support and collision equations are now in Section3. Since3125^2 is1
modulo3, no integer exit can coincide with its entrance. Distinct
entrances have distinct integer indices. This repairs the argument,
rather than using a true irrationality claim about the wrong equation.
The finite list also verifies all334 actual boundary cases. The disk
and uniform kernel arguments in Section3 supply the cited analytic
theorems' full local hypotheses. Equality almost everywhere is upgraded
on each open real interval by continuity before using the identity
theorem. Neither a nonzero endpoint value nor a first nonzero derivative
is assumed. The nonzero finite profile cannot vanish on a right interval.

**Exact coordinates, projection and domain.** The audit contracts all
1020 frozen free coordinates, separately by parity, without importing
the712 script. C999l(1)'s exact factors are used symbolically: the
same factor kills both +/- moments in each parity. No rounded head
completion is substituted. The free l1 sums in Section1 are reproduced
exactly; all510 coordinates of each vector are nonzero. The stated
r_n inequalities bound both completed coefficients, including every
term, and give (3).

For arbitrary complex w, the real exponentials u_+,u_- represent C
under the first-slot-linear convention. If h=w-sum_j t_j u_j, then
<h,u_i>=m_i-sum_j G_ij t_j because the real Gram matrix is symmetric.
Consequently t=G^-1m, with no conjugation of m. Formula(6), its positive
determinant bound and the exact orthogonality equations justify (7)
and L2 contraction; no source coercivity or energy inverse is used.
The geometric derivative bound in(4) holds uniformly on the full
closed square, so its image variation is bounded. Each zero-extended
shift's two possible jumps is paid in(5); the identity shift is also
retained. Reflection doubles interval variation and adds no seam
jump because the one-sided traces coincide at each identified end.
The normalization of Nair's Fourier coefficient is exactly the one in
Section2. Its bound gives the complete logarithmically weighted
summability, and exact Ch=0 then gives V0 membership. This remains
a form-domain assertion, with no H1 or generator-domain claim.

**Independent complete arithmetic.** Run

    python3 scripts/separation-seven/remote-image-preparation-audit-714.py

The certificate is `scripts/separation-seven/remote-image-preparation-audit-714.json`.
It factors every integer candidate in the active squared interval,
independently of712's prime-generation algorithm, and compares the
entire334-element list. It includes2187 and the frozen3125, and checks
all possible entrance/exit collisions at the selected entrance.
Every one of712's24 checks, all bound fractions and every work count
are independently reproduced. All53 audit checks pass, with no
failures. Every frozen coordinate, candidate factorization and active
boundary comparison is saved, not sampled. The witness and original
script/certificate pins are retained. Small exact exponential-series
comparisons also check the coarse ell, kernel and logarithm bounds.
These finite checks do not purport to prove the analytic prose by software.

**Infinite-index and surrogate scope.** The digamma remainder is
used in its positive-real-part sector for all indices, including0.
The bound log(65+4n)<log(n+2)+4 and260+4<512 gives the stated
uniform diagonal majorant. The function(512+log(x+2))/x^2 decreases
for x>=1: multiplying its derivative by x^3 gives
x/(x+2)-2(512+log(x+2))<0. Integral comparison from N-1 and
log(x+2)<=log x+2 give exactly(10). Bounded-S continuity in(11)
retains all mixed products. The exact reproduced diagonal error is
less than2^-25<1e-6; the other entries satisfy their stated bounds.

The true h is neutral, so the original remote pairing equals||h||^2
by P0 orthogonality. The cosine projection P_N is separately orthogonal,
giving ||h||^2-||h_N||^2=||h-h_N||^2. These two distinct uses of
orthogonality justify the ideal remote surrogate; they do not assert
that h_N is neutral or that <Uf,h_N>=||h_N||^2. The surrogate diagonal
is a(h_N,h_N) in the unrestricted form. No truncated admissible triple
or Gram sign is inferred from this array of approximate scalar entries.

The334*512*2^136 count is a sufficient specified loop count, not a
complexity lower bound. Full finite response, moment, diagonal and
rounding errors remain unpaid. Thus audit714 preserves the direct-cost
stop712 and all unfinished entry work. It supplies a local proof repair
and trusted prerequisites, not an affordable certificate, new general
theorem, full S3 sign or RH candidate. All inherited qualifications
persist. The existing DAG inputs are unchanged; no new lemma is added.

## Mathlib

Full matching Mathlib coverage for this fixed projected profile,
its non-head structural certificate and its quantitative truncation
bounds has not been checked. The cited BV Fourier and projection
theorems are standard supporting inputs, not a matching theorem for
this specialization. No absence claim or new formal verification is made.
