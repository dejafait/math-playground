# Lemma 98: consecutive packets obstruct optimized subset criteria

**Definitions and construction.** Use the suffix set S and blocks B_N
of Lemma 94 and the selected-subset ratio W_N(F) of Lemma 96. For a
nonempty B_N define W*_N=min_{∅≠F⊆B_N}W_N(F); this finite minimum
exists. For k≥2 set U_k=2^(4k²), d_k=2^(2k²), and

P={1} ∪ ⋃_{k≥2}{U_k,U_k+1,…,U_k+d_k−1}.

At s∈P put x_s=s^(3/4). Between consecutive s<t in P put

x_n=sqrt(n)t^(1/4)(1+(t−n)/(4t)),  s<n<t.

**Conclusion.** These coordinates strictly increase, have summable
reciprocal squares, and have S=P. Moreover,

Σ_{n∈S} n/x_n²=∞,   liminf_{N→∞}|B_N|/N=0,

W*_N→∞ as N→∞ through all nonempty integer blocks, and

Σ_{j≥0:B_(2^j)≠∅}1/W*_(2^j)<∞.

Thus both criteria in Lemma 96 can fail even after optimizing over all
nonempty subsets. This is not a failure of the upward-subsequence
conclusion itself.

## Proof

First establish a finite estimate. Let F={t_1<⋯<t_m} be any nonempty
subset of d consecutive integers, where d≥256. Suppose the crowding
maximum c includes evaluation at every t_i. Then

c/m ≥ log(d)/(32d).                                      (1)

For m<sqrt(d), its self term gives c≥1, so c/m>1/sqrt(d).
The inequality log(d)≤sqrt(d) for d≥256 follows from its value at
256 and the nonnegative derivative of sqrt(d)−log(d) for d≥4;
this proves (1) in this case.

For m≥sqrt(d), sum the crowding values at all t_i. For each rank
difference 1≤q≤floor(m/2), every consecutive gap t_(i+1)−t_i
occurs at most q times in Σ_{i=1}^{m−q}(t_(i+q)−t_i). Hence this
sum is at most q(d−1). Cauchy's inequality for positive numbers gives

Σ_{i=1}^{m−q} 1/(t_(i+q)−t_i+1)
 ≥ (m−q)²/[q(d−1)+m−q] ≥ m²/(8qd),

since m≤d, m−q≥m/2, and the denominator is at most 2qd.
All these terms occur in the summed crowding values. Therefore

m c ≥ (m²/(8d)) H_floor(m/2).

Writing H_l=Σ_{q=1}^l1/q, the integral bound H_l≥log(l+1)
gives H_floor(m/2)≥log(m/2)≥(1/2)log(d)−log(2)
≥(1/4)log(d), since d≥256. This proves (1). The argument
allows any missing indices and consequently covers clipped packets.

We next verify the coordinates directly. On a gap the real-variable
interpolant has derivative t^(1/4)(5t−3v)/(8t sqrt(v))>0 for
s≤v≤t. Its value at s exceeds s^(3/4), and its value at t equals
t^(3/4). Adjacent prescribed values increase too. Thus x_n strictly
increases. Since x_n≥n^(3/4), Σ x_n^(-2) converges. Every interior
index of a gap has x_n/sqrt(n)>t^(1/4), so is not a suffix minimum.
Every prescribed index s has normalized value s^(1/4), smaller than
all later prescribed values and than every later interior value.
Thus S=P exactly.

Each packet lies in [U_k,2U_k) and contributes at least

d_k/sqrt(2U_k)=1/sqrt(2)

to the suffix-weight sum. The packets are disjoint, proving divergence.
The blocks [2U_k,4U_k) are empty, proving the lower-density assertion.

Fix a nonempty block B_N with N≥2. It meets exactly one packet:
if it met packets starting at U<V, then N<2U and V<2N would imply
V<4U, whereas successive starts have ratio 2^(8k+4)>4. Write
U=d² for the start of its packet. Necessarily N>U/2. For any
nonempty F⊆B_N its normalized minimum satisfies α_N²<sqrt(2U).
Every selected point belongs to [U,U+d), and its own index is among
the allowed crowding evaluation indices N≤r<4N. Applying (1),

W_N(F)=N c_N/(|F| α_N²)
 > [d/(2sqrt(2))] [log(d)/(32d)]
 = log(d)/(64sqrt(2)).                                  (2)

The minimum over finitely many F retains this strict bound. As
nonempty N tend to infinity, their packet indices tend to infinity,
so (2) proves the every-block limit.

The nonempty dyadic blocks are precisely [1,2) and [U_k,2U_k).
The singleton prefix has W*_1=1. For the others, (2) yields

1/W*_(U_k)<64sqrt(2)/log(d_k)
             =32sqrt(2)/(k² log(2)).

Comparison with Σ k^(-2) proves summability. ∎

## Qualifications and verification

Any positive strictly increasing bounded height sequence is permitted;
the obstruction concerns only coordinate ratios, which do not use
heights. It neither produces a positive lower bound for actual near
sums nor excludes a vanishing full-upward subsequence. In particular,
there is no theta-specific or RH conclusion. The proof is analytic;
finite enumeration is only a sanity check, not a certificate for the
infinite construction. Formalization would require the finite minimum,
the rank-gap counting and Cauchy estimate, interpolation endpoints,
exact suffix membership, clipped-block bounds and dyadic summability.
