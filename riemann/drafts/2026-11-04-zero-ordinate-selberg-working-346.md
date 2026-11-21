# Step 346 — dyadic specialization working note

Approved target: the exact TARGET of the supplied
`literature/2026-11-04-zero-ordinate-selberg-specialization.md` (SPECIALIZE).
Reuse its parent comparison and BPT coverage; no RH corollary or contour
argument. Existing changes are extensive and remain preserved.

Let N_+ be the inclusive, full-multiplicity count and M(u)=
u/(2pi) log(u/(2pi e))+7/8. R=N_+-M is right continuous and locally BV.
For f(u)=u^(-i tau), ordinary partial summation on (T,2T] gives exactly
Z=integral f M' +[f R]_T^(2T)+i tau integral_T^(2T) R(u)f(u)/u du.
Off the discrete ordinate set, R=S+q with |q(u)|<=1/(150u) by BPT
Lemma 2; values at those points do not affect Lebesgue integrals.
The averaged count is N_*=N_+-m/2; right/left S values differ by m.
Endpoint orders m(u) are bounded by L467's closed unit shell.

Pending full write-up checks: endpoint R=O(log T) uniformly; moment
Cauchy--Schwarz bound tau*(integral |S|^2)^(1/2)*(1/(2T))^(1/2)
=O(T sqrt(log log T)); q integral <=tau/(300T)<=1/150;
smooth primitive u^(1-i tau)/(2pi(1-i tau))*(log(u/(2pi))-
1/(1-i tau)) gives O(log T) for T<=tau<=2T.
Ratio to T log T tends to zero. No beta weights, short windows or
sign claims are proved. This is specialization/reproduction of known
inputs, not a new source theorem. Full canonical proof and metadata
remain to be saved; do not treat this draft as an audit.

Completed: full proof saved as `../lemmas/L756-uniform-dyadic-zero-ordinate-cancellation.md`; preliminary checks above are resolved there. Independent critical audit remains pending.
