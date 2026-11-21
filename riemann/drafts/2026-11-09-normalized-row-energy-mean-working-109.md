# Fixed normalized row-energy mean test — step109

Completed. Approved target and method were exactly those of
`drafts/literature/2026-11-09-normalized-row-energy-mean-test-107.md`.
Main gap: actual-Xi all-degree mixed positivity. Test only lambda=0
and the necessary mean condition for mu_minus <=icx mu_plus.
Use all34 L938 rows and twelve labelled factors, retaining M_0^12.
No source search, parameter sweep or refinement is planned.

For A_k=M_(2k)/(2k)! and B_k=M_(2k+2)/(2k)!, Tonelli gives each
row mass product A_k^alpha_k and first moment
sum_k alpha_k B_k A_k^(alpha_k-1) product_(j!=k) A_j^alpha_j.
Only k with alpha_k>0 are included. There is no multinomial factor.
L019 positivity and L058 domination give positive finite masses and
finite first moments. The increasing test E on nonnegative support
requires delta=mean_plus-mean_minus>=0 for the proposed order.

Tail extension to k<=14 at lambda=0: u^k<=exp(14u), X=exp(2u).
K_n<=128 n^4 exp(9u/2-3n^2 X). Summing the geometric theta bound
gives 256 exp(37u/2-3X). With du=dX/(2X), X^(33/4)<=X^9.
Thus spatial tail <=128 exp(-150) sum_(j=0)^9
[9!/(9-j)!]50^(9-j)/3^(j+1). Omitted n>=5 over all u>=0 is
<=64*9!*625*2 exp(-74), using n=5+j, n^4<=625*16^j,
n^2>=25+11j and 16exp(-33)<1/2. Full proof and arithmetic
evidence are now canonical in L954, with the arithmetic contracts.

Fixed budget:64 panels on[0,2],theta1..4,Taylor order8,precision100.
Negative upper delta stops this direction; nonnegative lower passes
only necessity; zero-containing enclosure is inconclusive and ends
this test. Independent mass/full order/exponential comparison, other
degrees, initialization, contacts, continuation and realization remain.

Result: both normalizers are positive, but the complete delta enclosure
contains zero within[-8.574e-7,8.576e-7], width>1.714e-6. Exact-rational
replay passed; the fixed test ends inconclusively without refinement.
Full proof and evidence: `lemmas/L954-normalized-row-energy-mean-fixed-budget-stop.md`.
