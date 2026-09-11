# Lemma 97: endpoint packets realize subset selection

**Construction.** For k≥2 put U_k=2^(4k²) and d_k=2^(2k²), so
U_k=d_k² and d_k≥256. Define three sets of integer indices

L_k={U_k+e: 0≤e<d_k},
G_k={U_k+2d_k+j d_k: 0≤j<d_k/2},
R_k={U_k+U_k/2+2d_k+e: 0≤e<d_k},
P={1} ∪ ⋃_{k≥2}(L_k∪G_k∪R_k).

At s∈P set x_s=s^(3/4). Between consecutive s<t in P set

x_n=sqrt(n)t^(1/4)(1+(t−n)/(4t)),   s<n<t.

Use S, B_N, M_N, A_N, C_N, V_N of Lemma 94. For selected blocks
N=U_k choose F_N=G_k and use W_N of Lemma 96.

**Conclusion.** The coordinates strictly increase, Σ_n x_n^(-2)<∞,
and S=P. They satisfy

- Σ_{n∈S}n/x_n²=∞ and liminf_{N→∞}M_N/N=0;
- V_N→∞ over all nonempty integer blocks;
- Σ_{m≥0:B_(2^m)≠∅}1/V_(2^m)<∞;
- W_(U_k)≤4 for every k≥2.

For every positive strictly increasing bounded height sequence there
is consequently a common vanishing subsequence of Q_n and E_f.

## Proof

Abbreviate U=U_k and d=d_k. The left packet ends at U+d−1,
the grid starts at U+2d and ends at U+U/2+d, and the right packet
runs from U+U/2+2d through U+U/2+3d−1. These sets are ordered,
disjoint, and lie in [U,2U), since 3d<U/2. Successive cluster starts
have ratio 2^(8k+4)>4.

The interpolation argument of Lemma 95 applies. For completeness, the
gap function has derivative t^(1/4)(5t−3v)/(8t sqrt(v))>0 on [s,t],
its left endpoint value exceeds s^(3/4), and its right endpoint value
is t^(3/4). Adjacent prescribed values increase directly. Thus all
coordinates strictly increase. Also x_n≥n^(3/4), proving reciprocal-
square summability. Inside a gap a_n>a_t=t^(1/4), so n∉S. At a
prescribed index s, every later prescribed normalized value is larger,
and every later interior value exceeds its right endpoint's normalized
value. Hence s∈S and S=P.

Each cluster has (5/2)d members, each less than 2U. Its suffix weight
is at least (5/2)d/sqrt(2U)=5/(2sqrt(2)); the disjoint clusters prove
divergence. The blocks [2U_k,4U_k) are empty, giving zero lower density.

Fix a nonempty block with N≥2. It meets at most one cluster: meeting
clusters based at U<V would imply N<2U and V<2N, hence V<4U,
contrary to their separation. For its cluster we have N>U/2 and
A_N²<sqrt(2U). Writing M=M_N, it follows that

V_N > d C_N/(2sqrt(2) M),       M≤(5/2)d.                (1)

If the block meets the grid, it contains a full endpoint packet.
For N≤U, its left endpoint precedes the left packet, while its right
endpoint exceeds a grid point and hence the end of that packet. For
N>U, meeting the grid implies N≤U+U/2+d, before the right packet;
also 2N>2U, beyond that packet's end. Thus the right packet is fully
contained. Evaluate the crowding sum at the last index of the contained
packet: it is at least H_d=Σ_{q=1}^d1/q. Equation (1) implies

V_N>H_d/(5sqrt(2)).                                    (2)

If the block meets no grid point, it cannot meet both endpoint packets,
since an interval containing a point of each contains the entire grid.
It therefore consists of a consecutive portion of just one packet.
Here M≤d and evaluation at its last point gives C_N≥H_M.
The sequence H_m/m decreases for m≥1: H_m≥m/(m+1) proves
(H_m+1/(m+1))/(m+1)≤H_m/m. Consequently d H_M/M≥H_d,
and (1) gives V_N>H_d/(2sqrt(2)), stronger than (2).
These cases exhaust every nonempty block with N≥2. As such N tend
to infinity their cluster indices k do too, and H_d≥log(d+1)→∞.
This proves the required every-block limit, including clipped packets.

The nonempty dyadic blocks are exactly [1,2) and [U_k,2U_k), since
all clusters lie inside those disjoint dyadic blocks. We have V_1=1.
For each remaining one (2) gives

1/V_(U_k)<5sqrt(2)/H_(d_k)≤5sqrt(2)/(2k² log 2).

Comparison with Σ k^(-2) proves the asserted inverse-ratio summability.

On the other hand, F_(U_k)=G_k has m=d/2 points with spacing d and
α²≥sqrt(U)=d. For any integer r in the crowding maximum, listing
eligible grid points backwards bounds their contribution by

Σ_{q=0}^{m−1}1/(1+qd)≤1+H_(m−1)/d≤2.

(The empty case contributes zero, and H_(m−1)≤m−1≤d.) Thus
W_(U_k)≤2U/((d/2)d)=4. Lemma 96 now gives the common vanishing
subsequence for each height sequence in the statement. ∎

## Qualifications and verification

This construction proves that selected-subset averaging covers coordinates
where both full-block exact-crowding criteria fail. It does not settle the
unrestricted upward-subsequence assertion or identify these coordinates
with theta zeros. The argument is analytic; no numerical certificate is
needed. Formalization should check interpolation at adjacent indices,
exact suffix membership, cluster ordering, the two endpoint-containment
cases, clipped-packet harmonic averages, dyadic endpoints and summability,
and the restricted-grid crowding estimate.
