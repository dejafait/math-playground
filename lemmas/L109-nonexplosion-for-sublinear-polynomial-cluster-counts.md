# Lemma 109: nonexplosion for sublinear polynomial cluster counts

**Hypotheses.** For every integer k≥1 let C_k be a nonempty finite set
of m_k distinct real points in [k,k+1/4]. Suppose there are constants
M>0 and 0≤alpha<1 with m_k≤M k^alpha for every k. Enumerate their
union increasingly as 0<x_1<x_2<⋯. Use the forward jump process of
Lemma 107, whose rates are q_ij=(x_j−x_i)^(-2) for j>i and whose
lifetime is T. No lower bound on gaps within C_k is imposed.

**Conclusion.** From every starting point, T=∞ almost surely.
For every strictly increasing positive bounded height sequence on these
coordinates, the full upward contributions of Lemma 107 admit a
subsequence tending to zero.

## Proof

First Σ_i x_i^(-2)≤Σ_k m_k/k²≤MΣ_k k^(alpha−2)<∞.
Thus Lemma 107 supplies finite positive total rates K_i and the embedded
chain with independent exponential holding times. Write c(i)=k when
x_i belongs to C_k. Fix 0<p<1−alpha and set f(i)=c(i)^p.
We prove a uniform upper bound on the nonnegative generator sum

L f(i)=Σ_{j>i}q_ij(f(j)−f(i)).                         (1)

If c(i)=c(j), its summand is exactly zero. If c(i)=k<l=c(j), then
x_j−x_i≥l−k−1/4≥3(l−k)/4. Consequently

L f(i)≤(16/9)Σ_{l>k} m_l(l^p−k^p)/(l−k)².            (2)

For k<l≤2k, concavity of t^p (since 0<p<1) gives
l^p−k^p≤p k^(p−1)(l−k), and m_l≤M 2^alpha k^alpha.
The corresponding part of (2) is at most

(16/9)M 2^alpha p k^(alpha+p−1)(1+log k).             (3)

For l>2k, use l−k≥l/2 and l^p−k^p≤l^p. This part is at most

(64/9)M Σ_{l>2k}l^(alpha+p−2)
 ≤ (64M/(9(1−alpha−p))) (2k)^(alpha+p−1).              (4)

The integral bound in (4) applies because alpha+p−2<−1.
Put delta=1−alpha−p>0. Both expressions are uniformly bounded:
k^(−delta)≤1 and k^(−delta)log k≤1/(e delta).
Thus (1) is at most a finite constant B independent of i. Arbitrarily
large internal jump rates have contributed zero, not been omitted
from the process.

Here is the finite-state stopping argument, as in Lemma 108, with the
cluster cutoff made explicit. Start at index n in cluster k_0, and fix
an integer R>k_0. Stop at the first embedded-chain point in a cluster
with label at least R; let tau_R be the sum of holding times before
that exit. The transient states are the finitely many points with
index at least n in clusters below R. Every transition increases the
index, so exit occurs after finitely many jumps almost surely. Collapse
all exit destinations into an absorbing state partial, retaining their
full summed rates. Use payoff g_R(i)=c(i)^p on transient states and
g_R(partial)=R^p. For any transient i, replacing an exit payoff c(j)^p
by R^p only decreases its increment. Hence Q_R g_R(i)≤L f(i)≤B;
at the absorbing state the generator is zero.

The finite-state expectation identity justified in Lemma 108 gives

E_n[g_R(X_t)]≤k_0^p+Bt,
P_n(tau_R≤t)≤(k_0^p+Bt)/R^p.                         (5)

Internal transitions keep their actual finite rates in this finite
matrix, regardless of their size. No estimate uniform in those rates
is needed for the finite-state identity.

On the original holding-time probability space, tau_R increases to T:
the embedded indices tend to infinity, each cluster is finite, and each
fixed visited holding time is included for all sufficiently large R.
In particular {T≤t} is contained in {tau_R≤t}. Let R→∞ in (5), then
take the union over positive integer t, to obtain P_n(T<∞)=0.
The final height-dependent subsequence statement follows from Lemma 107.
∎

## Qualifications

This resolves a scoped part of the finite-cluster question, including
unbounded polynomial cluster counts and unrestricted internal gaps.
It does not prove the assertion for all counts with Σ_k m_k/k²<∞.
For example m_k=max(1,floor(k/log(k+1)²)) satisfies that summability
condition but exceeds M k^alpha eventually for each fixed M and
alpha<1. Summability follows by comparison with 1/[k(log k)²] for k≥2; the power comparison follows from
k^(1−alpha)/log(k+1)²→∞. No explosion is claimed for that example.
No universal coordinate theorem or RH conclusion follows.

## Verification and formalization obligations

The proof is analytic and requires no numerical certificate. Verify the
3/4 intercluster distance constant, vanishing internal increments,
concavity bound, harmonic sum, convergent far-tail integral and strict
exponent margin. The stopped process retains every exit rate and every
internal rate. Its transient set is finite because each cluster is
finite. The payoff is capped downward on exit, and the holding-time
coupling does not assume nonexplosion. Formalization would require the
cluster enumeration, these estimates, the finite-state expectation
identity and exit coupling of Lemma 108, and the selection implication
of Lemma 107.
