# Effective Hermite tail calculation: saved reasoning

Approved target: the exact TARGET in
`literature/2026-10-31-hermite-effective-tail-specialization.md`.
No change of source hypotheses or signed-positivity target is made.

Candidate elementary estimate, still being checked: Romik's even Phi_R
satisfies 0<=Phi_R(u)<=10000 exp(-u^2). For u>=0, drop only the
negative summand in its positive theta summands, split
m^2 exp(2u)>=(m^2+exp(2u))/2, and use
sum m^4/2^m=150, 3<pi<4 and exp(2u)>=1+2u+2u^2.

With a=5/4 the coefficient integral would then give
b_(2n) sqrt(2^(2n)(2n)!)<=20000*5^(-n).
DLMF's real Hermite bound and derivative identity would give, for
j=0,1,2 and n>=1, a term bound
80000 n exp(t^2/2) 5^(-n).
The complete sum from n=N+1 is at most
80000 N exp(2T^2) 5^(-N), N>=1, |t|<=2T.
The proposed cutoff is N=ceil(16(T+1)^2). Using N<=2^N,
80000<exp(17), log(5/2)>1/2 would imply an exponent
17+2T^2-N/2<=-8T for T>=1, stronger than -2pi T.

Completed calculation: the full proof, including normalization,
Gaussian moment factors, derivative limits and all-T inequalities,
is canonical in `lemmas/L564-effective-hermite-derivative-tail.md`.
The bound succeeds with C=16 and the stronger error exp(-8T).
Independent audit is pending. These are absolute errors only;
the truncation discriminant margin and all higher signs remain open.
