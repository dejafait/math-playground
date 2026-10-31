# Fixed-sector aggregate calculation — working checkpoint

Approved target: test L471's original B sum restricted to d_j>=1/16
by aggregating its nonnegative real-window kernels before using the
continuous fourth moment. Inputs read: L471 (complete), L018, L467,
and the completed fixed-displacement source notes. The historical
aggregation stop was procedural; no previous aggregate estimate was
found in these records. Preserve all existing work.

Candidate calculation, still being checked: with delta=1/16 and
k_d(u)=(d^2-u^2)/(u^2+d^2)^2 on |u|<=d, zero otherwise,
B_sector=integral_[T,2T] |Z(t)|^2 K(t) dt where
K=sum_selected m_j k_(d_j)(t-gamma_j). The full-window scalar
integral is 1/d, and k_d<=delta^(-2). The closed-shell estimate
therefore bounds sup K by 18 delta^(-2) log(2T+2), while
integral K<=delta^(-1) M, M=sum_selected m_j. Pair selection maps
injectively to right-side zeta zeros with beta>=9/16 at heights
<=3T, retaining multiplicities. Chourasiya--Simonic v1 Corollary 1
then gives M=O(T^(21/23)(log T)^3). Combined with the ordinary fourth
moment this suggests B_sector=O(T^(22/23)(log T)^4), which is little-o
of T(log T)^3. This checkpoint is not a canonical proved result;
check constants, endpoints, density onset and correspondence before
promoting it. No inference about the complementary sector or signs.

Completed: the candidate kernel calculation is proved in canonical
L483, including the explicit squared bound 73728 log(2T+2) H(3T) Q_4(T).
The ratio to the required scale is O(T^(-1/23) log T)->0. A separate
critical audit remains pending; the moving-cutoff proposal is uncovered.
