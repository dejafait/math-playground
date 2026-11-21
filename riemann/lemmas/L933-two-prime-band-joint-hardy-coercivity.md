# Lemma 933: fixed two-prime-band joint Hardy coefficient coercivity

## Hypotheses

Use the actual Hardy function and smooth real Hardy phase of L637,
with Z(t)=exp(i theta(t)) zeta(1/2+it) on the real axis. Fix
w>=0 in C_c^infinity((0,1)), with integral w=1. As in L928, put

    L=log T, N=floor(T^(1/5)), T<=X<=2T,
    w_XT(t)=w((t-X)/T), ||f||_T^2=integral w_XT(t)|f(t)|^2 dt,
    P_s(t)=sum_(n<=N)c_(s,n)n^(-it), s in {-1,+1},
    U(t)=sum_(s=+/-1) Z(t+s/L)P_s(t),
    S=sum_(s=+/-1)sum_(n<=N)|c_(s,n)|^2.

The coefficient vectors are arbitrary complex vectors and may depend
on T and X. Every constant and sufficiently-large-T onset below is
independent of X and these vectors. Positive-base powers use real
logarithms. No RH, zero simplicity, nonvanishing of Z, signed
realization, or mixed positivity is assumed.

The two prime sets are exactly

    B_1={p prime:T^(22/100)<=p<=T^(24/100)},
    B_2={p prime:T^(27/100)<=p<=T^(29/100)}, B=B_1 union B_2,
    K={p*m:p in B, 1<=m<=N}, H=T^(49/100).

Here and below K is a set of output integers, not a multiset. Define
the finite analysis map on L2(w_XT dt) by

    (E f)_k=T^(-1) integral w_XT(t)f(t)exp(-i theta(t))k^(it) dt.

The standard inputs, within the previously assessed scope, are:

1. The undifferentiated Riemann–Siegel formula, including cutoff
   crossings, in Titchmarsh–Heath-Brown, *The Theory of the Riemann
   Zeta-Function*, second edition (1986), Section 4.17, (4.17.4),
   p89; also [Hughes, July2017, Theorem2.2, pp18–19](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20).
   L637 supplies this normalization and the smooth gamma-phase
   bounds. On intervals comparable to T these include

       theta'(t)=1/2 log(t/(2*pi))+O(T^(-1)),
       theta''(t)=O(T^(-1)),
       d^r/dt^r exp(i[theta(t+s/L)-theta(t)])=O_r(T^(-r))

   for fixed r and s=+/-1. The last assertion uses L622 Section 2,
   (7)–(8), with b=(s,0,0,0), inherited in L637 Section 4's
   paragraph following (19). L637(19)–(20) themselves describe a
   moment and its error, not these derivative estimates. Only r<=2
   is used; the explicit specialization is checked in the audit below.
   No derivative of a Riemann–Siegel remainder is taken.
2. The separated-frequency Hilbert inequality of Montgomery–Vaughan,
   [*Hilbert's Inequality*, JLMS (2)8 (1974), 73–82, Theorem2 and
   Section4](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
   DOI10.1112/jlms/s2-8.1.73. Use the clean uniform-spacing statement
   in the authors' [*Multiplicative Number Theory II*, served draft,
   TheoremG.14, printed p422](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=434):
   the off-diagonal bilinear Hilbert form for distinct real
   frequencies separated by delta>0 is bounded by
   (pi/delta)||x||_2||y||_2. The arbitrary complex-vector statement
   is needed. No exact constant is extracted from the garbled
   original-paper formulas; no publication date is assigned to the draft.
3. Rosser–Schoenfeld, [*Approximate formulas for some functions of
   prime numbers*, Illinois J. Math.6 (1962), Theorem5, (3.17)–(3.18),
   printed p70](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=7),
   DOI10.1215/ijm/1255631807. Only its consequence
   sum_(p<=x)1/p=log log x+B+o(1) is imported, not an independently
   verified effective constant.
4. Finite Möbius inversion, [DLMF27.5.2–3](https://dlmf.nist.gov/27.5#E3)
   (citing Apostol, 1976, Chapter2); the divisor bound
   tau(m)<=D_delta*m^delta for each fixed delta>0, from
   [Tao, *The divisor bound*, (3)](https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/);
   and the finite p=2 weighted Schur test in
   [Grafakos–Torres, *A multilinear Schur test and multiplier
   operators*, Section2, p2](https://grafakos.missouri.edu/preprints/multilinear_schur.pdf).
   The scalar and Schur inputs and their scope are reused from audited
   L926. Its upward divisor transform is not substituted for the
   different downward transform proved below.
5. Endpoint-sensitive integration by parts, [Tao, 247B Notes8,
   Lemma2.3 and (4), pp4–5; smooth-amplitude passage and Lemma2.6,
   p6](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf#page=4).
   The interval boundary terms and the scaled amplitude bounds are
   checked below. A sharp internal cutoff receives only one
   integration by parts, not smooth-window rapid decay.

The invocation-start EXPLORE assessment is
drafts/literature/2026-11-09-two-prime-band-extraction-test-22.md;
its inspected source cases and duplicate/failure comparison are in
drafts/literature/2026-11-09-two-prime-band-joint-extraction-21.md.
The standard results above are imported, not reproved. L928 is used
for its charged main-form comparison only after the actual norm has
been bounded. L737 is window/context provenance through L928, not a
separate analytic input here. L925, L929, L930 and L932 are not inputs.

## Conclusion

There are fixed beta,C_B,C_R,c>0 and one sufficiently-large-T onset,
uniform in X and both coefficient vectors, with the following properties.
Let A c be E applied to precisely the positive-phase Riemann–Siegel
terms whose product j*n equals the selected output k. Retain their
actual cutoff indicators in this definition. Let R c=E U-A c.
Then

    ||E f||_2^2 <= (C_B/T)||f||_T^2,                         (1)
    ||A c||_2^2 >= beta N^(-1/8) S,                         (2)
    ||R c||_2 <= C_R T^(-1/4) sqrt(S).                      (3)

In particular,

    ||U||_T^2 >= c T N^(-1/8) S
               >= c T L N^(-1/4) S                         (4)

eventually. The second inequality has its own, still common, onset.
The principal squared scale exceeds the requested scale by the factor
N^(1/8)/L, which tends to infinity. The residual-to-principal norm
ratio is O(T^(-19/80)). These are not effective small-height claims.

L928's exact main form M consequently satisfies, possibly increasing
the onset and decreasing c,

    M(c_-,c_+) >= c T N^(-1/8) S >= c T L N^(-1/4) S.       (5)

This establishes the joint coefficient margin required in that local
comparison; it does not assert the stronger normalized contraction
L928(11). The separate conceptual audit below, completed 9 November
2026, step26, validates (1)–(30) under the named imports and corrects
the phase citation. The original proof's classification is
POTENTIALLY_NEW only in the limited sense
that the recorded search did not supply the combined estimate; no
certified originality or improvement beyond all literature is claimed.
This is not a candidate resolution of RH. Signed realization, signed
transfer and actual-Xi all-degree mixed positivity remain unresolved.

## Proof

### 1. Integer geometry and the bounded analysis map

All primes in B exceed N eventually. If p*m=q*n with p,q in B and
m,n<=N, then p divides q*n. Since p>n, primality forces p=q,
and then m=n. Thus the indexing by pairs (p,m) is injective, including
across the two disjoint prime bands. Also

    max K <= N*T^(29/100) <= H, |K| <= N*|B| <= H.          (6)

The last bound uses only |B|<=floor(T^(29/100)).

Distinct integers k,l<=H have |log k-log l|>=1/H, by integrating
1/u between them. The cited Hilbert inequality, applied to each of
the two endpoint terms in the integrated off-diagonal exponential
sum, gives for arbitrary complex z and any interval I of length T

    integral_I |sum_(k in K) z_k k^(-it)|^2 dt
        <= (T+2*pi*H) sum_k |z_k|^2.                       (7)

Indeed the diagonal integral is T sum|z_k|^2; each endpoint Hilbert
form has coefficients z_k times unimodular endpoint phases, so its
absolute value is at most pi*H sum|z_k|^2. This is precisely the
finite-frequency specialization of the imported theorem.

Take I=[X,X+T]. Multiplication by exp(i theta(t)) preserves modulus,
and the weight is at most ||w||_infinity. Duality for the finite
coefficient space, followed by weighted Cauchy–Schwarz, therefore gives

    ||E f||_2^2 <= ||w||_infinity*(T+2*pi*H)/T^2 * ||f||_T^2.

Since H<=T for T>=1, (1) holds with
C_B=(1+2*pi)||w||_infinity>0. The same argument at the integer
frequencies n<=N gives, with this same permissible constant,

    ||P_s||_T^2 <= C_B T ||c_s||_2^2.                     (8)

No orthogonality assertion about a discarded Riemann–Siegel term
has been used.

### 2. Exact principal coefficient map, including all collisions

Put h_s=s/L and J_s(t)=floor(sqrt((t+h_s)/(2*pi))). The actual
Riemann–Siegel expansion is

    Z(t+h_s)=sum_(j<=J_s(t)) j^(-1/2)
       [exp(i theta(t+h_s)) j^(-it-is/L)
        +exp(-i theta(t+h_s)) j^(it+is/L)] + r_s(t),
    |r_s(t)|<=C T^(-1/4)                                 (9)

uniformly on I, including cutoff crossings. Eventually

    2H <= sqrt((T-1/L)/(2*pi)).                           (10)

This follows from 1/2-49/100=1/100>0. Thus every integer j<=2H
is below J_s(t) throughout the window for both shifts.

For k=p*m, the equality j*n=k with n<=N forces n|m, because
p>N>=n. Conversely each n|m gives j=p*m/n<=H, and (10) proves
that its cutoff indicator is identically one. Hence the actual
principal map, with no cutoff deleted by assumption, is exactly

    alpha_s=T^(-1) integral_I w_XT(t)
                       exp(i[theta(t+h_s)-theta(t)]) dt,
    B_(s,m)=sum_(n|m) (m/n)^(-1/2-is/L)c_(s,n),
    (A c)_(p*m)=p^(-1/2)
                sum_(s=+/-1) alpha_s p^(-is/L) B_(s,m).    (11)

Every divisor collision is retained inside B_(s,m). There is no
shift of P_s or of its coefficients. By the theta' estimate and the
mean value/integral formula on the segment from t to t+h_s,

    theta(t+h_s)-theta(t)=s/(2L)*log(t/(2*pi))+O(1/(T L))
                         =s/2+O(1/L),                    (12)

uniformly on I and in X. The O(1/(T L)) may absorb the smaller
O(1/(T L^2)) Taylor term. Since T^(-1) integral w_XT=1,
(12) gives alpha_s=exp(is/2)+O(1/L), hence |alpha_s|>=1/2
eventually. The exact alpha_s in (11) is retained, not replaced by
its limiting phase.

### 3. Prime-band separation and the correct divisor inverse

Write M_j=sum_(p in B_j)1/p. The imported reciprocal-prime asymptotic
gives M_1->log(12/11) and M_2->log(29/27). Inclusion of a possible
prime exactly at a lower endpoint changes a strict-endpoint difference
by at most T^(-22/100) or T^(-27/100), respectively. Thus eventually

    min(M_1,M_2)>=m_*=1/2*min{log(12/11),log(29/27)}>0.    (13)

For p in B_1, q in B_2 put u=log p/L and v=log q/L. Then
3/100<=v-u<=7/100. For arbitrary y_-,y_+ the two-row matrix with
rows (exp(iu),exp(-iu)) and (exp(iv),exp(-iv)) has squared
Frobenius norm 4 and determinant of modulus 2 sin(v-u).
Its positive Hermitian square has trace 4 and determinant
4 sin^2(v-u). Its smaller eigenvalue is at least its determinant
divided by its trace, so

    |e^(iu)y_-+e^(-iu)y_+|^2
     +|e^(iv)y_-+e^(-iv)y_+|^2
       >=sin^2(3/100)(|y_-|^2+|y_+|^2).                  (14)

Here sin is increasing on [3/100,7/100], a subset of (0,pi/2).
Multiply (14) by 1/(p*q), sum over both prime bands, and bound the
left side by max(M_1,M_2) times the combined weighted sum. Dividing
by this positive maximum yields

    sum_(p in B) (1/p)|p^(i/L)y_-+p^(-i/L)y_+|^2
      >=m_* sin^2(3/100)(|y_-|^2+|y_+|^2).                (15)

Apply (15) for each m to y_s=alpha_s B_(s,m), and use
|alpha_s|>=1/2. The injective output indexing in (6) gives

    ||A c||_2^2 >= kappa sum_s ||B_s||_2^2,
    kappa=m_* sin^2(3/100)/4>0.                           (16)

For clarity the inverse orientation is verified directly. The function
a_s(d)=d^(-1/2-is/L) is completely multiplicative, so finite
Möbius inversion gives

    c_(s,m)=sum_(d|m) mu(d)d^(-1/2-is/L) B_(s,m/d).        (17)

Substituting (11) into (17), the coefficient for c_(s,m/r) is
a_s(r) sum_(d|r)mu(d), which is 1 at r=1 and 0 otherwise.
All divisors stay within the finite prefix. Thus this identity does
not use an inverse with the multiples/divisors orientation reversed.

The absolute inverse matrix has entries
K_(m,n)=1_(n|m)|mu(m/n)|sqrt(n/m). Choose positive Schur weights
h_m=m^(-1/2). Its weighted row and column sums satisfy, respectively,

    sum_n K_(m,n)h_n/h_m =sum_(n|m)|mu(m/n)| <=tau(m),
    sum_m K_(m,n)h_m/h_n
        =sum_(d<=N/n)|mu(d)|/d <=1+log N.                 (18)

Take delta=1/16 in the imported divisor bound. The elementary
integral inequality log x<=(x^delta)/delta for x>=1 gives
1+log N<=17 N^(1/16). The cited weighted Schur theorem now gives
the squared inverse norm at most 17 D_(1/16) N^(1/8). Complex
phases are harmless because the absolute matrix dominates (17)
coordinatewise. Therefore, simultaneously for both s,

    ||B_s||_2^2 >= [17 D_(1/16)]^(-1) N^(-1/8)||c_s||_2^2.

Together with (16) this proves (2) with
beta=kappa/[17 D_(1/16)]>0. No epsilon-to-zero uniformity or
unproved two-channel inverse theorem was invoked.

### 4. All positive-phase off-products, with sharp cutoffs charged

For an output k, a positive-branch off-product has q=j*n!=k and
normalized integral

    I^+_(s,j,n,k)=T^(-1) integral_(I intersect [2*pi*j^2-h_s,infinity))
       w_XT(t) eta_s(t) exp(it log(k/q)) dt,
    eta_s(t)=exp(i[theta(t+h_s)-theta(t)]).                (19)

The separate coefficient is c_(s,n)j^(-1/2-is/L).
Split these off-products into q<=2H and q>2H. This partitions every
off-product and changes neither selected prime band nor dictionary.

If q<=2H, then j<=q<=2H, so (10) removes the indicator by a proved
uniform inequality. The amplitude w_XT*eta_s has compact support
inside I. Its first two derivatives are O_w(T^(-1)) and O_w(T^(-2))
by the imported smooth phase bounds and the product rule. Since
k,q are distinct integers with max(k,q)<=2H,
|log(k/q)|>=1/(2H). Two integrations by parts with zero endpoint
terms give

    |I^+_(s,j,n,k)|<=C_w/(T^2 |log(k/q)|^2)
                   <=C_w H^2/T^2.                        (20)

In detail the second derivative has L1 norm O_w(T^(-1)); the
normalizing factor T^(-1) gives the displayed T^(-2).
Using sum_(j<=2H)j^(-1/2)<=C sqrt(H),
sum_(s,n)|c_(s,n)|<=sqrt(2N)*sqrt(S), and |K|<=H, the entire
low-product output vector is bounded by

    ||R^+_low c||_2 <= C_w H^3 sqrt(N) T^(-2) sqrt(S)
                     <=C_w T^(-43/100) sqrt(S).           (21)

Overcounting all j<=2H for each n only increases this upper bound;
the resonant q=k terms themselves were excluded before (20).

If q>2H, then |log(k/q)|>=log 2. The domain in (19) is an interval
or is empty; there is at most one internal starting endpoint.
One integration by parts gives the bound C_w/T: both endpoint
values of the amplitude are bounded, and its derivative has L1
norm O_w(1). This explicitly includes a possible nonzero amplitude
at t=2*pi*j^2-h_s. It is not a twice-integrated smooth cutoff.
Every nonempty term has j<=J_*=ceil(2 sqrt(T)) eventually, since
t<=3T and |h_s|<=1. Thus

    sum_(j<=J_*) j^(-1/2)<=C T^(1/4),
    ||R^+_high c||_2
       <=C_w sqrt(H)*sqrt(N)*T^(1/4)*T^(-1)*sqrt(S)
       <=C_w T^(-81/200) sqrt(S).                        (22)

The estimate covers products of every size above 2H, including all
moving-cutoff contributions. No other positive-phase terms remain.

### 5. The complete negative phase and the Riemann–Siegel error

For the negative branch the analogous oscillatory integral has phase

    phi(t)=-theta(t+h_s)-theta(t)+t log(j*k/n).            (23)

Its coefficient is c_(s,n)j^(-1/2+is/L), and its integration
domain is the same interval as in (19). Uniformly for all indices
that can occur, j<=J_*, k<=H, n>=1, and t>=T. The theta' estimate
gives

    phi'(t)=log(2*pi*j*k/(n*t))+O(T^(-1))
            <=-(1/100)L+C,
    |phi''(t)|<=C/T.                                    (24)

The first inequality uses j*k/(n*t)<=C T^(-1/100).
At one common onset, phi'<=-L/200 throughout I. Thus no omitted
negative-branch term has a stationary point on the relevant interval.

For explicit boundary control, one integration by parts for amplitude
w_XT bounds the unnormalized integral by a constant times

    ||w||_infinity/L
      + (integral_I |w_XT'(t)| dt)/L
      + (integral_I w_XT(t)|phi''(t)| dt)/L^2 = O_w(1/L).

The first term includes both interval endpoints, including an internal
cutoff endpoint. After normalization it is O_w(1/(T L)). Summing
all j,n,s and all outputs exactly as in (22) proves

    ||R^- c||_2 <= C_w T^(-81/200) L^(-1) sqrt(S).         (25)

Finally let V(t)=sum_s r_s(t)P_s(t). The undifferentiated bound
in (9), triangle inequality, (8), and Cauchy–Schwarz for the two
coefficient norms give

    ||V||_T <= C_w T^(1/4) sqrt(S).

Applying (1) to this actual remainder, with no expansion or
differentiation of r_s, yields

    ||E V||_2 <= C_w T^(-1/4) sqrt(S).                    (26)

Equations (21), (22), (25), (26) exhaust the definition R=E U-A:
positive off-products, the whole negative branch, and the original
Riemann–Siegel remainder. Their sum is bounded by C_R T^(-1/4)
sqrt(S) for T sufficiently large, proving (3). A finite number of
common onsets suffices; none depends on either coefficient vector.

### 6. Actual and required margins

Take a_T=sqrt(beta) N^(-1/16) and b_T=C_R T^(-1/4).
Then

    b_T/a_T <= (C_R/sqrt(beta))*T^(-1/4)*N^(1/16)
              <=C T^(-19/80) ->0.                        (27)

Consequently b_T<=a_T/2 eventually. For S>0 the reverse triangle
inequality in the finite output space, followed by (1), gives

    ||U||_T^2 >= (T/C_B)||E U||_2^2
               >= beta/(4 C_B) T N^(-1/8) S.              (28)

For S=0 every vector and expression is zero and the same conclusion
holds. Since N>=T^(1/5)/2 eventually,

    N^(1/8)/L >= 2^(-1/8) T^(1/40)/log T ->infinity.      (29)

Thus (28) implies exactly (4), with c=beta/(4 C_B), after increasing
the onset so that N^(1/8)>=L. In the assessment's certificate notation,

    (a_T-b_T)^2/C_B >= beta/(4 C_B) N^(-1/8)
                         >= c L N^(-1/4).

Both the actual and required scales have been compared; no positive
prime-mass constant alone was claimed to produce the logarithmic factor.

Only now use L928(3). Its full error obeys

    |E_L928|/[T N^(-1/8) S]
        <=C_w T^(-13/80)N^(1/8) <=C_w T^(-11/80) ->0      (30)

for S>0. Subtracting this error from (28) proves (5), with a smaller
positive c if necessary. At S=0 it is again immediate. This use of
L928 is downstream of the independently established actual norm, so
its previously missing joint positivity has not been assumed.

All arithmetic sums in the extraction and inverse are finite. The
only asymptotics invoked have fixed exponents and uniform phase/weight
bounds on comparable positive heights. Sharp cutoffs and both Hardy
phases are explicitly accounted for. The proof supplies an unsigned
coefficient norm, not any unproved Xi sign or signed transfer estimate.
Written 9 November 2026, step24; separately audited below in step26.

### Separate conceptual audit — 9 November 2026, step26

The invocation-start SPECIALIZE assessment was
drafts/literature/2026-11-09-two-prime-band-coercivity-audit-24.md,
approved separately in step25. This audit reuses its primary theorem
and proof-case coverage. It reproduces the existing local estimates;
it imports no stronger result and claims no discovery beyond the
sources checked. The bands, N, w, shifts, windows and arbitrary
moving complex vectors are unchanged.

**Actual phase and the corrected citation.** L622 defines
theta(z)=[g(1/2+iz)-g(1/2-iz)]/(2i), where
g(v)=log Gamma(v/2)-(v/2)log pi with compatible conjugate branches.
This agrees with L637's Riemann–Siegel normalization. L622(7) is
obtained from the sector digamma expansion used in L465(4), with
analytic remainders controlled on disks of radius a fixed multiple
of T. These disks stay away from the gamma poles and negative real
axis; Cauchy bounds justify theta''=O(T^(-1)) and
theta'''=O(T^(-2)). This is not differentiation of an error given
only on the real axis. The source is the sector asymptotic in
[DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11#E2), already
imported in that local argument.

In particular, for Delta_s(t)=theta(t+h_s)-theta(t), signed
integration from 0 to h_s gives

    Delta_s'(t)=integral_0^(h_s) theta''(t+u) du
                    =O(1/(T L)),
    Delta_s''(t)=integral_0^(h_s) theta'''(t+u) du
                    =O(1/(T^2 L)).

Since |exp(i Delta_s)|=1 on the real axis, its derivatives are
i Delta_s' exp(i Delta_s) and
(i Delta_s''-(Delta_s')^2)exp(i Delta_s). Thus eta_s and its
first two derivatives have exactly the bounds used in (20) and
the endpoint estimate after (21), uniformly on [X,X+T]. The balanced
four-phase expression with b=(s,0,0,0) is precisely exp(i Delta_s).
Integrating theta' also verifies (12), including negative h_s;
averaging against the nonnegative weight of mass T proves the
claimed alpha_s limit and eventual lower modulus. The original
pointer L637(19)–(20) was misplaced and has been corrected above.
L622 is now an explicit direct input in the canonical DAG.

**Arithmetic and Hilbert-space checks.** From p>N and n<=N,
gcd(p,n)=1. Hence n|pm implies n|m; no resonant divisor is missing
in (11). Unique factorization also proves uniqueness of (p,m),
including between bands. Each resonant j<=H satisfies (10).
The logarithmic spacing in (7) is at least 1/H, and the two
endpoint Hilbert forms each cost pi H. Duality uses synthesis
functions exp(i theta(t))k^(-it) in the same weighted Hilbert space;
its unweighted bound is multiplied only by ||w||_infinity. This
checks the factor T^(-1) in (1), rather than an entrywise bound.

For the two prime rows, the Hermitian square has trace 4 and
determinant 4 sin^2(v-u); dividing by its largest eigenvalue,
which is at most 4, verifies (14). Summing with weights 1/(pq)
gives exactly min(M_1,M_2) in (15), so no cardinality loss is
omitted. The endpoint corrections in (13) tend to zero. For each
channel the convolution inverse in (17) has coefficient
a_s(r) sum_(d|r)mu(d), verifying the finite inverse at every r.
Its weighted rows are divisor counts and its weighted columns are
harmonic sums, as in (18). Their product is
17 D_(1/16) N^(1/8), bounding the squared operator norm. This
verifies (2) for both channels together, including arbitrary phases;
L926's different upward transform is never substituted.

**Exhaustion of leakage and all dimension factors.** For q=jn<=2H,
the cutoff is inactive for every index, and both integrations by
parts have zero endpoint terms. The second amplitude derivative
has L1 norm O(T^(-1)). The operator bound in (21) includes the
frequency loss H^2/T^2, the sum of j^(-1/2) of order sqrt(H),
the coefficient l1 loss sqrt(2N), and the output l2 loss sqrt(H).
Their exponent is 3(49/100)+1/10-2=-43/100. The resonant q=k
is excluded before this estimate.

For q>2H, the phase frequency has modulus at least log 2. The
intersection of the window with [2 pi j^2-h_s,infinity) has at
most one internal starting endpoint, whose amplitude is explicitly
charged. The normalized integral is O(T^(-1)). The coefficient
sum over j is O(T^(1/4)), giving exponent
49/200+1/10+1/4-1=-81/200, with no omitted factor for either
input or output dimension. For the entire negative branch,
2 pi j k/(nt)<=C T^(-1/100), so (24) holds simultaneously for
all its indices, even before imposing the cutoff. The derivative
is eventually at most -L/200 and its second derivative is O(T^(-1)).
One integration by parts on the actual interval charges its endpoint
values, integral |w_XT'|, and integral w_XT |phi''|, yielding
O(1/(T L)). This verifies (25), including internal cutoff jumps.

For the actual, undifferentiated Riemann–Siegel remainder,
triangle inequality followed by (8) costs T^(-1/4)*sqrt(T)
in the function norm, and (1) then costs T^(-1/2) in analysis.
Their product is T^(-1/4). Thus (26) controls the whole remainder
homogeneously in sqrt(S), without a pointwise-to-operator shortcut
or a derivative of that remainder. These four disjoint contributions
exhaust E U-A c and prove the stated residual bound.

**Common onset and downstream error.** The residual/principal norm
ratio is O(T^(-1/4)N^(1/16))=O(T^(-19/80)). The surviving squared
scale is N^(-1/8); relative to L N^(-1/4) its ratio is
N^(1/8)/L, which tends to infinity using the lower bound for the
floor N in (29). L928's charged error divided by T N^(-1/8)S
is O(T^(-13/80)N^(1/8))=O(T^(-11/80)). These are the correct
norm, squared-norm and downstream exponents respectively. Choose the
maximum of the finitely many onsets for the cutoff, prime masses,
alpha_s, phase gap and these three comparisons. All depend only on
fixed data and imported constants, never on X or the vectors.
S=0 is covered separately as in the proof.

Equations (1)–(30) therefore pass this conceptual audit; no numerical
certificate or effective onset is asserted. The only correction is
the phase reference and its explicit specialization/dependency. The
actual-norm proof is independent of L928's positivity question, and
L928(3) is used only afterward. This secures an unsigned coefficient
margin. It proves neither L928(11), a joint bump projection estimate,
signed realization/transfer, nor any actual-Xi mixed sign.

## Mathlib

Full matching coverage for this joint extraction theorem, its combined
Riemann–Siegel leakage bounds, and the precise standard analytic imports
has not been checked and remains unknown. Finite sums, Möbius inversion,
complex norm inequalities and Hermitian matrix estimates are supporting
mathematics, not a verified full matching Mathlib theorem. No formal
verification or absence claim is made.
